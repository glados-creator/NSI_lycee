import dataclasses


def handy_cmd_prompt(q: str):
    print(q)
    while True:
        i = input("y/n : ")
        if i.lower() == "y":
            return 1
        elif i.lower() == "n":
            return 0


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        else:
            # Modify the existing instance's attributes
            # calling
            # project(save_file_path='', menu_stack=[], GLOBAL={}, DATA_W=False)
            # with existing instance will cause
            # cls._instances[cls] = super().__call__(*args, **kwargs)
            #                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            # TypeError: project.__init__() got an unexpected keyword argument 'gen'
            # because dataclasse instance don't expect arg/kwarg
            # (thx chat GPT) (i could have done it be myself but it's so obscure)
            instance = cls._instances[cls]
            for key, value in kwargs.items():
                if hasattr(instance, key):
                    setattr(instance, key, value)
        return cls._instances[cls]


@dataclasses.dataclass
class project(metaclass=Singleton):
    save_file_path: str = ""
    pygame: bool = False
    tkinter: bool = False
    gen: bool = False
    DATA : str = None
    resolver_mode : str = ""
    menu_stack: list = dataclasses.field(default_factory=list)
    GLOBAL: dict = dataclasses.field(default_factory=dict)
    DATA_W: bool = False  # false labirith normal ||  True weighted lab
    # [ [1,0,1],   => {vertex(0,0) : link  , vertex(0,1) : link , vertex(0,2) : link}
    #   [0,0,1],   =>
    #   [1,1,1]    =>
    # ]

    @staticmethod
    def get_size(grid=None):
        # row | column
        if grid is None:
            p = project()
        else:
            # basicaly mock it wizardery
            p = type("mock_prokect",(object,),{"DATA" : grid,"DATA_W" : False})
        if p.DATA is None:
            return (0,0)
        if isinstance(p.DATA,list):
            # print("isinstance(p.DATA,list) and p.DATA_W")
            # print("doesn't make sense mate so i fix it")
            p.DATA_W = False
        elif isinstance(p.DATA,dict):
            # print("isinstance(p.DATA,dict) and not p.DATA_W")
            # print("doesn't make sense mate so i fix it")
            p.DATA_W = True
        if p.DATA_W:
            max_i = [0,0]
            for i in p.DATA.keys():
                s = i.split(",")
                max_i[0] = max(max_i[0],int(s[0][1])+1)
                max_i[1] = max(max_i[1],int(s[1][0])+1)
            return tuple(max_i)
        else:
            if len(p.DATA):
                return (len(p.DATA),len(p.DATA[0]))
            else:
                return (0,0)

    @staticmethod
    def conv_to_W(normal_weight=1):
        # conv to data w with default weight
        projecti = project()
        raise NotImplementedError
        ###! if projecti.DATA_W:
        ###!     # print("already DATA W dummy")
        ###!     return projecti
        ###!
        ###! def do_thing(lis, neighbor, i, j):
        ###!     if i < 0 or j < 0 or i > len(lis)-1 or j > len(lis[0])-1:
        ###!         return False
        ###!     # true there is a neighbor append to it
        ###!     if not lis[i][j]:
        ###!         neighbor.append([f"({i},{j})", normal_weight])
        ###! projecti.DATA_W = True
        ###! L_DATA = {}
        ###! for i in range(projecti.get_size()[0]):
        ###!     for j in range(projecti.get_size()[1]):
        ###!         neighbor = []
        ###!         if projecti.DATA[i][j]:
        ###!             # black case no neighbor
        ###!             L_DATA[f"({i},{j})"] = []
        ###!             continue
        ###!         do_thing(projecti.DATA, neighbor, i, j-1)
        ###!         do_thing(projecti.DATA, neighbor, i, j+1)
        ###!         do_thing(projecti.DATA, neighbor, i+1, j)
        ###!         do_thing(projecti.DATA, neighbor, i-1, j)
        ###!         L_DATA[f"({i},{j})"] = neighbor
        ###! projecti.DATA = L_DATA
        ###! return projecti

    @staticmethod
    def conv_to_N():
        # converte to normale lab
        projecti = project()
        if not projecti.DATA_W:
            # print("idk why but you call conv to Normal labarithm , but it is already")
            return projecti
        projecti.DATA_W = False
        ret = []
        for i in range(projecti.get_size()[0]):
            ret.append([])
            for j in range(projecti.get_size()[1]):
                if len(projecti.DATA[f"({i},{j})"]) == 0:
                    ret[i].append(1)
                else:
                    ret[i].append(0)
        projecti.DATA = ret
        return projecti

    @staticmethod
    def conv_to_matrix():
        projecti = project()
        raise NotImplementedError
        # return projecti


# @dataclasses.dataclass
# class graph:
# link: dict
###
# def get_nodes(self):
# return self.link.keys()
# def get_link(self,k):
# return self.link[k]
###
###
# @classmethod
# def from_dlist(cls, link: list):
# """
# convert [a,b,c] + [(a,b),(a,c),(b,c)] to graph
# """
# node = set(link)
# d = dict.fromkeys(node)
# for x in d.keys():
# d[x] = []
# for k, v in link:
# d[k].append(v)
# return cls(link=d)

if __name__ == "__main__":
    # test of convertion of lab
    print("Testing myc conversion")
    proj = project()
    lab = [
        [1, 0, 1],
        [0, 0, 1],
        [1, 1, 1]
    ]
    proj.DATA = lab
    print(proj)
    print(proj.conv_to_N().DATA)
    ###! print(proj.conv_to_W().DATA)
    ###! print(proj.conv_to_W().DATA)
    print(proj.conv_to_N().DATA)
    # print(proj.conv_to_matrix().DATA)
