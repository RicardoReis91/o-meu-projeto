def carregar_menu(ficheiro):
    menu = {}
    try:
        with open(ficheiro, 'r') as f:
            for linha in f:
                codigo, nome, preco = linha.strip().split(', ')
                menu[int(codigo)] = {'nome': nome, 'preco': float(preco)}
    except FileNotFoundError:
        print("Erro: ficheiro de menu não encontrado.")
    return menu

def mostrar_menu(menu):
    print("\n--- MENU ---")
    for codigo, item in menu.items():
        print(f"{codigo} - {item['nome']} - {item['preco']:.2f}€")

def fazer_pedido(menu, carrinho):
    try:
        codigo = int(input("Código do item: "))
        if codigo in menu:
            quantidade = int(input("Quantidade: "))
            carrinho.append((menu[codigo], quantidade))
            print(f"{quantidade}x {menu[codigo]['nome']} adicionados ao pedido.")
        else:
            print("Item inválido.")
    except ValueError:
        print("Entrada inválida.")

def mostrar_pedido(carrinho):
    print("\n--- PEDIDO ATUAL ---")
    total = 0
    for item, qtd in carrinho:
        subtotal = item['preco'] * qtd
        print(f"{qtd}x {item['nome']} - {subtotal:.2f}€")
        total += subtotal
    print(f"Total: {total:.2f}€")

def main():
    menu = carregar_menu('menu.txt')
    if not menu:
        return

    carrinho = []
    while True:
        print("\n1. Ver Menu")
        print("2. Fazer Pedido")
        print("3. Ver Pedido Atual")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            mostrar_menu(menu)
        elif opcao == '2':
            fazer_pedido(menu, carrinho)
        elif opcao == '3':
            mostrar_pedido(carrinho)
        elif opcao == '4':
            print("Obrigado pela preferência! Até breve.")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
