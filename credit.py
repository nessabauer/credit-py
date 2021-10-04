from cs50 import get_int

# Input do número do cartão
number = get_int("Number:")

contador = verifica = resultado = segundo = primeiro = 0

while number > 0:
    # Os pares soma
    if contador % 2 == 0:
        resultado = int(resultado + (number % 10))
    else:
        # Impares multiplica
        verifica = (number % 10) * 2

        # Se a multiplicação der mais que 10 soma um ao outro
        if verifica % 10 != 0 or verifica % 10 == 0:
            verifica = (verifica % 10) + (verifica / 10)

        # Soma as multiplicações
        resultado = int(resultado + verifica)

    # Salvando os primeiros numeros para verificação da bandeira
    segundo = primeiro
    primeiro = number
    contador += 1
    number = int(number / 10)

if resultado % 10 == 0 and (primeiro == 4 or primeiro == 3 or primeiro == 5):
    # All American Express numbers start with 34 or 37
    if (segundo == 34 or segundo == 37) and contador == 15:
        print("AMEX")
    # MasterCard numbers start with 51, 52, 53, 54, or 55
    elif (segundo == 51 or segundo == 52 or segundo == 53 or segundo == 54 or segundo == 55) and contador == 16:
        print("MASTERCARD")
    # Visa numbers start with 4
    elif primeiro == 4 and (contador == 13 or contador == 16):
        print("VISA")
    else:
        print("INVALID")
else:
    # Cartões inválidos
    print("INVALID")
