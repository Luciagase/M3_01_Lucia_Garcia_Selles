from ast import main

#Ejercicio1

# Utilizar el método class para crear una clase. Dentro de ella se crea el constructor. 
class Producto:
    def _init_(self, nombre, codigo, precio, tipo):
        self.nombre = nombre
        self.codigo = codigo
        self.precio = precio
        self.tipo = tipo
    print('El producto se ha creado con éxito')

def _str_(self):#Para mostrar la información
    return 'El producto {} tiene el código {}, precio en euros de {} y su categoria es {}'.format(self.nombre, self.codigo, self.precio, self.tipo)

producto1=Producto('Secador', 3467764, 30, 'Electrodomésticos')
producto2=Producto('Gorro', 3467765, 12, 'Accesorios')
producto3=Producto('Silla', 4467764, 50, 'Muebles')


if _name_=='_main_':
    main()

