ESCOLHAS = {'1': 'Pedra', '2': 'Papel', '3': 'Tesoura'}


def determinar_vencedor(j1, j2):
    if j1 == j2:
        return "Empate!"
    if (j1 == 'Pedra' and j2 == 'Tesoura') or \
       (j1 == 'Tesoura' and j2 == 'Papel') or \
       (j1 == 'Papel' and j2 == 'Pedra'):
        return "Jogador 1 venceu!"
    return "Jogador 2 venceu!"
