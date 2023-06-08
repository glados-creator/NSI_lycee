import time
import os
import enum
import json
import csv
import myc


class FileTypeCustome(enum.Enum):
    Project_Type = enum.auto()
    Graph_Data_Type_csv = enum.auto()
    Graph_Data_Type_json = enum.auto()
    Unknown_Type = enum.auto()
    Graph_Data_Image = enum.auto()


def xml_serializer(tobe: object):
    # print("serializer")
    # print(repr(tobe))
    # "<class bool>" -> "bool"
    T = str(type(tobe)).strip("<").strip(">").strip("class").strip(" ")[1:-1]
    if T == "bool":
        # conv bool to int because that what python do anyway
        T = "int"
    ret_str = f"[{T}]"
    ret_str += "{\n"
    if T == "str":
        # idk str types dissapear so here a bypass fix
        return "[str]{" + str(repr(tobe)) + "}\n"
    # well to be effective any iter type doesn't work sooooo ...
    # if isinstance(my_iterable, (list, tuple, set, dict)):
    if T == "dict":
        # special for dict
        return "[dict]" + json.dumps(tobe) + "\n"
    elif T == "list" or T == "set" or T == "tuple":
        # serializer by iter
        ret_str += "("
        for x in tobe:
            ret_str += xml_serializer(x) + ","
        ret_str = ret_str[:-1]
        ret_str += ")"
        ret_str += "}\n"
        return ret_str
    else:
        # serializer by attr
        for attr in dir(tobe):
            if callable(getattr(tobe, attr)) or "__" in attr:
                continue
            # NOTE : just check if type of type is not first type
            # if attr == "denominator":
            # return "[int]{" + str(tobe) + "}\n"
            if type(getattr(tobe, attr)) == type(tobe):
                # recursive type see note above
                # int(denominator=[int]->denominator.....)
                return f"[{T}]" + "{" + str(repr(tobe)) + "}"
            se = xml_serializer(getattr(tobe, attr))
            # print(se)
            ret_str += f"{attr}={se}," if se else ""
        # print(repr(ret_str))
        # remove the last char
        ret_str = ret_str[:-1]
        ret_str += "}\n"
        return ret_str


