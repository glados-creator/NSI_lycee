def __convert_base(inp  ,bas   = 2 ,bigbase = False):
    #on convertie 
    ret = []
    level = 0
    while inp - bas**level >= 0:
        level = level + 1
    #parametre returne la plus grande base de division disponible
    if bigbase:
        return level
    for x in range(0,level):
        ret.append(0)
    level = level-1
    while level >= 0:
        if inp - bas**level >= 0:
            inp = inp - bas**level
            ret[len(ret)-(level+1)] = ret[len(ret)-(level+1)] +1
        else:
            level = level-1
    return ret

def convert_to_bin(inp):
    if not isinstance(inp,int):
        # NOTE: la conversion en binaire n'a pas été tester pour les flotants
        raise RuntimeError(f"depuis quoi tu essaye de convertir en binaire ? {type(inp)} ?")
    if inp > 0:
        return __convert_base(inp,2)
    else:
        return (__convert_base(-inp,2),-inp)

def convert_to_octal(inp):
    if inp < 0:
        return convert_to_octal(-inp)
    return (inp,"".join([str(x) if x <= 9 else 
                    "A" if x == 10 else 
                    "B" if x == 11 else
                    "C" if x == 12 else 
                    "D" if x == 13 else
                    "E" if x == 14 else
                    "F" if x == 15 else -1
                    for x in __convert_base(inp,8)]))


def convert_to_hex(inp):
    if inp < 0:
        return convert_to_hex(-inp)
    return (inp, "".join([str(x) if x <= 9 else 
                    "A" if x == 10 else 
                    "B" if x == 11 else
                    "C" if x == 12 else 
                    "D" if x == 13 else
                    "E" if x == 14 else
                    "F" if x == 15 else -1
                    for x in __convert_base(inp,16)]))

def __convert_to_int(inp,fraction=False):
    #focntion de conversion vers entier ou fraction de base 10
    return [inp[x]/2**(x+1) for x in range(len(inp))] if fraction else [inp[len(inp)-1-x]*2**x for x in range(0,len(inp))]

def convert_to_base_10(inp):
    if not isinstance(inp,list):
        # l'inpout est fauw cela convertie une list bin vers un entier de base 10
        #et inp doiit être positif
        return (convert_to_bin(inp) if inp > 0 else convert_to_bin(-inp) ,inp if inp > 0 else -inp)
    return sum([inp[len(inp)-1-x]*2**x for x in range(0,len(inp))])


class __base:

    def __init__(self,name,base,Nsignificand,bias,Nmantissa):
        self._name = name
        self._base = base
        self._Nsignificand = Nsignificand
        self._bias = bias
        self._Nmantissa = Nmantissa

    @property
    def name(self):
        return self._name
    @property
    def base(self):
        return self._base
    @property
    def Nsignificand(self):
        return self._Nsignificand
    @property
    def bias(self):
        return self._bias
    @property
    def Nmantissa(self):
        return self._Nmantissa

def __check_base(inp):
    if not isinstance(inp.name,str):
        raise RuntimeError(f"base type {type(inp.name)} not str")
    if not isinstance(inp.base,int):
        raise RuntimeError(f"base type {type(inp.base)} not int")
    if not isinstance(inp.Nsignificand,int):
        raise RuntimeError(f"base type {type(inp.Nsignificand)} not int")
    if not isinstance(inp.bias,int):
        raise RuntimeError(f"base type {type(inp.bias)} not int")
    if not isinstance(inp.Nmantissa,int):
        raise RuntimeError(f"base type {type(inp.Nmantissa)} not int")

    if (inp.Nmantissa + inp.Nsignificand +1) != inp.base:
        raise RuntimeError(f"base not correct {inp.base}")
    if 2**(inp.Nsignificand-1)-1 != inp.bias:
        raise RuntimeError(f"base {inp.base} bias {inp.bias} isnt {2**(inp.Nsignificand-1)-1}")

__base_table = {
    16 :__base("Half precision",16,               5,    15, 10),
    32 :__base("Single precision",32,             8,   127, 23),
    64 :__base("Double precision",64,         11,  1023, 52),
    128:__base("Quadruple precision",128 ,15, 16383,112),
    256:__base("Octuple precision",256    ,19,262143,236)
}

for __x in __base_table.keys():
    __check_base(__base_table[__x])

def float_to_ieee(inp,bas=__base_table[16]):
    __check_base(bas)
    B = bas

    if inp == 0:
        raise RuntimeError(0)
    inp = float(inp)

    significand = []
    mantissa = []

    interger = None
    fraction = None

    interger , fraction = str(inp).split(".")
    interger , fraction = int(interger) , float(fraction)
    if interger != 0:
        interger = convert_to_bin(-int(interger)) if inp < 0 else convert_to_bin(int(interger))
    else:
        interger = [0]
    interger.pop(0) 

    significand = convert_to_bin(B.bias + len(interger))

    fraction =  fraction/10**(len(str(fraction))-2)
    

    for x in range(B.Nmantissa - len(interger)):
        fraction = fraction *2
        if fraction >= 1:
            mantissa.append(1)
            fraction = fraction - 1
        else:
            mantissa.append(0)

    mantissa = interger + mantissa
    
    fill = [0 for x in range(B.Nsignificand-len(significand))]

    #test de sécurité
    assert len(mantissa) == B.Nmantissa
    assert len(significand) + len(fill) == B.Nsignificand

    return [1] + fill + significand + mantissa if inp < 0 else [0] + fill + significand + mantissa

def ieee_to_float(inp ,bas =None):
    if not isinstance(inp,list):
        #on peut refaire le format de retour incorrect en
        # question futur , réponse 
        return (float_to_ieee(inp),float(inp))
        #si inp n'est pas une list comme attendu cela est la cas pour la génération
        #on retourne la fonction inverse
    B = None
    if bas:
        __check_base(bas)
        B = bas
        #si une base spécifique est fournie on la check
    else:
        try:
            B = __base_table[len(inp)]
            #sinon on prend la longeur et on regarde dans la table de base
        except Exception as exce:
            raise exce
    if len(inp) != B.base:
        raise RuntimeError("__base for iee to float invalide {} expected {}".format(len(inp),B.__base))
    
    e = sum(__convert_to_int(inp[1:1+B.Nsignificand])) - B.bias
    #on calcule l'exponent
    ex = (1+sum(__convert_to_int(inp[1+B.Nsignificand:1+B.Nsignificand+B.Nmantissa],True)))*(2**e)
    #calcule 1+mantisse x 2^exponent
    return -1* ex if inp[0] else ex #negatif si le premier bit est 1

def int_to_c2(inp,bas = 8):
    #par défaut la base est 8
    if inp > 0:
        x = convert_to_bin(inp)
        fill = [0 for x in range(8-len(x))]
        return fill + x
    else:
        return [0 for x in range(8- len(convert_to_bin(2**bas-(-inp)))) ] + convert_to_bin(2**bas-(-inp))
        
def c2_to_int(inp):
    if not isinstance(inp,list):
        return (int_to_c2(inp) ,inp)
        #si inp n'est pas une list comme attendu cela est la cas pour la génération
        #on retourne la fonction inverse
    return -1*2**(len(inp)-1) + sum(__convert_to_int(inp[1::])) if inp[0] else sum(__convert_to_int(inp[1::]))