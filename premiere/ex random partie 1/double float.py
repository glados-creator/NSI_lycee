from struct import pack,unpack
import unittest

def floattohexa(s,e,m):
    if not s == 0 or s == 1 :
        return -1
    else:
        if s == 1:
         return -1*((m+1)*2**(e-127 if e > 129 else 1023))  
        else :
            m = (m+1)
            e = (e - 127 if e < 129 else 1023)
            return m*2**e

def ex(s,e,m):
    return -1 if not s == 0 or s == 1 else -1*((m+1)*2**(e-127 if e < 129 else 1023)) if s == 1 else (m+1)*2**(e-127 if e < 129 else 1023) 

f = [(0, 23, 2567051787601183),(0, 127, 0),(1, 1, 2567051787601183)]

class eeee(unittest.TestCase):
    def test_ok(self):
        for x in f:
            print("test : ",*x)
            print(floattohexa(*x))
            print(ex(*x))
            self.assertEqual(floattohexa(*x),ex(*x))

if __name__ == "__main__":
    unittest.main()
