class Kalkulator:
    operand1 = 5
    operand2 = 2

    def __init__(self,op1,op2):
        self.operand1 = op1
        self.operand2 = op2

    def add(self):
        result = self.operand1 + self.operand2
        return result
    def sub(self):
        return self.operand1 - self.operand2
    def mul(self):
        return self.operand1 * self.operand2
    def div(self):
        return self.operand1 / self.operand2


a = int(input("unesite  operand1: "))
b = int(input("unesite  operand2: "))
k = Kalkulator(a,b)
#k2 = Kalkulator()


result = k.add()
print(k.operand1, " + ", k.operand2, " = ", result)
result = k.sub()
print(k.operand1, " - ", k.operand2, " = ", result)
result = k.mul()
print(k.operand1, " * ", k.operand2, " = ", result)
result = k.div()
print(k.operand1, " / ", k.operand2, " = ", result)