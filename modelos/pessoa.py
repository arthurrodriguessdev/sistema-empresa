class Pessoa:
    def __init__(self, nome, cpf, data_nascimento):
        self.nome = nome
        self.__cpf = cpf 
        self.data_nascimento = data_nascimento

    @property
    def cpf(self):
        return self.__cpf