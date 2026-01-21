"""
Ejercicio 2: Herencia
Autora: Virginia Paloma
Año: 2026

Crear una clase PARCELA con atributos y métodos básicos. 
Usar Herencia y Herencia Múltiple. 
"""

class Parcela:
    
    def __init__(self, numero, superficie, zona):
        """Inicializa la clase Parcela

        Args:
            numero (int): Número identificador de la parcela
            superficie (float): Superficie de la parcela en metros cuadrados [m2]
            zona (str): Zona Urbana, Rural, Industrial
        """
        self.numero = numero
        self.superficie = superficie
        self.zona = zona
    
    def calcular_has(self):
        """Conversión de la superficie en metros cuadrados [m2] a hectáreas [has]

        Returns:
            float: Superficie en hectáreas
        """
        sup_has = self.superficie / 10000
        return sup_has
        
    def __str__(self):
        return f'Parcela {self.numero}: Superficie: {self.superficie} m² - Zona: {self.zona}'
    
class ParcelaUrbana(Parcela):
    def __init__(self, numero, superficie, zona, edificada):
        """Inicializa la clase ParcelaUrbana

        Args:
            edificada (bool): Tiene edificación o no.
        
        Note:
            Los demás parámetros se heredan de la clase Parcela.
        """
        super().__init__(numero, superficie, zona)
        self.edificada = edificada
        
    def calcular_impuesto_municipal(self):
        """Calculo de impuesto municipal

        Returns:
            float: Impuesto municipal
        """
        if self.edificada == True:
            impuesto = self.superficie * 15
        else:
            impuesto = self.superficie * 8
        
        return impuesto

class ParcelaRural(Parcela):
    pass

class ParcelaIndustrial(Parcela):
    pass



parcela1 = Parcela(1, 1500, 'Industrial')
print(parcela1)