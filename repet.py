string = input("Digite uma string: ")
número = int(input("Digite um número: "))

multiplicação = string * número

if multiplicação != "":
    multiplicação =( string + " ") * número   
    print(multiplicação)
else:
 print("A string é vazia ou o número é zero.")
