import google.generativeai as genai
import os

# Configuração da API do Google
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# O modelo que a gente vai usar para a nossa IA
modelo = genai.GenerativeModel('gemini-1.5-flash')

# Uma pergunta para a IA responder
pergunta_usuario = "Me ajude a pensar em uma ideia para um projeto sobre inteligência artificial."

# Usa o Gemini para gerar a resposta
try:
    response = modelo.generate_content(pergunta_usuario)
    print("Pensabot: " + response.text)
except Exception as e:
    print(f"Ocorreu um erro: {e}")
