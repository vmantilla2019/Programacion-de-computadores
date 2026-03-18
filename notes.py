class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = []

    def agregar_notas(self, notas):
        self.notas = notas

    def calcular(self):
        return calcular_definitiva(self.notas)

    def clasificar(self):
        return clasificar_estudiante(self.calcular())
        

def validar_nota(nota):
    return 0 <= nota <= 5

def calcular_definitiva(notas):
    return sum(notas) / len(notas)

def clasificar_estudiante(definitiva):
    if definitiva >= 4.5:
        return "Excelente"
    elif definitiva >=3:
        return "aprobado"
    else:
        return "reprobado"


estudiantes = []

cantidad = int(input("¿Cuántos estudiantes?: "))

for i in range(cantidad):
    nombre = input("Nombre: ")
    est = Estudiante(nombre)

notas = []
for j in range(3):
    while True:
        nota = float(input(f"Nota {j+1}: "))
        if validar_nota(nota):
            notas.append(nota)
            break
        else:
            print("Nota inválida")

est.agregar_notas(notas)
estudiantes.append(est)


print("resultados:")
for est in estudiantes:
    definitiva = est.calcular()
    estado = est.clasificar()
    print(est.nombre, "-", round(definitiva, 2), "-", estado)