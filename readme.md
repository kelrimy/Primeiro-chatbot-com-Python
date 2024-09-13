# Chatbot de Atendimento Ao Cliente

Este projeto é um chatbot simples desenvolvido em Python para fornecer atendimento automatizado às dúvidas frequentes dos clientes da marca de camisetas **de.cada.canto**. O chatbot oferece um menu interativo com respostas pré-definidas para dúvidas frequentes (FAQs), permitindo que os usuários obtenham rapidamente as informações que desejam.

## Vídeo Demonstrativo

Veja o vídeo demonstrativo do chatbot para uma visão mais detalhada de como ele funciona:

[![Veja o vídeo](./chatbot3.jpg)](https://youtu.be/x4dbBhDXieU)


## Funcionalidades

- Exibe um menu com as principais perguntas frequentes (FAQs) no primeiro contato.
- Responde automaticamente de acordo com a escolha do usuário no menu.
- Oferece a opção de falar com um atendente humano.
- Finaliza o atendimento quando o usuário escolhe a opção de sair.

## Menu de Opções

Após a saudação inicial, o chatbot exibe as seguintes opções para o usuário:

1. Formas de pagamento  
2. Material das camisetas  
3. Prazo de entrega  
4. Como rastrear o pedido  
5. Locais de entrega  
6. Trocas e Devoluções  
7. Falar com um atendente  
8. Sair  

## Como o código funciona

O chatbot é implementado com três funções principais:

1. **`exibir_menu()`**: Exibe a saudação inicial e o menu de opções para o cliente.  
   - Esta função é chamada apenas uma vez, no início do atendimento.
  
2. **`processar_entrada(opcao)`**: Recebe a opção selecionada pelo usuário e retorna a resposta correspondente das perguntas frequentes.  
   - Caso o usuário selecione uma opção inválida, uma mensagem de erro é retornada.

3. **`chatbot()`**: A função principal que controla o fluxo de interação.  
   - Exibe o menu de opções e, em seguida, inicia um loop onde o usuário pode interagir com o chatbot até escolher a opção de sair (opção 8).

## Código

```python
import nltk

# Baixar dados necessários para a análise de linguagem natural
nltk.download('punkt')

# Respostas pré-definidas para perguntas frequentes
faq_respostas = {
    "1": "Aceitamos cartões de crédito, débito e PIX.",
    "2": "Todas as nossas camisetas são 100% algodão.",
    "3": "O prazo de entrega é de 2 a 15 dias úteis, dependendo da sua localização. Consulte detalhes no nosso site: www.decadacanto.com.br",
    "4": "Você pode rastrear seu pedido no site dos correios usando o código de rastreamento enviado por e-mail após a confirmação do pagamento ou no nosso site: www.decadacanto.com.br.",
    "5": "Enviamos para todo o Brasil através dos correios. Consulte taxas e prazos no nosso site: www.decadacanto.com.br",
    "6": "Para trocas ou devoluções, entre em contato conosco pelo whatsapp (85) 999999999.",
    "7": "Por favor, deixe a sua dúvida e um atendente entrará em contato assim que possível.",
    "8": "Agradecemos o seu contato. Volte sempre e até logo!"
}

# Função para exibir o menu
def exibir_menu():
    return (
        "Selecione uma das opções abaixo para mais informações:\n"
        "1 - Formas de pagamento\n"
        "2 - Material\n"
        "3 - Prazo de entrega\n"
        "4 - Como rastrear o pedido\n"
        "5 - Locais de entrega\n"
        "6 - Trocas e Devoluções\n"
        "7 - Falar com um atendente\n"
        "8 - Sair"
    )

# Função para processar a entrada do usuário
def processar_entrada(opcao):
    if opcao in faq_respostas:
        return faq_respostas[opcao]
    return "Opção inválida. Por favor, selecione um número válido do menu."

# Função principal do chatbot
def chatbot():
    iniciado = False  # Flag para verificar se o chatbot já foi iniciado

    while True:
        if not iniciado:
            # Entrada do usuário sem prefixo
            usuario_input = input().strip()

            saudacoes = ["olá", "oi", "bom dia", "boa tarde", "boa noite", "como vai", "oi, tudo bem"]
            if any(saludo in usuario_input.lower() for saludo in saudacoes):
                iniciado = True
                # Saudação inicial e menu
                print("de.cada.canto: Olá! Bem-vindo ao atendimento de.cada.canto. Como posso te ajudar hoje?")
                print(f"de.cada.canto: {exibir_menu()}")
            else:
                print("Por favor, inicie a conversa com uma saudação ou pergunta.")
        else:
            usuario_input = input("Você: ").strip()

            if usuario_input == '8':  # Se o usuário escolher a opção de sair
                print(f"de.cada.canto: {faq_respostas['8']}")
                break
            elif usuario_input == '7':  # Se o usuário quiser falar com um atendente
                print(f"de.cada.canto: {faq_respostas['7']}")
                # Solicita uma mensagem do cliente
                mensagem_atendente = input("Você: ").strip()
                print(f"de.cada.canto: Agradecemos a sua mensagem. Um atendente entrará em contato. Até logo!")
                break
            else:
                resposta = processar_entrada(usuario_input)
                print(f"de.cada.canto: {resposta}")

# Executa o chatbot
chatbot()
```


## Dificuldades encontradas

Durante o desenvolvimento deste chatbot, algumas dificuldades foram:

- Controlar a interação do usuário de forma dinâmica, garantindo que o chatbot forneça respostas precisas.
- Evitar redundância de mensagens, especialmente na saudação inicial e ao exibir o menu.
- Gerenciar a lógica do menu de forma a permitir a interação fluida até que o usuário decida encerrar o atendimento.

## Como usar

1. Clone o repositório ou copie o código acima.
2. Instale o [NLTK](https://www.nltk.org/) usando o comando:

   ```bash
   pip install nltk

    ```
## Executando o Chatbot

Execute o arquivo `chatbot.py` no terminal e interaja com o chatbot conforme o menu exibido.

## Melhorias Futuras

- Adicionar mais perguntas frequentes.
- Implementar funcionalidades adicionais, como integração com sistemas de pedidos e rastreamento em tempo real.
- Melhorar o tratamento de linguagem natural para permitir uma interação mais flexível com o cliente.

