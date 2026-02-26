from datetime import datetime

#Nodo Reserva:
class RNodo:
	def __init__(self, Cedula, Nombre, Habitacion):
		self.dataC = Cedula
		self.dataN = Nombre
		self.dataH = Habitacion
		self.siguiente = None

#Nodo Entrada-Salida:
class LSNodo:
	def __init__(self, Cedula, Nombre, Habitacion, Tiempo):
		self.dataC = Cedula
		self.dataN = Nombre
		self.dataH = Habitacion
		self.dataT = Tiempo
		self.siguiente = None

#Lista:
class ListaSE:
	def __init__(self):
		self.cabeza = None

	#Vacio:
	def Vacio(self):
		if self.cabeza == None:
			print("Está vacia")
		else:
			print("Lista no vacia")

	#Agregar al Inicio (Reserva):
	def AgregarInicioR(self, Cedula, Nombre, Habitacion):
		nuevo_nodo = RNodo(Cedula, Nombre, Habitacion)
		if self.cabeza is None:
			self.cabeza = nuevo_nodo
			return
		else:
			nuevo_nodo.siguiente = self.cabeza
			self.cabeza = nuevo_nodo

	#Agregar al Inicio (Llegada-Salida):
	def AgregarInicioLS(self, Cedula, Nombre, Habitacion, Tiempo):
		nuevo_nodo = LSNodo(Cedula, Nombre, Habitacion, Tiempo)
		if self.cabeza is None:
			self.cabeza = nuevo_nodo
			return
		else:
			nuevo_nodo.siguiente = self.cabeza
			self.cabeza = nuevo_nodo

	#Agregar al Final (Reserva):
	def AgregarFinalR(self, Cedula, Nombre, Habitacion):
		nuevo_nodo = RNodo(Cedula, Nombre, Habitacion)
		if self.cabeza is None:
			self.cabeza = nuevo_nodo
			return
		else:
			actual = self.cabeza
			while actual.siguiente is not None:
				actual = actual.siguiente
			actual.siguiente = nuevo_nodo

	#Agregar al Final (Llegada-Salida):
	def AgregarFinalLS(self, Cedula, Nombre, Habitacion, Tiempo):
		nuevo_nodo = LSNodo(Cedula, Nombre, Habitacion, Tiempo)
		if self.cabeza is None:
			self.cabeza = nuevo_nodo
			return
		else:
			actual = self.cabeza
			while actual.siguiente is not None:
				actual = actual.siguiente
			actual.siguiente = nuevo_nodo

	#Agregar antes de un Valor (Reserva):
	def AgregarAntesR(self, CX, NX, HX, Cedula, Nombre, Habitacion):
		nuevo_nodo = RNodo(Cedula, Nombre, Habitacion)
		if self.cabeza is None:
			print("Lista Vacia")
			return
		if self.cabeza.dataC==CX and self.cabeza.dataN==NX and  self.cabeza.dataH==HX:
			nuevo_nodo.siguiente = self.cabeza
			self.cabeza = nuevo_nodo
			return
		prev = self.cabeza
		actual = self.cabeza.siguiente
		while actual is not None and actual.dataC!=CX and actual.dataN!=NX and actual.dataH!=HX:
			prev = actual
			actual = actual.siguiente
		if actual is None:
			print(f"El valor {CX}/{NX}/{HX} no se encuentra en la lista")
			return
		else:
			nuevo_nodo.siguiente = actual
			prev.siguiente = nuevo_nodo

	#Agregar antes de un Valor (Llegada-Salida):
	def AgregarAntesLS(self, CX, NX, HX, Cedula, Nombre, Habitacion, Tiempo):
		nuevo_nodo = LSNodo(Cedula, Nombre, Habitacion, Tiempo)
		if self.cabeza is None:
			print("Lista Vacia")
			return
		if self.cabeza.dataC==CX and self.cabeza.dataN==NX and  self.cabeza.dataH==HX:
			nuevo_nodo.siguiente = self.cabeza
			self.cabeza = nuevo_nodo
			return
		prev = self.cabeza
		actual = self.cabeza.siguiente
		while actual is not None and actual.dataC!=CX and actual.dataN!=NX and actual.dataH!=HX:
			prev = actual
			actual = actual.siguiente
		if actual is None:
			print(f"El valor {CX}/{NX}/{HX} no se encuentra en la lista")
			return
		else:
			nuevo_nodo.siguiente = actual
			prev.siguiente = nuevo_nodo

	#Agregar despues de un Valor (Reserva):
	def AgregarDespuesR(self, CX, NX, HX, Cedula, Nombre, Habitacion):
		nuevo_nodo = RNodo(Cedula, Nombre, Habitacion)
		if self.cabeza is None:
			print("Lista Vacia")
			return
		actual = self.cabeza
		while actual is not None and actual.dataC!=CX and actual.dataN!=NX and actual.dataH!=HX:
			actual = actual.siguiente
		if actual is None:
			print(f"El valor {CX}/{NX}/{HX} no se encuentra en la lista")
			return
		else:
			nuevo_nodo.siguiente = actual.siguiente
			actual.siguiente = nuevo_nodo

	#Agregar despues de un Valor (Llegada-Salida):
	def AgregarDespuesLS(self, CX, NX, HX, Cedula, Nombre, Habitacion, Tiempo):
		nuevo_nodo = LSNodo(Cedula, Nombre, Habitacion, Tiempo)
		if self.cabeza is None:
			print("Lista Vacia")
			return
		actual = self.cabeza
		while actual is not None and actual.dataC!=CX and actual.dataN!=NX and actual.dataH!=HX:
			actual = actual.siguiente
		if actual is None:
			print(f"El valor {CX}/{NX}/{HX} no se encuentra en la lista")
			return
		else:
			nuevo_nodo.siguiente = actual.siguiente
			actual.siguiente = nuevo_nodo

	#Eliminar Valor Inicio:
	def EliminarInicio(self):
		if self.cabeza is None:
			print("Lista Vacia")
			return
		else:
			self.cabeza = self.cabeza.siguiente

	#Eliminar Valor Final:
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

	#Eliminar Valor Especifico (Reserva):
	def EliminarEspecificoR(self, Cedula, Nombre, Habitacion):
		if self.cabeza is None:
			print("Lista Vacia")
			return
		else:
			prev = None
			actual = self.cabeza
			while actual.siguiente is not None and (actual.dataC!=Cedula or actual.dataN!=Nombre or actual.dataH!=Habitacion):
				prev = actual
				actual = actual.siguiente
			if actual.siguiente is None:
				if actual.dataC==Cedula and actual.dataN==Nombre and actual.dataH==Habitacion:
					self.EliminarFinal()
					return
				else:
					print(f"El valor {Cedula}/{Nombre}/{Habitacion} no se encuentra en la lista")
					return
			else:
				if prev is None:
					self.EliminarInicio()
					return
				else:
					prev.siguiente = actual.siguiente

	#Eliminar Valor Especifico (Llegada-Salida):
	def EliminarEspecificoLS(self, Cedula, Nombre, Habitacion, Tiempo):
		if self.cabeza is None:
			print("Lista Vacia")
			return
		else:
			prev = None
			actual = self.cabeza
			while actual.siguiente is not None and (actual.dataC!=Cedula or actual.dataN!=Nombre or actual.dataH!=Habitacion or actual.dataT!=Tiempo):
				prev = actual
				actual = actual.siguiente
			if actual.siguiente is None:
				if actual.dataC==Cedula and actual.dataN==Nombre and actual.dataH==Habitacion and actual.dataT==Tiempo:
					self.EliminarFinal()
					return
				else:
					print(f"El valor {Cedula}/{Nombre}/{Habitacion}/{Tiempo} no se encuentra en la lista")
					return
			else:

				if prev is None:
					self.EliminarInicio()
					return
				else:
					prev.siguiente = actual.siguiente

	#Busca Nodo a partir de Cedula:
	def BuscarCedula(self, Cedula):
		ValorEsta = False
		actual = self.cabeza
		while actual is not None:
			if	actual.dataC == Cedula:
				ValorEsta = True
				break
			actual = actual.siguiente
		return ValorEsta

	#Busca Nodo a partir de Nombre:
	def BuscarNombre(self, Nombre):
		ValorEsta = False
		actual = self.cabeza
		while actual is not None:
			if	actual.dataN == Nombre:
				ValorEsta = True
				break
			actual = actual.siguiente
		return ValorEsta

	#Busca Nodo a partir de Habitacion:
	def BuscarHabitacion(self, Habitacion):
		ValorEsta = False
		actual = self.cabeza
		while actual is not None:
			if	actual.dataH == Habitacion:
				ValorEsta = True
				break
			actual = actual.siguiente
		return ValorEsta

	#Busca Nodo a partir de Tiempo:
	def BuscarTiempo(self, Tiempo):
		ValorEsta = False
		actual = self.cabeza
		while actual is not None:
			if	actual.dataT == Tiempo:
				ValorEsta = True
				break
			actual = actual.siguiente
		return ValorEsta

	#Busca Nodo a partir de Todos los Valores (Reserva):
	def BuscarTodoR(self, Cedula, Nombre, Habitacion):
		ValorEsta = False
		actual = self.cabeza
		while actual is not None:
			if	actual.dataC == Cedula and actual.dataN == Nombre and actual.dataH == Habitacion:
				ValorEsta = True
				break
			actual = actual.siguiente
		return ValorEsta

	#Busca Nodo a partir de Todos los Valores (Llegada-Salida):
	def BuscarTodoLS(self, Cedula, Nombre, Habitacion, Tiempo):
		ValorEsta = False
		actual = self.cabeza
		while actual is not None:
			if	actual.dataC == Cedula and actual.dataN == Nombre and actual.dataH == Habitacion and actual.dataT == Tiempo:
				ValorEsta = True
				break
			actual = actual.siguiente
		return ValorEsta

	#Contar Nodos:
	def ContarElementos(self):
		contador = 0
		actual = self.cabeza
		while actual is not None:
			contador += 1
			actual = actual.siguiente
		return contador

	#Escribir Lista (Reserva):
	def Escribir_ListaR(self):
		if self.cabeza is None:
			print("Lista Vacia")
		else:
			actual = self.cabeza
			while actual is not None:
				print(f"Cedula: {actual.dataC}/Nombre: {actual.dataN}/Habitacion: {actual.dataH}")
				actual = actual.siguiente

	#Escribir Lista (Llegada-Salida):
	def Escribir_ListaLS(self):
		if self.cabeza is None:
			print("Lista Vacia")
		else:
			actual = self.cabeza
			while actual is not None:
				print(f"Cedula: {actual.dataC}/Nombre: {actual.dataN}/Habitacion: {actual.dataH}/Tiempo: {actual.dataT}")
				actual = actual.siguiente

	#Añadir Reserva:
	def Añadir_Reserva(self):
		C=int(input("Ingrese el numero de cedula: "))
		N=input("Ingrese el nombre: ")
		while True:
			H=int(input("Ingrese el numero de la habitacion: "))
			if R.BuscarHabitacion(H)==False:
				if 0<H<=MH:
					T=datetime.now()
					break
				else:
					print("La habitacion no existe.")
			else:
				print("La habitacion ya esta ocupada.")
		self.AgregarFinalR(C,N,H)
		L.AgregarFinalLS(C,N,H,T)

	#Eliminar Reserva:
	def Eliminar_Reserva(self):
		C=int(input("Ingrese el numero de cedula: "))
		N=input("Ingrese el nombre del cliente: ")
		H=int(input("Ingrese el numero de habitacion: "))
		if R.BuscarTodoR(C,N,H) == True:
			R.EliminarEspecificoR(C,N,H)
			T=datetime.now()
			S.AgregarFinalLS(C,N,H,T)
		else:
			print("No se encontro ninguna reserva con los datos ingresados.")

	#Reservas repecto a una Cedula:
	def Lista_Cedula(self):
		RC=ListaSE()
		C=int(input("Ingrese el numero de cedula: "))
		actual=self.cabeza
		while actual is not None:
			if actual.dataC==C:
				print(" ")
				print(f"Cedula: {actual.dataC}/Nombre: {actual.dataN}/Habitacion: {actual.dataH}")
			actual=actual.siguiente

	#Buscar Habitaciones Disponibles:
	def Habitaciones_Disponibles(self):
		for i in LH:
			if self.BuscarHabitacion(i) is False:
				HD.append(i)
		if HD==[]:
			print("No hay habitaciones disponibles.")¨
		else:
			print("Las habitaciones disponibles son: ")
			print(" ")
			for i in HD:
				print(i)

	#Buscar Habitaciones Ocupadas:
	def Habitaciones_Ocupadas(self):
		for i in LH:
			if self.BuscarHabitacion(i) is True:
				HO.append(i)
		if HO==[]:
			print("No hay habitaciones ocupadas.")
		else:
			print("Las habitaciones ocupadas son: ")
			print(" ")
			for i in HO:
				print(i)

#Iniciacion:
R=ListaSE()
L=ListaSE()
S=ListaSE()
MH=int(input("Ingrese el numero total de habitaciones del hotel: "))
LH=[]
HD=[]
HO=[]
for i in range(1,MH+1):
	LH.append(i)
print(" ")

#Menu:
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
		case 2:
			print(" ")
			R.Eliminar_Reserva()
			print(" ")
		case 3:
			print(" ")
			R.Escribir_ListaR()
			print(" ")
		case 4:
			print(" ")
			R.Lista_Cedula()
			print(" ")
		case 5:
			print(" ")
			print("Reservas en orden de llegada: ")
			print(" ")
			L.Escribir_ListaLS()
			print(" ")
			print("Reservas en orden de salida: ")
			print(" ")
			S.Escribir_ListaLS()
			print(" ")
		case 6:
			print(" ")
			R.Habitaciones_Disponibles()
			print(" ")
		case 7:
			print(" ")
			R.Habitaciones_Ocupadas()
			print(" ")
		case 8:
			print(" ")
			print("Saliendo.")
			break
		case _:
			print(" ")
			print("ERROR---Opcion no Valida")
			print(" ")
