# texto = input("Digite uma palavra: ")
# vogal = "AEIOU"

# for letra in texto:
#     if letra.upper() in vogal:
#         print(letra, end="")
        
# print()
number = int(input("Digite um número: "))

for num in range(0, (number*10)+1, number):
    print(num, end=" ")
else:
    print(f"\nEssa é a tabuada do {number}")