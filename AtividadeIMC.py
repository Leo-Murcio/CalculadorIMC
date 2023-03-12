print("Calculador de IMC\n")

altura = float(input("Digite a sua altura: "))
peso = float(input("Digite o seu peso: "))
imc = peso / (altura ** 2)

print("O seu IMC é: {:.2f}".format(imc))