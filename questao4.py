class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    
    def calcular_total(self):
        return self.preco * self.quantidade
    
    def imprimir(self):
        print("Nome:", self.nome)
        print("Preço:", self.preco)
        print("Quantidade:", self.quantidade)
        print("Total:", self.calcular_total())


class Livro(Produto):
    def __init__(self, nome, preco, quantidade, genero):
        super().__init__(nome, preco, quantidade)
        self.genero = genero
    
    def imprimir(self):
        super().imprimir()
        print("genero:", self.genero)


class CD(Produto):
    def __init__(self, nome, preco, quantidade, estilo):
        super().__init__(nome, preco, quantidade)
        self.estilo = estilo
    
    def imprimir(self):
        super().imprimir()
        print("Estilo:", self.estilo)


class DVD(Produto):
    def __init__(self, nome, preco, quantidade, classificacao):
        super().__init__(nome, preco, quantidade)
        self.classificacao = classificacao
    
    def imprimir(self):
        super().imprimir()
        print("Classificacão:", self.classificacao)


def exibir_menu():
    print("Escolha uma opção:")
    print("1. Produto")
    print("2. Livro")
    print("3. CD")
    print("4. DVD")
    print("0. Sair")
    return int(input("Opção: "))


while True:
    opcao = exibir_menu()
    
    if opcao == 0:
        break
    
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    quantidade = int(input("Digite a quantidade do produto: "))
    
    if opcao == 1:
        produto = Produto(nome, preco, quantidade)
    elif opcao == 2:
        genero = input("Digite o genero do livro: ")
        produto = Livro(nome, preco, quantidade, genero)
    elif opcao == 3:
        estilo = input("Digite o estilo de artista: ")
        produto = CD(nome, preco, quantidade, estilo)
    elif opcao == 4:
        classificacao = input("Digite a classificacao do filme: ")
        produto = DVD(nome, preco, quantidade, classificacao)
    else:
        print("Opção inválida!")
        continue
    
    print("\nInformações do Produto:")
    produto.imprimir()
    print()

print("Programa encerrado.")
