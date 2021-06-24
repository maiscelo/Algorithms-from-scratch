for i in range(5):
    fold(data)
    score=np.zeros((n_test,3))
    for i in range(n_test):
        for j in range(3):
            for d in range(4):
                score[i,j]=-np.log(np.sqrt(vart[j][d]))-0.5*((testx[i][d]-mut[j][d])/vart[j][d])+score[i,j]
    predicao=np.argmax(score[:,0:4],axis=1)
    
    for i in range(30):
            confusao4[int(testy[i])][int(predicao[i])]=confusao4[int(testy[i])][int(predicao[i])]+1
        
            
print('\n')
print('Naive Bayes')
for i in confusao4:
    print(i)


r=random.randrange(0,120),random.randrange(0,120),random.randrange(0,120)
centro_3=trainx[list(r)]
d=[]
for j in range(3):
   # print(j)
    for i in range(4):
        #print(-math.exp(i))
        d.append(centro_3[j][i]) 
d1=(centro_3[1]-d[0:4])**2
d2=(centro_3[1]-d[8:12])**2
d3=(centro_3[2]-d[0:4])**2
h=math.sqrt(sum(d1)),math.sqrt(sum(d2)),math.sqrt(sum(d3))
h=sum(h)/3
