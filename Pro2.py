
import numpy as np
import sys

class Nodo:
    """
    Clase nodos
    """
    def __init__(self, n):
        print("  ")
    def crear(n):
        nodos={}
        j=0
        while (j < n):
            nodos[j]=list([])
            j+=1
        return nodos

class Arista:
    """
    Clase Aristas
    """
    def __init__(self, n):
        print("  ")
    def creara(n,matriz0,nodos):
        for i in range(n):
            temp=[]
            for j in range(n):
                if matriz0[i,j]==1:
                    temp.append(j)
            nodos[i]=temp
        # print(nodos)
        return nodos

class dictio:
    """
    Clase nodos
    """
    def __init__(self, n,value):
        # value, [] vector vacio
        # value, False False
        print("  ")
    def crear(n,value):
        nodos={}
        j=0
        while (j < n):
            nodos[j] = value
            j+=1
        return nodos

class Grafo:
  """
  clase grafo
  mll para malla
  er para redosrenyi
  gil para gilbert
  geo para geografico
  bal para BarabasiAlbert
  dor para dorovovt
  """
  def __init__(self, tipo):
        self.graphtpe = tipo
        self.menuini(tipo)
        
  def menuini(self,tipo):
        print("Bienvenido a grafos! \n")
        print("Escogiste un grafo de ")

        if tipo == 'mll':
          print("modelo de malla\n")
          m=0; n=0
          while (m<=0 or n<=0):
            print("Nada de ceros")
            print("\n")
            m =  int(input("Define el numero de filas:  "))
            n =  int(input("Define el numero de columnas:   "))
          nodos = self.modelomalla(self,m,n)
        
        elif tipo == 'er':
          print("modelo de Erdös y Rényi\n")
          m=0; n=0
          while (m < n-1 or n<=0):
            print("Nada de ceros")
            print("\n")
            n =  int(input("Define el numero de nodos:  "))
            m =  int(input("Define el numero maximo de aristas que puede tener el grafo (>= n-1):   "))
          nodos=self.modeloerdosrenyi(self,n,m,dirigido=False, auto=False)
         
        elif tipo == 'gil':
          print("modelo de Gilbert\n")
          n=0;
          while (n<=0):
            print("Nada de ceros")
            print("\n")
            n =  int(input("Define el numero de nodos:  "))
            p =  float(input("Define la probabilidad de un nodo de formar arista(0, 1):   "))
          nodos = self.modelogilbert(self,n, p, dirigido=False, auto=False)
          
        elif tipo == 'geo':
          print("modelo geografico simple\n")
          n=0;
          while (n<=0):
            print("Nada de ceros")
            print("\n")
            n =  int(input("Define el numero de nodos:  "))
            r =  int(input("Define la distancia maxima para formar arista (<70):   "))
          nodos = self.modelogeo(self,n, r, dirigido=False, auto=False)
          
        elif tipo == 'bal':
          print("modelo variante de Barabási-Albert\n")
          n=0;d=1
          while (n<=0 and d<=1):
            print("Nada de ceros")
            print("\n")
            n =  int(input("Define el numero de nodos:  "))
            d =  int(input("Define el numero de aristas que pueden existir:   "))
          nodos = self.modeloBarabasiAlbert(self,n, d, dirigido=False, auto=False)
          
        elif tipo == 'dor':
          print("modelo de Dorogovtsev-Mendes\n")
          n=0
          while (n<=0):
            print("Nada de ceros")
            print("\n")
            n =  int(input("Define el numero de nodos:  "))
          nodos = self.modelodorogovt(self,n, dirigido=False)
          
        else:
            print("unrecognized :(")
            sys.exit()
        quessav=input("¿Salvamos el grafo? Presiona s para si, n para no")
        if quessav == 's' or quessav == 'S':
            self.savegraph(self,nodos,"E:\grafo.gv")
        else:
            print("Bye :)")
        return nodos
    
  def modelomalla(self,m,n):
    # m=7 #numero de filas
    # n=6 #numero de columnas
    #crear nodos
    nodos = Nodo.crear(m*n)
    #print(nodos)
    # metodo
    matriz0=np.zeros([m,n])
    cont=0
    for i in range(m):
        for j in range(n):
            matriz0[i,j]=int(cont)
            cont+=1
    # print(matriz0)
    for ni in nodos:
        temp=[]
        cordd=np.argwhere(matriz0==ni)[0][0],np.argwhere(matriz0==ni)[0][1]
        if cordd[0]+1 >= m and cordd[1]+1 >= n:
            continue
        elif cordd[0]+1 >= m:
            temp=list([int(matriz0[cordd[0],cordd[1]+1])])
        elif cordd[1]+1 >= n:
            temp=list([int(matriz0[cordd[0]+1,cordd[1]])])
        elif(cordd[0]+1 < m and cordd[1]+1 < n):
            temp=list([int(matriz0[cordd[0]+1,cordd[1]]),int(matriz0[cordd[0],cordd[1]+1])])
        # print(ni,cordd,temp)
        nodos[ni]=list(temp)
    print(nodos)
    return nodos

  def modeloerdosrenyi(self,n,m,dirigido=False, auto=False):
    #crear nodos
    # n=8#numero de nodos
    # m=10#numero maximo de aristas que puede tener un nodo (>= n-1)    
    nodos = Nodo.crear(n)
    # print(nodos)
    # metodo
    import random
    i=0
    matriz0=np.zeros([n,n])
    while i<m:
        noari=random.randrange(0,n)
        noari2=random.randrange(0,n)
        while noari==noari2 or matriz0[noari,noari2]==1:
            noari2=random.randrange(0,n)
        # print(noari,noari2)
        matriz0[noari,noari2]=1
        i+=1
    # print(matriz0)
    nodos=Arista.creara(n,matriz0,nodos)
    nodos=self.compconn(self,nodos,n)
    print(nodos)
    return nodos
  
  def modelogilbert(self,n, p, dirigido=False, auto=False):
    #crear nodos
    # n=8     #numero de nodos
    m=n
    # m=10    #numero maximo de aristas que puede tener un nodo (>= n-1)
    # p=0.1   #probabilidad de formar arista
    nodos = Nodo.crear(m)
    # print(nodos)
    
    # metodo
    import random
    i=0
    matriz0=np.zeros([n,n])
    while i<m:
        for ni in range(n):
            for nj in range(n):
                probi=random.random()
                if probi<=p:
                    matriz0[ni,nj]=1
                    i+=1
                else:
                    i=i
    # print(matriz0)
    nodos=Arista.creara(n,matriz0,nodos)
    nodos=self.compconn(self,nodos,n)
    print(nodos)
    return nodos
  
  def modelogeo(self,n, r, dirigido=False, auto=False):
    import random
    # n=8     #numero de nodos
    rect=[70,80]
    # m=10    #numero maximo de aristas que puede tener un nodo (>= n-1)
    # r=20   #distancia maximapara formar arista
    coordennodos={}
    nodos = Nodo.crear(n)
    coordennodos=nodos
    for ci in coordennodos:
        coordi=[random.randrange(rect[0]), random.randrange(rect[1])]
        coordennodos[ci]=coordi
    
    # metodo
    matriz0=np.zeros([n,n])
    for ci in coordennodos:
        coordi=coordennodos[ci]
        for cj in coordennodos:
            if cj != ci:
                coordi2=coordennodos[cj]
            else:
                continue
            rminys=np.sqrt(np.abs(float(np.dot((coordi2[0]-coordi[0]),(coordi2[1]-coordi[1])))))
            if  rminys <= r:
                matriz0[ci,cj]=1
    # print(matriz0)
    # crear aristas
    nodos=Arista.creara(n,matriz0,nodos)
    nodos=self.compconn(self,nodos,n)
    print(nodos)
    return nodos
  
  def modeloBarabasiAlbert(self,n, d, dirigido=False, auto=False):
    import random
    # n=10      #numero de nodos
    # d=1     #numero de aristas a las que se puede conectar cada nodo.
    # pmax=0.5
    nodos={}
    matriz0=np.zeros([n,n])
    # metodo
    for i in range(n):
        nodos[i]=[]
            
        # print(i,nodos)
        for j in nodos:
            for it in nodos:
                temp=[]
                for jt in nodos:
                    if matriz0[it,jt]==1:
                        temp.append(jt)
                nodos[it]=temp
            # print(len(nodos[j]) )
            if i==j:
                continue
            elif len(nodos[j])>=d:
                # print("here")
                p=1-(d/len(nodos[j]))
            elif len(nodos[j])<d:
                # print("now")
                p=0
            # print(p)
            if p <= random.random() and i!=j:
                matriz0[i,j]=1
                matriz0[j,i]=1
    # print(nodos)
    # print(matriz0)
    # crear aristas
    nodos=Arista.creara(n,matriz0,nodos)
    nodos=self.compconn(self,nodos,n)
    print(nodos)
    return nodos
  
  def modelodorogovt(self,n, dirigido=False):
    import random
    #crear nodos
    nodos = Nodo.crear(n)
    # print(nodos)
    
    # metodo
    matriz0=np.zeros([n,n])
    matriz0[0,1]=1
    matriz0[1,2]=1
    matriz0[2,0]=1
    
    for ni in range(3,n,1):
        aris=np.argwhere(matriz0==1)
        noaris=len(aris)
        arislct=random.randrange(noaris)
        arislct=aris[arislct]
        # print(arislct)
        matriz0[ni,arislct[0]]=1
        matriz0[ni,arislct[1]]=1
    # print(matriz0)
    # crear aristas
    nodos=Arista.creara(n,matriz0,nodos)
    nodos=self.compconn(self,nodos,n)
    print(nodos)
    return nodos
    
  def savegraph(self,nodos,nombre):
    header = "graph {\n"
    nodost = ""
    aristast =""
    cierre = "}"
    tmpi=[]
    for i in nodos:
        nodost += str("\t"+str(i)+"\n")
        if (len(nodos[i])>0):
            var=nodos[i]
            for j in var:
                tmpi.append([i,j])
    for i in tmpi:
        if (list(np.flip(i)) in tmpi):
            tmpi.remove(list(np.flip(i)))
    for i in tmpi:
        var=i
        aristast += "\t"+str(var[0])+" -- " + str(var[1]) + ";\n"
    
    savegf=header + nodost + aristast + cierre
    # print(savegf)
    
    # text_file = open("E:\sample.gv", "wt")
    text_file = open(nombre, "wt")
    text_file.write(savegf)
    text_file.close()
  
  def contarist(self,nodos,n):
    j=0
    longnod2={}
    while (j < n):
        longnod2[j]=0
        j+=1
    for i in nodos:
        longnod2[i]=longnod2[i]+len(nodos[i])
        for j in nodos:
            if len(nodos[j])>0:
                if (i in nodos[j])==True:
                    longnod2[i]=longnod2[i]+1
                else:
                    continue
            else:
                continue
    print(longnod2)
    return longnod2

  def cambarist(self,nodos,n):
    longnod2=self.contarist(self,nodos,n)
    for i in longnod2:
        xo=list(longnod2.items())
        x=np.array(xo)
        if longnod2[i]==0:
            maxnod=np.argmax(x[:,1])
            while (len(nodos[maxnod])==0):
                xo.remove(xo[maxnod])
                x=np.array(xo)
                maxnod=np.argmax(x[:,1])
            print(maxnod)
            print(nodos[maxnod])
            nodos[i]=[nodos[maxnod][0]]
            y=list(nodos[maxnod])
            y.remove(y[0])
            if len(nodos[maxnod])>0:
                nodos[maxnod]=y
            else:
                nodos[maxnod]=[]
        longnod2=self.contarist(self,nodos,n)
    # print(nodos)
    return nodos
  
  def compconn(self,nodos,n):
    longnod2=self.contarist(self,nodos,n)
    while (0 in np.array(list(longnod2.values()))) == True:
        print("unfortunately tru")
        nodos=self.cambarist(self,nodos,n)
        longnod2=self.contarist(self,nodos,n)
    return nodos
  
  def arreglarnodos(self,nodos):
    prenodos = {}
    for i in nodos:
        vec = []
        if len(nodos[i]) > 0:
            for k in nodos[i]:
                vec.append(k)
        for j in nodos:
            if (i in nodos[j]) == True and ((j in nodos[i]) == False):
                vec.append(j)
        prenodos[i] = vec
    # print(prenodos)
    return prenodos
  
  def BFS(self, nodos, s):
    nodos = self.arreglarnodos(self,nodos)
    n = len(nodos)
    ni = s
    Capas = {}
    Capas[0] = list(nodos[0])
    Discovered = dictio.crear(n,False)
    Tree = dictio.crear(n,[])
    
    Discovered[ni] = True
    cont=0
    
    while len(Capas[cont]) > 0:
        Capas[cont+1] = []
        vec=[]
        for i in Capas[cont]:
            for j in nodos[i]:
                if Discovered[j] == False:
                    Tree[i] = Tree[i] + [j]
                    Discovered[j] = True
                    vec.append(j)
        Capas[cont+1] = vec
        cont += 1
    return Tree
  
  def DFS_R(self, nodos, s):
    nodos = self.arreglarnodos(self,nodos)
    n = len(nodos)
    ni = s
    Discovered = dictio.crear(n,False)
    Tree = dictio.crear(n,[])
    
    def dfs(grafo,Dscovd,ni,Tree):
        Dscovd[ni]=True
        if len(grafo[ni]) > 0:
            for i in grafo[ni]:
                if Dscovd[i] == False:
                    Tree[ni] = Tree[ni]+[i]
                    Dscovd, Tree = dfs(grafo,Dscovd,i,Tree)
        return Dscovd, Tree
    discovered, Tree = dfs(nodos,Discovered,ni,Tree)
    return Tree

print("Elige que tu tipo de grafo")
print("mll para malla")
print("er para redosrenyi")
print("gil para gilbert")
print("geo para geografico")
print("bal para BarabasiAlbert")
print("dor para dorovovt")
dec = input()
grafo = Grafo.menuini(Grafo,dec)
# Grafo.savegraph(Grafo,grafo)

arbolBFS = Grafo.BFS(Grafo, grafo, 15)
# Grafo.savegraph(Grafo,arbolBFS,"E:\grafo2.gv")

arbolDFSr = Grafo.DFS_R(Grafo, grafo, 15)
# Grafo.savegraph(Grafo,arbolDFSr,"E:\grafo3.gv")