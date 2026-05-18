# 🤖 Bot Drive - Telegram Bot com Gemini AI

Um bot Telegram inteligente alimentado pela API do Google Gemini que responde perguntas e mantém conversas naturais.

## ✨ Recursos

- 💬 Conversas naturais usando Gemini AI
- 🧠 Respostas inteligentes e contextualizadas
- 📱 Interface simples via Telegram
- 🔒 Suporte a variáveis de ambiente para segurança
- ⚡ Processamento de mensagens longas (até 4000 caracteres)

## 🚀 Como Começar

### Pré-requisitos

- Python 3.8+
- Conta no Telegram
- Chave de API do Google Gemini
- Pip (gerenciador de pacotes Python)

### Instalação

1. **Clone o repositório**
```bash
git clone https://github.com/opsib49-collab/bot-drive.git
cd bot-drive
```

2. **Crie um ambiente virtual**
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. **Instale as dependências**
```bash
pip install -r requirements.txt
```

4. **Configure as variáveis de ambiente**
```bash
cp .env.example .env
```

Edite o arquivo `.env` e adicione suas credenciais:
```
TELEGRAM_TOKEN=seu_token_do_bot
GEMINI_API_KEY=sua_chave_api_do_gemini
```

### Como Obter as Credenciais

#### Token do Telegram
1. Abra o Telegram e procure por [@BotFather](https://t.me/botfather)
2. Use o comando `/newbot` para criar um novo bot
3. Siga as instruções e copie o token gerado

#### Chave de API do Gemini
1. Acesse [Google AI Studio](https://aistudio.google.com/apikey)
2. Clique em "Create API Key"
3. Selecione seu projeto e gere a chave
4. Copie a chave para o arquivo `.env`

## 💻 Uso

Execute o bot com:
```bash
python main.py
```

O bot ficará rodando e pronto para receber mensagens no Telegram.

### Comandos Disponíveis

- `/start` - Inicia o bot e exibe mensagem de boas-vindas
- Envie qualquer mensagem de texto para receber uma resposta inteligente

## 🔒 Segurança

⚠️ **Importante**: Nunca commit suas chaves de API ou tokens no Git!

- O arquivo `.env` está protegido pelo `.gitignore`
- Use sempre o arquivo `.env.example` como template
- Revogue chaves comprometidas imediatamente nos seus respectivos painéis

## 📦 Dependências

- `python-telegram-bot` - Biblioteca oficial do Telegram
- `google-generativeai` - SDK do Google Gemini
- `python-dotenv` - Gerenciamento de variáveis de ambiente

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:
- Relatar bugs
- Sugerir melhorias
- Fazer pull requests

## 📝 Licença

Este projeto está sob a licença MIT.

## 📧 Contato

Dúvidas ou sugestões? Abra uma issue ou entre em contato!

---

**Desenvolvido com ❤️ por [opsib49-collab](https://github.com/opsib49-collab)**
