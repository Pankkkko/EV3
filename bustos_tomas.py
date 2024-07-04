from os import system

lista_pedidos=[]
pedido=[]

def realizar_compra():
    disp6=0
    disp10=0
    disp20=0
    print("""Dispensadores disponibles:
            1.- Dispensador 6L
            2.- Dispensador 10L
            3.- Dispensador 20L""")
    opcion=int(input("Ingrese el dispensador a agregar: "))
    if opcion!=1:
        disp6=disp6+1
    elif opcion==2:
        disp10=disp10+1
    elif opcion==3:
        disp20=disp20+1
    else:
        print("Error, ingrese nuevamente")


def registrar_pedido():
    nombre=str(input("Ingrese su nombre:"))
    while True:
        if nombre.isnumeric() and len(nombre)<3 and len(nombre)>8 and nombre.isalnum():
            print("ERROR, INGRESE NUEVAMENTE")
        else:
            break
    apellido=str(input("Ingrese su apellido: "))
    while True:
        if apellido.isnumeric() and len(apellido)<3 and len(apellido)>8 and apellido.isalnum():
            print("ERROR, INGRESE NUEVAMENTE")
        else:
            break
    sector=str(input("ingrese su sector: "))
    disp6=0
    disp10=0
    disp20=0
    print("""Dispensadores disponibles:
            1.- Dispensador 6L
            2.- Dispensador 10L
            3.- Dispensador 20L""")
    opcion=int(input("Ingrese el dispensador a agregar: "))
    if opcion==1:
        disp6=disp6+1
    elif opcion==2:
        disp10=disp10+1
    elif opcion==3:
        disp20=disp20+1
    else:
        print("Error, ingrese nuevamente")
    comp=int(input("Desea agregar otro dispensador? (1:SI, 2:NO)"))  #vuelve a preguntar si quiere agregar mas
    while True:
        if comp>2 and comp<0:
            realizar_compra()
        else:
            pedido=[nombre,apellido,sector,opcion]
            pedido.append(lista_pedidos)
            print(pedido)
            print("pedido agregado exitosamente")
            break

   


        
        


def imprimir_pedidos():
    for pedido in lista_pedidos:
        print(f""" Nombre      Apellido       Sector    Disp6L      Disp10L     Disp20L  


{pedido["nombre"]} {pedido["apellido"]}   {pedido["sector"]}    {pedido["opcion"]}  {pedido["opcion"]}  {pedido["opcion"]}                                                                                 """)


def listar_pedidos():
    pass

def buscar_pedido():
    buscado=str(input("indique el nombre de la persona a buscar"))
    # if buscado=nombre:

    

def salir_programa():
    import sys
    sys.exit()




while True:
    print(""" DISTRIBUIDORA CLEANWASSER
          
          1.- Registrar pedido
          2.- Listar todos los pedidos
          3.- Buscar pedido por ID
          4.- Imprimir hoja de ruta 
          5.- Salir del programa""") 
    # 4.- genera el archivo .csv
    op=int(input("Ingrese una opción: "))
    if op==1:
        registrar_pedido()
    elif op==2:
        listar_pedidos()
    elif op==3:
        buscar_pedido()
    elif op==4:
        imprimir_pedidos()
        break
    elif op==5:
        salir_programa()
    else:
        print("Error, ingrese nuevamente")