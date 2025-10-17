cursos = [{"curso": "matematicas", "nota": 90}, 
    {"curso": "historia", "nota": 75}, {"curso": "calculo1", "nota": 100}]
historial = []
def registrar_curso_nota():#ciclo while para que el usuario elija cuando salir 
    while True:
        curso = input("Ingresel nombre del curso a registrar: ")
        nota = float(input("Ingrese la nota del curso (0-100): "))
        if  0 <= nota <= 100: 
            cursos.append({"curso": curso, "nota": nota})
            historial.append(f"Registrado: {curso} - nota {nota}")
            #las llaves es lo que el programa va a cambiar
            print("Cursos registrado con exito.")
            break
        else:   
            print("Error")   

def mostrar_curso_nota():
    if cursos:
        print("Notas registradas: ")
        #Nnumerate recorre toda la litas y start hace que en vez de empezar en 0 empieze en 1
        #i es el contador que enumera los cursos y C es lo que contiene los datos del los cursos por cada iteracion
        for i, c in enumerate(cursos, start=1): 
            print(f"{i}. {c['curso']} - {c['nota']}: ")
        historial.append("Mostrado cursos y notas")
    else: 
        print("No hay cursos registrados")

def calcular_promedio():
    if cursos: #verifica que la lista no este vacia 
        #sum para sumar todas las notas
        #len es para saber cuantos elemntos hay en la lista y las dividimos entre ella
        #for c recore la listra y toma los calores de notas en cada curso
        promedio = sum(c["nota"] for c in cursos) / len(cursos)
        print("El promedio general es:", promedio)
        historial.append(f"Promedio calculado, {promedio}")
    else:
        print("No hay notas para calcular promedio")

def cursos_aprovados_reprovados():
    if cursos:
        # 1 para que sume 1 por cada curso mayores o iguales a 60 al recorrerla con c  
        #luego len toma el total de elementos que hay que cursos y le restra lo valores que son mayores o iguales a 60
        aprovados = sum(1 for c in cursos if c["nota"]>= 60)
        reprovados = len(cursos)- aprovados
        print("cursos aprovados es de: ", aprovados)
        print("cursos reprovados es de: ", reprovados)
        historial.append("Conteo de cursos aprovados y reprovados")
    else:
        print("Sin cursos reprovados")

def buscar_curso_nombre(nombre):
    for c in cursos: 
        #c recorre la lista y verifica si es igual a al nombre ingresado por el usuario
        #.lower es para que pase cualquier letra ingresada por el usuario a minuscula
        if c["curso"].lower() == nombre.lower():
            print(f"Curso encontrado: {c['curso']} - nota {c['nota']}")
            return
    historial.append(f"Buscado: {c['curso']}")  
    print("Curso no encontrado")

def actualizar_nota_curso(nombre):
    for c in cursos: 
        #c recorre la lista y verifica si el nombre ingresado por el usuario exista
        #.lower es para que pase cualquier letra ingresada por el usuario a minuscula
        if c["curso"].lower() == nombre.lower():
            #al verificar que exista el curso pide una nueva nota al usuario
            nuevaNota = float(input("Ingrese la nueva nota: "))
            #C recorre la lista y remplaza la nota por la que ha sido ingresada por el usuario
            historial.append(f"Actualizada nota de {c['curso']} de {c['nota']} a {nuevaNota}")
            c["nota"] = nuevaNota
            print("nota actualizada con correctamente")
            return
    print("Curso no encotrado")

def eliminar_curso():
    if len(cursos)>0:
        nombre=input("Ingrese el nombre del curso a eliminar: ")
        confirmar = input(f"Esta sefuro de que desea elimarlo (si/no): ")
        if confirmar.lower() == "si":
            for c in cursos: 
                #c recorre la lista y verifica si el curso ingresado exista
                if c["curso"].lower() == nombre.lower():
                    #recorre la lista y compara si el curso ingresado es igual a alguno en existencia
                    cursos.remove(c)
                    print("Eliminado correctamente")
                historial.append(f"Curso eliminado: {c['curso']}")
                    #return para que el programa no siga buscando
                return
            print("Curso no encontrado....")
    else: 
        print("No hay cursos en existensia....")

def ordenamiento_burbuja(lista):
    n = len(lista)
    for i in range(n):
        #j recorre la lista desde el inicio hasta n-i-1
        for j in range(0, n - i - 1):
            if lista[j]["nota"] > lista[j + 1]["nota"]:
                #intercambia valores si el valor encontrado es mayor al siguiente
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
        historial.append("Cursos ordenados por nota (burbuja)")
    return lista
