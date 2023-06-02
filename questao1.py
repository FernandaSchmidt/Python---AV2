def cadastrar_pessoa():
    pessoa = {}
    pessoa['nome'] = input("Digite o nome da pessoa: ")
    pessoa['idade'] = int(input("Digite a idade da pessoa: "))
    pessoa['cpf'] = input("Digite o CPF da pessoa: ")
    return pessoa

def remover_menores(dicionario):
    maiores = {}
    menores = {}
    for chave, valor in dicionario.items():
        if valor['idade'] >= 18:
            maiores[chave] = valor
        else:
            menores[chave] = valor
    return maiores, menores


pessoas = {}
opcao = 's'
while opcao.lower() == 's':
    pessoa = cadastrar_pessoa()
    pessoas[pessoa['cpf']] = pessoa
    opcao = input("Deseja cadastrar outra pessoa? (s/n): ")

maiores_de_idade, menores_de_idade = remover_menores(pessoas)

print("Pessoas maiores de idade:")
for chave, valor in maiores_de_idade.items():
    print("CPF:", chave)
    print("Nome:", valor['nome'])
    print("Idade:", valor['idade'])
    print()

print("Pessoas menores de idade:")
for chave, valor in menores_de_idade.items():
    print("CPF:", chave)
    print("Nome:", valor['nome'])
    print("Idade:", valor['idade'])
    print()