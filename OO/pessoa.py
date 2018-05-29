class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Ola {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42


if __name__ == '__main__':
    paulo = Pessoa(nome='Paulo')
    rafael = Pessoa(nome='Rafael')
    sidney = Pessoa(paulo, rafael, nome='Sidney')
    print(paulo.nome)
    print(sidney.nome)
    for filho in sidney.filhos:
        print(filho.nome)
    sidney.sobrenome = 'Barbosa'
    del paulo.filhos
    print(sidney.__dict__)
    print(paulo.__dict__)
    print(Pessoa.metodo_estatico(),sidney.metodo_estatico())
