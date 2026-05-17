import os

def limpar_tela():
    """Limpa o terminal de acordo com o sistema operacional."""
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_tabuleiro(tabuleiro):
    """Exibe o tabuleiro formatado no terminal."""
    print(f"\n {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]} ")
    print("-----------")
    print(f" {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]} ")
    print("-----------")
    print(f" {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]} \n")

def obter_jogada_valida(tabuleiro, jogador):
    """Solicita e valida a entrada do usuário até que ela seja correta."""
    while True:
        entrada = input(f"Jogador {jogador}, escolha uma posição (1-9): ").strip()
        
        if not entrada.isdigit():
            print("Entrada inválida! Digite apenas números de 1 a 9.")
            continue
            
        posicao = int(entrada)
        
        if posicao < 1 or posicao > 9:
            print("Posição inválida. Escolha um número de 1 a 9.")
            continue
            
        if tabuleiro[posicao - 1] in ['X', 'O']:
            print("Essa posição já está ocupada. Escolha outra.")
            continue
            
        return posicao - 1

def verificar_vitoria(tabuleiro, jogador):
    """Verifica todas as 8 combinações possíveis de vitória."""
    combinacoes_vitoria = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]              
    ]
    for combo in combinacoes_vitoria:
        if tabuleiro[combo[0]] == tabuleiro[combo[1]] == tabuleiro[combo[2]] == jogador:
            return True
    return False

def verificar_empate(tabuleiro):
    """Retorna True se todas as posições foram preenchidas sem vencedor."""
    return all(posicao in ['X', 'O'] for posicao in tabuleiro)

def jogar_partida():
    """Controla o loop principal de uma única partida."""
    tabuleiro = [str(i) for i in range(1, 10)]
    jogador_atual = 'X'
    
    while True:
        limpar_tela()
        print("=== JOGO DA VELHA ===")
        exibir_tabuleiro(tabuleiro)
        
        index = obter_jogada_valida(tabuleiro, jogador_atual)
        tabuleiro[index] = jogador_atual
        
        if verificar_vitoria(tabuleiro, jogador_atual):
            limpar_tela()
            exibir_tabuleiro(tabuleiro)
            print(f"Parabéns! Jogador {jogador_atual} venceu!")
            return jogador_atual
            
        if verificar_empate(tabuleiro):
            limpar_tela()
            exibir_tabuleiro(tabuleiro)
            print("O jogo terminou empatado!")
            return 'Empate'
        
        jogador_atual = 'O' if jogador_atual == 'X' else 'X'

def executar_jogo():
    """Gerencia o fluxo global, placar e reinicialização."""
    vitorias_x = 0
    vitorias_o = 0
    
    while True:
        resultado = jogar_partida()
        
        if resultado == 'X':
            vitorias_x += 1
        elif resultado == 'O':
            vitorias_o += 1
            
        print("\n=== PLACAR ===")
        print(f"Jogador X: {vitorias_x} | Jogador O: {vitorias_o}")
        
        deve_continuar = input("\nDeseja jogar novamente? (S/N): ").strip().upper()
        if deve_continuar != 'S':
            print("\nObrigado por jogar! Até a próxima.")
            break

if __name__ == "__main__":
    executar_jogo()
