"""
	@naludena1
"""
# Funcional - Aplicando función filter
#
# Dado un conjunto de palabras filtrar todas aquellas que sean palindromas
#


datos = ["oro", "pais", "ojo", "oso", "radar", "sol", "seres"]

resultado = filter(lambda x: "".join(reversed(x)) == x, datos)

print(list(resultado))





