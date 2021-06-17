
#EJERCICIO PRUEBA

print('EJERCICIO OCURRENCIAS')
file1=open('harry.txt')
file=file1.read()
file=file.split()
file2=[]

for i in file:
	if i not in file2:
		file2.append(i)

print('==RESULTADO EJERCICIO== ')
for i in range (0, len(file2)):
	if len(file2[i])>4:
		print ('(', file2[i],')',file.count(file2[i]),')')




