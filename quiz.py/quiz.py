def es_primo (num):
     
     if num < 2:
         return False
     for i in range(2, int(num**0.5)+1 ): 
         if num % i == 0: 
          return False
     return True
 
 
def encontrar_primos_gemelos(limite):
    primos = [num for num in range (2, limite + 1) if es_primo(num)]
    gemelos = [(primos[i], primos [i+1]) for i in range (len(primos) - 1 )if primos [i+1] - primos[i] == 21]
    return gemelos if gemelos else "no se econtraron primos en el rango dado"
 
def es_palindromicos (num):
    return str(num) == str(num)[::-1]


def encontrar_primos_palindromicos(limite):
   return [num for num in range (10, limite +1 ) if es_primo (num) and es_palindromicos(num)]


def menu():

 while True:
     print("/nSeleccione una opciòn:")
     print("1. encontrar primos gemelos")
     print("2. encontrar primos palindromicos")
     print("3. salir")
     opc = input(">")
     
     if opc == "1":
         limite = int(input("ingrese el limite superior:"))
         primos_gemelos = encontrar_primos_gemelos(limite)
         print("pares de primos encontrados:", primos_gemelos)
    
     elif opc == "2":
         limite = int(input("ingrese el limite superior:"))
         primos_palindromicos = encontrar_primos_palindromicos(limite)
         print("numeros primos palindromicos encontrados:", primos_palindromicos)
         
     elif opc == "3":
         print("¡hasta luego!")
         break
     else:
         print("opcion no valida, por favor intente de nuevo.") 
if __name__ == "__main__":
    menu()
            