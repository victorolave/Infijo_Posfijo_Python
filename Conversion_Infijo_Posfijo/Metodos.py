class Metodos:

    letras = list ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    numeros = list ('0123456789')
    tamaño = 0
    pila = []
    expresion_postfija = []
    tope = 0

    def __init__(self, tamaño, expresion_postfija):
        self.tamaño = tamaño
        self.expresion_postfija = expresion_postfija
        self.tope = -1
        self.letras = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.numeros = list('0123456789')

    def pila_llena(self):
        if self.tope == self.tamaño:
            print("La pila esta llena")
            return True
        return False

    def pila_vacia(self):
        if self.tope == -1:
            return True
        return False

    def apilar(self, dato):
        if not self.pila_llena():
            self.pila.insert(self.tope, dato)
            self.tope += 1

    def desapilar(self):
        if not self.pila_vacia():
            aux = self.pila[self.tope]
            del self.pila[self.tope]
            self.tope -= 1
            return aux

    def prioridad_operacion(self, EI, i):
        if EI[i] == '^':
            prioridadop = 4
            return prioridadop
        elif EI[i] == '*':
            prioridadop = 2
            return prioridadop
        elif EI[i] == '/':
            prioridadop = 2
            return prioridadop
        elif EI[i] == '+':
            prioridadop = 1
            return prioridadop
        elif EI[i] == '-':
            prioridadop = 1
            return prioridadop
        elif EI[i] == '(':
            prioridadop = 5
            return prioridadop

        return 0

    def prioridad_pila(self):
        if self.pila[self.tope] == '^':
            prioridadpila = 3
            return prioridadpila
        elif self.pila[self.tope] == '*':
            prioridadpila = 1
            return prioridadpila
        elif self.pila[self.tope] == '/':
            prioridadpila = 1
            return prioridadpila
        elif self.pila[self.tope] == '+':
            prioridadpila = 2
            return prioridadpila
        elif self.pila[self.tope] == '-':
            prioridadpila = 2
            return prioridadpila
        elif self.pila[self.tope] == '(':
            prioridadpila = 0
            return prioridadpila
        elif self.pila[self.tope] == ')':
            prioridadpila = 0
            return prioridadpila

        return 0
    def es_operador(self, ei, i):
        if ei[i] in self.letras or ei[i] in self.numeros:
            return False
        return True
