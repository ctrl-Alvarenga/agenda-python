def menu():
    while True:    
            opcao = input('''
======================================================
                Projeto Agenda em Python

Menu:

[1] CADASTRAR CONTATO
[2] LISTAR CONTATO
[3] DELETAR CONTATO
[4] BUSCAR CONTATO PELO NOME
[5] SAIR

======================================================
Escolha uma opção: \n''')
    
            if opcao == "1":
                cadastrarContato()
            elif opcao == "2":
                listarContato()
            elif opcao == "3":
                deletarContato()
            elif opcao == "4":
                buscarCnttID()
            elif opcao == "5":
                print("Programa encerrado")
                break
            else:
                print("Opção inválida!")

def cadastrarContato():
    print('Cadastrar contato:')
    id = input("Digite o ID do seu contato: ")
    nome = input("Digite o nome do seu contato: ")
    tel = input("Digite o telefone do seu contato: ")
    email = input("Digite o email do seu contato: ")
    try:
        agenda = open(r"C:\Users\rafae\OneDrive\Documentos\Pessoal\programacao\projeto_agenda_py\agenda.txt", "a", encoding="utf-8")
        dados = f'{id};{nome};{tel};{email}\n'
        agenda.write(dados)
        print('Contato gravado com sucesso.')
    except Exception as e:
        print("Erro na gravação do contato:", e)
    fecharPrograma()

def listarContato():
    print('Listar contato')
    agenda = open(r"C:\Users\rafae\OneDrive\Documentos\Pessoal\programacao\projeto_agenda_py\agenda.txt", "r")
    for contato in agenda:
            print (contato)
    agenda.close()
    fecharPrograma()
        

def deletarContato():
    print('Deletar contato')
    nomeDel = input("Digite o nome do contato para ser deletado: ")
    
    # Lê todos os contatos
    with open(r"C:\Users\rafae\OneDrive\Documentos\Pessoal\programacao\projeto_agenda_py\agenda.txt", "r", encoding="utf-8") as agenda:
        linhas = agenda.readlines()
    
    # Filtra os contatos que não contêm o nome
    novas_linhas = [linha for linha in linhas if nomeDel not in linha]

    # Reescreve o arquivo sem o contato deletado
    with open(r"C:\Users\rafae\OneDrive\Documentos\Pessoal\programacao\projeto_agenda_py\agenda.txt", "w", encoding="utf-8") as agenda:
        agenda.writelines(novas_linhas)

    print(f'Contato deletado com sucesso')
    listarContato()
    fecharPrograma()

    
    
def buscarCnttID():
    nome = input(f'Digite o nome a ser procurado')
    print('Buscar contato pelo nome')
    agenda = open(r"C:\Users\rafae\OneDrive\Documentos\Pessoal\programacao\projeto_agenda_py\agenda.txt", "r")
    for contato in agenda:
        if nome in contato.split(";")[1]:
            print(contato)
    agenda.close()
    fecharPrograma()

def fecharPrograma():
    voltar=input("Deseja voltar ao menu(s/n)? ")
    if voltar == 's':
        menu()
    else:
        print('programa encerrado')
        exit()

def main():
    menu()

main()
