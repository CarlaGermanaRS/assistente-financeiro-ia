# 🤖 FinAI - Assistente Virtual de Relacionamento Financeiro com IA Generativa

Este projeto foi desenvolvido como desafio prático para a plataforma **DIO**, focando na criação de uma experiência digital inteligente para o setor financeiro. A solução utiliza a API oficial do **Google Gemini** para fornecer respostas contextualizadas, seguras e personalizadas.

## 🎯 Escopo do Desafio Atendido
Conforme a descrição do projeto, o assistente foi projetado sob os seguintes pilares:
*   **IA Generativa & Persistência de Contexto:** Utilização do modelo `gemini-2.5-flash` mantendo o histórico da sessão (chat contínuo).
*   **Boas Práticas de UX:** Instruções de sistema customizadas para garantir que a IA responda de forma simples, clara, empática e sem jargões complexos.
*   **Segurança Financeira:** Filtros comportamentais para evitar promessas de ganhos ou conselhos de investimento de alto risco, mantendo o foco em educação financeira e FAQs inteligentes.

## 🛠️ Tecnologias
*   Python 3
*   Google GenAI SDK (Interface oficial do Gemini)

## 🚀 Como Executar
1. Instale as dependências: `pip install -r requirements.txt`
2. Configure sua chave de API do Google AI Studio:
   * No Windows (CMD): `set GEMINI_API_KEY="sua_chave_aqui"`
   * No Linux/Mac: `export GEMINI_API_KEY="sua_chave_aqui"`
3. Execute o assistente: `python main.py`