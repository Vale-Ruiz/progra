import json
def agregarCategoria (titulo:str):
    with open ('biblioteca.json', mode='r') as archivoJson:
        leerJson=json.load(archivoJson)
        tituloCategoria= {
            "id":len(leerJson["Categoria"])+1,
            "titulo":titulo

        }
        leerJson["Categoria"].append(tituloCategoria)
    with open('biblioteca.json',mode='w') as archJson:
        json.dump(leerJson,archJson,indent=4)

tituloCategoria=input("Escriba nombre de la nueva categoria")
agregarCategoria(tituloCategoria)

def editarCategoria (id:int):
    with open ("biblioteca.json", mode="r") as archivoJson:
        leerJson= json.load(archivoJson)
        contador=0
        for i in leerJson["Categoria"]:
            if i ["CategoriaID"]==id:
                print("encontre la categoria", contador)
                break
            contador+=1
        #print(leerJson["Categoria"]["contador"])
        leerJson["Categoria"][contador]["CategoriaID"]=input("ingrese el nombre de la nueva categoria:")

    with open("biblioteca.json", mode="w") as archivoJson:
        json.dump(leerJson, archivoJson, indent=4)

#nuevoTitulo=input("Escriba el nombre de la nueva categoria")
editarCategoria()

def eliminarCategoria(id:int):

    with open ('biblioteca.json', mode='r') as archivoJson:
        leerJson=json.load(archivoJson)
        contador=0
        for i in leerJson["Categoria"]:
            if i ["CategoriaID"]==id:
                print("Encontre la categoria, eliminando...")
                break
            contador+=1
            leerJson["Categoria"].remove(i)
            print ("Eliminada la categoria")

    with open("biblioteca.json", mode="w") as archivoJson:
        json.dump(leerJson, archivoJson, indent=4)

eliminarCategoria()