#           Variable para pedir numeros
def pedir_float(mensaje, minimo, maximo):
    while True:
        pedir_valor = input(mensaje)
        
        try:
            valor = float(pedir_valor)
            if valor < minimo or valor > maximo:
                print(f'el valor ingresado debe estar entre {minimo} y {maximo}.')
            else:
                return valor # en la funcion no usamos break, usamos RETURN, ya que asi se termina el bucle y ademas se guarda el valor de la VARIABLE            

        except ValueError:
            print("Ingrese un numero valido")

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def clasificar_imc(imc):
    if imc < 18.5:
        print("Clasificación: Bajo peso ⚠️")
    elif imc < 25:
        print("Clasificación: Peso normal ✅")
    elif imc < 30:
        print("Clasificación: Sobrepeso ⚠️")
    elif imc < 35:
        print("Clasificación: Obesidad grado 1 ❗")
    elif imc < 40:
        print("Clasificación: Obesidad grado 2 ❗❗")
    else:
        print("Clasificación: Obesidad grado 3 (mórbida) 🚨")
#       Apartado grafico del programa        

print("📊 Calculadora de IMC - Índice de Masa Corporal")

peso = pedir_float('Ingrese su peso en Kg: ', 1, 400)
altura = pedir_float('Ingrese su altura en Metros: ', 0.5, 3)

imc = calcular_imc(peso, altura)
clasificar_imc(imc)