class Cliente:
    def __init__(self, nombre="", direccion="", telefono="", email="", cotizacion=50, total_cotizaciones=100):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        self.cotizacion = cotizacion
        self.total_cotizaciones = total_cotizaciones

    def modCotizacion(self, dato):
        self.cotizacion = dato
        self.total_cotizaciones += dato

indra = Cliente()
print(indra)
indra.nombre = "Pikachu"
indra.direccion = "Pueblo paleta"
indra.telefono = "658957561"
indra.email = "cristian@gmail.com"

indra.modCotizacion(1200000)
print(indra.nombre)
print(indra.direccion)
print(indra.telefono)
print(indra.email)
print(indra.cotizacion)
print(indra.total_cotizaciones)

timon = Cliente()
timon.nombre = "Charizard"
timon.telefono = "123456789"
timon.cotizacion = 100
timon.modCotizacion(200)

print(timon.nombre)
print(timon.cotizacion)
print(timon.total_cotizaciones)