Jailson Nunes
Adivinhacao

print("******** Bem Vindo ao Jogo de Adivinhacao *********")

numero_secreto = 31

chute = input("Digite Seu Chute: ")

chute_inteiro = int(chute)

if(chute_inteiro == numero_secreto):
	print("Voce Acertou")
elif(chute_inteiro>numero_secreto):
	print("Não Foi Dessa Vez. Seu Chute acima do numero secreto")
elif(chute_inteiro<numero_secreto):
	print("Não Foi Dessa Vez. Seu Chute Foi abaixo do numero secreto")
else:
	print("Voce errou")

