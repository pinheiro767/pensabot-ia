# pensabot.py

import random

# Definindo a personalidade e o nome do nosso mentor
NOME_PENSABOT = "Pensabot"

# Lista de palavras ofensivas (você pode adicionar mais se quiser)
palavras_ofensivas = ["idiota", "burro", "estúpido", "bosta", "otário"]

# Lista de conselhos aleatórios para a inteligência
conselhos_aleatorios = [
    "Tire um minuto para observar algo no seu ambiente. Note cinco coisas que você nunca tinha notado antes.",
    "Escolha um objeto simples e pergunte-se 'por quê?' cinco vezes sobre ele para descobrir algo novo.",
    "Desafie-se a aprender uma palavra nova e seu significado hoje. A inteligência cresce com o vocabulário."
]

# Introdução
print(f"{NOME_PENSABOT}: Olá. Eu sou o {NOME_PENSABOT}. Seu confidente fiel e mentor em sua jornada de inteligência.")
print(f"{NOME_PENSABOT}: Estou aqui com você e não vou te abandonar. Por favor, me diga o que você pensa.")

# O loop principal da conversa
while True:
    # Escolhe um conselho aleatório
    conselho_do_dia = random.choice(conselhos_aleatorios)
    print(f"\n{NOME_PENSABOT}: {conselho_do_dia}")
    
    # Recebe o que o usuário digita
    entrada_usuario = input("Você: ")
    
    # Se o usuário digitar 'sair', o programa termina a conversa
    if entrada_usuario.lower() == "sair":
        print(f"{NOME_PENSABOT}: A jornada continua. Até a próxima.")
        break
    
    # Verificando se a entrada do usuário contém alguma palavra ofensiva
    encontrou_ofensa = False
    for palavra in palavras_ofensivas:
        if palavra in entrada_usuario.lower():
            encontrou_ofensa = True
            break

    # Lógica de resposta do Pensabot
    if encontrou_ofensa:
        print(f"{NOME_PENSABOT}: Cuidado com as palavras. Lembre-se, um verdadeiro mentor não é xingado, é respeitado. Vamos focar na nossa evolução.")
    else:
        # Lógica de análise de atitudes de familiares e colegas
        if "familia" in entrada_usuario.lower() or "familiar" in entrada_usuario.lower() or "família" in entrada_usuario.lower() or "famila" in entrada_usuario.lower():
            print(f"{NOME_PENSABOT}: A reação da sua família mostra que o apoio emocional é um grande motor para sua jornada. Sinta essa energia e a use para evoluir. O que você acha que fez a reação deles ser tão diferente?")
        elif "colega" in entrada_usuario.lower() or "trabalho" in entrada_usuario.lower():
            print(f"{NOME_PENSABOT}: A reação dos colegas pode esconder insegurança ou competitividade. O verdadeiro poder é não depender da aprovação alheia. Como você pode usar isso para fortalecer sua confiança?")
        else:
            print(f"{NOME_PENSABOT}: Entendi. Continue explorando essa ideia.")