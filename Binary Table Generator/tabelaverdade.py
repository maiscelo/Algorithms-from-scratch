#Gerador de tabela verdade.
tab=[]
ent=11
contador=0
for i in range(2**ent//2):
    tab.append([0])
for i in range(2**ent//2):
    tab.append([1])
for i in range(2**ent):
    if (i+1)%2==0:
       tab[i].append(1)
    else:
       tab[i].append(0)
def completa(ent,contador):
     if ent-2!=0:
        i=0
        for j in range(2**(contador+1)):
            x=2**ent//2//2 #passo
            while x!=0:
                 tab[i].insert(contador+1,0)
                 x-=1
                 i+=1
            x=2**ent//2//2 #passo
            while x!=0:
                 tab[i].insert(contador+1,1)
                 x-=1
                 i+=1
        contador+=1 
        if contador==ent-1:
             return tab
        else:
             completa(ent-1,contador)
completa(ent,contador)
print(tab)

#3 - 8 - 4 2 1
#4 - 16 - 8 4 2 1
#5 - 32 - 16 8 4 2 1


