from mesa import Agent,Model
from mesa.time import BaseScheduler,RandomActivation
from mesa.datacollection import DataCollector
from mesa.space import MultiGrid,SingleGrid
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random, math
from random import randrange
from collections import Counter
from scipy.stats import norm, multivariate_normal
from numpy.linalg import inv

class Ant(Agent):
    
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.wealth = 1
        self.carga=False
        
    def step(self):
        #print(self.unique_id)
        self.probabilidade()
        self.model.i=self.model.i+1
        other_agent = self.random.choice(self.model.schedule.agents)
        other_agent.wealth += 1
        self.wealth -= 1
        
    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos,
            moore=True,
            include_center=False
        )
        new_position = self.random.choice(possible_steps)
        if self.model.grid.is_cell_empty(new_position):
            self.model.grid.move_agent(self, new_position)
        else:
            self.move()
            
    def movedado(self,i):
        possible_steps = self.model.grid1.get_neighborhood(
            self.pos,
            moore=True,
            include_center=False
        )
        z=[b for b in model.schedule_dados.agents]
        new_position = self.random.choice(possible_steps)
        if self.model.grid.is_cell_empty(new_position) and self.model.grid1.is_cell_empty(new_position) :
            self.model.grid.move_agent(self, new_position)
            self.model.grid1.move_agent(z[i],new_position)
        else:
            self.movedado(i)
      
    def probabilidade(self):
        flag=False
        y=[b.pos for b in model.schedule_dados.agents]
        z=[b.unique_id for b in model.schedule_dados.agents]
        for i in range(150):
            if self.pos==y[i] and self.carga==False and flag==False:
                flag=True
                p=dado.pick(self,y[i],z[i])
                
                aleatorio_p=random.uniform(0,1)
                #print('pick',p,aleatorio_p)
                if p>=aleatorio_p:
                    self.carga=True
                    self.movedado(i)
                    #print('pick',p)
                else:
                    self.move()
            if  self.pos==y[i] and self.carga==True and flag==False:
                flag=True
                d=dado.drop(self,y[i],z[i])
                
                aleatorio_d=random.uniform(0,1)
                #print('drop',d,aleatorio_d)
                if d>=aleatorio_d:
                    self.carga=False
                    self.move()
                else:
                    #print('drop',d)
                    self.movedado(i)
        if flag==False and self.carga==False:
            self.move()
        
        
class dado(Agent):
    def __init__(self, unique_id,model):
        super().__init__(unique_id, model) 
        self.valor=np.loadtxt('iris.data.txt', delimiter=',')
        
    def step(self):
        pass
    
    def funcao(self,data_pos,z):
        v=dado.valor(self)
        dj=[]
        df=[]
        xjotas=[]
        f=0
        possible_vizinhos = self.model.grid1.get_neighborhood(
            data_pos,
            moore=True,
            include_center=False
        )
        y=possible_vizinhos
        for i in y:
            if self.model.grid1.is_cell_empty(i)==False:
                df.append(i)
                quem=[c.unique_id for c in self.model.grid1.get_cell_list_contents(i)]
                xjotas.append(quem)
            if self.model.grid1.is_cell_empty(i)==True:
                dj.append(i)
        soma=0
        total=0
        if len(df)==0:
            f=1/16*1
        if len(df)!=0:
            #print(z)
            #print(xjotas)
            for i in range(len(xjotas)):
                for j in range(4):
                    soma=(v[z][j]-v[xjotas[i][0]][j])**2+soma
                    
                total=(1-(math.sqrt(soma)/3.5))+total
                #print(soma)
            f=total*0.0625
            #print(f)
        if f<0:
            #print(f)
            f=0
        return(f)
    
    def drop(self,data_pos,z):
        valor=dado.funcao(self,data_pos,z)
        #print('f de drop',valor)
        return (valor/(valor+0.09))**2
    def pick(self,data_pos,z):
        valor=dado.funcao(self,data_pos,z)
        #print('f de pick', valor)
        return (0.1/(0.1+valor))**2
    def valor(self):
        valor=np.loadtxt('iris.data.txt', delimiter=',')
        return valor
    

class Antcluster(Model):
    """A model with some number of agents."""
    def __init__(self, N):
        self.num_agents = N
        self.i=1
        self.grid = SingleGrid(120,120, True)
        self.grid1= SingleGrid(120,120,True)
        self.schedule = RandomActivation(self)
        self.schedule_dados=BaseScheduler(self)
        # Create agents
        for i in range(self.num_agents):
            a = Ant(i, self)
            self.schedule.add(a)
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            #z = np.asarray([x,y])
            #print(z)
            plt.axis([-10, 125, -10, 125])
            #plt.scatter(x,y)
            self.grid.place_agent(a, (x, y))
        #create data    
        for i in range(150):
            b = dado(i,self)
            self.schedule_dados.add(b)
            x = self.random.randrange(self.grid1.width)
            y = self.random.randrange(self.grid1.height)
            #print(x,y)
            z = np.asarray([x,y])
            plt.axis([-10, 125, -10, 125])
            plt.scatter(x,y)
            self.grid1.place_agent(b, (x, y))
    def step(self):
        '''Advance the model by one step.'''
        self.schedule_dados.step()
        self.schedule.step()


model=Antcluster(10)
for i in range(1000):
    model.step()
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(1, 1, 1)
#ax = plt.subplots(figsize=(10, 8))
# Major ticks every 20, minor ticks every 5
major_ticks = np.arange(-10, 125, 20)
minor_ticks = np.arange(-10, 125, 5)

ax.set_xticks(major_ticks)
ax.set_xticks(minor_ticks, minor=True)
ax.set_yticks(major_ticks)
ax.set_yticks(minor_ticks, minor=True)
for i,txt in enumerate(u):
    x,y=g[i]
    #ax.scatter(x,y)
    ax.annotate(txt, (x, y))
    
# And a corresponding grid

ax.grid(which='both')
g=[c.pos for c in model.schedule_dados.agents]
u=[b.unique_id for b in model.schedule_dados.agents]
plt.figure(figsize=(6, 5))
plt.axis([-10, 125, -10, 125])
plt.grid(b=True,in_layout=True)
for i,txt in enumerate(u):
    x,y=g[i]
    plt.scatter(x,y)
    #plt.annotate(txt, (x, y))
     #ax.grid(which='both')
