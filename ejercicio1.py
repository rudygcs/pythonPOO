class ProcesadorDeTextos:
    def __init__(self, textos):
        self.textos = textos

    def promedio_longitudes(self):
        longitud_total = sum(len(texto) for texto in self.textos)
        return longitud_total / len(self.textos)

    def concatenar_textos(self):
        texto_concatenado = ''.join(self.textos)
        return texto_concatenado

    def comparar_longitud_con_15(self):
        texto_concatenado = self.concatenar_textos()
        longitud = len(texto_concatenado)
        if longitud > 15:
            return f"Mayor a 15, longitud: {longitud}"
        elif longitud < 15:
            return f"Menor a 15, longitud: {longitud}"
        else:
            return f"Igual a 15, longitud: {longitud}"

    def texto_con_mas_caracteres(self):
        longitud_maxima = max(len(texto) for texto in self.textos)
        for texto in self.textos:
            if len(texto) == longitud_maxima:
                return texto

    def contar_caracteres_numericos(self):
        texto_concatenado = self.concatenar_textos()
        return sum(caracter.isdigit() for caracter in texto_concatenado)

# Uso del programa
textos = []
for i in range(3):
    texto = input(f"Ingrese el texto {i+1}: ")
    textos.append(texto)

procesador = ProcesadorDeTextos(textos)

# a. Mostrar el promedio de las longitudes de los textos
print(f"El promedio de las longitudes de los textos es: {procesador.promedio_longitudes()}")

# b. Concatenar los textos e indicar si el largo es mayor, menor o igual a 15
print(f"La longitud del texto concatenado es {procesador.comparar_longitud_con_15()}")

# c. Indicar cuál de los textos posee más caracteres
print(f"El texto con más caracteres es: '{procesador.texto_con_mas_caracteres()}'")

# d. Concatenar los textos e indicar la cantidad de caracteres numéricos existentes
print(f"Número de caracteres numéricos en el texto concatenado: {procesador.contar_caracteres_numericos()}")
