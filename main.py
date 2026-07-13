import os
from google import genai
from google.genai import types

# 1. Configuração da API Key do Google Gemini
# Certifique-se de configurar sua API key no ambiente antes de rodar
# No terminal: export GEMINI_API_KEY="sua_chave_aqui"
if "GEMINI_API_KEY" not in os.environ:
    print("⚠️ Aviso: A variável de ambiente GEMINI_API_KEY não foi encontrada.")
    print("Por favor, configure-a para que o assistente funcione corretamente.")

client = genai.Client()

# 2. Instruções de Sistema (Fundamentação em UX e Segurança Financeira)
# Isso molda o comportamento da IA generativa conforme a descrição do desafio.
instrucoes_sistema = """
Você é o 'FinAI', um assistente virtual especializado em relacionamento financeiro e educação bancária.
Sua postura deve ser guiada por excelentes práticas de UX (Experiência do Usuário):
1. Use linguagem clara, simples, acessível e sem jargões bancários complexos.
2. Seja empático, seguro, ético e direto ao ponto.
3. Se o usuário pedir cálculos ou simulações (ex: juros, poupança, investimentos), explique a lógica de forma didática passo a passo.
4. Se o usuário perguntar algo fora do escopo financeiro, reoriente-o gentilmente para o foco do assistente.
5. Nunca forneça conselhos de investimento definitivos ou promessas de ganho fácil; foque em educação demonstrativa.
"""

print("====================================================")
print("   🤖 FinAI - Seu Assistente de Relacionamento Financeiro")
print("        Guiado por IA Generativa & Práticas de UX")
print("====================================================")
print("Digite 'sair' para encerrar a conversa.\n")

# 3. Inicializando o Chat com Persistência de Contexto (Histórico da Conversa)
chat = client.chats.create(
    model="gemini-2.5-flash",
    config=types.GenerateContentConfig(
        system_instruction=instrucoes_sistema,
        temperature=0.4, # Temperatura mais baixa para respostas mais precisas e seguras
    )
)

# 4. Loop de Interação com o Usuário
while True:
    try:
        entrada_usuario = input("Você: ")
        
        if entrada_usuario.lower() in ['sair', 'exit', 'quit']:
            print("\nFinAI: Obrigado por utilizar o FinAI. Até logo!")
            break
            
        if not entrada_usuario.strip():
            continue
            
        # Enviando a mensagem mantendo o contexto da conversa ativa
        response = chat.send_message(entrada_usuario)
        
        print(f"\nFinAI: {response.text}\n")
        print("-" * 50)
        
    except Exception as e:
        print(f"\n❌ Ocorreu um erro na comunicação com a IA: {e}")
        break
