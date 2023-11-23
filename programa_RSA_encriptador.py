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

def funcion_codificar_ecuacion(m):
    palabra = m
    lista_numeros = []

    for letra in palabra:
        numero = ord(letra.upper()) - ord('A')
        lista_numeros.append(numero)
    print(lista_numeros)

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
eulerR = funcion_calcular_d(euler,phi)
funcion_verificar_mcd(eulerR)

print("N: "+str(n))
print("phi: "+str(phi))
print("eulerR: "+str(eulerR))