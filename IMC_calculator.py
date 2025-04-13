#               Pedimos y validamos el valor de Peso
while True:
    peso = float(input('Ingrese su peso en Kg: '))

    try:
        PesoValid = float(peso)
        
        if PesoValid <= 0 or PesoValid >= 400:
            print('El valor indicado para el Peso es invalido, intentelo de nuevo.')    
        else:
            break
        
    except ValueError:
        print('Ingresa un valor valido para el Peso.')

#               Pedimos y validamos el valor de Altura
while True:
    altura = float(input('Ingrese su altura en Metros: '))
    
    try:
        AlturaValid = float(altura)
        
        if AlturaValid <= 0 or AlturaValid >= 3:
            print('El valor indicado para la Altura es invalido, intentalo de nuevo.')
        else:
            break
        
    except ValueError:
        print('Ingrese un valor valido para la Altura.')
        
#               Calculamos el IMC --> IMC = peso / (altura ** 2)
imc = peso / (altura ** 2)
print(f"\nTu IMC es: {imc:.2f}") #:2f hace que el valor de imc (al ser un float) corte en 2 decimales

if imc < 18.5:
    print("Clasificación: Bajo peso")
elif imc < 25:
    print("Clasificación: Peso normal")
elif imc < 30:
    print("Clasificación: Sobrepeso")
elif imc < 35:
    print("Clasificación: Obesidad grado 1")
elif imc < 40:
    print("Clasificación: Obesidad grado 2")
else:
    print("Clasificación: Obesidad grado 3 (mórbida)")