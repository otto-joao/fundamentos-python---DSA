# Pedra, Papel e Tesoura

Jogo clássico para dois jogadores implementado em Python.

## Regras

- **Pedra** vence **Tesoura** (quebrando-a)
- **Tesoura** vence **Papel** (cortando-o)
- **Papel** vence **Pedra** (cobrindo-a)
- Escolhas iguais resultam em **empate**

## Como jogar

```bash
python pedra_papel_tesoura.py
```

1. Insira os nomes dos dois jogadores
2. O Jogador 1 escolhe entre 1 (Pedra), 2 (Papel) ou 3 (Tesoura)
3. O Jogador 2 faz sua escolha (a escolha do Jogador 1 é ocultada)
4. O resultado da rodada é exibido
5. Escolha se deseja jogar novamente

## Estrutura do código

| Função | Descrição |
|--------|-----------|
| `limpar_tela()` | Limpa o terminal (Windows ou Unix) |
| `obter_escolha(jogador)` | Solicita e valida a escolha (1, 2 ou 3) |
| `determinar_vencedor(j1, j2)` | Compara as escolhas e retorna o resultado |
| `jogar()` | Gerencia o fluxo completo do jogo |
