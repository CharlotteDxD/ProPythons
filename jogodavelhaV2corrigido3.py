#Gustavo Reatti Sela - RM571545
#Rafael Gonçalves - RM569461
#Charles Augusto Miranda da Silva - RM571908
#Anthony Prado Pereira - RM572985

#Pseudo-código para o jogo da velha:
    ## inicializa o tabuleiro vazio
    # define os dois jogadores
    # loop infinito:  <- Todos juntos
        # exibir_tabuleiro()        <- função do Gon
        # pede linha e coluna pro jogador
        # jogada_valida()           <- função do Charles
        # coloca X ou O no tabuleiro
        # verificar_vencedor()      <- função do Gustavo
        # se venceu, acabou
        # verificar_empate()        <- função do Anthony
        # se empatou, acabou
        # troca o jogador

tabuleiro = [
    ['  ', ' ', ' '], #os espaços a mais no primeiro elemento de cada linha
    ['  ', ' ', ' '], #são pra deixar o tabuleiro(xadrezinho) alinhado 
    ['  ', ' ', ' '] 
]

def exibir_tabuleiro(tabuleiro):
    print('   1   2   3') # pra exibir os numeros das colunas do taubuleiro
                          # os espaços também são pra alinhamento do tabuleiro
# pra cada linha do tabuleiro numerada (i = 0, 1, 2):    
    for i, linha in enumerate(tabuleiro): 
        print(i + 1, end=' ')
        print(' | '.join(linha)) 
#coloca o separador de colunas ' | ' e junta ele com a linha
        if i < len(tabuleiro) - 1: 
#se o indice da linha for menor que o numero total de linhas -1(ultima linha)
# o -1 foi pra impedir que o separador seja printado depois da ultima linha 
            print('  ---+---+---', end=' ')
# printa o separador de linhas '---+---+---'
# o grande espaço no print pro separador é pra ficar alinhado o tabuleiro.
# o end='' é pra evitar que o print pule mais uma linha, pra ficar mais "bonito"
            print()
#pula pra proxima linha o separador de colunas
#senão, os separadores iam ficar na mesma linha, o que não é o desejado



#função para validar a jogada do jogador - Charles:
    # converter linha e coluna de 1,2,3 para 0,1,2 (padrão da matriz)
    # verificar se linha e coluna estão entre 1 e 3
    # verificar se a célula escolhida está vazia (ainda tem ' ')
    # se tudo ok, retorna True
    # senão, retorna False  

# --- FUNÇÕES DO JOGO DA VELHA ---

# --- FUNÇÕES DO JOGO DA VELHA ---

def jogada_valida(tabuleiro, linha, coluna):
    """
    Verifica se a jogada pode ser realizada.
    """
    # 1. Verificar se linha e coluna estão dentro do limite visual (1 a 3)
    if 1 <= linha <= 3 and 1 <= coluna <= 3:
        
        # 2. Converter de 1,2,3 para 0,1,2 (ajuste para o índice da matriz)
        l_idx = linha - 1
        c_idx = coluna - 1
        
        # 3. Verificar se a célula escolhida está vazia (contém apenas um espaço)
        if tabuleiro[l_idx][c_idx] == ' ':
            return True
        else:
            print("\n!!! Erro: Célula já ocupada! Escolha outra. !!!")
            return False
    else:
        print("\n!!! Erro: Coordenadas fora do intervalo (use 1, 2 ou 3). !!!")
        return False

