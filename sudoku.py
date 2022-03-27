Letras_a = ["A","B","C","D","E","F","G","H","I"]
Letras_b = ["A","B","C","D","E","F","G","H","I"]
Letras_Merge = []
count = 8
while count > -1:
    for i in range(len(Letras_a)):
        Letras_Merge.append(Letras_a[count]+Letras_b[i])
    count=count-1

Letras_Merge.sort()
QuadA=[]
QuadB=[]
QuadC=[]
QuadD=[]
QuadE=[]
QuadF=[]
QuadG=[]
QuadH=[]
QuadI=[]

rango = 9 #Variable para aumentar en múltiplos de 9 el i
for i in range(0,9): #Distribución de las letras en cuadrantes según su letra inicial
    i=i%9
    QuadA.append(Letras_Merge[i])
    QuadB.append(Letras_Merge[i+(rango*1)])
    QuadC.append(Letras_Merge[i+(rango*2)])
    QuadD.append(Letras_Merge[i+(rango*3)])
    QuadE.append(Letras_Merge[i+(rango*4)])
    QuadF.append(Letras_Merge[i+(rango*5)])
    QuadG.append(Letras_Merge[i+(rango*6)])
    QuadH.append(Letras_Merge[i+(rango*7)])
    QuadI.append(Letras_Merge[i+(rango*8)])


#Las siguientes lineas son prescindibles a futuro, sólo existen para corroborar la función del programa

#for i in range(len(Letras_Merge)):
#    print(Letras_Merge[i]

#Para estudiar la relación matemática de cada cuadro, utilizo la siguiente acción:
#restos = [] //Creo una lista vacía para almacenar los datos
#for i i range(1,81):
#   restos.append(i%9) //Añado los restos de dividir los primeros 81 enteros por 9.





