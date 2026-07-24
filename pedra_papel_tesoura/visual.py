import os

ARTES = {
    'Pedra': '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',
    'Papel': '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',
    'Tesoura': '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
}


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def exibir_titulo():
    print('''\
  ___             _        ___                     _    ___                        
 | _ \\__ _ _ _ __| |_ ___ / __|_ __  ___ _ _  __ _| |_ / __|___ _____ _  _ ___ ___
 |  _/ _` | '_/ _|  _/ -_) (__| '_ \\/ -_) '_|/ _` |  _| (__/ _ / _ | || / -_|_-<
 |_| \\__,_|_| \\__|\\__\\___|\\___| .__/\\___|_|  \\__,_|\\__|\\___\\___\\___/\\_,_\\___/__/
                               |_|                                                \
''')


def exibir_arte(escolha):
    print(ARTES.get(escolha, ''))


def obter_nome(jogador_numero):
    nome = input(f"Nome do {jogador_numero}: ").strip()
    return nome if nome else f"Jogador {jogador_numero[-1]}"


def obter_escolha(jogador):
    while True:
        try:
            escolha = input(f"{jogador}, escolha (1) Pedra, (2) Papel ou (3) Tesoura: ")
            if escolha in ('1', '2', '3'):
                return escolha
            print("Opção inválida! Digite 1, 2 ou 3.")
        except (EOFError, KeyboardInterrupt):
            print("\nJogo encerrado.")
            exit()


def exibir_rodada(jogador1, j1_nome, jogador2, j2_nome):
    limpar_tela()
    print(f"  {j1_nome}  vs  {j2_nome}\n")
    exibir_arte(jogador1)
    print(f"{j1_nome} escolheu: {jogador1}\n")
    print("-" * 40)
    exibir_arte(jogador2)
    print(f"{j2_nome} escolheu: {jogador2}")


def exibir_resultado(resultado):
    print("-" * 40)
    print(f"  Resultado: {resultado}")
    print("-" * 40)


def perguntar_novamente():
    return input("\nJogar novamente? (s/N): ").lower() == 's'


def despedida():
    print("\nObrigado por jogar!\n")
