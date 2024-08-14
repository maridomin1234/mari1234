from datetime import datetime

# Lista com os meses por extenso
meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho",
         "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

# Função para validar e converter a data digitada pelo usuário
def converter_data(data_str):
    try:
        # Tenta converter a data no formato DD/MM/AAAA
        data = datetime.strptime(data_str, "%d/%m/%Y")
        dia = data.day
        mes = meses[data.month - 1]  # -1 para acessar o índice correto da lista
        ano = data.year
        data_extenso = f"{dia} de {mes} de {ano}"
        return data_extenso
    except ValueError:
        # Se a data for inválida, retorna None
        return None

# Função para exibir o menu e realizar as operações
def menu():
    datas_convertidas = []

    while True:
        print("\nMenu de Opções:")
        print("1 – Converter Data")
        print("2 – Listar Datas por extenso")
        print("3 – Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            while True:
                data_input = input("Digite uma data no formato DD/MM/AAAA: ")
                data_extenso = converter_data(data_input)
                if data_extenso:
                    print(f"Data por extenso: {data_extenso}")
                    datas_convertidas.append(data_extenso)
                    break
                else:
                    print("Data inválida. Tente novamente.")

        elif opcao == '2':
            if datas_convertidas:
                print("\nDatas convertidas:")
                for data in datas_convertidas:
                    print(data)
            else:
                print("Nenhuma data foi convertida ainda.")

        elif opcao == '3':
            if datas_convertidas:
                with open("datas_convertidas.txt", "w") as arquivo:
                    for data in datas_convertidas:
                        arquivo.write(data + "\n")
                print("As datas convertidas foram salvas no arquivo 'datas_convertidas.txt'.")
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")

# Executa o programa
menu()