#Programa del proyecto RSA encriptador
#Matemática Discreta UVG
#Nelson García 22434
#Brandon Reyes 22992


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
    numero = ""
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

def funcion_switch_numero_a_letra(numero):
    letra = ""
    if(numero == "00"):
        letra = "A"
    elif(numero == "01"):
        letra = "B"  
    elif(numero == "02"):
        letra = "C"   
    elif(numero == "03"):
        letra = "D"   
    elif(numero == "04"):
        letra = "E"   
    elif(numero == "05"):
        letra = "F"   
    elif(numero == "06"):
        letra = "G"   
    elif(numero == "07"):
        letra = "H"   
    elif(numero == "08"):
        letra = "I"   
    elif(numero == "09"):
        letra = "J"   
    elif(numero == "10"):
        letra = "K"   
    elif(numero == "11"):
        letra = "L"   
    elif(numero == "12"):
        letra = "M"   
    elif(numero == "13"):
        letra = "N"   
    elif(numero == "14"):
        letra = "O"   
    elif(numero == "15"):
        letra = "P" 
    elif(numero == "16"):
        letra = "Q"    
    elif(numero == "17"):
        letra = "R"
    elif(numero == "18"):
        letra = "S"
    elif(numero == "19"):
        letra = "T"
    elif(numero == "20"):
        letra = "U"
    elif(numero == "21"):
        letra = "V"
    elif(numero == "22"):
        letra = "W"
    elif(numero == "23"):
        letra = "X"  
    elif(numero == "24"):
        letra = "Y"  
    elif(numero == "25"):
        letra = "Z"                
    return letra

def funcion_concartenar_pares(palabra):
    lista_numeros = []
    
    for letra in range(0,len(palabra)):
        if palabra[letra] != " ":
            numero = funcion_switch_letra_a_numero(palabra[letra])
            lista_numeros.append(numero)
        else:
            continue
    if(len(lista_numeros)%2!=0):
        lista_numeros.append("23")

    lista_cadenas = [str(numero) if numero != -33 else '*' for numero in lista_numeros]

    concatenadas = [a + b if b != '*' else a + b for a, b in zip(lista_cadenas[::2], lista_cadenas[1::2] + [''])]
    return concatenadas    

def funcion_concartenar_pares_desencriptar(numeros):
    lista_letras = []
    
    for numero in range(0,len(numeros)):
        letra = funcion_switch_numero_a_letra(numeros[numero])
        lista_letras.append(letra)
    
    concatenadas = ''.join(lista_letras)

    return concatenadas

def multiplicar_base_exponente_Euler(concatenadas, euler,n):
    
    lista_de_cadenas = concatenadas

    lista_de_enteros = [int(cadena) for cadena in lista_de_cadenas]

    euler = euler
    n = n
    lista_de_enterosEponente = []
    for i in range(0,len(lista_de_enteros)):
        x = (lista_de_enteros[i]**euler)%n
        lista_de_enterosEponente.append(x)
    return lista_de_enterosEponente

def multiplicar_base_exponente_D(numeros, d,mod):
    lista_de_enterosEponente = []
    for i in range(0,len(numeros)):
        x = (int(numeros[i])**d)%mod
        lista_de_enterosEponente.append(str(x))
    return lista_de_enterosEponente


def funcion_resultado(lista_encriptada):
    lista_cadenas = [str(numero).zfill(4) for numero in lista_encriptada]
    return lista_cadenas