def xml_parser(txt: str):
    print("parsing ...")
    stack = []
    types = []
    args = []
    word = ""
    flag = False
    should_be = False
    should_be_two = False
    i = 0
    # print(txt)
    try:
        while i < len(txt):
            char = txt[i]
            # print(i, "stack", stack, "types", types,"args", args, "word", word, char)
            if word == "Save_Project.xml":
                flag = True
                word = ""
            elif char == "\n":
                pass
            elif char == ",":
                if not should_be and types[-1] != "dict":
                    print(" ',' not where it belong but anyway")
                    # raise RuntimeError(" ',' not where it belong")
                should_be = False
            elif char == "[":
                stack.append("]")
                if word:
                    args[len(types)-1].append(word)
                args.append([])
                word = ""
            elif char == "{":
                stack.append("}")
            elif char == "]":
                if char != stack.pop():
                    raise RuntimeError("parsing file wrong")
                if word == "dict":
                    inner_idk = ""
                    i += 1
                    while not txt[i-1] == "}":
                        inner_idk += txt[i]
                        i += 1
                    # print(args, types)
                    # print(inner_idk)
                    args.pop()
                    args[-1].append(json.loads(inner_idk))
                else:
                    types.append(word)
                word = ""
            elif char == "}":
                if char != stack.pop():
                    raise RuntimeError("parsing file wrong")
                should_be = False
                # NOTE : eval here danger but don't worry
                T = types.pop()
                args[len(types)].append(word)
                # print("parsing Types", T)
                if T == "NoneType":
                    args.pop()
                    args[len(types)-1].append(None)
                else:
                    # print("eval that")
                    # print("stack : ", stack)
                    # print("types : ", types)
                    # print("args : ", args)
                    # print("word : ", word)
                    local_arg = [str(x) for x in args.pop()]
                    # formating args
                    # need to work with arg | arg,arg | arg = parameter ect
                    format_arg = ""
                    if not len(local_arg):
                        format_arg = ","
                    elif len(local_arg) == 1:
                        # args[len(types)].append(word) || work == local_arg
                        format_arg = word
                        format_arg += ","
                    else:
                        # good old ways
                        j = 0
                        kwarg = False
                        while j != len(local_arg):
                            # print(format_arg)
                            if "=" in local_arg[j]:
                                # kwarg
                                kwarg = True
                                format_arg += local_arg[j]
                                # check where is the "="
                                if (j+1) <= len(local_arg):
                                    # it could be in one single str
                                    if local_arg[j].split("=")[1]:
                                        pass
                                    else:
                                        # else grab the next arg
                                        j += 1
                                        format_arg += local_arg[j]
                                else:
                                    # end of stack
                                    print(i, "stack", stack, "types", types,
                                          "args", args, "word", word, char)
                                    raise RuntimeError(
                                        f"parser kwarg : no more arg after = {local_arg[j]}\n; j {j} ;len(local_arg) {len(local_arg)}")
                                format_arg += ","
                            elif not kwarg:
                                format_arg += local_arg[j]
                                if local_arg[j] != "(" and local_arg[j] != ")":
                                    format_arg += ","
                            elif "=" not in local_arg[j] and kwarg:
                                print("args after kwarg in parser ignore",
                                      j, local_arg[j])
                                if i+1 == len(local_arg):
                                    # if last arg after kwarg ignore append "," else char disapear
                                    format_arg += ","
                            else:
                                raise RuntimeError("unreachable")
                            j += 1
                    # remove last ","
                    if format_arg[-1] == ")":
                        # can't forget the trailing )
                        format_arg = format_arg[:-2]
                        format_arg += ")"
                    else:
                        format_arg = format_arg[:-1]
                    # format if last types
                    # final conversion else there is a
                    # pop on empty list so set the flag
                    idk_flag = False
                    if len(types)-1 < 0:
                        idk_flag = True
                        args.append([])
                        # last one convertion
                    # print("args",args)
                    # print("format_arg", format_arg)
                    # print(
                    #     f"args[{len(types)-1}].append(eval({repr(T)}+\"(\"+{repr(format_arg)}+\")\"))")
                    # print()
                    # try to eval if args not accepted at all try without (aka default values > none)
                    try:
                        args[len(types)-1].append(repr(eval(T+"("+format_arg+")")))
                    except Exception as ex:
                        # print(ex)
                        args[len(types)-1].append(repr(eval(T+"()")))
                    if idk_flag:
                        # actually with the repr to do with the strings
                        # the return is in the forme of a lovely formated string
                        # project(save_file_path='', menu_stack=[], GLOBAL={}, DATA_W=False)
                        # but we need to eval it one more time to return it
                        # no even going to try except it because how could there be an error we don't eval before
                        # also the class type name is wrong
                        # project -> myc.project
                        # print("RETURN FINISH")
                        # print(args)
                        args[-1][-1] = eval(T+"("+format_arg+")")
                    # print("eval",args)
                should_be = True
                word = ""
            else:
                if should_be_two:
                    # it doesn't work to well
                    # as a matter of fact it work but it was the serializer
                    print(str(i)+" ',' expected but anyway")
                    should_be = False
                    should_be_two = False
                if should_be:
                    should_be_two = True
                word += char
            i += 1
        ret = args.pop()
        if len(args) or len(stack) or len(types) or not flag:
            raise RuntimeError("parser finish wrong")
        return ret
    except Exception as ex:
        # all of thoses print are for debuging
        # print("error while casting in parsing project file")
        # print("flag : ", flag)
        # print("stack : ", stack)
        # print("types : ", types)
        # print("args : ", args)
        # print("word : ", word)
        print("error in xml project file parser")
        print(ex)
        raise ex
        # delete singleton intance to have default one
        myc.project._instances.pop()
        return [myc.project()]


def parse_Project_file(path: str = ""):
    if path:
        path = os.path.abspath(path)
    else:
        path = os.path.abspath(
            myc.project().save_file_path + "./Save_Project.xml")
    try:
        with open(path, "r") as f:
            # save old variable like path we want to keep
            local_pygame = myc.project().pygame
            local_tkinter = myc.project().tkinter
            local_gen = myc.project().gen
            # local_menu_stack = myc.project().menu_stack.copy()
            # here is a litlle trick
            # NOTE : menu stack set to None for the redirect import loop
            # should be reset by the parsing
            myc.project().menu_stack = None
            # we shoudl have that by reparsing the project file
            # however if the file is just a decoy then we known and reparse it
            # parse xml file with the custome parser
            objs = xml_parser(f.read(-1))
            if len(objs) > 1:
                raise RuntimeError(
                    "something worng at parsing project file , not suppose to have more than one object in file")
            obj = objs[0]
            if obj.menu_stack is None:
                print("reparsing")
                return parse_Project_file()
            # if we use the same graphic api we can reuse the api
            if (local_pygame and obj.tkinter) or (local_tkinter and obj.pygame):
                obj.menu_stack = []  # local_menu_stack
                if myc.project().menu_stack is None or not len(myc.project().menu_stack):
                    if myc.project().pygame:
                        raise NotImplementedError
                    elif myc.project().tkinter:
                        myc.project().menu_stack = ["init"]
                    else:
                        myc.project().menu_stack = []
            # print("parser obj", obj)
            obj.pygame = local_pygame
            if local_pygame:
                obj.tkinter = False
                obj.pygame = True
            else:
                obj.tkinter = local_tkinter
                obj.pygame = False
            myc.project().gen = local_gen
            myc.project().DATA_W = False
    except Exception as ex:
        print(ex)


