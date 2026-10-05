import random

def jogar_computador_primeiro():
    total = 0
    print("\n--- Modo: Computador Joga Primeiro ---")
    # Para garantir a vitória, o computador joga 1 para o total ficar em 1 (11 x 0 + 1)
    jogada_inicial = 1
    total += jogada_inicial
    print(f"Computador joga: {jogada_inicial} | Total atual: {total}")
    
    while total < 100:
        # Jogada do Jogador
        while True:
            try:
                jogador = int(input("A tua vez (escolhe de 1 a 10): "))
                if 1 <= jogador <= 10 and total + jogador <= 100:
                    break
                print("Jogada inválida. Garante que está entre 1 e 10 e não ultrapassa 100.")
            except ValueError:
                print("Por favor, introduz um número válido.")
        
        total += jogador
        print(f"Total atual após a tua jogada: {total}")
        
        if total == 100:
            print("Parabéns! Venceu o jogo.")
            break
            
        # Jogada do Computador (Estratégia: manter múltiplos de 11)
        # O computador escolhe de forma a complementar a jogada do jogador para somar 11
        computador = 11 - jogador
        total += computador
        print(f"Computador joga: {computador} | Total atual: {total}")
        
        if total == 100:
            print("O computador venceu!")
            break

def jogar_computador_segundo():
    total = 0
    print("\n--- Modo: Computador Joga em Segundo ---")
    
    while total < 100:
        # Jogada do Jogador
        while True:
            try:
                jogador = int(input("A tua vez (escolhe de 1 a 10): "))
                if 1 <= jogador <= 10 and total + jogador <= 100:
                    break
                print("Jogada inválida. Garante que está entre 1 e 10 e não ultrapassa 100.")
            except ValueError:
                print("Por favor, introduz um número válido.")
                
        total += jogador
        print(f"Total atual após a tua jogada: {total}")
        
        if total == 100:
            print("Parabéns! Venceu o jogo.")
            break
            
        # Jogada do Computador (Tenta apanhar o oponente se ele falhar a estratégia, senão joga aleatório)
        # O objetivo do computador é tentar alcançar um múltiplo de 11
        resto = total % 11
        if resto == 0:
            computador = random.randint(1, 10) # Se já estiver num múltiplo, joga aleatório
        else:
            computador = 11 - resto # Tenta repor a estratégia para o próximo múltiplo de 11
            if computador > 10 or computador < 1:
                computador = random.randint(1, 10)
                
        # Garantir que não passa de 100
        if total + computador > 100:
            computador = 100 - total
            
        total += computador
        print(f"Computador joga: {computador} | Total atual: {total}")
        
        if total == 100:
            print("O computador venceu!")
            break

def main():
    print("=== JOGO: CORRIDA PARA O 100 ===")
    print("1. Computador joga primeiro")
    print("2. Computador joga em segundo")
    opcao = input("Escolhe a vertente (1 ou 2): ")
    
    if opcao == '1':
        jogar_computador_primeiro()
    elif opcao == '2':
        jogar_computador_segundo()
    else:
        print("Opção inválida.")

if __name__ == "__main__":
    main()