def ordenamiento_insercion(lista):
    #recorre desde el segundo valor de la lista hasta el ultimo
    for i in range(1, len(lista)):
        #clave es el valor a comparar
        clave = lista[i]
        #j es el indice del elemento anterior
        j = i - 1
        while j >= 0 and clave["curso"].lower() < lista[j]["curso"].lower():
            #mueve los valores mayores a la derecha
            lista[j + 1] = lista[j]
            #lista [j+1] es el valor que se mueve a la derecha
            j -= 1
            #j-=1 es para que pueda seguir comparando con los valores anteriores
        lista[j + 1] = clave
        #inserta la clave en su posicion correcta
    historial.append("Cursos ordenados por nombre (insercion)")
    return lista

def busqueda_curso(lista):
    nombre = input("Ingrese el nombre del curso a buscar: ").lower()
    #pide el nombre del curso a buscar
    for curso in lista:
        #for curso in lista recorre la lista
        if curso["curso"].lower() == nombre:
            #si el nombre ingresado es igual al alguno en la lista imprime
            print(f"Curso '{nombre}' encontrado con nota {curso['nota']} pts.")
            #f para que imprima solo los valores y no los corchetes
            return
    historial.append("Buscado (binaria)")
    print("Curso no encontrado.")

def simular_cola_revision():
    cola = []
    print("Ingrese los cursos a enviar a revisión (escriba 'fin' para salir):")
    while True:
        curso = input("Curso: ")
        if curso.lower() == "fin":
            break
        cola.append(curso)
    print("Procesando solicitudes de revisión:")
    for curso in cola:
        print(f"Revisando solicitud del curso: {curso}")
    historial.append(f"Solicitud de revisión procesada para: {curso}")

def mostrar_historial_cambios():
    if historial:
        print("Historial de cambios:")
        for cambio in historial:
            print(cambio)
        historial.append("Historial consultado")
    else:
        print("No hay cambios")


#ciclo while para que al realizar algun cambio o accion el programa no termine
#hasta que el usuario elija salir del programa

while True:
    print("")
    print("======================================")
    print("===== Gestor de notas academicas =====")
    print("1. Registrar nuevo curso")
    print("2. Mostrar todos los cursos y notas")
    print("3. calcular promedio general")
    print("4. Contar cursos aprobados y reprobados")
    print("5. Buscar curso por nombre (búsqueda lieal)")
    print("6. Actualizar nota de un curso")
    print("7. Eliminar un curso")
    print("8. Ordenar cursos por nota (ordenamiento burbuja)")
    print("9. Ordenar cursos por nombre (ordenamiento inserción)")
    print("10. Buscar curso por nombre (búsque binaria)")
    print("11. Simular cola de solicitudes de revisión")
    print("12. Mostrar historial de cambios (pila)")
    print("13. salir")
    opcion = int(input("Selecione una opcion: "))
    if opcion == 1: 
        print("== Registrar nuevo curso ==")
        registrar_curso_nota()    
    elif opcion == 2: 
        print("== Mostrar cursos ==")
        mostrar_curso_nota()
    elif opcion == 3: 
        print("== Calcular promedio ==")
        calcular_promedio()
    elif opcion == 4: 
        print("== Contar cursos ==")
        cursos_aprovados_reprovados()
    elif opcion == 5: 
        print("== Buscar curso ==")
        nombre = input("Ingrese el nombre del curso a buscar: ")
        buscar_curso_nombre(nombre)
    elif opcion == 6: 
        print("== Actualizar nota ==")
        nombre = input("Ingrese el nombre de curso a cambiar la nota: ")
        actualizar_nota_curso(nombre)
    elif opcion == 7: 
        print("== Eliminar curso ==")
        eliminar_curso()
    elif opcion == 8: 
        print("== Ordenar curso por nota ==")
        ordenado = ordenamiento_burbuja(cursos)
        print("Ordenada: ", ordenado)
    elif opcion == 9: 
        print("== Ordenar curso por nobre ==")
        print("Lista original: ", cursos)
        ordenado2 = ordenamiento_insercion(cursos)
        print("Lista ordenadas: ", ordenado2)
    elif opcion == 10: 
        print("== Buscar curso ==")
        cursos = ordenamiento_insercion(cursos.copy())
        busqueda_curso(cursos)
    elif opcion == 11: 
        print("== Simular cola de solicitudes  ==")
        simular_cola_revision()
    elif opcion == 12: 
        print("== Hitorial ==")
        mostrar_historial_cambios()
    elif opcion == 13: 
        print("Gracias por usar el Gestor de Notas Académicas. ¡Hasta pronto!")
        break
    else:
        print("Opción invalida....")
        break