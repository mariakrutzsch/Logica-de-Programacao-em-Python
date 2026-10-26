#1. Encapsulamento
#Proteger o salário para que só mude seguindo regras

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.__salario = salario #Privado: com dois sublinhados

    def apresentar(self):
        print(f"Sou  {self.nome} e ganho R${self.__salario:.2f}")

    #@property deixa ler o salario como se fosse atributo
    @property
    def salario(self):
        return self.__salario

    def dar_aumento(self, porcentagem):
        if porcentagem <= 0:
            print(f"Aumento inválido para {self.nome}")
            return

        self.__salario = self.__salario * (1 + porcentagem / 100)
        print(f"{self.nome} recebeu {porcentagem}% de aumento")


###################################################################################
ana = Funcionario("ana" , 3000)
ana.__salario = 4000
print(ana.salario)
ana.apresentar()
ana.dar_aumento(20)

#O try/excepté um bloco usado em programação para tratar erro

try:
    ana.salario = 10000
except AttributeError:
        print("Não é permitido alterar o salário diretamente")

try:
    print(ana.__salario)
except AttributeError:
    print("O atributo __salalrio não pode ser acessado de fora.")