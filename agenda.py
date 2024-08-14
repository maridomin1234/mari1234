# Lista global para armazenar os contatos
agenda = []
# Variável para marcar uma alteração na agenda
alterada = False

# Função para solicitar o nome do contato, com um padrão opcional
def pede_nome(padrão=""):
    nome = input("Nome: ")
    if nome == "":
        nome = padrão
    return nome

# Função para solicitar o telefone do contato, com um padrão opcional
def pede_telefone(padrão=""):
    telefone = input("Telefone: ")
    if telefone == "":
        telefone = padrão
    return telefone

# Função para solicitar o endereço do contato, com um padrão opcional
def pede_endereco(padrão=""):
    endereco = input("Endereço: ")
    if endereco == "":
        endereco = padrão
    return endereco

# Função para solicitar a cidade do contato, com um padrão opcional
def pede_cidade(padrão=""):
    cidade = input("Cidade: ")
    if cidade == "":
        cidade = padrão
    return cidade

# Função para solicitar o UF (Unidade Federativa) do contato, com um padrão opcional
def pede_uf(padrão=""):
    uf = input("UF: ")
    if uf == "":
        uf = padrão
    return uf

# Função para exibir os dados do contato
def mostra_dados(nome, telefone, endereco, cidade, uf):
    print(f"Nome: {nome} Telefone: {telefone} Endereço: {endereco} Cidade: {cidade} UF: {uf}")

# Função para solicitar o nome do arquivo
def pede_nome_arquivo():
    return input("Nome do arquivo: ")

# Função para pesquisar um contato pelo nome
def pesquisa(nome):
    mnome = nome.lower()
    for p, e in enumerate(agenda):
        if e[0].lower() == mnome:
            return p
    return None

# Função para adicionar um novo contato à agenda
def novo():
    global agenda, alterada
    nome = pede_nome()
    telefone = pede_telefone()
    endereco = pede_endereco()
    cidade = pede_cidade()
    uf = pede_uf()
    agenda.append([nome, telefone, endereco, cidade, uf])
    alterada = True

# Função para confirmar uma operação
def confirma(operação):
    while True:
        opção = input(f"Confirma {operação} (S/N)? ").upper()
        if opção in "SN":
            return opção
        else:
            print("Resposta inválida. Escolha S ou N.")

# Função para apagar um contato da agenda
def apaga():
    global agenda, alterada
    nome = pede_nome()
    p = pesquisa(nome)
    if p is not None:
        if confirma("apagamento") == "S":
            del agenda[p]
            alterada = True
    else:
        print("Nome não encontrado.")

# Função para alterar os dados de um contato
def altera():
    global alterada
    p = pesquisa(pede_nome())
    if p is not None:
        nome, telefone, endereco, cidade, uf = agenda[p]
        print("Encontrado:")
        mostra_dados(nome, telefone, endereco, cidade, uf)
        nome = pede_nome(nome)  # Se nada for digitado, mantém o valor
        telefone = pede_telefone(telefone)
        endereco = pede_endereco(endereco)
        cidade = pede_cidade(cidade)
        uf = pede_uf(uf)
        if confirma("alteração") == "S":
            agenda[p] = [nome, telefone, endereco, cidade, uf]
            alterada = True
    else:
        print("Nome não encontrado.")

# Função para listar todos os contatos da agenda
def lista():
    print("\nAgenda\n\n\------")
    # Usamos a função enumerate para obter a posição na agenda
    for posição, e in enumerate(agenda):
        # Imprimimos a posição, sem saltar linha
        print(f"Posição: {posição} ", end="")
        mostra_dados(e[0], e[1], e[2], e[3], e[4])
    print("\------\n")

# Função para ler a última agenda gravada
def lê_última_agenda_gravada():
    última = última_agenda()
    if última is not None:
        leia_arquivo(última)

# Função para obter o nome do último arquivo de agenda
def última_agenda():
    try:
        arquivo = open("ultima agenda.dat", "r", encoding="utf-8")
        última = arquivo.readline()[:-1]
        arquivo.close()
    except FileNotFoundError:
        return None
    return última

# Função para atualizar o nome do último arquivo de agenda gravado
def atualiza_última(nome):
    arquivo = open("ultima agenda.dat", "w", encoding="utf-8")
    arquivo.write(f"{nome}\n")
    arquivo.close()

# Função para ler os dados de um arquivo para a agenda
def leia_arquivo(nome_arquivo):
    global agenda, alterada
    arquivo = open(nome_arquivo, "r", encoding="utf-8")
    agenda = []
    for l in arquivo.readlines():
        nome, telefone, endereco, cidade, uf = l.strip().split("#")
        agenda.append([nome, telefone, endereco, cidade, uf])
    arquivo.close()
    alterada = False

# Função para ler uma nova agenda
def lê():
    global alterada
    if alterada:
        print("Você não salvou a lista desde a última alteração. Deseja gravá-la agora?")
        if confirma("gravação") == "S":
            grava()
    print("Ler\n---")
    nome_arquivo = pede_nome_arquivo()
    leia_arquivo(nome_arquivo)
    atualiza_última(nome_arquivo)

# Função para ordenar a agenda por nome
def ordena():
    global alterada
    fim = len(agenda)
    while fim > 1:
        i = 0
        trocou = False
        while i < (fim - 1):
            if agenda[i] > agenda[i + 1]:
                # Opção: agenda[i], agenda[i+1] = agenda[i+1], agenda[i]
                temp = agenda[i + 1]
                agenda[i + 1] = agenda[i]
                agenda[i] = temp
                trocou = True
            i += 1
        if not trocou:
            break
    alterada = True

# Função para gravar a agenda em um arquivo
def grava():
    global alterada
    if not alterada:
        print("Você não alterou a lista. Deseja gravá-la mesmo assim?")
        if confirma("gravação") == "N":
            return
    print("Gravar\n\------")
    nome_arquivo = pede_nome_arquivo()
    arquivo = open(nome_arquivo, "w", encoding="utf-8")
    for e in agenda:
        arquivo.write(f"{e[0]}#{e[1]}#{e[2]}#{e[3]}#{e[4]}\n")
    arquivo.close()
    atualiza_última(nome_arquivo)
    alterada = False

# Função para validar um valor inteiro dentro de uma faixa
def valida_faixa_inteiro(pergunta, inicio, fim):
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor <= fim:
                return valor
        except ValueError:
            print(f"Valor inválido, favor digitar entre {inicio} e {fim}")

# Função para exibir o menu e obter a escolha do usuário
def menu():
    print("""
1 - Novo
2 - Altera
3 - Apaga
4 - Lista
5 - Grava
6 - Lê
7 - Ordena por nome
0 - Sai
""")
    print(f"\nNomes na agenda: {len(agenda)} Alterada: {alterada}\n")
    return valida_faixa_inteiro("Escolha uma opção: ", 0, 7)

# Função principal para gerenciar o programa
lê_última_agenda_gravada()
while True:
    opção = menu()
    if opção == 0:
        break
    elif opção == 1:
        novo()
    elif opção == 2:
        altera()
    elif opção == 3:
        apaga()
    elif opção == 4:
        lista()
    elif opção == 5:
        grava()
    elif opção == 6:
        lê()
    elif opção == 7:
        ordena()