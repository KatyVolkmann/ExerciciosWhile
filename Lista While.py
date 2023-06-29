# Ex 1

n = 1

while n < 11:
   print(n)
   n += 1
    
# Ex 2

n = 2

while n < 21:
    print(n)
    n += 2
    
# Ex 3

n = int(input("Digite um número: "))
cont = 0  

while cont <= n:
    print(cont)
    cont += 1
    
# Ex 4

n = int(input("Digite um número: "))
cont = 1  

while cont <= 10:
    result = n * cont
    print(n, "*", cont, " = ", result)
    cont += 1
    
# Ex 5 
senha = input("Digite uma senha: ")

while senha != '1234':
    senha = input("Digite uma senha:")

print("Senha criada com sucesso!")

# Ex 7

n = int(input("Digite um número: "))
soma = 0 

while n >= 0:
    soma = soma + n
    n = int(input("Digite um número: "))

print("A soma dos números digitados é: ", soma)

