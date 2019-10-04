from tkinter import ttk
from tkinter import *

class Product:

    def __init__(self, windows):
      self.wind = windows
      self.wind.title('Aplicacion de Productos')

      #Creando Un Frame Contenedor
      frame = LabelFrame(self.wind, text = 'Reguistra Un nuevo Producto')
      frame.grid(row = 1, column = 0 , columnspan = 3, pady = 20)

      #Entrada Para Nombre
      Label(frame, text = 'Nombre: ').grid(row = 1, column = 0)
      self.name = Entry(frame)
      self.name.focus()
      self.name.grid(row = 1, column = 1)
      
      #Entrada Precio
      Label(frame, text = 'Precio: ').grid(row = 2, column = 0)
      self.producto = Entry(frame)
      self.producto.grid(row = 2, column = 1)

      #Boton Añadir Producto
      ttk.Button(frame, text = 'Guardar Producto').grid(row = 3, columnspan = 2, sticky = W + E)

      #Tabla
      self.tree = ttk.Treeview(height = 10, columns = 2)
      self.tree.grid(row = 4, column = 0, columnspan = 2)
      self.tree.heading('#0',text = 'Nombre', anchor = CENTER)
      self.tree.heading('#1',text = 'Precio', anchor = CENTER)

if __name__=='__main__':
    windows = Tk()
    application = Product(windows)
    windows.mainloop()
