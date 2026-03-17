#Empeze hace unos dias a aprender python por mi cuenta asi que decidi hacer un mini proyecto basico para empezar mi portafolio
def suma():
    #creare todas las operaciones mendiantes funciones asi se vea mas organizado
    print("Bienvenido al menu de Sumar")
    #Float para que pueda sumar decimales o lo que el usuario pida 
    num1=float(input("Ingrese el primer numero:"))
    num2=float(input("Ingrese el segundo numero:"))
    resultado=num1+num2
    print(f"El resultado es:{resultado}")
    #Un pequeño error fue poner esta funcion despues del menu ocasionando error

def resta():
    print("Bienvenido al menu de Resta")
    num1=float(input("Ingrese el primer numero:"))
    num2=float(input("Ingrese el segundo numero:"))
    resultado=num1-num2
    print(f"El resultado de la resta es:{resultado}")
    #Es la misma logica que de suma

def division():
    print("Bienvenido al menu de Division")
    #el try servira para que el usuario no agregue letras en vez de numeros
    try:
            num1=float(input("Ingrese el primer numero:"))
            #decidi poner un while para que solo se repita en caso el usuario ponga un 0 en el num2 asi no se sobre carga la memoria
            while True:
                    #Un try para evitar que el usuario ingrese datos como una cadena de texto o string en vez de un int(entero)
                    try:
                        num2=float(input("Ingrese el segundo numero:"))
                        #puse un if para evitar el programa se pare cuando el usuario quiera dividir con 0
                        if(num2==0):
                            print("No se puede dividir entre cero ")
                            #para evitar que se el programa se pare y tenga que pasar la verificacion denuevo se ejecute la funcion de division denuevo
                        else:
                            resultado=num1/num2
                            print(f"El resultado es:{resultado}")
                            break
                    except ValueError:
                        print("ERROR Ingrese un numero")
    except ValueError:
                print("ERROR ingrese un numero")
    

def multiplicacion():
    print("Bienvenido al menu de Multiplicacion")
    num1=float(input("Ingrese el primer numero:"))
    num2=float(input("Ingrese el segundo numero:"))
    resultado=num1*num2
    print(f"El resultado de la multiplicacion es:{resultado}")

def VerParImpar():
    print("Bienvenido al menu de Par o Impar")
    num=int(input("Ingrese el numero para ver si es par o impar:"))
    #la logica es sencilla solo debemos sacar el residuo y si el residuo es 0 es par, si es 1 es impar
    if(num%2==0):
        print(f"El numero {num} es Par")
    else:
        print(f"El numero {num} es Impar")

def VerTabla():
    print("Bievenido al menu Para ver las tablas")
    numero=int(input("Ingrese el numero para ver su tabla:"))
    #Puse un  for con un rango de 11 recordemos que el rango siempre empieza de 0 y asi ocupe desde el 0 al 10 el for es para que la secuencia de repita hasta que se cumpla la condicion
    for i in range(11):
        resultado=numero*i
        print(f"{numero} * {i} = {resultado}")

def verificacion():
    #al final puse la verificacion como una funcion asi el usuario no tenga que repetirlo cada vez que llamemos al menu()
    while True:
        usuario=input("Ingrese su usuario:")
        try:
            contraseña=int(input("Ingrese su contraseña(123):"))
            #Decidi poner una verificacion basica con un simple IF
            if contraseña==123:
                menu(usuario)
                break
            else:
                print("La contraseña es incorrecta")
        except ValueError:
            print("La contraseña es un entero no ingrese datos o cadenas")
        
    


def menu(usuario):
        while True:
            try:
                    #While true servira para que el programa no se detenga en ningun momento hasta que el usuario decida finalizarlo
                    print(f"///Bienvenido {usuario}///")
                    print("1.Sumar")
                    print("2.Restar")
                    print("3.Division")
                    print("4.Multiplicacion")
                    print("5.Ver Par o Impar")
                    print("6.Ver tabla")
                    print("7.Salir ")
                    opcion=(int(input("Ingrese la opcion:")))
                    match opcion:
                        case 1:
                            suma()
                        case 2:
                            resta()
                        case 3:
                            division()
                        case 4:
                            multiplicacion()
                        case 5:
                            VerParImpar()
                        case 6:
                            VerTabla()
                        case 7:
                            break
                        
            except ValueError:
                print("Error Ingrese un numero ")
                #poner el tryExcept para evitar que el programa se cierre en caso el usuario introduzca un string o dato en vez de un entero


if __name__=="__main__":
    #Hago que el programa empieze y se ejecute con la funcion del verificacion()
    verificacion()