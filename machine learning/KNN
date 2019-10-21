#1-NN
def um_nn(dado):
   k=[]
   for i in range(120):
   x=0
   for d in range(4):
   x=(dado[d]-trainx[i][d])**2+x
   k.append(np.sqrt(x))
   return k
confusao2=[[0,0,0],
           [0,0,0],
          [0,0,0]]
for f in range(5):
    resulta2=[]
    fold(data)
for i in range(30):
    go=um_nn(testx[i])
    vai=np.asarray(go)
    resulta2.append(np.argmin(vai))
    resulta2=np.asarray(resulta2)
for i in range(30):
    if trainy[resulta2[i]]==testy[i]:
    confusao2[int(testy[i])][int(trainy[resulta2[i]])] =\
    confusao2[int(testy[i])][int(trainy[resulta2[i]])]+1
else:
    confusao2[int(testy[i])][int(trainy[resulta2[i]])] =\
    confusao2[int(testy[i])][int(trainy[resulta2[i]])]+1
    print('\n')
    print('1 vizinho mais próximo')
for i in confusao2:
print(i)
#3-NN
def tres_nn(dado):
   kkk=[]
   for i in range(120):
   x=0
   for d in range(4):
       x=(dado[d]-trainx[i][d])**2+x
       kkk.append(np.sqrt(x))
   return kkk
confusao3=[[0,0,0],
           [0,0,0],
           [0,0,0]]
for f in range(5):
    fold(data)
    resultado3=[]
for i in range(30):
    mn=[]
    go=tres_nn(testx[i])
    go=np.asarray(go)
    mn.append(np.argmin(go))
    test=np.delete(go,mn)
    mn.append(np.argmin(test))
    test=np.delete(go,mn)
    mn.append(np.argmin(test))
    test=np.delete(go,mn)
teste=trainy[mn]
teste=teste.tolist()
classe=Counter()
for n in teste:
classe[n]+=1
mais=classe.most_common(1)
resultado3.append(mais[0][0])
for i in range(30):
confusao3[int(trainy[i])][int(resultado3[i])] =\
confusao3[int(trainy[i])][int(resultado3[i])]+1
print('\n')
print('3 vizinho mais próximo')
for i in confusao3:
print(i)
muclass_0=[]
muclass_1=[]
muclass_2=[]
varclass_0=[]
varclass_1=[]
varclass_2=[]
for i in range(4):
    #mu=np.mean(data[trainy==0,i])
    muclass_0.append(np.mean(trainx[trainy==0,i]))
    muclass_1.append(np.mean(trainx[trainy==1,i]))
    muclass_2.append(np.mean(trainx[trainy==2,i]))
    varclass_0.append(np.var(trainx[trainy==0,i]))
    varclass_1.append(np.var(trainx[trainy==1,i]))
    varclass_2.append(np.var(trainx[trainy==2,i]))
    mu=muclass_0,muclass_1,muclass_2
    var=varclass_0,varclass_1,varclass_2
    mut=np.asarray(mu)
    vart=np.asarray(var)
    n_test=len(testx)
