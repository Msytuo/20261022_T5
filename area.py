"""
Vamos a calcular el area de un rectangulo
Para ello haremos una funcion simple que devuelve el area directamente
Vamos a necesitar dos input que pidan los datos al usuario
Las unidades son indiferentes

"""
figuras_validas = ["rectangulo", "circulo", "cuadrado", "triangulo"]

#Comenzamos la funcion
def area_rectangulo(altura, base):
    """
    Resolvemos el area:
    Entrada: Los parametros sin importar la unidades

    Salida: Devuelve el area sin unidades 

    """
    area = altura * base 
    return area



def area_circulo(radio):
    """
    Resolvemos el area:
    Entrada: Los parametros sin importar la unidades
    
     Salida: Devuelve el area sin unidades 
    
    """
    area = 3.1415926535 * radio * radio
    return area


def area_cuadrado(lado):
    """
    Resolvemos el area:
    Entrada: Los parametros sin importar la unidades
    
     Salida: Devuelve el area sin unidades 
    
    """
    area = lado * lado
    return area

def area_triangulo(altura, base):
    """
    Resolvemos el area:
    Entrada: Los parametros sin importar la unidades

    Salida: Devuelve el area sin unidades 

    """
    area = (altura * base)/2
    return area


while True:
    """
    Vamos a crear un bucle, para que el usuario nos diga la figura de la que quiere calcular el area.

    Si me dice un figura que no esta programada, el bucle te pedira una figura valida y se repetira el proceso.

    Utilizaremos las funciones previas para poder minimizar el codigo dentro del bucle.

    """
    
    #Primero pedimos la figura y comenzamos el bucle.
    figura = input("Figura: ").lower()
   
    if figura in figuras_validas:
        if figura == "rectangulo":
            altura = float(input("Dime la altura de tu rectangulo: "))
            base = float(input("Ahora cuanto mide la base: "))
            area_r =  round(area_rectangulo(altura, base),2)
            print(f"El area del rectangulo es {area_r} unidades")

        elif figura == "circulo":
            radio = float(input("Cuanto es el radio de tu circulo: "))
            area_c = round(area_circulo(radio),2)
            print(f"Y el area de tu circulo es {area_c} unidades")

        elif figura == "cuadrado":
            lado = float(input("Ahora cuanto mide el lado: "))
            area_cd =  round(area_cuadrado(lado),2)
            print(f"El area del cudrado es {area_cd} unidades")


        elif figura == "triangulo":
            base = float(input("Ahora cuanto mide la base: "))
            altura = float(input("Y la altura: "))
            area_t =  round(area_triangulo(altura, base),2)
            print(f"El area del triangulo es {area_t} unidades")

    else:
        print("Introduce una figura correcta: ")
