#Ultima modificación 23/11/2023
def funcion_calculan_n(p,q):
    #se calcula el modulo
    n = q*p
    return n

def funcion_calcular_Phi(p,q):
    #se calcula euler
    phi = (p-1)*(q-1)
    return phi

def funcion_calcular_d(euler,phi):
    # mdc entre d y euler sea igual a 1 || mdc(d,e)=1
    #d existen varios valores, se elige
    while phi:
        euler, phi = phi, euler % phi
    return euler

def funcion_verificar_mcd(eulerR):
    if(eulerR==1):
        print("El MCD es igual a 1")

    else:
        print("El MCD no es igual a 1")

def funcion_ecuacion():
    pass
    #e·d ≡ 1(mod Euler)
    #ed(x) +Euler(y) = 1

def funcion_switch_letra_a_numero(letra):
    if(letra == "A"):
        numero = "00"
    elif(letra == "B"):
        numero = "01"  
    elif(letra == "C"):
        numero = "02"   
    elif(letra == "D"):
        numero = "03"   
    elif(letra == "E"):
        numero = "04"   
    elif(letra == "F"):
        numero = "05"   
    elif(letra == "G"):
        numero = "06"   
    elif(letra == "H"):
        numero = "07"   
    elif(letra == "I"):
        numero = "08"   
    elif(letra == "J"):
        numero = "09"   
    elif(letra == "K"):
        numero = "10"   
    elif(letra == "L"):
        numero = "11"   
    elif(letra == "M"):
        numero = "12"   
    elif(letra == "N"):
        numero = "13"   
    elif(letra == "O"):
        numero = "14"   
    elif(letra == "P"):
        numero = "15" 
    elif(letra == "Q"):
        numero = "16"    
    elif(letra == "R"):
        numero = "17"
    elif(letra == "S"):
        numero = "18"
    elif(letra == "T"):
        numero = "19"
    elif(letra == "U"):
        numero = "20"
    elif(letra == "V"):
        numero = "21"
    elif(letra == "W"):
        numero = "22"
    elif(letra == "X"):
        numero = "23"  
    elif(letra == "Y"):
        numero = "24"  
    elif(letra == "Z"):
        numero = "25"                
    return numero

def funcion_codificar_ecuacion(m):
    """
    lista_numeros = []
    palabra = m
    for letra in range(0,len(palabra)):
        numero = funcion_switch_letra_a_numero(palabra[letra])
        lista_numeros.append(numero)
    return lista_numeros
        """
        
    palabra = m
    lista_numeros = []

    for letra in palabra:
        numero = ord(letra.upper()) - ord('A')
        lista_numeros.append(numero)
    print("funcion_codificar_ecuacion")
    print(lista_numeros)


def funcion_concartenar_pares(palabra):
    lista_numeros = []
    
    for letra in range(0,len(palabra)):
        numero = funcion_switch_letra_a_numero(palabra[letra])
        lista_numeros.append(numero)
    #return lista_numeros
    """
    lista_numeros = []

    # Obtener los números correspondientes a las letras, considerando -33 para espacios en blanco
    for letra in palabra:
        if letra == ' ':
            numero = -33  # Utilizar -33 para representar espacios en blanco
        else:
            numero = ord(letra.upper()) - ord('A')
        lista_numeros.append(numero)

    print(lista_numeros)
    """

    # Usar list comprehension para convertir cada elemento a cadena
    lista_cadenas = [str(numero) if numero != -33 else '*' for numero in lista_numeros]

    print(lista_cadenas)

    # Concatenar cada par de índices sucesivos y manejar el último índice
    concatenadas = [a + b if b != '*' else a + b for a, b in zip(lista_cadenas[::2], lista_cadenas[1::2] + [''])]
    return concatenadas
    #print(concatenadas)
    


def multiplicar_base_exponente_Euler(concatenadas, euler,n):
    

    # Lista de cadenas que representan números
    lista_de_cadenas = concatenadas#x

    # Convertir la lista de cadenas a una lista de enteros
    lista_de_enteros = [int(cadena) for cadena in lista_de_cadenas]

    # Mostrar la lista resultante
    print("---Impresion de listados enteros---")
    print(lista_de_enteros)  # Salida: 
    print("")
    euler = euler
    n = n
    lista_de_enterosEponente = []
    for i in range(0,len(lista_de_enteros)):
        x = (lista_de_enteros[i]**euler)%n
        lista_de_enterosEponente.append(x)
    return lista_de_enterosEponente
    #print(lista_de_enterosEponente)



m = (input("Ingres el mesaje: \n ->"))
m = m.upper()
mCodificado = funcion_codificar_ecuacion(m)

p = int(input("Ingrese el valor de p: \n ->"))
q = int(input("Ingrese el valor de q: \n ->"))
euler = int(input("Ingrese un valor de euler(e): \n ->"))

#paso 2
n = funcion_calculan_n(p,q)
#paso 3
phi = funcion_calcular_Phi(p,q)
#llave publica
eulerR = funcion_calcular_d(euler,n)#phi)
funcion_verificar_mcd(eulerR)

#trasncribir palabra a digitos y concatenar en pares
concatenadas = funcion_concartenar_pares(m)

#la lista anterior concatenas en pares de dos, se multiplica por expoencial euler y (mod n) y devuelde encriptada
lista_encriptada = multiplicar_base_exponente_Euler(concatenadas, euler,n)

#-------- Resultado.-----------------
print("N: "+str(n))
print("phi: "+str(phi))
print("eulerR: "+str(eulerR))
print("Lalve publica es: ("+str(euler)+", "+str(n)+")")
print("Lista encriptada: "+str(lista_encriptada))


