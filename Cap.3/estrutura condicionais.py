MAIOR_IDADE = 18
IDADE_ESPECIAL = 12 

idade = int(input("Informe sua Idade: "))

# ? IF / ELSE / ELIF

# ! EXEMPLO 1

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH")

if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a CNH")
    
# ! EXEMPLO 2

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH")
else:
    print("Ainda não pode tirar a CNH")

# ! EXEMPLO 3

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teoricas, mas não pode faer aulas praticas")    
else:
    print("Ainda não pode tirar a CNH")
    
# ? IF ANINHADO

conta = int(input("Digite qual o tipo da sua conta: \n 1- para normal. \n 2- para especial\n"))

if conta == 1:
    print("Sua conta é normal\n")
    print("VocÇe não pode fazer saque")
else:
    print("Sua conta é especial\n")
    saque = int(input("Você deseja fazer saque? Escolha sua opção: \n 1- SIM\n 2 - NÃO\n"))
    if saque == 1:
        valor = float(input("Qual o valor do saque que deseja efetuar? "))
        print(f"Você sacou o total de R${valor:.2f}")
    else:
        print("OK!")

