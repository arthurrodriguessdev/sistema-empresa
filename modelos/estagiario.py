from vendedor import Vendedor

class Estagiario(Vendedor):
    def __init__(self, nome, cpf, data_nascimento, matricula, salario_base, faltas, comissao, desconto):
        super().__init__(nome, cpf, data_nascimento, matricula, salario_base, faltas, comissao)

        self.__desconto = desconto

        
    @property
    def desconto(self):
        return self.__desconto
    
    
    #override
    def calcular_salario(self):
        salario = self.salario_base - (self.faltas * self.desconto) + self.comissao
        return salario

    
    def registrar_falta(self):
        super().registrar_falta()
    
v1 = Estagiario("Arthur", "83893939", "18/01/2007", 1899, 2000, 8, 100, 10)
print(v1.calcular_salario())




