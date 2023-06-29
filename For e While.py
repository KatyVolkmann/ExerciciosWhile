# Ex 1

N = float(input("Digite uma nota: "))

while N < 0 or N > 10:
    print("Valor inválido, digite uma nota de 0 a 10")
    N = float(input("Digite uma nota: "))
    
print("Nota digitada: ", N)

# Ex 2

Usuario = input("Informe o nome do usuário: ")
Senha = input("Informe a senha do usuário: ")

while Usuario == Senha:
    print("Usuário e Senha não podem ser iguais!")
    Usuario = input("Informe o nome do usuário: ")
    Senha = input("Informe a senha do usuário: ")
    
print("Usuário e Senha criados com Sucesso!")

# Ex 3

print("Prencha as informações abaixo:")
nome = input("Nome: ")
idade = int(input("Idade: "))
salario = float(input("Salário: "))
sexo = input("Sexo: ")
estCivil = input("Estado Civil: ")

while len(nome) <= 3 or idade < 0 or idade > 150 or salario <= 0 or sexo.lower() not in ["f", "m"] or estCivil.lower() not in ["s", "c", "v", "d"]:
    if len(nome) < 3:
        print("Nome inválido, digite novamente.")
    if idade < 0 or idade > 150:
        print("Idade inválida, digite novamente.")
    if salario <= 0 :
        print("Salário inválido, digite novamente.")
    if sexo.lower() not in ["f", "m"]: 
        print("Sexo inválido, digite f ou m.")
    if estCivil.lower() not in ["s", "c", "v", "d"]:
        print("Estado Civil inválido, digite s, c, v ou d.")
        
    nome = input("Nome: ")
    idade = input("Idade: ")
    salario = float(input("Salário: "))
    sexo = input("Sexo: ")
    estCivil = input("Estado Civil: ")

print("Informações validadas!")
print("Nome: ", nome)
print("Idade: ", idade)
print("Salário: ", salario)
print("Sexo: ", sexo)
print("Estado Civil: ", estCivil)

# Ex 4 

popPA = 80000
TaxA = 0.03
popPB = 200000
TaxB = 0.015
anos = 0

while popPA < popPB:
    crescimentoA = popPA*TaxA
    popPA = popPA + crescimentoA
    crescimentoB = popPB*TaxB
    popPB  = popPB + crescimentoB
    anos += 1

print("Levará ", anos, "anos para a população A ultrapassar ou igualar a população B, sendo:")
print ("população A: ", round(popPA,0), " habitantes")
print ("população B: ", round(popPB,0), " habitantes")