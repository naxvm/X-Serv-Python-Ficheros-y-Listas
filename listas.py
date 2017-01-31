#! /usr/bin/python3.5


file = open('/etc/passwd', 'r')

maquinas = file.readlines()

for maquina in maquinas:
	login = maquina.split(':')[0]
	shell = maquina.split(':')[-1]
	print(login, '-', shell)


print('-------------\n', maquinas.__len__(), 'users') 


file.close()
