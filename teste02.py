#Equação do 2º Grau
a=float(input("Digite o Valor A:\n"))
b=float(input("Digite o Valor B:\n"))
c=float(input("Digite o Valor C:\n"))
delta=float((b**2)-(4*a*c))
x1=float((((-1)*b)+(delta**(1/2)))/(2*a))
x2=float((((-1)*b)-(delta**(1/2)))/(2*a))
print("Delta={}, x1={}, x2={} ".format(delta,x1,x2))
