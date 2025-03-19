def es_primo(numero):

    if numero < 2:
        return False
    
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    
    return True

def encontrar_primos_gemelos(limite):
 
    pares_gemelos = []
    
    for num in range(2, limite - 1):
        if es_primo(num) and es_primo(num + 2):
            pares_gemelos.append((num, num + 2))
    
    return pares_gemelos

def es_palindromo(numero):
    
    numero_str = str(numero)
    return numero_str == numero_str[::-1]

def encontrar_primos_palindromicos(limite):
    
    primos_palindromicos = []
    
    for num in range(10, limite + 1):
        if es_palindromo(num) and es_primo(num):
            primos_palindromicos.append(num)
    
    return primos_palindromicos

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
            
