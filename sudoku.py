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
for i in range(0,rango): #Distribución de las letras en cuadrantes según su letra inicial
    i=i%rango
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

COL1=[]
COL2=[]
COL3=[]
COL4=[]
COL5=[]
COL6=[]
COL7=[]
COL8=[]
COL9=[]

rango_COL =9

for i in range(0,3): #Distribución de las letras en cuadrantes según su letra inicial
    i=i*3
    COL1.append(QuadA[i]) 
    COL2.append(QuadA[i+1])
    COL3.append(QuadA[2+i])

    COL4.append(QuadB[i]) 
    COL5.append(QuadB[1+i])
    COL6.append(QuadB[2+i])

    COL7.append(QuadC[i]) #!
    COL8.append(QuadC[i+1])
    COL9.append(QuadC[i+2])

for i in range(0,3):
    i=i*3
    COL1.append(QuadD[i])
    COL2.append(QuadD[i+1])
    COL3.append(QuadD[i+2])

    COL4.append(QuadE[i]) 
    COL5.append(QuadE[1+i])
    COL6.append(QuadE[2+i])

    COL7.append(QuadF[i]) 
    COL8.append(QuadF[1+i])
    COL9.append(QuadF[2+i])

for i in range(0,3):
    i=i*3
    COL1.append(QuadG[i])
    COL2.append(QuadG[i+1])
    COL3.append(QuadG[i+2])

    COL4.append(QuadH[i]) 
    COL5.append(QuadH[1+i])
    COL6.append(QuadH[2+i])

    COL7.append(QuadI[i]) 
    COL8.append(QuadI[1+i])
    COL9.append(QuadI[2+i])

FIL1=[]
FIL2=[]
FIL3=[]
FIL4=[]
FIL5=[]
FIL6=[]
FIL7=[]
FIL8=[]
FIL9=[]

rango_FIL = 9

for i in range (0,3):
    i=i%3
    FIL1.append(Letras_Merge[i]) #9*0
    FIL1.append(Letras_Merge[i+3*3]) #9*1
    FIL1.append(Letras_Merge[i+3*3*2])#9*2

    FIL2.append(Letras_Merge[i+3*1]) #3*1
    FIL2.append(Letras_Merge[i+3*4]) #3*4
    FIL2.append(Letras_Merge[i+3*7]) #3*7

    FIL3.append(Letras_Merge[i+(3*2)]) #6
    FIL3.append(Letras_Merge[i+(3*5)]) # 15
    FIL3.append(Letras_Merge[i+(3*8)]) # 18

    FIL4.append(Letras_Merge[i+(3*9)]) #27 = 3*9
    FIL4.append(Letras_Merge[i+(3*12)]) #36 = 3*12
    FIL4.append(Letras_Merge[i+(3*15)]) #45 = 3*15

    FIL5.append(Letras_Merge[i+3*10])
    FIL5.append(Letras_Merge[i+3*13])
    FIL5.append(Letras_Merge[i+3*16])

    FIL6.append(Letras_Merge[i+3*11]) #Fin de la segunda triadad de cuadrantes
    FIL6.append(Letras_Merge[i+3*14])
    FIL6.append(Letras_Merge[i+3*17])

    FIL7.append(Letras_Merge[i+3*18])
    FIL7.append(Letras_Merge[i+3*21])
    FIL7.append(Letras_Merge[i+3*24])

    FIL8.append(Letras_Merge[i+3*19])
    FIL8.append(Letras_Merge[i+3*22])
    FIL8.append(Letras_Merge[i+3*25])

    FIL9.append(Letras_Merge[i+3*20])
    FIL9.append(Letras_Merge[i+3*23])
    FIL9.append(Letras_Merge[i+3*26])

FIL1.sort()
FIL2.sort()
FIL3.sort()
FIL4.sort()
FIL5.sort()
FIL6.sort()
FIL7.sort()
FIL8.sort()
FIL9.sort()
