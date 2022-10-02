class Calculator:
    def add(self,number1,number2):
        return  number1 + number2
    def substract(self,number1,number2):
        return number1 - number2
    def multiply(self,number1,number2):
        return  number1 * number2
    def delit(self,number1,number2):
        return number1 / number2
calculate = Calculator()
print(calculate.add(10,5))
print(calculate.substract(10,5))
print(calculate.multiply(10,5))
print(calculate.delit(10,5))
