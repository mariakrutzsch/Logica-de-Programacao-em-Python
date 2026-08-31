#AULA: OPERADORES LÓGICOS E ESTRUTURAS CONDICIONAIS
#1. OPERADORES LÓGICOS

#and
# Todas as condições precisam ser verdadeirassssss.

idade = 20
possui_carteira = True

resultado = idade >= 18 and possui_carteira
print(resultado)

#or
#Pelo menos uma condição precisa ser verdadeira.

idade = 16
acompanhado =  True

resultado = idade >= 18 or acompanhado
print(resultado)

#not
#Inverte o resultado de uma condição

aluno_matriculado = True
print(not aluno_matriculado)

#Operadores de Comparação

idade = 18

print(idade == 18)
print(idade != 18)
print(idade > 18)
print(idade < 18)
print(idade >= 18)
print(idade <= 18)

#3. Estrutura IF

if idade >= 18:
    print("maior de idade")

#4. Estrutura IF/else

if idade = 16
if idade >= 18:
    print("maior de idade")
else:
    print("menor de idade")