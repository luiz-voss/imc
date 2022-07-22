altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso em Kg: "))

imc = peso / altura ** 2

print("Seu IMC é : %.5f" % imc) ## o comando %.5f % imc : 5f é chamado de especificação de formato, o que denota que a saída deve mostrar apenas quatro casas após o decimal.

if imc < 16:
    print("Magreza grave")
elif imc < 17:
    print("Magreza moderada")
elif imc < 18.5:
    print("Magreza leve")
elif imc < 25:
    print("Saudável")
elif imc < 30:
    print("Sobrepeso")
elif imc < 35:
    print("Obesidade Grau I")
elif imc < 40:
    print("Obesidade Grau II (severa)")
else:
    print("Obesidade Grau III (mórbida)")