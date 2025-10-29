# Calculadora binaria de 8 bits (Python) - README.

> CLI que **suma** y **resta** números binarios de **1 a 8 bits**.

> **Salida exclusivamente en binario de 8 bits** (relleno con ceros a la izquierda).

> Si no se indica signo, el programa ejecuta **ambas operaciones** (suma y resta).

## 1. Descripción del módulo.
Este proyecto implementa una **calculadora binaria de 8 bits** que opera con **enteros sin signo**.
- Los **operandos** se introducen como **cadenas binarias** de **1 a 8 bits** (`0`/`1`).
- La **operación** se define por **signo**: `+` (suma) o `-` (resta).
- Si **no** se especifica el signo, el programa **realiza ambas operaciones** con los mismos operandos y muestra **dos bloques** de salida.
- Antes de calcular, cada operando se **rellena a 8 bits** para el cálculo/visualización.

## 2. Requisitos.
- **Python 3.10 o superior**

## 3. Instalación de python.
Mi instalación de Python está hecha desde Microsoft Store.

## 4. Ejecución fuera del módulo.
```bash
python calculadora.py b1 simbolo b2
```
- **b1** y **b2** son binarios de **1 a 8 bits**
- El símbolo es opcional, si no pones nada te hará la suma y la resta y en caso de que pongas + te hará la suma y si pones - te hará la resta.

### Ejemplos
- Con el simbolo **+**
```bash
python calculadora.py 111 + 11
La suma de los bits es 000001010
```
- Con el símbolo **-**
```bash
python calculadora.py 111 - 11
La resta de los bits es 000000100
```
- Sin símbolo (En caso de que el segundo número sea mayor, te hará la suma pero en la resta te mostrará un error.)
```bash
python calculadora.py 111 11
La suma es: 000001010
La resta es: 000000100
```

## 5. Mensajes de error y códigos de salida.
- Operando inválido (no binario o mayor a 8 bits): "Error: Escribalo con el siguiente formato: calculadora_binaria.py numero binario simbolo numero binario". 
    - Además abajo viene una explicacion de como deben ser los números: "Numero: Los números escritos deben de ser en binario y ser mayor a 1 dígito y menor a 8"
- Signo/operación invalida (que sea distinto de + o -): "Error: Escriba un símbolo que sea + o -"
- En la resta, si el segundo número es máyor al primero te mostrará lo siguiente: "Error el segundo número es mayor al primero por lo que no se puede realizar la resta"

## 6. Problemas frecuentes (FAQ)

- **“python: command not found” / “py no se reconoce”** → Instala Python o ajusta el **PATH**.
- **“pip no se reconoce”** → Usa `python -m pip` (o `py -m pip` en Windows).
- **Formato de operando incorrecto** → Revisa que sean solo `0`/`1` y longitud ≤ 8.
- **Signo en posición incorrecta** → Asegúrate de usar `OPERANDO1 [SIGNO] OPERANDO2`