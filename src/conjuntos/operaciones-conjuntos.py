class Conjunto:
    def __init__(self, elementos):
        self.elementos = []
        for e in elementos:
            if e not in self.elementos:
                self.elementos.append(e)

    def union(self, otros):
        resultado = self.elementos[:]
        for conjunto in otros:
            for elemento in conjunto.elementos:
                if elemento not in resultado:
                    resultado.append(elemento)
        return Conjunto(resultado)

    def interseccion(self, otros):
        resultado = self.elementos[:]
        for conjunto in otros:
            resultado = [e for e in resultado if e in conjunto.elementos]
        return Conjunto(resultado)

    def diferencia(self, otro):
        resultado = [e for e in self.elementos if e not in otro.elementos]
        return Conjunto(resultado)

    def diferencia_simetrica(self, otro):
        diferencia1 = self.diferencia(otro).elementos
        diferencia2 = otro.diferencia(self).elementos
        return Conjunto(diferencia1 + diferencia2)

    def es_subconjunto(self, otro):
        for e in self.elementos:
            if e not in otro.elementos:
                return False
        return True

    def es_superconjunto(self, otro):
        return otro.es_subconjunto(self)

    def __str__(self):
        return "{" + ", ".join(map(str, self.elementos)) + "}"

    def propiedades(self):
        return {
            "Conmutatividad Unión": self.union([self]).elementos == self.union([self]).elementos,
            "Conmutatividad Intersección": self.interseccion([self]).elementos == self.interseccion([self]).elementos,
            "Asociatividad Unión": self.union([self.union([self])]).elementos == self.union([self]).union([self]).elementos,
            "Asociatividad Intersección": self.interseccion([self.interseccion([self])]).elementos == self.interseccion([self]).interseccion([self]).elementos,
            "Distributividad": self.union([self.interseccion([self])]).elementos == self.interseccion([self.union([self])]).elementos,
            "Idempotencia": self.union([self]).elementos == self.elementos and self.interseccion([self]).elementos == self.elementos
        }

# Ejemplo de uso:
A = Conjunto([1, 2, 3])
B = Conjunto([3, 4, 5])
C = Conjunto([5, 6, 7])
D = Conjunto([3,4])

print("Unión:", A.union([B, C]))
print("Intersección:", B.interseccion([C]))
print("Diferencia:", A.diferencia(B))
print("Diferencia Simétrica:", A.diferencia_simetrica(B))
print("D es subconjunto de B:", D.es_subconjunto(B))
print("B es superconjunto de D:", B.es_superconjunto(D))
print("Propiedades:", A.propiedades())
