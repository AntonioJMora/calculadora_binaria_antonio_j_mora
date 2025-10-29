"""Calculadora binaria"""
import sys

def suma(bin1, bin2):
    """Suma de 2 numeros binarios"""
    acarreo = 0
    b4 = [0]*9 #Lista de 0 para el total de b1 y b2
    for i in range(7,-1,-1):
        bit1 = int(bin1[i])
        bit2 = int(bin2[i])
        sumar = bit1 + bit2 + acarreo
        b4[i+1] = sumar % 2 #Resultado del bit
        acarreo = sumar // 2 #Siguiente acarreo
    b4[0] = acarreo
    return "".join(str(x) for x in b4)

def resta(bin1, bin2):
    """Resta de dos numeros binarios"""
    acarreo = 0
    b4 = [0]*9
    for i in range(7,-1,-1):
        bit1 = int(bin1[i])
        bit2 = int(bin2[i])
        restar = bit1 - (bit2 + acarreo)
        b4[i+1] = restar % 2
        if bit1 < (bit2 + acarreo):
            acarreo = 1
        else:
            acarreo = 0
    return "".join(str(x) for x in b4)

def main():
    if len(sys.argv) <= 3:
        b1 = sys.argv[1]
        if len(b1) > 8 or not all(c in "01" for c in b1):
            print("Error: Escribalo con el siguiente formato: calculadora_binaria.py numero binario simbolo numero binario")
            print("Numero: Los números escritos deben de ser en binario y ser mayor a 1 dígito y menor a 8")
        else:
            b1 = b1.zfill(8) #El zfill rellena la cadena con 0
            b1 = list(b1)
        b2 = sys.argv[2]
        if len(b2) > 8 or not all(c in "01" for c in b2):
            print("Error: Escribalo con el siguiente formato: calculadora_binaria.py numero binario simbolo numero binario")
            print("Numero: Los números escritos deben de ser en binario y ser mayor a 1 dígito y menor a 8")
        else:
            b2 = b2.zfill(8)
            b2 = list(b2)

        resultado1 = print(f"La suma es: {suma(b1,b2)}")
        if b2>b1:
            print("Error el segundo número es mayor al primero por lo que no se puede realizar la resta")

            #Resta binaria de dos numeros
        elif b2<b1:
            resultado = resta(b1, b2)
            print(f"La resta de los bits es {resultado}")

    else:

        b1 = sys.argv[1]
        if len(b1) > 8 or not all(c in "01" for c in b1):
            print("Error: Escribalo con el siguiente formato: calculadora_binaria.py numero binario simbolo numero binario")
            print("Numero: Los números escritos deben de ser en binario y ser mayor a 1 dígito y menor a 8")
        else:
            b1 = b1.zfill(8) #El zfill rellena la cadena con 0
            b1 = list(b1)

        b2 = sys.argv[3]
        if len(b2) > 8 or not all(c in "01" for c in b2):
            print("Error: Escribalo con el siguiente formato: calculadora_binaria.py numero binario simbolo numero binario")
            print("Numero: Los números escritos deben de ser en binario y ser mayor a 1 dígito y menor a 8")
        else:
            b2 = b2.zfill(8)
            b2 = list(b2)

        b3 = sys.argv[2]

        if b3 != '+' and b3 != '-':
            print("Error: Escriba un símbolo que sea + o -")
        else:
            #Suma binaria de los bits y el acarreo
            if b3 == '+':
                resultado = suma(b1, b2)
                #El join une la cadena para no dejar espacios en medio
                print(f"La suma de los bits es {resultado}")

            #Bloquear que no se le pueda restar al primer numero uno que sea mayor
            elif b3 == '-':
                if b2>b1:
                    print("Error el segundo número es mayor al primero por lo que no se puede realizar la resta")

            #Resta binaria de dos numeros
                elif b2<b1:
                    resultado = resta(b1, b2)
                    print(f"La resta de los bits es {resultado}")

if __name__ == "__main__":
    main()
