#A CLASSE: O modelo (a planta)
#Definição de Classe e Atributos
class Celular:
    def __init__(self , marca , modelo , cor , bateria = 100):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.bateria = bateria
        self.ligado = False

    def ligar(self):
        if self.bateria == 0:
            print("Sem bateria! Coloque para carregar")
        else:
            self.ligado = True
            print(f"{self.modelo} Ligado!")

#Os Objetos: Criados a partir da Classe (as "casas")

#Criação de Objeto (Celular1) da Classe Celular

celular1 = Celular ("Sansung" , "Galaxy S23" , "Preto")

celular2 = Celular ("Motorola" , "MotoG" , "Azul" , 30)

#Acessando e alterando atributos
print(celular2.marca)

#Também podemos alterar diretamente
celular1.cor = "Branco"
print(celular1.cor)

#Chamando Métodos
celular1.ligar()


# ATIVIDADE 1 - CACHORRO
class Cachorro:
    def __init__(self , nome , raca , idade , latir = True):
        self.nome = nome
        self.raca = raca
        self.idade = idade


    def latir(self):
        if self.latir == True:
            print("Rex diz: Au Au!")
        else:
            self.ligado = False
            print(f"{self.nome} não late!")

    def mostrar(self):
        print(self.nome, self.raca, self.idade)


#Os Objetos: Criados a partir da Classe (as "casas")

#Criação de Objeto (Celular1) da Classe Celular

cachorro1 = Cachorro ("Rex" , "Vira-lata" , 5)

cachorro2 = Cachorro ("Kinder" , "Pinscher" , 2)

#Acessando e alterando atributos
print(cachorro1.nome)

#Também podemos alterar diretamente
cachorro1.idade = 4
print(cachorro1.idade)

#Chamando Métodos
cachorro1.latir()
cachorro1.mostrar()
