import random
numero_secreto = random.randint(1, 10)

numeroIngresado = int(input("El numero secreto se encuentra entre el 1 y el 50. Ingrese un numero: "))
intentos = 1
while numeroIngresado != numero_secreto and intentos < 5:
        if numeroIngresado < numero_secreto:
            print ("El numero secreto es mayor al numero ingresado")
        else:
            print ("El numero secreto es menor al ingresado")
            intentos = intentos + 1
        numeroIngresado = int(input("ingrese otro numero: "))

if numeroIngresado == numero_secreto:
     print ("Felicidades, usted logro adivinar el numero secreto")
else:
     print (f"Usted no logro adivinar, el numero secreto era {numero_secreto}")