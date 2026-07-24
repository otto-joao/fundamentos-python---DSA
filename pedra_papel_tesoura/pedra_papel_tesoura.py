from pedra_papel_tesoura.logica import ESCOLHAS, determinar_vencedor
from pedra_papel_tesoura.visual import (
    limpar_tela, exibir_titulo, exibir_arte,
    obter_nome, obter_escolha,
    exibir_rodada, exibir_resultado,
    perguntar_novamente, despedida
)


def jogar():
    limpar_tela()
    exibir_titulo()

    j1_nome = obter_nome("Jogador 1")
    j2_nome = obter_nome("Jogador 2")

    while True:
        limpar_tela()
        print(f"  {j1_nome}  vs  {j2_nome}\n")

        e1 = obter_escolha(j1_nome)

        limpar_tela()
        print(f"{j1_nome} já escolheu. Vez do {j2_nome}.\n")
        e2 = obter_escolha(j2_nome)

        esc1 = ESCOLHAS[e1]
        esc2 = ESCOLHAS[e2]
        resultado = determinar_vencedor(esc1, esc2)

        exibir_rodada(esc1, j1_nome, esc2, j2_nome)
        exibir_resultado(resultado)

        if not perguntar_novamente():
            despedida()
            break


if __name__ == "__main__":
    jogar()
