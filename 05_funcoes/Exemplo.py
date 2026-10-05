#O que que é uma FUNÇÃO:

#Uma FUNÇÃO é um bloco de código criado para realizar uma detarminada tarefa.
#Ela permite organizar e reutilizar código.

#1. Criando uma FUNÇÃO
#Utilizar a palavra "def" para uma FUNÇÃO

def saudacao():
    print("Olá, Seja Bem-Vindo!")

saudacao()

#2. Criando uma FUNÇÃO com parâmetro
#Parâmetros permitem enviar informações para a função

def saudacao(nome):
    print(f"Ola {nome}")

saudacao("Maria")
saudacao("Ana")

#3. Mais de um Parâmetro
def apresentar(nome , idade):
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")

apresentar("Maria" , 17)
apresentar("João" , 20)

#4. FUNÇÃO  com calculo

def somar (numero_1 , numero_2):
    resultado = numero_1 + numero_2
    print(f"Resultado:{resultado}")

somar(10 , 20)
somar(10 , 90)

#5. Retornando um valor
#"Return" devolve o valor para o local onde a FUNÇÂO foi chamada

def somar (numero_1 , numero_2):
    return numero_1 + numero_2

print(somar(10 , 5))

#6. FUNÇÃO com condição
def verificarIdade(idade):
    if idade >= 18:
        return "Maior de 18 anos"
    else:
        return "Menor de 18 anos"

print(verificarIdade(20))

#7. Parâmetro com valor padrão
def suadacao(nome = "Aluno"):
    print(f"Olá {nome}")

saudacao("João")

#8. FUNÇÃO  utlizando lista
def calcularMedia(notas):
    soma = 0
    for nota in notas:
        soma += nota

    return soma / len(notas)

notas = [7 , 8 , 9 , 10]
media = calcularMedia(notas)
print(f"Média: {media}")

#9. FUNÇÕES PARA ORGANIZAR UM PROGRAMA
def cadastrar_produto():

    nome = input("Digite o nome do produto: ")
    preco = float(input("Difite o preço: "))
    return nome, preco

def exibir_produto(nome , preco):

    print("\n---PRODUTO---")
    print(f"Nome: {nome}")
    print(f"Preço: {preco:.2f}")

nome, preco = cadastrar_produto()
exibir_produto(nome, preco)