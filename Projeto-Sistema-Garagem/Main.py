def validarCpf(cpf):
    # Remove os caracteres nao numericos
    cpf = ''.join(filter(str.isdigit, cpf))
    
    # Verifica se o CPF possui apenas 11 digitos
    if len(cpf) != 11:
        return False
    
    # Verifica se todos os digitos sao iguais
    if cpf == cpf[0] * 11:
        return False
    
    # Calcula o primeiro digito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    digito1 = 11 - (soma % 11)
    if digito1 >= 10:
        digito1 = 0

    # Calcula o segundo digito verificador
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    digito2 = 11 - (soma % 11)
    if digito2 >= 10:
        digito2 = 0
    
    # Verifica se os digitos verificadores calculados correspondem aos digitos do CPF
    if int(cpf[9]) == digito1 and int(cpf[10]) == digito2:
        return True
    else:
        return False

# Cria a lista de veiculos
veiculos = []

# Funcao para adicionar um veiculo na lista
def adicionarVeiculo():
    print("== ADICIONAR VEICULO ==========================")

    placa = input("Informe a placa do veiculo: ")
    modelo = input("Informe o modelo do veiculo: ")
    hora_entrada = input("Informe a hora que o veiculo estacionou: ")
    nome = input("Informe o nome da pessoa: ")
    cpf = input("Informe o cpf da pessoa: ")
    # Enquanto o cpf nao for valido ira repetir o scaneamento
    while not validarCpf(cpf):
        cpf = input("Cpf invalido! tente novamente: ")
    
    veiculo = {
        "placa": placa,
        "modelo": modelo,
        "nome": nome,
        "cpf": cpf,
        "Hora da entrada": hora_entrada
    }
    # add na lista veiculos
    veiculos.append(veiculo)
        
    print(" >> Veiculo adicionado no sistema! << ")

def removerVeiculo():
    print("== REMOVER VEICULO ==========================")

    placa = input("Informe a placa do veiculo que vai sair: ")

    encontrado = False

    for veiculo in veiculos:
        if veiculo["placa"] == placa:
            encontrado = True
            veiculos.remove(veiculo) # funcao para remover veiculo da lista
            print(f" >> Veiculo foi removido! - Placa: {placa} << ")
            return

    if not encontrado:
        print(" >> Veiculo nao encontrado! <<")

def listarVeiculo():
    if not veiculos:
        print(" >> Nao ha veiculos na garagem! << ")
    else:
        print("== LISTAR VEICULOS ==========================")

        for veiculo in veiculos:
            print(veiculo)

def buscarVeiculo():
    print("== BUSCAR VEICULO ==========================")

    buscar_placa = input("Digite a placa do veiculo que deseja buscar: ")

    encontrado = False

    for veiculo in veiculos:
        if veiculo["placa"] == buscar_placa:
            encontrado = True
            print(" > Placa: ", veiculo["placa"])
            print(" > Modelo: ", veiculo["modelo"])
            print(" > Nome: ", veiculo["nome"])
            print(" > CPF: ", veiculo["cpf"])
            print(" > Hora da entrada: ", veiculo["Hora da entrada"])
            return
        
    if not encontrado:
        print(" >> Veiculo nao encontrado! <<")

# Inicio do programa - MAIN
def main():
    while True:
        print("============ GARAGEM ============")
        print(" >   [1] Entrada de veiculo    < ")
        print(" >   [2] Saida de veiculo      < ")
        print(" >   [3] Lista de vagas        < ")
        print(" >   [4] Encontrar veiculo     < ")
        print(" >   [0] Encerrar programa     < ")

        opc = int(input("Escolha uma opcao: "))

        if opc == 1:
            adicionarVeiculo()
        elif opc == 2:
            removerVeiculo()
        elif opc == 3:
            listarVeiculo()
        elif opc == 4:
            buscarVeiculo()
        elif opc == 0:
            print(" >>  Saindo do programa... << ")
            break
        else:
            print(" >> Opcao Invalida! tente novamente: ")

# Chama a funcao main para iniciar o programa
main()