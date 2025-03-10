import Pila
import math
import InFix2PostFix

def postfix2Value(postfix):
    lista = postfix.split()
    print("Expresión Postfix", lista)  # Mostrar la expresión postfija
    pila = Pila.Pila()
    for x in lista:
        if x.replace('.', '', 1).isdigit() or (x[0] == '-' and x[1:].replace('.', '', 1).isdigit()):
            number = float(x)
            pila.push(number)
        else:
            match x:
                case "+":
                    B = pila.pop()
                    A = pila.pop()
                    C = A + B
                case "-":
                    B = pila.pop()
                    A = pila.pop()
                    C = A - B
                case "*":
                    B = pila.pop()
                    A = pila.pop()
                    C = A * B
                case "/":
                    B = pila.pop()
                    A = pila.pop()
                    C = A / B
                case "^":
                    B = pila.pop()
                    A = pila.pop()
                    C = A ** B
                case "log":
                    A = pila.pop()
                    C = math.log10(A)
                case "ln":
                    A = pila.pop()
                    C = math.log(A)
                case "sin":
                    A = pila.pop()
                    C = math.sin(math.radians(A))
                case "cos":
                    A = pila.pop()
                    C = math.cos(math.radians(A))
                case "tan":
                    A = pila.pop()
                    C = math.tan(math.radians(A))
                case "arctan":
                    A = pila.pop()
                    C = math.degrees(math.atan(A))
                case "asin":
                    A = pila.pop()
                    C = math.degrees(math.asin(A))
                case "arccos":
                    A = pila.pop()
                    C = math.degrees(math.acos(A))
                case "sqrt":
                    A = pila.pop()
                    C = math.sqrt(A)
                case "exp":
                    A = pila.pop()
                    C = math.exp(A)
                case "alog":
                    A = pila.pop()
                    C = 10**(A)
                case 'aln':
                    A = pila.pop()
                    C = math.exp(A)
            pila.push(C)
    value = pila.pop()
    return value

#Para comvertir grados a radianes
"""
def grados_a_radianes(grados):
    A=pil.pop()
    C=A * pi / 180
"""   
#Prueba 1
"""
infix = "4-3^2/3+7*(1-2)"
postfix = "4 3 2 ^ 3 / - 7 1 2 - * +"""
#valor = -6
#Prueba 2
"""
infix  = '2*(2^3*2-6/(4-2)-10)-2' 
postfix = "2 2 3 ^ 2 * 6 4 2 - / - 10 - * 2 -"
"""
#valor = 4
#Prueba 3
"""
infix = '5 * ( 6 + 2 ) - 12 / 4'	
postfix = '5 6 2 + * 12 4 / -'
"""
#Valor = 37
#Prueba 4
"""
infix = "4-3^2/3+7*(1-2)"
postfix = "4 3 2 ^ 3 / - 7 1 2 - * +"
"""
#valor = -6
#Prueba 5
"""
infix  = '2*(2^3*2-6/(4-2)-10)-2' 
postfix = "2 2 3 ^ 2 * 6 4 2 - / - 10 - * 2 -"
"""
#valor = 4
#Prueba 6
""""
"infix = '2 ^ 4 / ( 4 * 1 ) + log ( 110 - 10 ) ^ 2'  
postfix = '2 4 ^ 4 1 * / 110 10 - log 2 ^ +'
"""
#valor = 8

#Prueba 7
""""
"infix = '2*alog(0+2)^3'
postfix = '2', '0', '2', '+', 'alog', '3', '^', '*'
"""
#valor = 

#Prueba 8
""""
"infix = 
postfix = 
"""
#valor = 8

#Prueba 9
"""

"""
#valor = 8
if __name__ == "__main__":
    convertidor = InFix2PostFix.Infix2Postfix()
    expresion = '5--3'
    postfix = convertidor.infix2postfix(expresion)
    print("Expresión Infix:", expresion)
    valor = postfix2Value(postfix)
    print("Valor calculado:", valor)
