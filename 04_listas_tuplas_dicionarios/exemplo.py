#Listas, Tuplas e Dicionários

#1. LISTA
#São utilizadas para armazenar vários valores dentro de uma única variável.
nome = ["Ana" , "Maria" , "João" , "Joana"]
print(nome)

#2. Acessando Elementos da LISTA
print(nome[2])
#Podemos acessar o último elemento usando o -1
print(nome[-1])

#3. Alterando Elementos
nome[0] = "Pedro"
print(nome)

#4. Adicionar Elementos
#append() - Adiciona um elemento no final da lista
nome.append("Lucas")
print(nome)

#insert() - Adiciona um elemento em uma posição específica.
nome.insert(1, "Mariana")
print(nome)

#5. Removendo Elementos
#Remove um elemento pelo valor

nome.remove("Lucas")
print(nome)

#pop() - remove um elemento pelo índice
nome.pop(0)
print(nome)

#6. Tamanho da Lista
#len() - Informa a quantidade de elemntos
print(len(nome))

#7 Percorrendo uma Lista
for nome in nome:
    print(nome)

#8. Verificando se um elemento existe
if "João" in nome:
    print("João está na lista")
else:
    print("João não está na lista")

#9. Lista com diferentes tipos de dados
dados = ["João" , 18 , 1.75 , True]
print(dados)

#10. Lista de Números.
notas = [7.5 , 8.0 , 6.5 , 9.0]

soma = 0
for nota in notas:
    soma = soma + nota
    media = soma / len(notas)
    print(f"Média: {media}")

#1. TUPLAS
#São semelhantes às listas (não podem ser alteradas).

coordenadas = (10 , 20)
print(coordenadas)

print(coordenadas[0])

#1. DICIONÁRIOS
#Dicionários armazeam informações no formato: chave: valor
aluno = {
    "nome" : "Carlos",
    "idade" : 17,
    "nota" : 8.5
}
print(aluno)