"""
Ejercicio 1: Introducción a Clases y Objetos
Autora: Virginia Paloma
Año: 2026

Crear una clase RECTANGULO con atributos y métodos básicos
"""

class Rectangulo:
    def __init__(self, base, altura):
        """
        Inicializa la clase Rectángulo
        
        Args:
            base (float): Base del rectángulo
            altura (float): Altura del rectángulo
        """
        
        self.base = base
        self.altura = altura
        
    def calcular_perimetro(self):
        """
        Calcula el perímetro del rectángulo

        Returns:
            float: Perímetro del rectángulo
        """
        
        return 2 * (self.altura + self.base)
        
    def calcular_area(self):
        """
        Calcula el área del rectángulo

        Returns:
            float: Área del rectángulo
        """
        
        return self.altura * self.base
    
    def __str__(self):
        return f'\nRectángulo (base = {self.base}, altura = {self.altura})'
    

def main():
    # Programa Principal
    
    # Caso 1: Datos predefinidos
    rectangulo1 = Rectangulo(2.5, 3.5) # Creo el primer objeto, o sea, instancio la clase
    print(rectangulo1)
    print(f'- Su perímetro es {rectangulo1.calcular_perimetro():.2f}m')
    print(f'- Su área es {rectangulo1.calcular_area():.2f} m²')


    # Caso 2: Datos ingresados por el usuario
    base = float(input('\nIngrese la base de un rectángulo en metros: '))
    altura = float(input('\nIngrese la altura de un rectángulo en metros: '))
    rectangulo2 = Rectangulo(base, altura)
    print(rectangulo2)
    print(f'- Su perímetro es {rectangulo2.calcular_perimetro():.2f}m')
    print(f'- Su área es {rectangulo2.calcular_area():.2f} m²')
    
if __name__ == '__main__':
    main()
    