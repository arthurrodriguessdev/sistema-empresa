from modelos.funcionario import Funcionario

class Gerente(Funcionario):
    BONIFICACAO = 20

    def __init__(self, nome, cpf, data_nascimento, matricula, salario_base):
        super().__init__(nome, cpf, data_nascimento, matricula, salario_base)

     
    #override
    def calcular_salario(self):
        salario = self.salario_base + ((self.BONIFICACAO * self.salario_base) / 100)

        return salario

    


