class Nodo:
    def __init__(self, nombre, tipo="carpeta"):
        self.nombre = nombre        # Nombre del archivo o carpeta
        self.tipo = tipo            # Puede ser "carpeta" o "archivo"
        self.hijos = []             # Lista de hijos (otros nodos)

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)     # Agrega un hijo a la lista (si es carpeta)

    def mostrar_estructura(self, nivel=0):
        sangria = "  " * nivel
        print(sangria + (self.nombre + "/" if self.tipo == "carpeta" else self.nombre))
        
        # Si es carpeta, imprime sus hijos de forma recursiva
        if self.tipo == "carpeta":
            for hijo in self.hijos:
                hijo.mostrar_estructura(nivel + 1)

# Crear el nodo raíz
root = Nodo("root")

# Carpeta: documentos
documentos = Nodo("documentos")
documentos.agregar_hijo(Nodo("tp_final.pdf", tipo="archivo"))
documentos.agregar_hijo(Nodo("apuntes.txt", tipo="archivo"))

# Carpeta: fotos/vacaciones
fotos = Nodo("fotos")
vacaciones = Nodo("vacaciones")
vacaciones.agregar_hijo(Nodo("playa.jpg", tipo="archivo"))
fotos.agregar_hijo(vacaciones)

# Archivo suelto en raíz
readme = Nodo("readme.txt", tipo="archivo")

# Armamos el árbol
root.agregar_hijo(documentos)
root.agregar_hijo(fotos)
root.agregar_hijo(readme)

# Mostrar el árbol
root.mostrar_estructura()