def jogar():
    """
    Função principal que gerencia o fluxo do jogo.
    """
    # Inicializa o tabuleiro (Matriz 3x3)
    tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]
    jogador_atual = 'X'
    jogadas = 0 

    # Loop Principal: O jogo permite no máximo 9 jogadas (tabuleiro cheio)
    while jogadas < 9:
        exibir_tabuleiro(tabuleiro)
        print(f"--- Vez do jogador: {jogador_atual} ---")
        
        # Entrada de dados com proteção contra erros de digitação (letras)
        try:
            lin = int(input("Digite a Linha (1-3): "))
            col = int(input("Digite a Coluna (1-3): "))
        except ValueError:
            print("\n!!! Erro: Por favor, digite apenas números inteiros! !!!")
            continue

        # Verifica se a jogada é válida antes de aplicar ao tabuleiro
        if jogada_valida(tabuleiro, lin, col):
            # Coloca o símbolo do jogador atual no tabuleiro usando a conversão de índice
            tabuleiro[lin - 1][col - 1] = jogador_atual
            jogadas += 1
            
            # --- MECÂNICA DE ALTERNÂNCIA ---
            # Troca o símbolo para a próxima rodada
            if jogador_atual == 'X':
                jogador_atual = 'O'
            else:
                jogador_atual = 'X'
        else:
            # Se a jogada for inválida, o 'continue' pula o resto e pede o input de novo
            continue
        
        #Verifica se há um vencedor:
        vencedor = verificar_vencedor(tabuleiro)
        empate=verificar_empate(tabuleiro)

        if vencedor:
            exibir_tabuleiro(tabuleiro)
            print(f"\nJogador {vencedor} venceu o jogo!") 
            return  
        # verifica se há um empate:
        if empate:
            exibir_tabuleiro(tabuleiro)
            print("\n O jogo empatou! Deu velha!")
            return
        
#Outros pontos:
    #fique esperto com o alinhamento do tabuleiro
    #o alinhamento é importante para a estética do jogo e conclusão do trabalho

# --- FUNÇÕES DO JOGO DA VELHA (VERIFICANDO VENCEDOR!) --- 
 
# --- FUNÇÕES DO JOGO DA VELHA (VERIFICANDO VENCEDOR!) --- 
 
 #Esta função "verificar_vencedor" serve para identiicar se há um vencedor no tabuleiro
 #Retornará "X" ou "O" se houver vencedor... Caso não haja retornará "None".
def verificar_vencedor(tabuleiro):      
    
    # --- Verificar Linha ---
    for linha in tabuleiro:                 
       
        #Verifica se em alguma linha há três símbolos iguais: "X" ou "O"
        if linha[0] == linha[1] == linha[2] and linha[0] != ' ':
            
            #Se passou na Verificação Retorna o simbolo do vencedor e encerra a função
            return linha[0]
        
    # --- Verificar Coluna ---
    #O Range(3) serve para percorrer os índices das colunas 
    #Pois, Diferente das linhas, as colunas não estão prontas como listas. 
    for coluna in range(3):

        #Verifica se em alguma coluna há três símbolos iguais: "X" ou "O"
        if tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] and tabuleiro[0][coluna] != ' ':
           
            #Se passou na Verificação Retorna o simbolo do vencedor e encerra a função
             return tabuleiro[0][coluna]

    # --- Verificar Diagonal Principal ---
    #Como as diagonais (Principal/Secundária) são fixas, não há a necessidade de usar um "For | in"      
    #Verifica se na diagonal principal há três símbolos iguais: "X" ou "O"
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] and tabuleiro[0][0] != ' ':
                  
            #Se passou na Verificação Retorna o simbolo do vencedor e encerra a função
        return tabuleiro[0][0]

    # --- Verificar Diagonal Secundária ---
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] and tabuleiro[0][2] != ' ':
            
            #Se passou na Verificação Retorna o simbolo do vencedor e encerra a função
            return tabuleiro[0][2]
    
    #Se não há vencedor:
    return 

# verifica se há um empate no tabuleiro:

def verificar_empate(tabuleiro):
    #Verifica se o tabuleiro está cheio,e retorna true se der velha 
    for linha in tabuleiro:
        # Se ainda houver um espaço vazio (' ') na linha, o jogo não acabou
        if ' ' in linha:
            return False 
            
    # Se o loop terminar e não achar nenhum ' ', o tabuleiro está cheio (Empate)
    return True

# --- INÍCIO DO JOGO ---
jogar()


#Observações
#Removi a função de imprimir tabuleiro porque a primeira função já faz isso, e não é necessário ter duas funções para a mesma tarefa.
#Também adicionei uma função principal 'jogar()' para organizar melhor o fluxo do jogo, e para facilitar a leitura e manutenção do código.
#Arrumei a ordem na função jogada valida, pra ficar bonitinho e certo - "(tabuleiro, linha, coluna)" 

