def bhask(a, b, c):
    disc= (b**2 - 4*a*c)
    if disc>0:  #si el discriminante es mayor a cero, habra dos raices reales.
        y=-b/(2*a)
        z= disc**(1/2) / (2*a)
        return f"la raices de la función son: x1={y+z}, x2={y-z}" 

    elif disc==0: #si el discriminante es igual a cero, habra solo un raiz real.
        x= -b/(2*a)
        return f"La función tiene una sola raiz: x={x}" 

    else: #si el discriminante es negativo, no habra raices reales.
        return "la función no tiene raices reales"

def funcion_bhaskara():
    realizar_cuenta= True
    while realizar_cuenta:
        try:
            #pedimos el valor de las varaibles al usuario
            print("Coloque las variables a, b y c")
            a= float(input("a: "))
            b= float(input("b: "))
            c= float(input("c: "))

            #ejecutamos la funcion bhask e imprimimos el resultado
            print(bhask(a,b,c))

            #preguntamos al usuario si quiere realizar otro cálculo
            continuar= True
            while continuar:
                print("¿Desea realizar otro cálculo? ")
                resp= input("si/no: ").upper()
                if resp=="SI":  #Si desea realizar otro cálculo, volvemos al ciclo anterior
                    continuar= False
                elif resp=="NO":  #si no desea realizar otro cálculo, cerramos ambos ciclos
                    continuar= False
                    realizar_cuenta= False
                    print("Hasta luego.")
                else:  #si la respuesta no esta determinada, continuamos el ciclo actual.
                    print("Elija si/no.")
                
        except: #en el caso de ocurrir un error, se muestra un mensaje
            print("Debe colocar un numero, intente nuevamente")

funcion_bhaskara()
