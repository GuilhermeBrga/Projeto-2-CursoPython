from typing import List, Dict
from time import sleep

from models.produto import Produto
from utils.helper import formata_float_str_moeda

produtos: List[Produto] = []

carrinho: List[Dict[Produto, int]] = []

def main() -> None:
    menu()

def menu() -> None:
    print("=====================================")
    print("==========- Bem Vindo -==============")
    print("=====================================")
    print()

    print("Opções: ")
    print()
    print("1 - Cadastrar produto")
    print("2 - Listar produto")
    print("3 - Adicionar ao carrinho")
    print("4 - Visualizar carrinho")
    print("5 - Fechar compra")
    print("6 - Sair")
    print()

    opcao: int = int(input("Selecione a opção de sua escolha: "))

    if opcao == 1:
        cadastrar_produto()

    elif opcao == 2:
        listar_produtos()

    elif opcao == 3:
        comprar_produto()

    elif opcao == 4:
        visualizar_carrinho()

    elif opcao == 5:
        fechar_pedido()

    elif opcao == 6:
        print("Volte sempre!")
        sleep(2)
        exit(0)

    else:
        print("Opção inválida!")
        sleep(1)
        menu()

def cadastrar_produto() -> None:
    print("===========================")
    print("==- Cadastro de produto -==")
    print("===========================")

    nome: str = input("Informe o nome do produto: ")

    preco: float = float(input("Informe o preço do produto: "))

    ja_cadastrado = False

    for produto in produtos:
        if produto.nome == nome:
            ja_cadastrado = True

    if ja_cadastrado == True:
        print("Esse produto já está cadastrado!")
    
    elif ja_cadastrado == False:
        produto: Produto = Produto(nome, preco)

        produtos.append(produto)

        print()
        print(f"O produto {nome} foi cadastrado com sucesso!")

    sleep(1)

    menu()

def listar_produtos() -> None:
    
    if len(produtos) > 0:
        print("=====================")
        print("==- Seus produtos -==")
        print("=====================")

        for produto in produtos:
            print(produto)
            print()

            sleep(1)

    else:
        print("Nenhum produto foi cadastrado!")
    
    sleep(1)
    menu()

def comprar_produto() -> None:
    
    if len(produtos) > 0:
        
        print("==================================")
        print("===========- Produtos -===========")
        print("==================================")

        for produto in produtos:
            print(produto)
            print()
            sleep(1)

        codigo: int = int(input("Informe o código do produto: "))

        produto: Produto = pega_produto_codigo(codigo)

        if produto:
            if len(carrinho) > 0:
                
                tem_no_carrinho: bool = False

                for item in carrinho:

                    quantidade: int = item.get(produto)

                    if quantidade:
                        item[produto] = quantidade + 1

                        print(f"O produto {produto.nome} possui {quantidade + 1} unidades no carrinho!")
                        tem_no_carrinho = True

                        sleep(1)
                        menu()
                
                if not tem_no_carrinho:
                    
                    prod = {produto: 1}

                    carrinho.append(prod)

                    print(f"O produto {produto.nome} foi adicionado ao carrinho!")

            else:
                item = {produto: 1}
                carrinho.append(item)

                print(f"O produto {produto.nome} foi adicionado ao seu carrinho!")
                
                sleep(1)
                menu()

        else:
            print(f"O produto com o código: {codigo}, não foi encontrado!")

            sleep(2)
            menu()

    else:
        "Não há produtos cadastrados!"

    sleep(1)
    menu()


def visualizar_carrinho() -> None:
    
    if len(carrinho) > 0:
        
        print("================================")
        print("====- Produtos no carrinho -====")
        print("================================")
        print()

        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f"Quantidade: {dados[1]}")
                print()
                sleep(1)

    else:
        print("Ainda não existem produtos no carrinho...")
    
    sleep(1)
    menu()

def fechar_pedido() -> None:
    
    if len(carrinho) > 0:
        
        valor_total: float = 0

        print("============================")
        print("==- Produtos do carrinho -==")
        print("============================")

        for item in carrinho:
            for dados in item.items():

                print(dados[0])
                print(f"Quantidade: {dados[1]}")
                
                valor_total += dados[0].preco * dados[1]

        print()
        print(f"Sua fatura é: {formata_float_str_moeda(valor_total)}")
        print("Volte sempre!!!")

        carrinho.clear()

        sleep(3)
    
    else:
        print("O seu carrinho está vazio... Coloque produtos nele!")
    
    sleep(1)
    menu()


def pega_produto_codigo(codigo: int) -> Produto:
    
    produto_procurado: Produto = None

    for produto in produtos:

        if produto.codigo == codigo:
            
            produto_procurado = produto
    
    return produto_procurado

if __name__ == "__main__":
    main()