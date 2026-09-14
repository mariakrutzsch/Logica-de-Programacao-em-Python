#1. Estruturas condicionais

nota = 6

if nota >= 7:
    print('Aprovado')
elif nota >= 5:
    print('Recuperação')
else:
    print('Reprovado')

#2. Condições com operadores lógicos
#and -> todas as condições devem ser verdadeiras
#or -> pelo menos uma condição deve ser verdadeira
#not -> inverte o resultado

idade = 20
ingresso = True

if idade >= 18 and ingresso:
    print("Entrada Permitida")
else:
    print("Entrada não permitida")

#3. Estrutura de repetição

contador = 1

while contador <= 5:
    print(contador)
    contador += 1

#4. Estrutura de repetição for

for numero in range (1,6):
    print(numero)

#5. Percorrendo uma lista
nomes = ["Ana" , "Maria" , "Valentina" , "Chrystine"]

for nome in nomes:
    print(nome)

#6. break
#O brack interrompe completamente a repetição
#O pass não executa nenhuma ação
#O continue interrompe apenas

for numero in range(1,11):
    if numero == 7:
        #break
        #pass
        continue

    print(numero)

#7. Condição dentro da repetição

for numero in range(1,11):
    if numero % 2 == 0:
        print(f"{numero} é par")
    else:
        print(f"{numero} é Ímpar")