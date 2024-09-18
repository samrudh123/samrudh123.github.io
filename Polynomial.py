class Polynomial:
    """This is a Polynomial Class"""
    def __init__(self, input_list):
        for i in range(len(input_list)):
            if type(input_list[i]) == float or type(input_list[i]) == int:
                pass
            else:
                raise TypeError("Coefficients should be a real number")
        self.coeff_list = input_list[::-1]
        
    def __repr__(self):
        final_str = ""
        for i in range(len(self.coeff_list) - 1, 1, -1):
            if self.coeff_list[i] == 0:
                continue
            if self.coeff_list[i] == 1:
                final_str += f"x^{i} + "
            else:
                final_str += f"{self.coeff_list[i]}x^{i} + "    
        
        if self.coeff_list[1] != 0 and self.coeff_list[0] == 0:
            if self.coeff_list[1] == 1:
                final_str += "x + "
            else:
                final_str += f"{self.coeff_list[1]}x"
        elif self.coeff_list[1] != 0 and self.coeff_list[0] != 0:
            if self.coeff_list[1] == 1:
                final_str += f"x + {self.coeff_list[0]}"
            else:
                final_str += f"{self.coeff_list[1]}x + {self.coeff_list[0]}"
        elif self.coeff_list[1] == 0 and self.coeff_list[0] != 0:
            final_str += f"{self.coeff_list[0]}"
        else:
            pass
        if final_str[-2:] == "+ ":
            return final_str[:-2]
        return final_str
    
    def __add__(self, other):
        if isinstance(other, Polynomial):
            if len(self.coeff_list) > len(other.coeff_list):
                for i in range(len(other.coeff_list), len(self.coeff_list)):
                    other.coeff_list.append(0)
            if len(self.coeff_list) < len(other.coeff_list):
                for i in range(len(self.coeff_list), len(other.coeff_list)):
                    self.coeff_list.append(0)
                    
            result = Polynomial([0]*len(self.coeff_list))
            for i in range(len(self.coeff_list)):
                result.coeff_list[i] = self.coeff_list[i] + other.coeff_list[i]
            return result
        else:
            raise ValueError("Positional argument 2 not an instance of class Polynomial")
    
    def add(self, other):
        if isinstance(other, Polynomial):
            if len(self.coeff_list) > len(other.coeff_list):
                for i in range(len(other.coeff_list), len(self.coeff_list)):
                    other.coeff_list.append(0)
            if len(self.coeff_list) < len(other.coeff_list):
                for i in range(len(self.coeff_list), len(other.coeff_list)):
                    self.coeff_list.append(0)
                    
            result = Polynomial([0]*len(self.coeff_list))
            for i in range(len(self.coeff_list)):
                result.coeff_list[i] = self.coeff_list[i] + other.coeff_list[i]
            return result
        else:
            raise ValueError("Positional argument 2 not an instance of class Polynomial")
    
    def __sub__(self, other):
        if isinstance(other, Polynomial):
            if len(self.coeff_list) > len(other.coeff_list):
                for i in range(len(other.coeff_list), len(self.coeff_list)):
                    other.coeff_list.append(0)
            if len(self.coeff_list) < len(other.coeff_list):
                for i in range(len(self.coeff_list), len(other.coeff_list)):
                    self.coeff_list.append(0)
                    
            result = Polynomial([0]*len(self.coeff_list))
            for i in range(len(self.coeff_list)):
                result.coeff_list[i] = self.coeff_list[i] - other.coeff_list[i]
            return result
        else:
            raise ValueError("Positional argument 2 not an instance of class Polynomial") 
    
    def subtract(self, other):
        if isinstance(other, Polynomial):
            if len(self.coeff_list) > len(other.coeff_list):
                for i in range(len(other.coeff_list), len(self.coeff_list)):
                    other.coeff_list.append(0)
            if len(self.coeff_list) < len(other.coeff_list):
                for i in range(len(self.coeff_list), len(other.coeff_list)):
                    self.coeff_list.append(0)

            result = Polynomial([0]*len(self.coeff_list))
            for i in range(len(self.coeff_list)):
                result.coeff_list[i] = self.coeff_list[i] - other.coeff_list[i]
            return result
        else:
            raise ValueError("Positional argument 2 not an instance of class Polynomial") 
    
    def __mul__(self, other):
        if isinstance(other, Polynomial):
            if len(self.coeff_list) > len(other.coeff_list):
                for i in range(len(other.coeff_list), len(self.coeff_list)):
                    other.coeff_list.append(0)
            if len(self.coeff_list) < len(other.coeff_list):
                for i in range(len(self.coeff_list), len(other.coeff_list)):
                    self.coeff_list.append(0)
                    
            result = Polynomial([0]*(len(self.coeff_list) + len(other.coeff_list)))
            for i in range(len(self.coeff_list)):
                for j in range(len(other.coeff_list)):
                    result.coeff_list[i+j] += self.coeff_list[i] * other.coeff_list[j]
            return result
        else:
            raise ValueError("Positional argument 2 not an instance of class Polynomial")
    
    def multiply(self, other):
        if isinstance(other, Polynomial):
            if len(self.coeff_list) > len(other.coeff_list):
                for i in range(len(other.coeff_list), len(self.coeff_list)):
                    other.coeff_list.append(0)
            if len(self.coeff_list) < len(other.coeff_list):
                for i in range(len(self.coeff_list), len(other.coeff_list)):
                    self.coeff_list.append(0)
                    
            result = Polynomial([0]*(len(self.coeff_list) + len(other.coeff_list)))
            for i in range(len(self.coeff_list)):
                for j in range(len(other.coeff_list)):
                    result.coeff_list[i+j] += self.coeff_list[i] * other.coeff_list[j]
            return result
        else:
            raise ValueError("Positional argument 2 not an instance of class Polynomial")
        
    def evaluate(self, x):
        if type(x) == int or type(x) == float:
            result = 0
            for i in range(len(self.coeff_list)):
                result += self.coeff_list[i]*(x**i)
            return result
        else: 
            raise TypeError("Values at which polynomial is evaluated have to be a real number")