import nltk

# Baixar dados necessários para a análise de linguagem natural
nltk.download('punkt')

# Respostas pré-definidas para perguntas frequentes
faq_respostas = {
    "1": "Aceitamos cartões de crédito, débito e PIX.",
    "2": "Todas as nossas camisetas são 100% algodão.",
    "3": "O prazo de entrega é de 2 a 15 dias úteis, dependendo da sua localização. Consulte detalhes no nosso site: www.decadacanto.com.br",
    "4": "Você pode rastrear seu pedido no site dos correios usando o código de rastreamento enviado por e-mail após a confirmação do pagamento ou no nosso site: www.decadacanto.com.br .",
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
    print("Olá! Bem-vindo ao atendimento de.cada.canto. Como posso te ajudar hoje?")
    print(exibir_menu())  # Exibe o menu após a saudação inicial

    while True:
        usuario_input = input("Você: ")

        if usuario_input == '8':
            print(f"de.cada.canto: {faq_respostas['8']}")
            break
        elif usuario_input == '7':
            print(f"de.cada.canto: {faq_respostas['7']}")
            # Registra a dúvida do cliente e encerra o atendimento
            duvida_cliente = input("Você: ")  # Cliente envia a dúvida
            print(f"de.cada.canto: Aguarde só um instante que logo retornaremos com sua resposta.")
            break
        else:
            resposta = processar_entrada(usuario_input)
            print(f"de.cada.canto: {resposta}")

# Rodar o chatbot
chatbot()

