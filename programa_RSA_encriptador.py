#Programa del proyecto RSA encriptador
#Matemática Discreta UVG
#Nelson García 22434
#Brandon Reyes 22


def funcion_calculan_n(p,q):
    n = q*p
    return n

def funcion_calcular_Phi(p,q):
    phi = (p-1)*(q-1)
    return phi

def funcion_calcular_mcd(euler,phi):
    while phi:
        euler, phi = phi, euler % phi
    return euler

def funcion_verificar_mcd(mcd):
    cond = True
    if(mcd==1):
        print("El MCD es igual a 1")
    else:
        print("El MCD no es igual a 1")
        cond = False
    return cond


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
    pass


def funcion_concartenar_pares(palabra):
    lista_numeros = []
    
    for letra in range(0,len(palabra)):
        numero = funcion_switch_letra_a_numero(palabra[letra])
        lista_numeros.append(numero)

    lista_cadenas = [str(numero) if numero != -33 else '*' for numero in lista_numeros]

    concatenadas = [a + b if b != '*' else a + b for a, b in zip(lista_cadenas[::2], lista_cadenas[1::2] + [''])]
    return concatenadas    


def multiplicar_base_exponente_Euler(concatenadas, euler,n):
    
    lista_de_cadenas = concatenadas#x

    lista_de_enteros = [int(cadena) for cadena in lista_de_cadenas]

    euler = euler
    n = n
    lista_de_enterosEponente = []
    for i in range(0,len(lista_de_enteros)):
        x = (lista_de_enteros[i]**euler)%n
        lista_de_enterosEponente.append(x)
    return lista_de_enterosEponente


def funcion_resultado(lista_encriptada):
    # Convierte cada número a cadena y agrega ceros a la izquierda si es necesario
    lista_cadenas = [str(numero).zfill(4) for numero in lista_encriptada]
    return lista_cadenas
    

def encriptar():
    m = (input("(1) Ingrese el mesaje a encriptar: \n ->"))
    m = m.upper()
    mCodificado = funcion_codificar_ecuacion(m)

    p = int(input("(2) Ingrese el valor de p: \n ->"))
    q = int(input("(3) Ingrese el valor de q: \n ->"))

    n = funcion_calculan_n(p,q)

    phi = funcion_calcular_Phi(p,q)
    
    cond = False
    euler = 0
    while(cond==False):
        euler = int(input("(4) Ingrese un valor de euler(e): \n ->"))
        mcd = funcion_calcular_mcd(euler,phi)
        cond = funcion_verificar_mcd(mcd)
    
    concatenadas = funcion_concartenar_pares(m)

    lista_encriptada = multiplicar_base_exponente_Euler(concatenadas, euler,n)

    resultadoF = funcion_resultado(lista_encriptada)

    print("-------Resultado-------")
    print("(1) N: "+str(n))
    print("(2) phi: "+str(phi))
    print("(3) euler: "+str(euler))
    print("(4) LLave publica es: ("+str(euler)+", "+str(n)+")")
    print("(5) Lista encriptada: "+str(lista_encriptada))
    print("(6) El mensaje encriptado es: "+str(resultadoF))

def desencriptar():
    pass

print("-------Bienvenido al programa RSA encriptador-------")
print("Elija una opcion: ")
print("(1) Encriptar")
print("(2) Desencriptar")
print("(3) Salir")
opcion = 0
while(opcion!=1 and opcion!=2 and opcion!=3):
    opcion = int(input("->"))
    print("Opción no valida")
if(opcion==1):
    print("-------Encriptar-------")
    encriptar()
elif(opcion==2):
    print("-------Desencriptar-------")
    desencriptar()
else:   
    print("-------Salir-------")
    exit()

