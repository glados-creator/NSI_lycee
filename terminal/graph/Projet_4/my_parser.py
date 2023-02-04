import os
import enum
import json
import csv
import myc

class  FileTypeCustome(enum.Enum):
    Project_Type = enum.auto()
    Graph_Data_Type_txt = enum.auto()
    Graph_Data_Type_csv = enum.auto()
    Graph_Data_Type_json = enum.auto()
    Unknown_Type = enum.auto()

def xml_serializer(tobe : object):
    T = str(type(tobe)).strip("<").strip(">").strip("class").strip(" ")[1:-1]
    ret_str = f"[{T}]"
    ret_str += "{\n"
    for attr in dir(tobe):
        if callable(getattr(tobe,attr)) or "__" in attr:
            continue
        if attr == "denominator":
            return "[int]{" + str(tobe) + "}\n" 
        se = xml_serializer(getattr(tobe,attr))
        ret_str += f"{attr}={se}" if se else ""
    ret_str += "}\n"
    return ret_str

def xml_parser(txt : str):
    stack = []
    types = []
    args = []
    word = ""
    flag = False
    i = 0
    try:
        while i < len(txt):
            char = txt[i]
            print(flag, "stack",stack,"types",types,"args",args,"word",word,char)
            if word == "Save_Project.xml": 
                flag = True
                word = ""
            if char == "\n": pass
            elif char == "[":
                stack.append("]")
                if word:
                    args.append(word)
                args.append([])
                word = ""
            elif char == "{":
                stack.append("}")
            elif char == "]":
                if char != stack.pop():
                    raise RuntimeError("parsing file wrong")
                types.append(word)
                word = ""
            elif char == "}":
                if char != stack.pop():
                    raise RuntimeError("parsing file wrong")
                # NOTE : eval here danger but don't worry
                T = types.pop()
                if T == "NoneType":
                    args[len(types)] = None
                else:
                    print("eval that")
                    print(args)
                    print(types)
                    print(f"args[{len(types)}].append(eval({str(T)}+\"(\"+ {''.join([str(x) for x in args[len(types)]])} +\")\"))")
                    ### args[len(types)-1].append(eval(str(T)+"("+''.join([str(x) for x in args[len(types)]])+" "+str(word)+")"))
                word = ""
            else:
                word += char
            i += 1
        ret = args.pop()
        if  len(args) or len(stack) or len(types) or not flag:
            raise RuntimeError("parser finish wrong")
        return ret
    except Exception as ex:
        print("error while casting in parsing project file")
        print("flag : ", flag)
        print("stack : ",stack)
        print("types : ",types)
        print("args : ",args)
        print("word : ",word)
        print("error")
        print(ex)
    raise

def parse_Project_file(path : str):
    with open(path,"r") as f:
        # TODO : redo parser pass list of data conv to real
        objs = xml_parser(f.read(-1))
        if len(objs) > 1:
            raise RuntimeError("something worng at parsing project file more than one object")
        raise NotImplementedError

def parse_cvs(path : str):
    with open(path,"r") as f:
        # TODO : finish
        raise 
        csv.DictReader(f.read(-1))

def save_cvs():
    raise NotImplementedError

def parse_json(path : str):
    raise NotImplementedError

def save_json():
    raise NotImplementedError

def quick_cache_save():
    with open(myc.project().save_file_path + "/Save_Project.xml","w") as f:
        f.write("Save_Project.xml\n")
        f.write(xml_serializer(myc.project()))

def parse_file_all(path : str):
    ext = os.path.basename(path)[-3:]
    if ext == ".py":
        return FileTypeCustome.Unknown_Type
    ext = os.path.basename(path)[-4:]
    if ext == ".xml":
        parse_Project_file(path)
        return FileTypeCustome.Project_Type
    elif ext == ".csv":
        parse_cvs(path)
        return FileTypeCustome.Graph_Data_Type_csv
    elif os.path.basename(path)[-5:] == ".json":
        parse_json(path)
        return FileTypeCustome.Graph_Data_Type_json
    return FileTypeCustome.Unknown_Type

def quick_cache_load():
    if os.path.exists(myc.project().save_file_path +"/Save_Project.xml"):
        print("loading cache project...")
        parse_Project_file(myc.project().save_file_path +"/Save_Project.xml")
    else:
        print("no cache project file")
    quick_cache_save()

if __name__ == "__main__":
    quick_cache_save()
    print(quick_cache_load())
            