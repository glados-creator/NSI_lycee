import dataclasses
import os
import my_parser

def handy_cmd_prompt(q : str):
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
        return cls._instances[cls]

@dataclasses.dataclass
class project(metaclass=Singleton):
    save_file_path : str = ""
    pygame = False
    tkinter = False
    menu_stack : list = dataclasses.field(default_factory=list)
    GLOBAL : dict = dataclasses.field(default_factory=dict)
    DATA_W : bool = False # false labirith normal ||  True weighted lab
    DATA = None


@dataclasses.dataclass
class graph:
    link: dict

    def get_nodes(self):
        return self.link.keys()
    def get_link(self,k):
        return self.link[k]


    @classmethod
    def from_dlist(cls, link: list):
        """
        convert [a,b,c] + [(a,b),(a,c),(b,c)] to graph
        """
        node = set(link)
        d = dict.fromkeys(node)
        for x in d.keys():
            d[x] = []
        for k, v in link:
            d[k].append(v)
        return cls(link=d)