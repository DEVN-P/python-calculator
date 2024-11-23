class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        for i in range(abs(b)):
            result = self.add(result, a)

        if (a >= 0 and b >= 0):
            return result
        else:
            return -result

    def divide(self, a, b):
        absA = abs(a)
        absB = abs(b)

        result = 0
        while absA >= absB:
            absA = self.subtract(absA, absB)
            result += 1
        
        if (a >= 0 and b >= 0) or (a < 0 and b < 0):
            return result
        else:
            return -result
    
    def modulo(self, a, b):
        while a >= b:
            a = a - b
        return a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))