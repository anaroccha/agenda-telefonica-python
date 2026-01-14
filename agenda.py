def adicionar_contato (agenda, nome_contato, telefone, email):
    contato = {"nome": nome_contato, "telefone": telefone, "email": email, "favorito": False}
    agenda.append (contato)
    print(f"O contato {nome_contato} foi adicionado com sucesso!")
    return

def vizualizar_contato (agenda): 
     print ("\nLista de contatos:")
     for indice, contato in enumerate (agenda, start=1):
         status = "✓" if contato["favorito"] else " "
         nome_contato = contato ["nome"]
         telefone = contato["telefone"]
         email = contato ["email"]
         print(f"{indice}. [{status}] {nome_contato} - {telefone} - {email}")
     

def editar_contato (agenda, indice, contato_editado):
     indice_ajustado = int (indice) - 1
     if indice_ajustado >= 0 and indice_ajustado < len (agenda):
          agenda [indice_ajustado] ["nome"] = contato_editado
          print (f"Contato {indice} atualizado para {contato_editado}")
     else:
          print("Indice de contato invalido")
     return

def favoritar_contato (agenda, indice):
    indice_ajustado = int (indice) - 1
    agenda [indice_ajustado] ["favorito"] = not agenda [indice_ajustado] ["favorito"] 
    status = "favoritado" if agenda [indice_ajustado] ["favorito"] else "removido dos favoritos"
    print (f"Contato {indice} {status}")
    return

def contatos_favoritos (agenda):
     print (f"\nEsses são seus contatos favoritos:")
     for contato in agenda:
        if contato ["favorito"]:
            print(f"✓ {contato['nome']} - {contato['telefone']} {contato ['email']}")
     return

def deletar_contato (agenda, indice):
    indice_ajustado = int(indice) - 1
    if 0 <= indice_ajustado < len(agenda):
        contato_removido = agenda.pop (indice_ajustado)
        print(f"Contato {contato_removido['nome']} removido com sucesso!")
    else:
        print("Índice inválido!")
    return
    
agenda = []
while True:
    print("\nMinha agenda telefonica")
    print ("1. Adicionar contato")
    print ("2. Vizualizar contato")
    print ("3. Editar contato")
    print ("4. Favoritar contato")
    print ("5. Contatos favoritos")
    print ("6. Deletar contato")
    print ("7. Sair")

    escolha = input ("Digite o que deseja fazer:") 

    if escolha == "1":
          nome_contato = input ("Digite o nome do contato que deseja adicionar: ")
          telefone = input ("Digite o numero:")
          email = input ("Digite o email: ")
          adicionar_contato (agenda, nome_contato, telefone, email)

    elif escolha == "2":
         vizualizar_contato (agenda)

    elif escolha == "3":
        vizualizar_contato (agenda)
        indice_contato = input ("Digite o numero do contato que deja editar: ")
        novo_nome = input ("Digite o novo nome: ")
        editar_contato (agenda, indice_contato, novo_nome)

    elif escolha == "4":
        vizualizar_contato (agenda)
        indice_contato = input ("Digite o numero do contato que deseja favoritar: ")
        favoritar_contato (agenda, indice_contato) 

    elif escolha == "5":
        contatos_favoritos (agenda)

    elif escolha == "6":
        vizualizar_contato (agenda)
        indice_contato = input("Digite o número do contato que deseja deletar: ")
        deletar_contato (agenda, indice_contato)
        

    elif escolha == "7":
        break
