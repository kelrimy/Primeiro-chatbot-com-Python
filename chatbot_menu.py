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
