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
        while cls.menu:
            print("\n=== SISTEMA EMPRESARIAL ===\n")
            print("1 - Cadastrar funcionário")
            print("2 - Registrar falta")
            print("3 - Exibir salário")
            print("4 - Sair\n")
            
            selecionar_opcao = input("Informe o número da opção desejada: ")

            try:
                selecionar_opcao = int(selecionar_opcao)
            except ValueError:
                print("\nSomente valores válidos!\n")
                return

            if selecionar_opcao >= 1 and selecionar_opcao <= 4:
                if selecionar_opcao == 1:
                    cls.dados_funcionarios()

                elif selecionar_opcao == 4:
                    cls.menu = False
                    print("\nSaída realizada com sucesso!\n")
            else:
                print("\nNúmero inválido!\n")

    @classmethod
    def cadastro_gerente(cls):
        print("\n=== CARGOS ===\n")
        print("1 - Gerente")
        print("2 - Vendedor")
        print("3 - Estagiário\n")

        selecionar_cargo = input("Informe o número equivalente ao cargo designado: ")

        try:
            selecionar_cargo = int(selecionar_cargo)
        except ValueError:
            print("\nSomente números válidos!\n")
            return

        if selecionar_cargo >= 1 and selecionar_cargo <= 3:
            if selecionar_cargo == 1:
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
                    return

                gerente = Gerente(nome, cpf, data_nascimento, matricula, salario_base)
                cls.lista_gerentes.append(gerente)
                cls.lista_funcionarios.append(gerente)

                print("\nGerente cadastrado com sucesso!\n")

            elif selecionar_cargo == 2:
                pass
        else:
            print("\nOpção inválida!\n")