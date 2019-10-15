"""
	@naludena1
"""
# Funcional - Aplicando funciones
#
"""
	Dadas las siguiente ciudades, filtrar aquellas que tienen un
	número par como longitud en sus caracteres.
	Loja, Pichincha, Guayaquil, Zamora, Ibarra, Manabi, Machala,
	Portoviejo, Macas
"""

datos = ["Loja", "Pichincha", "Guayaquil", "Zamora", "Ibarra", "Manabi", 
	"Machala", "Portoviejo", "Macas"]

resultado = filter(lambda x: len(x)%2 == 0, datos)
print(list(resultado))