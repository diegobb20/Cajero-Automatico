# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 17:30:00 2024

"""

import random
from datetime import datetime

class Cliente:
	def __init__(self, numero_cuenta, nombre, contraseña):
		self.numero_cuenta = numero_cuenta
		self.nombre = nombre
		self.contraseña = contraseña
		self.cuenta = Cuenta()

class Cuenta:
	def __init__(self):
		self.saldo = 0
		self.movimientos = []

class Cajero:
	def __init__(self, ubicacion, codigo):
		self.ubicacion = ubicacion
		self.codigo = codigo
		self.dispensador = {
			200: 0,
			100: 0,
			50: 0,
			20: 0
		}

class Administrador:
	def __init__(self, credencial, contraseña):
		self.credencial = credencial
		self.contraseña = contraseña

class SistemaCajeroAutomatico:
	def __init__(self):
		self.clientes = {}
		self.administradores = []
		self.cajeros = []
		self.administrador_principal = Administrador("admin", "admin123")
		self.en_ejecucion = True  

	def generar_numero_cuenta(self):
		while True:
			numero_cuenta = ''.join(random.choices('0123456789', k=14))
			if numero_cuenta not in self.clientes:
				return numero_cuenta

	def adicionar_cliente(self, nombre, contraseña):
		numero_cuenta = self.generar_numero_cuenta()
		nuevo_cliente = Cliente(numero_cuenta, nombre, contraseña)
		self.clientes[numero_cuenta] = nuevo_cliente
		print (chr(27)+"[1;32m")
		print(f"Cliente añadido con éxito. Número de cuenta: {numero_cuenta}")
		print (chr(27)+"[1;37m")

	def adicionar_cajero(self, ubicacion, codigo):
		nuevo_cajero = Cajero(ubicacion,codigo)
		self.cajeros.append(nuevo_cajero)
		print (chr(27)+"[1;32m")
		print(f"Cajero añadido con éxito.")
		print (chr(27)+"[1;37m")

	def adicionar_administrador(self, credencial, contraseña):
		nuevo_administrador = Administrador(credencial, contraseña)
		self.administradores.append(nuevo_administrador)
		print (chr(27)+"[1;32m")
		print(f"Administrador añadido con éxito.")
		print (chr(27)+"[1;37m")

	def actualizar_dispensador(self, cajero, billetes):
		for denominacion, cantidad in billetes.items():
			if denominacion in cajero.dispensador:
				cajero.dispensador[denominacion] += cantidad
		print("Dispensador actualizado con éxito.")

	def iniciar_sesion(self):
		while True:
			print(chr(27) + "[1;34m")
			print("\n------INICIO------")
			print(chr(27) + "[1;37m")
			print("1. Iniciar Sesión como Administrador")
			print("2. Iniciar Sesión como Cliente")
			print("3. Salir")
			print(chr(27) + "[1;35m")
			opcion = int(input("Seleccione una opción: "))
			print(chr(27) + "[1;37m")
	
			if opcion == 1:
				credencial = input("Ingrese la credencial del administrador: ")
				contraseña = input("Ingrese la contraseña del administrador: ")
				if credencial == self.administrador_principal.credencial and contraseña == self.administrador_principal.contraseña:
					self.menu_administrador()
				else:
					print(chr(27) + "[1;31m")
					print("Credenciales de administrador incorrectas.")
					print(chr(27) + "[1;37m")
			elif opcion == 2:
				cliente, tipo_usuario = self.iniciar_sesion_cliente()
				if cliente:
					self.menu_cliente(cliente)
			elif opcion == 3:
				print (chr(27)+"[1;36m")
				print("Gracias por usar el sistema de cajero automático.")
				print (chr(27)+"[1;37m")
				self.en_ejecucion = False
				break
			else:
				print(chr(27) + "[1;31m")
				print("Opción no válida.")
				print(chr(27) + "[1;37m")


	def iniciar_sesion_cliente(self):
		while True:
			print (chr(27)+"[1;34m")
			print("\n------MENU CLIENTE------")
			print (chr(27)+"[1;37m")
			print("1. Iniciar Sesión")
			print("2. Registrarse")
			print("3. Volver")
			print (chr(27)+"[1;35m")
			opcion = int(input("Seleccione una opción: "))
			print (chr(27)+"[1;37m")

			if opcion == 1:
				numero_cuenta = input("Ingrese su número de cuenta (14 dígitos): ")
				contraseña = input("Ingrese su contraseña: ")
				cliente = self.clientes.get(numero_cuenta)
				if cliente and cliente.contraseña == contraseña:
					print(f"Bienvenido, {cliente.nombre}")
					return cliente, "cliente"
				else:
					print (chr(27)+"[1;31m")
					print("Credenciales incorrectas.")
					print (chr(27)+"[1;37m")
			elif opcion == 2:
				nombre = input("Ingrese su nombre: ")
				contraseña = input("Ingrese su contraseña: ")
				self.adicionar_cliente(nombre, contraseña)
			elif opcion == 3:
				print (chr(27)+"[1;31m")
				print("Sesión del cliente finalizada.")
				print (chr(27)+"[1;37m")
				return None, None
			else:
				print (chr(27)+"[1;31m")
				print("Opción no válida.")
				print (chr(27)+"[1;37m")

	def menu_administrador(self):
		while True:
			print (chr(27)+"[1;34m")
			print("\n------BIENVENIDO ADMINISTRADOR------")
			print (chr(27)+"[1;37m")
			print("1. Agregar Cajero")
			print("2. Actualizar Dispensador de Billetes")
			print("3. Adicionar Administrador")
			print("4. Ver Cajeros Registrados")
			print("5. Ver Administradores Registrados")
			print("6. Ver Clientes Registrados")
			print("7. Buscar Cajero")
			print("8. Dar de Baja Cajero")
			print("9. Dar de Baja Cliente")
			print("10. Salir")
			print (chr(27)+"[1;35m")
			opcion = int(input("Seleccione una opción: "))
			print (chr(27)+"[1;37m")

			if opcion == 1:
				codigo = input("Registre el código del nuevo cajero: ")
				ubicacion = input("Ingrese la ubicación del nuevo cajero: ")
				self.adicionar_cajero(ubicacion, codigo)
			elif opcion == 2:
				cajero = self.seleccionar_cajero()
				if cajero:
					billetes = {
						200: int(input("Ingrese cantidad de billetes de 200: ")),
						100: int(input("Ingrese cantidad de billetes de 100: ")),
						50: int(input("Ingrese cantidad de billetes de 50: ")),
						20: int(input("Ingrese cantidad de billetes de 20: "))
					}
					self.actualizar_dispensador(cajero, billetes)
			elif opcion == 3:
				credencial = input("Ingrese la nueva credencial del administrador: ")
				contraseña = input("Ingrese la contraseña del nuevo administrador: ")
				self.adicionar_administrador(credencial, contraseña)
			elif opcion == 4:
				self.mostrar_cajeros_registrados()
			elif opcion == 5:
				self.mostrar_administradores_registrados()
			elif opcion == 6:
				self.mostrar_clientes_registrados()
			elif opcion == 7:
				self.buscar_cajero()
			elif opcion == 8:
				self.dar_de_baja_cajero()
			elif opcion == 9:
				self.dar_de_baja_cliente()
			elif opcion == 10:
				print("Sesión de administrador finalizada.")
				break
			else:
				print (chr(27)+"[1;31m")
				print("Opción no válida.")
				print (chr(27)+"[1;37m")

	def dar_de_baja_cajero(self):
		ubicacion = input("Ingrese la ubicación del cajero a dar de baja: ")
		for cajero in self.cajeros:
			if cajero.ubicacion == ubicacion:
				self.cajeros.remove(cajero)
				print (chr(27)+"[1;32m")
				print(f"Cajero en {ubicacion} dado de baja correctamente.")
				print (chr(27)+"[1;37m")
				return
		print (chr(27)+"[1;31m")	
		print("Cajero no encontrado.")
		print (chr(27)+"[1;37m")

	def dar_de_baja_cliente(self):
		numero_cuenta = input("Ingrese el número de cuenta del cliente a dar de baja: ")
		cliente = self.clientes.get(numero_cuenta)
		if cliente:
			del self.clientes[numero_cuenta]
			print (chr(27)+"[1;32m")
			print(f"Cliente {cliente.nombre} con número de cuenta {numero_cuenta} dado de baja correctamente.")
			print (chr(27)+"[1;37m")
		else:
			print (chr(27)+"[1;31m")
			print("Cliente no encontrado.")
			print (chr(27)+"[1;37m")

	def mostrar_administradores_registrados(self):
		if self.administradores:
			administradores_ordenados = self.quicksort(self.administradores, key=lambda admin: admin.credencial)
			print("\nAdministradores Registrados:")
			for admin in administradores_ordenados:
				print(f"- Credencial: {admin.credencial}")
		else:
			print (chr(27)+"[1;31m")
			print("\nNo hay administradores registrados.")
			print (chr(27)+"[1;37m")

	def mostrar_cajeros_registrados(self):
		if self.cajeros:
			cajeros_ordenados = self.quicksort(self.cajeros, key=lambda cajero: cajero.codigo)
			print("\nCajeros Registrados:")
			for cajero in cajeros_ordenados:
				print(f"- Código: {cajero.codigo}, Ubicación: {cajero.ubicacion}, Dispensador: {cajero.dispensador}")
		else:
			print (chr(27)+"[1;31m")
			print("\nNo hay cajeros registrados.")
			print (chr(27)+"[1;37m")

	def mostrar_clientes_registrados(self):
		if self.clientes:
			clientes_ordenados = self.quicksort(list(self.clientes.values()), key=lambda cliente: cliente.nombre)
			print("\nClientes Registrados:")
			for cliente in clientes_ordenados:
				print(f"- Nombre: {cliente.nombre}, Número de cuenta: {cliente.numero_cuenta}, Saldo: {cliente.cuenta.saldo}")
		else:
			print (chr(27)+"[1;31m")
			print("\nNo hay clientes registrados.")
			print (chr(27)+"[1;37m")

	def buscar_cajero(self):
		ubicacion = input("Ingrese la ubicación del cajero a buscar: ")
		for cajero in self.cajeros:
			if cajero.ubicacion == ubicacion:
				print(f"Cajero encontrado: Ubicación: {cajero.ubicacion}, Dispensador: {cajero.dispensador}")
				print (chr(27)+"[1;37m")
				return
		print (chr(27)+"[1;31m")	
		print("Cajero no encontrado.")
		print (chr(27)+"[1;37m")

	def menu_cliente(self, cliente):
		while True:
			print (chr(27)+"[1;34m")
			print("\n------MENU CLIENTE------")
			print (chr(27)+"[1;37m")
			print("1. Retirar Dinero")
			print("2. Depositar Dinero")
			print("3. Transferir Dinero")
			print("4. Pagar Servicios")
			print("5. Consultar Saldo")
			print("6. Consultar Movimientos")
			print("7. Salir")
			print (chr(27)+"[1;35m")
			opcion = int(input("Seleccione una opción: "))
			print (chr(27)+"[1;37m")

			if opcion == 1:
				cajero = self.seleccionar_cajero()
				if cajero:
					monto = int(input("Ingrese el monto a retirar: "))
					self.retirar_dinero(cliente, cajero, monto)
			elif opcion == 2:
				cajero = self.seleccionar_cajero()
				if cajero:
					monto = int(input("Ingrese el monto a depositar: "))
					self.depositar_dinero(cliente, cajero, monto)
			elif opcion == 3:
				numero_cuenta_destino = input("Ingrese el número de cuenta destino: ")
				monto = int(input("Ingrese el monto a transferir: "))
				self.transferir_dinero(cliente, numero_cuenta_destino, monto)
			elif opcion == 4:
				self.pagar_servicio(cliente)
			elif opcion == 5:
				self.consultar_saldo(cliente)
			elif opcion == 6:
				self.consultar_movimientos(cliente)
			elif opcion == 7:
				print("Sesión de cliente finalizada.")
				break
			else:
				print (chr(27)+"[1;31m")
				print("Opción no válida.")
				print (chr(27)+"[1;37m")

	def seleccionar_cajero(self):
		print("Cajeros Disponibles:")
		for i, cajero in enumerate(self.cajeros):
			print(f"{i + 1}. {cajero.ubicacion}")
		opcion = int(input("Seleccione el cajero: "))
		if 1 <= opcion <= len(self.cajeros):
			return self.cajeros[opcion - 1]
		else:
			print (chr(27)+"[1;31m")
			print("Opción no válida.")
			print (chr(27)+"[1;37m")
			return None

	def retirar_dinero(self, cliente, cajero, monto):
		if cliente.cuenta.saldo >= monto:
			cliente.cuenta.saldo -= monto
			cliente.cuenta.movimientos.append(f"Retiro: -{monto} - {datetime.now()}")
			print (chr(27)+"[1;32m")
			print(f"Retiro exitoso. Nuevo saldo: {cliente.cuenta.saldo}")
			print (chr(27)+"[1;37m")
		else:
			print (chr(27)+"[1;31m")
			print("Saldo insuficiente.")
			print (chr(27)+"[1;37m")

	def depositar_dinero(self, cliente, cajero, monto):
		cliente.cuenta.saldo += monto
		cliente.cuenta.movimientos.append(f"Depósito: +{monto} - {datetime.now()}")
		print (chr(27)+"[1;32m")
		print(f"Depósito exitoso. Nuevo saldo: {cliente.cuenta.saldo}")
		print (chr(27)+"[1;37m")

	def transferir_dinero(self, cliente, numero_cuenta_destino, monto):
		cliente_destino = self.clientes.get(numero_cuenta_destino)
		if cliente_destino:
			if cliente.cuenta.saldo >= monto:
				cliente.cuenta.saldo -= monto
				cliente.cuenta.movimientos.append(f"Transferencia: -{monto} a {numero_cuenta_destino} - {datetime.now()}")
				cliente_destino.cuenta.saldo += monto
				cliente_destino.cuenta.movimientos.append(f"Transferencia: +{monto} de {cliente.numero_cuenta} - {datetime.now()}")
				print (chr(27)+"[1;32m")
				print(f"Transferencia exitosa. Nuevo saldo: {cliente.cuenta.saldo}")
				print (chr(27)+"[1;37m")
			else:
				print (chr(27)+"[1;31m")
				print("Saldo insuficiente.")
				print (chr(27)+"[1;37m")
		else:
			print (chr(27)+"[1;31m")
			print("Número de cuenta destino no encontrado.")
			print (chr(27)+"[1;37m")

	def pagar_servicio(self, cliente):
		servicios = ["Electricidad", "Agua", "Recarga móvil", "Internet", "Cable"]
		print (chr(27)+"[1;34m")
		print("Servicios Disponibles:")
		print (chr(27)+"[1;37m")
		for i, servicio in enumerate(servicios):
			print(f"{i + 1}. {servicio}")
		print (chr(27)+"[1;35m")	
		opcion = int(input("Seleccione el servicio a pagar: "))
		print (chr(27)+"[1;37m")
		if 1 <= opcion <= len(servicios):
			monto = int(input(f"Ingrese el monto a pagar para {servicios[opcion - 1]}: "))
			if cliente.cuenta.saldo >= monto:
				cliente.cuenta.saldo -= monto
				cliente.cuenta.movimientos.append(f"Pago de servicio {servicios[opcion - 1]}: -{monto} - {datetime.now()}")
				print (chr(27)+"[1;32m")
				print(f"Pago de servicio {servicios[opcion - 1]} exitoso. Nuevo saldo: {cliente.cuenta.saldo}")
				print (chr(27)+"[1;37m")
			else:
				print (chr(27)+"[1;31m")
				print("Saldo insuficiente.")
				print (chr(27)+"[1;37m")
		else:
			print (chr(27)+"[1;31m")
			print("Opción no válida.")
			print (chr(27)+"[1;37m")

	def consultar_saldo(self, cliente):
		print (chr(27)+"[1;32m")
		print(f"Saldo actual: {cliente.cuenta.saldo}")
		print (chr(27)+"[1;37m")

	def consultar_movimientos(self, cliente):
		print("Movimientos de la cuenta:")
		for movimiento in cliente.cuenta.movimientos:
			print(movimiento)

	def quicksort(self, array, key=lambda x: x):
		if len(array) <= 1:
			return array
		pivot = array[0]
		less = [x for x in array[1:] if key(x) <= key(pivot)]
		greater = [x for x in array[1:] if key(x) > key(pivot)]
		return self.quicksort(less, key) + [pivot] + self.quicksort(greater, key)
	
	
#---------------------------------------------------------------------------	
def main():
	sistema = SistemaCajeroAutomatico()
	while sistema.en_ejecucion:
		sistema.iniciar_sesion()

if __name__ == "__main__":
	main()