import os
import funciones ("agregarCategoria", "editarcategoria", "eliminarCategoria")

print("Mundo libro")
print("Porfavor elija alguna de las opciones: \n 1.Mantenedor de categorias \n 2.Reportes \n 3.Salir")
opcion=input("porfavor seleccione un numero: ")
if opcion =="1":
    print("1.Agregar Categoria \n 2.Editar \n 3.Eliminar categoria \n 4.Buscar categoria \n 5.Salir")
while True:
    opcion_mantenedores=("Porfavor seleccione un numero: ")
    if opcion_mantenedores=="1":
        print("Accediendo a añadir categoria...")


    elif opcion_mantenedores=="2":
        print("Accediendo a editar categoria...")

    elif opcion_mantenedores=="3":
        print("Accediendo a eliminar categoria...")
    else:
        print("Accediendo a buscar categoria...")
        


