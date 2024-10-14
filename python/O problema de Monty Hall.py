import random

# O problema de Monty Hall envolve três portas: atrás de uma está um carro, e atrás das outras duas, cabras. 
# Você escolhe uma porta, e o apresentador abre outra, mostrando uma cabra. Então, você pode trocar de porta ou manter sua escolha. 
# A melhor estratégia é sempre trocar, pois isso aumenta suas chances de ganhar de 1/3 para 2/3. 
# Embora pareça contra-intuitivo, trocar é vantajoso porque, inicialmente, você tem mais chance de ter escolhido uma cabra do que o carro.

portas = [1,0,0]

def monty_hall(trocar, numeroTentativas):

    contador1 = 0
    contador2 = 0
    
    for i in range(numeroTentativas):

        # O jogador escolhe sua porta
        escolha = random.randint(0, 2)
        random.shuffle(portas)

        # O apresentador abre uma outra porta sem prêmio
        portas_para_abrir = [i for i in range(3) if i != escolha and portas[i] == 0]
        porta_eliminada = random.choice(portas_para_abrir)

        # Cálculo quando o jogador troca de porta
        if trocar:            
            ultima_porta = [i for i in range(3) if i != escolha and i != porta_eliminada][0]
            if portas[ultima_porta] == 1:
                    contador1 += 1
        # Cálculo quando o jogador não troca de porta
        else:
            if portas[escolha] == 1:
                contador2 += 1
    
    if trocar:
        print(f"  Porcetagem média de vitória quando o jogador troca de porta: {(contador1 / numeroTentativas):.1%}")
    else:
        print(f"  Porcetagem média de vitória quando o jogador não troca de porta: {(contador2 / numeroTentativas):.1%}")

if __name__ == "__main__":
    print('\n')
    monty_hall(1, 1000)
    monty_hall(0, 1000)
    print('\n')