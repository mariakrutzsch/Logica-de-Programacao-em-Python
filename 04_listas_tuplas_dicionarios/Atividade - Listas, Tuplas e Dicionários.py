#ATIVIDADE - Listas, Tuplas e Dicionários

#ATIVIDADE 1. Lista - Nomes dos Filmes e exibição
filmes = ["Depois do Universo", "Ela é o Cara", "De Repente 30", "As Branquelas", "A Nova Cinderela" ]
print(filmes)

#Exibindo o Primeiro Filme
print("Primeiro Filme:" ,filmes[0])

#Exibindo o Último Filme
print("Último Filme:" , filmes[-1])

#Adicionando um novo filme
filmes.append("O Senor dos Anéis")
print(filmes)

#Adicionando um novo filme em posição específica
filmes.insert(2, "O Diabo Veste Prada")
print(filmes)

#Removendo um filme da lista
filmes.remove("As Branquelas")
print(filmes)

#Alterando o nome de um dos filmes
filmes[1] = "Miss Simpatia"
print(filmes)

#Quantidade de filmes cadastrados
print(len(filmes))

#Verificando se "Miss Simpatia" está na lista
if "Miss Simpatia" in filmes:
    print("O Filme Miss Simpatia está na lista")
else:
    print("O Filme Miss Simpatia não está na lista")


#ATIVIDADE 2. Lista - Notas e exibição
notas = [8.0, 8,5, 9.0, 9.5, 10.0]
print(notas)

#Soma e média das notas
for nota in notas:
    soma = soma + nota
    print(f"Soma: {soma}")
    media = soma / len(notas)
    print(f"Média: {media}")

#Maior nota
maior = notas[0]
for nota in notas:
    if nota > maior:
        maior = nota

print(f"A maior nota é: {maior}")

#Menor nota
menor = notas[0]
for nota in notas:
    if nota < menor:
        menor = nota

print(f"A menor nota é: {menor}")

#Nota = 10
if 10 in notas:
    print("Existe uma nota = 10")

#Estudante Aprovado ou Reprovado
if media >= 7:
    print("Estudante Aprovado!")
else:
    print("Estudante Reprovado!")


#3. Informação - Produto

#Nome, Categoria, Preço e Código
produto = ("Notebook", "Informática", 3650, 56789)

#Exibindo as informações individualmente
print("Nome do produto: ")
print(produto[0])

print("Categoria: ")
print(produto[1])

print("Preço: ")
print(produto[2])

print("Código do produto: ")
print(produto[3])

#Quantidade de Informações
print("Informações do produto: ")

for informacao in produto:
    print(informacao)

#Alterando informações
print(f"Quantidade de informações: {len(produto)}")

#Observação
produto[0] = "Computador"

print("Não é possível alterar uma informação da tupla.")
print("As tuplas não podem ser alteradas depois de criadas.")


#4. Cadastro de funcionário
#Cadastro
funcionario = {
    "nome": "Maria",
    "idade": 26,
    "cargo": "Programadora",
    "salario": 3900,
    "setor": "Tecnologia"
}

print("\nNome: ")
print(funcionario["nome"])

print("\nIdade: ")
print(funcionario["idade"])

print("\nCargo: ")
print(funcionario["cargo"])

print("\nSalário: ")
print(funcionario["salario"])

print("\nSetor: ")
print(funcionario["setor"])


funcionario["salario"] = 4000

print("\nNovo salário: ")
print(funcionario["salario"])


funcionario["email"] = "maria@email.com"

print("\nCadastro com nova informação: ")
print(funcionario)


funcionario.pop("idade")

print("\nCadastro após remover a idade: ")
print(funcionario)


if "cargo" in funcionario:
    print("\nA chave cargo existe no cadastro")
else:
    print("\nA chave cargo não existe no cadastro")


print("\nInformações do funcionário: ")

for chave in funcionario:
    print(chave, ":", funcionario[chave])


#5. Sistema de estoque
estoque = [
    {
        "nome": "Notebook",
        "categoria": "Informática",
        "preco": 3650,
        "quantidade": 6
    },
    {
        "nome": "Mouse",
        "categoria": "Periféricos",
        "preco": 85,
        "quantidade": 16
    },
    {
        "nome": "Teclado",
        "categoria": "Periféricos",
        "preco": 155,
        "quantidade": 9
    },
    {
        "nome": "Monitor",
        "categoria": "Informática",
        "preco": 1300,
        "quantidade": 10
    },
    {
        "nome": "Headset",
        "categoria": "Periféricos",
        "preco": 220,
        "quantidade": 3
    }
]


print("\nProdutos cadastrados: ")
print(estoque)


print("\nInformações dos produtos: ")

for produto in estoque:
    print("Nome:", produto["nome"])
    print("Preço:", produto["preco"])
    print("Quantidade:", produto["quantidade"])
    print()


quantidade_total = 0

for produto in estoque:
    quantidade_total = quantidade_total + produto["quantidade"]

print(f"A quantidade total de itens no estoque é: {quantidade_total}")


valor_total = 0

for produto in estoque:
    valor = produto["preco"] * produto["quantidade"]
    valor_total = valor_total + valor

print(f"\nO valor total do estoque é: R$ {valor_total}")


print("\nProdutos com menos de 10 unidades: ")

for produto in estoque:
    if produto["quantidade"] < 10:
        print(produto["nome"])


nome_produto = "Mouse"

encontrado = False

for produto in estoque:
    if produto["nome"] == nome_produto:
        encontrado = True

if encontrado:
    print(f"\n{nome_produto} está cadastrado")
else:
    print(f"\n{nome_produto} não está cadastrado")


for produto in estoque:
    if produto["nome"] == "Mouse":
        produto["quantidade"] = 21

print("\nQuantidade do Mouse alterada.")


novo_produto = {
    "nome": "Webcam",
    "categoria": "Periféricos",
    "preco": 320,
    "quantidade": 8
}

estoque.append(novo_produto)

#10:
print("\nRelatório final do estoque: ")

for produto in estoque:
    print("Nome:", produto["nome"])
    print("Categoria:", produto["categoria"])
    print("Preço:", produto["preco"])
    print("Quantidade:", produto["quantidade"])
