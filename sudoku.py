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


#Las siguientes lineas son prescindibles a futuro, sólo existen para corroborar la función del programa

#for i in range(len(Letras_Merge)):
#    print(Letras_Merge[i])

for i in range(len(Letras_a)):
    QuadA.append(Letras_Merge[i])