def euclides_extendido(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = euclides_extendido(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def inverso_modular(a, m):
    gcd, x, _ = euclides_extendido(a, m)
    if gcd != 1:
        print("El inverso no existe porque a y m no son coprimos")
    return x % m  

def obtener_input_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Por favor, ingrese un número entero.")

def obtener_input_cadena(mensaje):
    cond = False
    while True:
        cadena = input(mensaje)
        cadena = cadena.upper()
        lista = list(cadena)
        lista = [x for x in lista if x != " "]
        for i in lista:
            if i.isalpha():
                if(i in ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]):
                    cond = True
                else:
                    cond = False
                    print("Por favor, ingrese solo letras del alfabeto inglés.")
            else:
                cond = False
                print("Por favor, ingrese solo caracteres alfabéticos.")
        if(cond==True):
            return cadena 
        else:
            break

def obtener_input_numerico_como_cadena(mensaje):
    while True:
        cadena = input(mensaje)
        if cadena.isdigit(): 
            return cadena
        else:
            print("Por favor, ingrese solo números.")

def es_primo(numero):
    contador = 0
    for i in range(1, numero + 1):
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            contador += 1
    if contador == 0:
        return True
    else:
        return False

def encriptar():
    m = (obtener_input_cadena("Ingrese el mensaje a encriptar: \n ->"))

    p = int(obtener_input_entero("Ingrese el valor de p: \n ->"))

    while(es_primo(p)==False):
        print("El valor de p no es primo")
        p = int(obtener_input_entero("Ingrese el valor de p: \n ->"))

    q = int(obtener_input_entero("Ingrese el valor de q: \n ->"))

    while(es_primo(q)==False):
        print("El valor de q no es primo")
        q = int(obtener_input_entero("Ingrese el valor de q: \n ->"))

    n = funcion_calculan_n(p,q)
    phi = funcion_calcular_Phi(p,q)
    cond = False
    euler = 0

    while(cond==False):
        euler = int(obtener_input_entero("Ingrese el valor de euler(e): \n ->"))
        mcd = funcion_calcular_mcd(euler,phi)
        cond = funcion_verificar_mcd(mcd)
    
    concatenadas = funcion_concartenar_pares(m)
    print(concatenadas)
    lista_encriptada = multiplicar_base_exponente_Euler(concatenadas, euler,n)

    resultadoF = funcion_resultado(lista_encriptada)

    print("-------Resultado-------")
    print("N: "+str(n))
    print("phi: "+str(phi))
    print("euler: "+str(euler))
    print("LLave publica es: ("+str(euler)+", "+str(n)+")")
    print("Lista encriptada: "+str(lista_encriptada))
    print("El mensaje encriptado es: "+str(resultadoF))

def desencriptar():
    m_ = (obtener_input_numerico_como_cadena("Ingrese el mensaje a desencriptar, todo junto por favor: \n ->"))

    print("Ahora con N = p*q")
    p = int(obtener_input_entero("Ingrese el valor de p: \n ->"))

    while(es_primo(p)==False):
        print("El valor de p no es primo")
        p = int(obtener_input_entero("Ingrese el valor de p: \n ->"))

    q = int(obtener_input_entero("Ingrese el valor de q: \n ->"))

    while(es_primo(q)==False):
        print("El valor de q no es primo")
        q = int(obtener_input_entero("Ingrese el valor de q: \n ->"))

    N = funcion_calculan_n(p,q)
    phi = funcion_calcular_Phi(p,q)
    mcd = 0
    cond = False
    while (cond == False):
        e = int(obtener_input_entero("Ingrese el valor de e: \n ->"))
        mcd = funcion_calcular_mcd(e,phi)
        cond = funcion_verificar_mcd(mcd)
    
    d = inverso_modular(e,phi)

    lista_numeros = []
    for i in range(0,len(m_),4):
        lista_numeros.append(m_[i:i+4])
    
    lista_desencriptada = multiplicar_base_exponente_D(lista_numeros, d,N)

    lista_desencriptada = funcion_resultado(lista_desencriptada)
    
    lista_numeros_2 = []
    for j in range(0,len(lista_desencriptada)):
        for i in range(0,len(lista_desencriptada[j]),2):
            lista_numeros_2.append(lista_desencriptada[j][i:i+2]) 
    
    resultadoF = funcion_concartenar_pares_desencriptar(lista_numeros_2)

    print("-------Resultado-------")
    print("N: "+str(N))
    print("phi: "+str(phi))
    print("LLave privada es: d = "+str(d))
    print("Lista desencriptada: "+str(lista_desencriptada))
    print("El mensaje desencriptado es: "+str(resultadoF))
    
print("-------Bienvenido al programa RSA encriptador-------")
print("Elija una opcion: ")
print("(1) Encriptar")
print("(2) Desencriptar")
print("(3) Salir")
opcion = 0
while(opcion not in [1, 2, 3]):
    opcion = obtener_input_entero("\n ->")
    if((opcion not in [1, 2, 3])):
        print("Ingrese una opcion valida")
        opcion = 0
if(opcion==1):
    print("-------Encriptar-------")
    encriptar()
elif(opcion==2):
    print("-------Desencriptar-------")
    desencriptar()
else:   
    print("-------Salir-------")
    exit()

