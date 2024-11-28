# Inicializando a matriz vazia
matriz = []
soma = 0

# Preenchendo a matriz com valores do usuário
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor para a posição [{i+1}, {j+1}]: "))
        linha.append(valor)
        soma += valor
    matriz.append(linha)

# Exibindo a matriz e a soma dos elementos
print("\nMatriz 3x3:")
for linha in matriz:
    print(linha)

print(f"\nSoma de todos os elementos: {soma}")
