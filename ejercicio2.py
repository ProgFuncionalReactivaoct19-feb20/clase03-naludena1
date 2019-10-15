"""
	@naludena1
"""
# Funcional - Aplicando función 
#
"""
	Dada las siguientes placas, filtrar aquellas que pertenecen a las provincias de :
	Loja, Pichincha, Esmeraldas, Azuay, Imbabura
	Placas: lba-001, gma-002, azx-003, ess-004,  oro-100, mab-001, iaj-002
"""

def es_prov(x):
	provincias = ["l", "p", "e", "a", "i"]
	prov = x[0]
	if prov in provincias:
		return True
	else:
		return False

datos = ["lba-001", "gma-002", "azx-003", "ess-004", "oro-100", "mab-001", "iaj-002"]
resultado = filter(es_prov, datos)

print(list(resultado))
