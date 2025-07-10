from modelos.funcionario import Funcionario
from modelos.gerente import Gerente

class Sistema:
    menu = True
    lista_funcionarios = []
    lista_gerentes = []
    lista_vendedores = []
    lista_estagiarios = []
    
    @classmethod
    def menu_principal(cls):
        while cls.menu == True:
            print("\n=== SISTEMA EMPRESARIAL ===\n")
            print("1 - Cadastrar funcionário")
            print("2 - Registrar falta")
            print("3 - Exibir salário")
            print("4 - Sair\n")
            
            selecionar_opcao = input("Informe o número da opção desejada: ")

            if selecionar_opcao >= 1 and selecionar_opcao <= 4:
                try:
                    selecionar_opcao = int(selecionar_opcao)
                except ValueError:
                    print("\nSomente valores válidos!\n")

                if selecionar_opcao == 1:
                    pass

                elif selecionar_opcao == 4:
                    cls.menu = False
                    print("\nSaída realizada com sucesso!\n")
            else:
                print("\nNúmero inválido!\n")

    @classmethod
    def dados_funcionarios(cls):
        nome = input("\nInforme o nome do funcionário: ").strip()
        cpf = input("Digite o número de CPF: ")
        data_nascimento = input("Qual é a data de nascimento do funcionário? ")
        matricula = input("Matrícula do funcionário: ")
        salario_base = input("Salário do trabalhador: ")

        try:
            matricula = int(matricula)
            salario_base = float(salario_base)
        except ValueError:
            print("\nSomente números válidos!\n")

        funcionario = Funcionario(nome, cpf, data_nascimento, matricula, salario_base)
        cls.lista_funcionarios.append(funcionario)

        print("\nFuncionário cadastrado com sucesso!\n")

        print("\n=== CARGOS ===\n")
        print("1 - Gerente")
        print("2 - Vendedor")
        print("3 - Estagiário\n")

        selecionar_cargo = input("Informe o número equivalente ao cargo designado: ")

        if selecionar_cargo >= 1 and selecionar_cargo <= 3:
            if selecionar_cargo == 1:
                gerente = Gerente(funcionario)
                cls.lista_gerentes.append(funcionario)

                print("\nGerente cadastrado com sucesso!\n")
        else:
            print("\nOpção inválida!\n")
            
        

