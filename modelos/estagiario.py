from modelos.vendedor import Vendedor

class Estagiario(Vendedor):
    def __init__(self, nome, cpf, data_nascimento, matricula, salario_base, comissao, desconto):
        super().__init__(nome, cpf, data_nascimento, matricula, salario_base, comissao)
        self.__desconto = desconto

        
    @property
    def desconto(self):
        return self.__desconto
    
    
    #override
    def calcular_salario(self):
        salario = self.salario_base - (self.faltas * self.desconto) + self.comissao
        return salario
    




