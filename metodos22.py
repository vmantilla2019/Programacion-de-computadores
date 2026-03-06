class Animal:
    nombre = "Lori"
    especie = "Felino"
    edad = 2
    color = "Negro"

    def establecer_nombre(self, nombre):
        self.nombre = nombre

    def obtener_datos(self):
        return self.nombre, self.especie, self.edad, self.color


GATO = Animal()
GATO.establecer_nombre("loki")
print(GATO.obtener_datos())


class Vehiculo:
    marca = "honda"
    tipo = "moto"
    color = "Negra"
    velocidad = 180

    def establecer_marca(self, marca):
        self.marca = marca
    def establecer_tipo(self, tipo):
        self.tipo = tipo
    def establecer_color(self, color):
        self.color = color
    def establecer_velocidad(self, velocidad):
        self.velocidad = velocidad

    def obtener_datos(self):
        return self.marca, self.tipo, self.color, self.velocidad


MOTO = Vehiculo()
MOTO.establecer_marca("Yamaha")
print(MOTO.obtener_datos())
CARRO = Vehiculo()
CARRO.establecer_marca("Toyota")
CARRO.establecer_tipo("carro")
CARRO.establecer_color("blanco")
CARRO.establecer_velocidad("200")
print(CARRO.obtener_datos())


class Comida:
    nombre = "Bandeja Paisa"
    origen = "Antioquia"
    calorias = 1200
    precio = 25000

    def establecer_precio(self, precio):
        self.precio = precio

    def obtener_datos(self):
        return self.nombre, self.origen, self.calorias, self.precio


BANDEJA_PAISA = Comida()
BANDEJA_PAISA.establecer_precio(30000)
print(BANDEJA_PAISA.obtener_datos())


class Arbol:
    tipo = "Pino"
    altura = 10
    edad = 5
    color = "Verde"

    def establecer_altura(self, altura):
        self.altura = altura

    def obtener_datos(self):
        return self.tipo, self.altura, self.edad, self.color


PINO = Arbol()
PINO.establecer_altura(12)
print(PINO.obtener_datos())


class Libro:
    titulo = ""
    autor = "Dostoevsky"
    paginas = 527
    genero = "Novela"

    def establecer_titulo(self, titulo):
        self.titulo = titulo

    def obtener_datos(self):
        return self.titulo, self.autor, self.paginas, self.genero


NOVELA = Libro()
NOVELA.establecer_titulo("Crimen y castigo")
print(NOVELA.obtener_datos())


class Pelicula:
    titulo = "Monsters Inc"
    genero = "Animacion"
    duracion = 92
    año = 2001

    def establecer_año(self, año):
        self.año = año

    def obtener_datos(self):
        return self.titulo, self.genero, self.duracion, self.año


MONSTERSINC = Pelicula()
MONSTERSINC.establecer_año(2001)
print(MONSTERSINC.obtener_datos())


class Dispositivo:
    tipo = "Portatil"
    marca = ""
    memoria = "16GB"
    procesador = "Intel i5"

    def establecer_marca(self, marca):
        self.marca = marca

    def obtener_datos(self):
        return self.tipo, self.marca, self.memoria, self.procesador


PORTATIL = Dispositivo()
PORTATIL.establecer_marca("Asus")
print(PORTATIL.obtener_datos())


class Servicio:
    tipo = "Energia"
    empresa = ""
    costo = 50000
    cobertura = "Nacional"

    def establecer_empresa(self, empresa):
        self.empresa = empresa

    def obtener_datos(self):
        return self.tipo, self.empresa, self.costo, self.cobertura


ENERGIA = Servicio()
ENERGIA.establecer_empresa("Codensa")
print(ENERGIA.obtener_datos())


class Empaque:
    tipo = "Caja"
    material = "Carton"
    tamaño = "Mediana"
    peso = "1kg"

    def establecer_material(self, material):
        self.material = material

    def obtener_datos(self):
        return self.tipo, self.material, self.tamaño, self.peso


CAJA = Empaque()
CAJA.establecer_material("Carton reciclado")
print(CAJA.obtener_datos())


class Persona:
    nombre = ""
    edad = 17
    ocupacion = "Estudiante"
    ciudad = "Giron"

    def establecer_nombre(self, nombre):
        self.nombre = nombre

    def obtener_datos(self):
        return self.nombre, self.edad, self.ocupacion, self.ciudad


ESTUDIANTE = Persona()
ESTUDIANTE.establecer_nombre("Valerie")
print(ESTUDIANTE.obtener_datos())