import numpy as np

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
            nodos[j]=0
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

class creararch:
    def __init__(self, nodos):
        print("  ")
    def getGraphivzText(nodos):
        header = "graph {\n"
        nodost = ""
        aristast =""
        cierre = "}"
        for i in nodos:
            nodost += str("\t"+str(i)+"\n")
            if len(nodos[i])>0:
                var=nodos[i]
                for j in var:
                    aristast += "\t"+str(i)+" -- " + str(j) + ";\n"
            else:
                continue
        return header + nodost + aristast + cierre

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

        print("Bienvenido a grafos! \n")
        print("Escogiste un grafo de ")

        if self.graphtpe == 'mll':
          print("modelo de malla\n")
          m=0; n=0
          while (m<=0 or n<=0):
            print("Nada de ceros")
            print("\n")
            m =  int(input("Define el numero de filas:  "))
            n =  int(input("Define el numero de columnas:   "))
          self.modelomalla(m,n)
        
        elif self.graphtpe == 'er':
          print("modelo de Erdös y Rényi\n")
          m=0; n=0
          while (m < n-1 or n<=0):
            print("Nada de ceros")
            print("\n")
            n =  int(input("Define el numero de nodos:  "))
            m =  int(input("Define el numero maximo de aristas que puede tener el grafo (>= n-1):   "))
          self.modeloerdosrenyi(n,m,dirigido=False, auto=False)
         
        elif self.graphtpe == 'gil':
          print("modelo de Gilbert\n")
          n=0;
          while (n<=0):
            print("Nada de ceros")
            print("\n")
            n =  int(input("Define el numero de nodos:  "))
            p =  float(input("Define la probabilidad de un nodo de formar arista(0, 1):   "))
          self.modelogilbert(n, p, dirigido=False, auto=False)
        elif self.graphtpe == 'geo':
          print("modelo geografico simple\n")
          n=0;
          while (n<=0):
            print("Nada de ceros")
            print("\n")
            n =  int(input("Define el numero de nodos:  "))
            r =  int(input("Define la distancia maxima para formar arista (<70):   "))
          self.modelogeo(n, r, dirigido=False, auto=False)
        elif self.graphtpe == 'bal':
          print("modelo variante de Barabási-Albert\n")
          n=0;d=1
          while (n<=0 and d<=1):
            print("Nada de ceros")
            print("\n")
            n =  int(input("Define el numero de nodos:  "))
            d =  int(input("Define el numero de aristas que pueden existir:   "))
          self.modeloBarabasiAlbert(n, d, dirigido=False, auto=False)
        elif self.graphtpe == 'dor':
          print("modelo de Dorogovtsev-Mendes\n")
          n=0
          while (n<=0):
            print("Nada de ceros")
            print("\n")
            n =  int(input("Define el numero de nodos:  "))
          self.modelodorogovt(n, dirigido=False)
        else:
          print("unrecognized :(")
    
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
            matriz0[i,j]=cont
            cont+=1
    # print(matriz0)
    for ni in nodos:
        temp=[]
        cordd=np.argwhere(matriz0==ni)[0][0],np.argwhere(matriz0==ni)[0][1]
        if cordd[0]+1 >= m and cordd[1]+1 >= n:
            continue
        elif cordd[0]+1 >= m:
            temp=matriz0[cordd[0],cordd[1]+1]
        elif cordd[1]+1 >= n:
            temp=matriz0[cordd[0]+1,cordd[1]]
        elif(cordd[0]+1 < m and cordd[1]+1 < n):
            temp=matriz0[cordd[0]+1,cordd[1]],matriz0[cordd[0],cordd[1]+1]
        # print(ni,cordd,temp)
        nodos[ni]=temp
    print(nodos)
    gf=creararch.getGraphivzText(nodos)
    print(gf)
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
    print(nodos)
    gf=creararch.getGraphivzText(nodos)
    print(gf)
  
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
    print(nodos)
    gf=creararch.getGraphivzText(nodos)
    print(gf)
  
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
    print(nodos)
    gf=creararch.getGraphivzText(nodos)
    print(gf)
  
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
    print(nodos)
    gf=creararch.getGraphivzText(nodos)
    print(gf)
  
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
    print(nodos)
    gf=creararch.getGraphivzText(nodos)
    print(gf)
    
    def getGraphivzText(self,nodos):
        header = "graph {\n"
        nodost = ""
        aristast =""
        cierre = "}"
        for i in nodos:
            nodost += str("\t"+str(i)+"\n")
            if len(nodos[i])>0:
                var=nodos[i]
                for j in var:
                    aristast += "\t"+str(i)+" -- " + str(j) + ";\n"
            else:
                continue
        var=header + nodost + aristast + cierre
        np.save('E:\Proyecto1\test.gv',var) 
        return var


print("Elige que tu tipo de grafo")
print("mll para malla")
print("er para redosrenyi")
print("gil para gilbert")
print("geo para geografico")
print("bal para BarabasiAlbert")
print("dor para dorovovt")
dec = input()
grafo = Grafo(dec)
