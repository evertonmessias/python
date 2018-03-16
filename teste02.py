#Equação do 2º Grau
from math import sqrt, pow
a=float(input("Digite o Valor A:\n"))
b=float(input("Digite o Valor B:\n"))
c=float(input("Digite o Valor C:\n"))
delta=float((pow(b,2))-(4*a*c))
x1=float((((-1)*b)+(sqrt(delta)))/(2*a))
x2=float((((-1)*b)-(sqrt(delta)))/(2*a))
print("Delta={}, x1={:.2f}, x2={:.2f} ".format(delta,x1,x2))
