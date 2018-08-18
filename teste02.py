#Equação do 2º Grau
import os
from math import sqrt, pow
r = str('s')
while r == 's':
    os.system("clear")
    print("\33[1;34m\n**Equacao do 2ºGrau**\n")    
    a=float(input("\33[0;34mDigite o Valor A:\n"))
    b=float(input("\33[0;34mDigite o Valor B:\n"))
    c=float(input("\33[0;34mDigite o Valor C:\n"))
    delta=float((pow(b,2))-(4*a*c))
    if a == 0:
        for c in range(2):
            print("\33[1;31m\nO valor A não pode ser zero!\n")
    elif delta > 0:
        x1=float((((-1)*b)+(sqrt(delta)))/(2*a))
        x2=float((((-1)*b)-(sqrt(delta)))/(2*a))
        print("\33[1;32m\nDelta={}, x1={:.2f}, x2={:.2f}\n".format(delta,x1,x2))
    else:
        print("\33[1;31m\nNão existe raiz real\n")
    r = str(input("\33[1;32m\nDeseja continuar? (s/n)"))
print ("\33[1;32m\nFIM\n")    
        
    
