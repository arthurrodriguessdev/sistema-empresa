from modelos.pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome, cpf, data_nascimento, matricula, salario_base):
        super().__init__(nome, cpf, data_nascimento)

        self.matricula = matricula
        self.__salario_base = salario_base
        self.__faltas = 0


    @property
    def salario_base(self):
        return self.__salario_base
    

    @property
    def faltas(self):
        return self.__faltas

    def calcular_salario(self):
        return self.salario_base
    

    def registrar_falta(self):
        self.faltas += 1



