# Créé par arthur.pavard, le 27/09/2021 en Python 3.7
import unittest

def x1():
    for i in range(0,101):
        if i % 15 == 0:
            yield "FizzBuzz"
        elif i % 3 == 0:
            yield "Fizz"
        elif i % 5 == 0 :
            yield "Buzz"
        else:
            yield i

x2 = [ "FizzBuzz" if i % 15 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0  else i for i in range(0,101)]

x1 = list(x1())

class Test(unittest.TestCase):
    def test_runx1(self):
        for x in range(1,len(x1)):
            if x % 15==0:
                self.assertEqual(x1[x],"FizzBuzz")
            elif x % 5==0:
                self.assertEqual(x1[x],"Buzz")
            elif x % 3==0:
                self.assertEqual(x1[x],"Fizz")
            else:
                self.assertEqual(x1[x],x)

    def test_runx2(self):
        for x in range(1,len(x2)):
            if x % 15==0:
                self.assertEqual(x2[x],"FizzBuzz")
            elif x % 5==0:
                self.assertEqual(x2[x],"Buzz")
            elif x % 3==0:
                self.assertEqual(x2[x],"Fizz")
            else:
                self.assertEqual(x2[x],x)
            
if __name__ == "__main__":
    unittest.main()
