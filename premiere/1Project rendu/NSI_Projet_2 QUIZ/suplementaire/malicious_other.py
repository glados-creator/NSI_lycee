def convert_base(inp,bas = 2 ,bigbase = False):
    ret = []
    level = 0
    while inp - bas**level >= 0:
        level = level + 1
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
    return convert_base(inp,2)

def convert_to_int(inp,fraction=False):
    return [inp[x]/2**(x+1) for x in range(len(inp))] if fraction else [inp[len(inp)-1-x]*2**x for x in range(0,len(inp))]

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

__base_table = {
    16 :__base("Half precision",16,               5,    15, 10),
    32 :__base("Single precision",32,             8,   127, 23),
    64 :__base("Double precision",64,         11,  1023, 52),
    128:__base("Quadruple precision",128 ,15, 16383,112),
    256:__base("Octuple precision",256    ,19,262143,236)
}


def float_to_ieee(inp,bas=__base_table[16],fr=False):
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
    
    
    if fraction != 0 and fr:
        print("fraction restante ",fraction)
    #décommenter ce code levra une exception pour chaque erreur d'arroundie de l'ieee 754 ->oui
    

    mantissa = interger + mantissa
    
    fill = [0 for x in range(B.Nsignificand-len(significand))]

    assert len(mantissa) == B.Nmantissa
    assert len(significand) + len(fill) == B.Nsignificand

    return [1] + fill + significand + mantissa if inp < 0 else [0] + fill + significand + mantissa

def ieee_to_float(inp):
    B = __base_table[len(inp)]
    if len(inp) != B.base:
        raise RuntimeError("__base for iee to float invalide {} expected {}".format(len(inp),B.__base))
    e = sum(convert_to_int(inp[1:1+B.Nsignificand])) - B.bias
    ex = (1+sum(convert_to_int(inp[1+B.Nsignificand:1+B.Nsignificand+B.Nmantissa],True)))*(2**e)
    return -1* ex if inp[0] else ex 

x = 1
while True:
    print("x ",x)
    try:
        if not x == 0:
            assert ieee_to_float(float_to_ieee(x,__base_table[16],True)) == x
    except AssertionError:
        print("bin ", "".join([str(x) for x in float_to_ieee(x)]))
        print("conv back " , ieee_to_float(float_to_ieee(x)))
        print("delta x", x-ieee_to_float(float_to_ieee(x)))
        print("")
    except Exception as ex:
        print(ex)
        print("")
    x = x +0.01
