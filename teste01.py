#Básico
nome=str(input("nome?\n"))
idade=int(input("idade?\n"))
n1=float(input("nota1?\n"))
n2=float(input("nota2?\n"))
media=float((n1+n2)/2)
print("Nome:{}, Idade:{}, e media:{} ".format(nome,idade,media))
print(type(nome));print(type(idade));print(type(media))
