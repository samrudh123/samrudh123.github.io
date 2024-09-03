from decimal import Decimal
from decimal import getcontext
from math import pi
import decimal

class MyMath():
    tolerance=1e-100
    precision=20
    getcontext().prec = precision
    ln_base = 2.7182818284590452238
    
    '''
    To Change all the above variables, create an object and set the parameters
    Example:
    a = MyMath(precision = 10)  
    
    and use the following functions using that object
    Example:
    a.exp(1)
    
    If you have created an object and not set any paramaters, they are set to default values
    (as shown in the __init__() method)
    
    '''
    def __init__(self, precision=20):
        getcontext().prec = precision
        
    @classmethod    
    def __doc__(cls):
        print(
'''
This is a math library created by me, using basic math operators(+, -, *, /) and Decimal library
(Imagine working with Python Floats)

If you ever encounter a situation where your program takes almost forever to run, 
it basically means you gave a very big input for the compiler to process.
(Press CTRL+C to end it in terminal)

The functions included in this library are:

a^b (pow(a,b))
square root of any real number(please put negative values as well) (sqrt(x))
absolute value (abs(x))
factorial of integer numbers (int_factorial(x))
e^x (exp(x))
natural logarithm (ln(x))
logarithm with any base (log(x, base))
sin(x)
cos(x)
tan(x)
'''
            )

    @classmethod     
    def pow(cls, a, b):
        if(a==0 and b==0):
            return "NaN"
        
        
        if(type(b)==int):
            if(b>=0):
                final_out = MyMath.int_pow(a,b)
            else:
                final_out = 1/Decimal(MyMath.int_pow(a,MyMath.abs(b)))
        else:    
            if(a==0):
                return 0
            else:
                final_out = MyMath.exp(Decimal(b)*MyMath.ln(a))
        return final_out
    
        
    @classmethod
    def sqrt(cls, x):
        if(x<0):
            x = MyMath.abs(x)
            return f"{MyMath.sqrt(x)}i"
        else:
            return MyMath.pow(x, 0.5)
        
    @staticmethod
    def int_pow(a,b):
        if(type(b) == int and b>=0):
            if(b==0):
                return 1
            if(a==0 and b!=0):
                return 0
            int_pow_out = a
            for i in range(1,b):
                int_pow_out *= a
            return int_pow_out
        else:
            raise ValueError ("Cannot compute non-natural number power")

    @classmethod
    def abs(cls, x):
        if(type(x) == int or type(x) == float or type(x) == Decimal):
            if x>=0:
                return x
            else:
                return (-x)
        else:
            raise TypeError ("Function accepts only int and float type inputs")

    @classmethod
    def int_factorial(cls, x):
        if type(x) == int:
            prod = 1
            for i in range(x, 0, -1):
                prod *= i
            return prod
        else:
            raise TypeError ("Function accepts only int type inputs")
        
    @classmethod  
    def exp(cls, x):
        n=1
        final_out = 1
        curr_out = 0
        x=Decimal(x)
        while True:
            curr_out = Decimal(MyMath.int_pow(x, n))/Decimal(MyMath.int_factorial(n)) 
            
              
            if(MyMath.abs(curr_out) < cls.tolerance):
                break
            
            final_out += curr_out
            n+=1
        return final_out
      
    @classmethod    
    def ln(cls, x):
        power_adjust = 0
        final_out = 0
        curr_out = 0
        base = 2.718281828459045235
        
        if x<=0:
            raise ValueError ("Cannot Compute Logarithm of a non-positive number")
        
        while Decimal(x) > 1.0:
            x = Decimal(x)/Decimal(base)
            power_adjust+=1
            
        while Decimal(x) < 0.5:
            x = Decimal(x)*Decimal(base)
            power_adjust-=1
        
        s=1
        for i in range(1, 100):
            curr_out = s*Decimal((Decimal(MyMath.int_pow(x-1, i))/Decimal(i)))
            final_out += curr_out
            s=-s
            
        return final_out + power_adjust
    
    @classmethod
    def log(cls, x, base=10):
        return Decimal(MyMath.ln(x)/MyMath.ln(base))
    
    '''Here ln is natural logarithm ( Logarithm with base (MyMath.exp(1) "e") ) and log is logarithm with any base (default base is 10)'''
    
    @classmethod
    def sin(cls, x):
        n=1
        s=1
        final_out = 0
        curr_out = 0
        if(x>0):
            x = x % (2*pi)
        else:
            x = -(MyMath.abs(x) % (2*pi))  
        if(x==pi or x==-(pi)):
            return 0
        x=Decimal(x)
        while True:
            curr_out = s*Decimal((Decimal(MyMath.int_pow(x, n))/Decimal(MyMath.int_factorial(n))))
            
            if(MyMath.abs(curr_out) < cls.tolerance):
                break
            
            final_out += curr_out
            n=n+2
            s=-s
        if (MyMath.abs(final_out)<1e-7):
            final_out = 0
        if (final_out>0.99999999999):
            final_out = 1
        if (final_out<(-0.99999999999)):
            final_out = -1
            
        return final_out
    
    @classmethod
    def cos(cls, x):
        n=2
        s=-1
        final_out = 1
        curr_out = 0
        x=MyMath.abs(x)
        x = x%(2*pi)  
        x=Decimal(x)
        while True:
            curr_out = s*Decimal((Decimal(MyMath.int_pow(x, n))/Decimal(MyMath.int_factorial(n))))
            
            if(MyMath.abs(curr_out) < cls.tolerance):
                break
            
            final_out += curr_out
            n=n+2
            s=-s
        if (MyMath.abs(final_out)<1e-7):
            final_out = 0
        if (final_out>0.99999999999):
            final_out = 1
        if (final_out<(-0.99999999999)):
            final_out = -1
            
        return final_out
    
    @classmethod
    def tan(cls, x):
        try:
            return Decimal(MyMath.sin(x)/MyMath.cos(x))
        except ZeroDivisionError:
            return "NaN"