def parse_cvs_DATA(path: str = ""):
    if path:
        path = os.path.abspath(path)
    else:
        path = os.path.abspath(myc.project().save_file_path + "./csv.csv")
    try:
        with open(path, "r") as f:
            myc.project().DATA_W = False
            myc.project().DATA = []
            reader = csv.reader(f.read(-1), delimiter=";")
            num_rows = int(next(reader)[0])
            next(reader)
            num_columns = int(next(reader)[0])
            next(reader)
            x = list(reader)
            xi = 0
            for i in range(num_rows):
                myc.project().DATA.append([])
                for j in range(num_columns):
                    # print(myc.project().DATA,i,j,xi,x)
                    myc.project().DATA[i].append(int(x[xi][0]))
                    xi += 2
    except Exception as ex:
        myc.project().DATA = None
        print(ex)
    myc.project().DATA_W = False
    quick_cache_save()


def save_cvs_DATA(path: str = ""):
    if path:
        path = os.path.abspath(path)
    else:
        path = os.path.abspath(
            myc.project().save_file_path + "./csv.csv")
    myc.project().conv_to_N()
    try:
        with open(path, "w") as f:
            f.write(str(myc.project().get_size()[0]))
            f.write("\n")
            f.write(str(myc.project().get_size()[1]))
            f.write("\n")
            for row in myc.project().DATA:
                for k, element in enumerate(row):
                    f.write(str(int(element)))
                    if k != myc.project().get_size()[1]-1:
                        f.write(";")
                f.write("\n")
    except Exception as ex:
        print(ex)


def parse_json_DATA(path: str = ""):
    if path:
        path = os.path.abspath(path)
    else:
        path = os.path.abspath(myc.project().save_file_path + "./json.json")
    try:
        myc.project().DATA = json.load(open(path, "r"))
        # print(myc.project().DATA)
        print("json data imported")
    except Exception as ex:
        myc.project().DATA_W = False
        myc.project().DATA = None
        print(ex)
    if isinstance(myc.project().DATA,dict):
        myc.project().DATA_W = True
        myc.project().conv_to_N()
    else:
        myc.project().DATA_W = False
    mode = myc.project().DATA_W
    quick_cache_save()
    myc.project().DATA_W = False ###! mode


def save_json_DATA(path: str = ""):
    if path:
        path = os.path.abspath(path)
    else:
        path = os.path.abspath(
            myc.project().save_file_path + "./json.json")
    try:
        myc.project().DATA_W = True
        json.dump(myc.project().conv_to_N().DATA, open(path, "w"))
    except Exception as ex:
        print(ex)


def quick_cache_save(path: str = ""):
    if path:
        path = os.path.abspath(path+"./Save_Project.xml")
    else:
        path = os.path.abspath(
            myc.project().save_file_path + "./Save_Project.xml")
    myc.project().DATA_W = False
    if myc.project().menu_stack is None or not len(myc.project().menu_stack):
        if myc.project().pygame:
            raise NotImplementedError
        elif myc.project().tkinter:
            myc.project().menu_stack = ["init"]
        else:
            myc.project().menu_stack = []
    try:
        with open(path, "w") as f:
            f.write("Save_Project.xml\n")
            f.write("[myc.project]{")
            f.write("\nDATA="+xml_serializer(myc.project().DATA))
            ###! f.write(",DATA_W="+xml_serializer(myc.project().DATA_W))
            f.write(",pygame="+xml_serializer(myc.project().pygame))
            f.write(",tkinter="+xml_serializer(myc.project().tkinter))
            f.write(",menu_stack="+xml_serializer(myc.project().menu_stack))
            f.write(",resolver_mode="+xml_serializer(myc.project().resolver_mode))
            f.write(",save_file_path=" +
                    (xml_serializer(myc.project().save_file_path) if myc.project().save_file_path else "'./'"))
            f.write("}")
    except Exception as ex:
        print(ex)


def parse_file_all(path: str = None):
    if path is None:
        print("path is None in parse_file_all arg")
        return FileTypeCustome.Unknown_Type
    print("parsing all", path)
    ext = os.path.basename(path)[-3:]
    if ext == ".py":
        return FileTypeCustome.Unknown_Type
    ext = os.path.basename(path)[-4:]
    if ext == ".xml":
        parse_Project_file(path)
        return FileTypeCustome.Project_Type
    elif ext == ".csv":
        parse_cvs_DATA(path)
        return FileTypeCustome.Graph_Data_Type_csv
    elif os.path.basename(path)[-5:] == ".json":
        parse_json_DATA(path)
        return FileTypeCustome.Graph_Data_Type_json
    return FileTypeCustome.Unknown_Type


def quick_cache_load():
    if os.path.exists(os.path.abspath(myc.project().save_file_path + "./Save_Project.xml")):
        print("loading cache project...")
        parse_Project_file(os.path.abspath(
            myc.project().save_file_path + "./Save_Project.xml"))
    else:
        print("no cache project file")
    # print(myc.project().DATA)

    quick_cache_save()


if __name__ == "__main__":
    quick_cache_save()
    time.sleep(1)
    print(quick_cache_load())
