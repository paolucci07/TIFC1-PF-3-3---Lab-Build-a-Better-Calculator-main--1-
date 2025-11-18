#LABORATORY: Build a Better Calculator-  Paola Gonzalez 
def main():
  print("Hello learners!")

#funcion suma 
def addmultiplenumbers(numeros):
    total = 0
    for number in numeros:
        total += number
    return total

#funcion multiplicacion
def multiplymultiplenumbers(numeros):
    total = 1
    for num in numeros:
        total *= num
    return total

#funcion de pares
def isiteven(numero):
  return numero % 2 == 0

# funcion de enteros
def isitaninteger(numero):
  return isinstance(numero, int)

if __name__=="__main__":
  print("Sumando 5 + 7 = " + addmultiplenumbers([5,7]).__str__())

  print("Multiplicando 12 * 5 = " + multiplymultiplenumbers([12,5]).__str__())  

  print("Numero par 4 " + isiteven(4).__str__())

  print ("Numero entero 3.5 " + isitaninteger(3.5).__str__())
