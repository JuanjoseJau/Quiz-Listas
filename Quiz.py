class Nodo:
	def __init__(self, Cedula, Nombre, Habitacion):
		self.dataC = Cedula
		self.dataN = Nombre
		self.dataH = Habitacion
		self.siguiente = None

class ListaSE:
	def __init__(self):
		self.cabeza = None
	def Vacio(self):
		if self.cabeza == None:
			print("Está vacia")
		else:
			print("Lista no vacia")

	def AgregarInicio(self, Cedula, Nombre, Habitacion):
		nuevo_nodo = Nodo(Cedula, Nombre, Habitacion)
		if self.cabeza is None:
			self.cabeza = nuevo_nodo
			return
		else:
			nuevo_nodo.siguiente = self.cabeza
			self.cabeza = nuevo_nodo

	def AgregarFinal(self, Cedula, Nombre, Habitacion):
		nuevo_nodo = Nodo(Cedula, Nombre, Habitacion)
		if self.cabeza is None:
			self.cabeza = nuevo_nodo
			return
		else:
			actual = self.cabeza
			while actual.siguiente is not None:
				actual = actual.siguiente
			actual.siguiente = nuevo_nodo

	def AgregarAntes(self, ValorX, Cedula, Nombre, Habitacion):
		nuevo_nodo = Nodo(Cedula, Nombre, Habitacion)
		if self.cabeza is None:
			print("Lista Vacia")
			return
		if self.cabeza.data == ValorX:
			nuevo_nodo.siguiente = self.cabeza
			self.cabeza = nuevo_nodo
			return
		prev = self.cabeza
		actual = self.cabeza.siguiente
		while actual is not None and actual.data != ValorX:
			prev = actual
			actual = actual.siguiente
		if actual is None:
			print(f"El valor {ValorX} no se encuentra en la lista")
			return
		else:
			nuevo_nodo.siguiente = actual
			prev.siguiente = nuevo_nodo

	def AgregarDespues(self, ValorX, Cedula, Nombre, Habitacion):
		nuevo_nodo = Nodo(Cedula, Nombre, Habitacion)
		if self.cabeza is None:
			print("Lista Vacia")
			return
		actual = self.cabeza
		while actual is not None and actual.data != ValorX:
			actual = actual.siguiente
		if actual is None:
			print("El valor no se encuentra en la lista")
			return
		else:
			nuevo_nodo.siguiente = actual.siguiente
			actual.siguiente = nuevo_nodo

	def EliminarInicio(self):
		if self.cabeza is None:
			print("Lista Vacia")
			return
		else:
			self.cabeza = self.cabeza.siguiente

	def EliminarFinal(self):
		if self.cabeza is None:
			print("Lista Vacia")
			return
		else:
			prev = self.cabeza
			actual = self.cabeza.siguiente
			while actual.siguiente is not None:
				prev = actual
				actual = actual.siguiente
			prev.siguiente = None

	def BuscarCedula(self, Cedula):
		ValorEsta = False
		actual = self.cabeza
		while actual is not None:
			if	actual.dataC == Cedula:
				ValorEsta = True
				break
			actual = actual.siguiente
		return ValorEsta

	def BuscarNombre(self, Nombre):
		ValorEsta = False
		actual = self.cabeza
		while actual is not None:
			if	actual.dataN == Nombre:
				ValorEsta = True
				break
			actual = actual.siguiente
		return ValorEsta

	def BuscarHabitacion(self, Habitacion):
		ValorEsta = False
		actual = self.cabeza
		while actual is not None:
			if	actual.dataH == Habitacion:
				ValorEsta = True
				break
			actual = actual.siguiente
		return ValorEsta
		
	def ContarElementos(self):
		contador = 0
		actual = self.cabeza
		while actual is not None:
			contador += 1
			actual = actual.siguiente
		return contador

	def Escribir_Lista(self):
		actual = self.cabeza
		while actual is not None:
			print(f"Cedula: {actual.dataC}/Nombre: {actual.dataN}/Habitacion: {actual.dataH}")
			actual = actual.siguiente

	def Añadir_Reserva(self):
		C=int(input("Ingrese el numero de cedula: "))
		N=input("Ingrese el nombre: ")
		while True:
			H=int(input("Ingrese el numero de la habitacion: "))
			if R.BuscarHabitacion(H)==False:
				break
			else:
				print("La habitacion ya esta ocupada.")
		self.AgregarFinal(C,N,H)
		E.AgregarFinal(C,N,H)

R=ListaSE()
E=ListaSE()
S=ListaSE()

while True:
	print("---MENU---")
	print("1. Agregar Reserva.")
	print("2. Eliminar Reserva.")
	print("3. Mostrar Reservas.")
	print("4. Mostrar todas las reservas respecto a una cedula.")
	print("5. Mostrar todas las reservas en orden de llegada.")
	print("6. Mostrar todas las habitaciones disponibles")
	print("7. Mostrar todas las habitaciones ocupadas")
	print("8. Salir")
	print(" ")
	O=int(input("Ingrese una opcion: "))
	match O:
		case 1:
			print(" ")
			R.Añadir_Reserva()
			print(" ")
		case 3:
			print(" ")
			R.Escribir_Lista()
			print(" ")
		case 8:
			print(" ")
			print("Saliendo.")
			break
		case _:
			print(" ")
			print("ERROR---Opcion no Valida")
			print(" ")
