from funcionario import Funcionario

class Gerente(Funcionario):
    BONIFICACAO = 20

    def __init__(self, nome, cpf, data_nascimento, matricula, salario_base, faltas):
        super().__init__(nome, cpf, data_nascimento, matricula, salario_base, faltas)


    #override
    def calcular_salario(self):
        salario = self.salario_base + ((self.BONIFICACAO * self.salario_base) / 100)

        return salario
    

    def registrar_falta(self):
        super().registrar_falta()
    

g1 = Gerente("Arthur", "83893939", "18/01/2007", 1899, 2000, 8)
print(g1.calcular_salario())

