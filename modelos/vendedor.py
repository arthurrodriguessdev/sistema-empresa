from funcionario import Funcionario

class Vendedor(Funcionario):
    BONIFICACAO = 5

    def __init__(self, nome, cpf, data_nascimento, matricula, salario_base, faltas, comissao):
        super().__init__(nome, cpf, data_nascimento, matricula, salario_base, faltas)

        self.__comissao = comissao


    @property
    def comissao(self):
        return self.__comissao
    
    
    #override
    def calcular_salario(self):
        salario = self.salario_base + ((self.BONIFICACAO * self.salario_base) / 100) + self.comissao

        return salario
    

    def registrar_falta(self):
        super().registrar_falta()
    
v1 = Vendedor("Arthur", "83893939", "18/01/2007", 1899, 2000, 8, 100)

