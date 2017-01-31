#! /usr/bin/python3.5

file = open('/etc/passwd','r')

maquinas = file.readlines()

for maquina in maquinas:
	userIndex = maquina.find(':')	
	shellIndex = maquina.rfind(':')
	print(maquina[:userIndex], '-', maquina[shellIndex+1:-1])

#El usuario y la shell son lo primero y lo último de cada línea


print('Número de usuarios:',maquinas.__len__())
#print(len(maquinas)) también funcionaría
# len es un método mágico
file.close()
