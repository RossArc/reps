import numpy as np
import sys

class Nodo():
    """
    Clase nodos
    value, [] vector vacio
    value, False False
    """
    def _init_(self, n, value):
        print(" ")
    def crear(n, value):
        nodos = {}
        j = 0
        while (j < n):
            nodos[j] = value
            j += 1
        return nodos

class Arista():
    """
    Clase Aristas
    """
    def _init_(self, n):
        print(" ")
    def creara(n, matriz0, nodos):
        for i in range(n):
            temp = []
            for j in range(n):
                if matriz0[i,j] == 1:
                    temp.append(j)
            nodos[i] = temp
        return nodos

class Grafo():
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
    
    def menuini(self, tipo):
        print("Bienvenid@ a grafos! \n")
        print("Escogiste un grafo de ")
        
        if tipo == 'mll':
            print("modelo de malla\n")
            m = 0; n = 0
            while (m <= 0 or n <= 0):
                print("Nada de ceros!")
                print("\n")
                m =  int(input("Define el numero de filas:  "))
                n =  int(input("Define el numero de columnas:  "))
            nodos = self.modelomalla(self, m, n)
        
        elif tipo == 'er':
            print("modelo de Erdös y Rényi\n")
            m = 0; n = 0
            while (m < n-1 or n <= 0):
                print("Nada de ceros!")
                print("\n")
                n =  int(input("Define el numero de nodos:  "))
                m =  int(input("Define el numero maximo de aristas que puede tener el grafo (>= n-1):   "))
            nodos = self.modeloerdosrenyi(self, n, m, dirigido = False, auto = False)
        
        elif tipo == 'gil':
            print("modelo de Gilbert\n")
            n = 0;
            while (n <= 0):
                print("Nada de ceros")
                print("\n")
                n =  int(input("Define el numero de nodos:  "))
                p =  float(input("Define la probabilidad de un nodo de formar arista(0, 1):   "))
            nodos = self.modelogilbert(self, n, p, dirigido = False, auto = False)
        
        elif tipo == 'geo':
            print("modelo geografico simple\n")
            n = 0;
            while (n <= 0):
                print("Nada de ceros")
                print("\n")
                n =  int(input("Define el numero de nodos:  "))
                r =  int(input("Define la distancia maxima para formar arista (<70):   "))
            nodos = self.modelogeo(self, n, r, dirigido = False, auto = False)
        
        elif tipo == 'bal':
            print("modelo variante de Barabási-Albert\n")
            n = 0; d = 1
            while (n <= 0 and d <= 1):
                print("Nada de ceros")
                print("\n")
                n =  int(input("Define el numero de nodos:  "))
                d =  int(input("Define el numero de aristas que pueden existir:   "))
            nodos = self.modeloBarabasiAlbert(self, n, d, dirigido = False, auto = False)
        
        elif tipo == 'dor':
            print("modelo de Dorogovtsev-Mendes\n")
            n = 0
            while (n <= 0):
                print("Nada de ceros")
                print("\n")
                n =  int(input("Define el numero de nodos:  "))
            nodos = self.modelodorogovt(self, n, dirigido = False)
        
        else:
            print("unrecognized :(")
            sys.exit()
        self.n = n
        quessav = input("¿Salvamos el grafo? Presiona s para si, n para no")
        if quessav == 's' or quessav == 'S':
            self.savegraph(self,nodos,"E:\grafo.gv")
        else:
            print("Bye :)")
        return nodos
    
    def modelomalla(self,m,n):
        """
        m:  numero de filas
        n:  numero de columnas
        """
        #crear nodos
        nodos = Nodo.crear(m*n,[])
        # metodo
        matriz0=np.zeros([m,n])
        cont=0
        for i in range(m):
            for j in range(n):
                matriz0[i,j]=int(cont)
                cont+=1
        
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
            nodos[ni]=list(temp)
        print(nodos)
        return nodos
    
    def modeloerdosrenyi(self,n,m,dirigido=False, auto=False):
        """
        crear nodos
        n: numero de nodos
        m: numero maximo de aristas que puede tener un nodo (>= n-1)   
        """
        nodos = Nodo.crear(m,[])
        # metodo
        from random import randrange
        i=0
        while i<m:
            noari=randrange(0,n)
            noari2=randrange(0,n)
            while ((noari == noari2) or ((noari2 in nodos[noari]) == True)):
                noari2 = randrange(0,n)
            nodos[noari] = nodos[noari] + [noari2]
            i+=1
        # print(nodos)
        # nodos=self.compconn(self,nodos,n)
        # print(nodos)
        return nodos
    
    def modelogilbert(self,n, p, dirigido=False, auto=False):
        """
        # n=8     #numero de nodos
        # m=10    #numero maximo de aristas que puede tener un nodo (>= n-1)
        # p=0.1   #probabilidad de formar arista
        """
        m = n
        #crear nodos
        nodos = Nodo.crear(m,[])
        # metodo
        from random import uniform
        i=0
        while i < m:
            for ni in range(n):
                for nj in range(n):
                    probi = uniform(0,1)
                    if probi <= p:
                        nodos[ni] = nodos[ni] + [nj]
                        i+=1
                    else:
                        i=i
        # nodos=Arista.creara(n,matriz0,nodos)
        # nodos=self.compconn(self,nodos,n)
        # print(nodos)
        return nodos
    
    def modelogeo(self,n, r, dirigido=False, auto=False):
        import random
        """
        # n=8     #numero de nodos
        # m=10    #numero maximo de aristas que puede tener un nodo (>= n-1)
        # r=20   #distancia maximapara formar arista
        """
        rect=[70,80]
        coordennodos={}
        nodos = Nodo.crear(n,[])
        coordennodos = Nodo.crear(n,[])
        for ci in coordennodos:
            coordi=[random.randrange(rect[0]), random.randrange(rect[1])]
            coordennodos[ci]=coordi
        
        # metodo
        for ci in coordennodos:
            coordi = coordennodos[ci]
            for cj in coordennodos:
                if cj != ci:
                    coordi2 = coordennodos[cj]
                else:
                    continue
                rminys = np.sqrt(np.abs(float(np.dot((coordi2[0]-coordi[0]),(coordi2[1]-coordi[1])))))
                if  rminys <= r:
                    nodos[ci] = nodos[ci] +[cj]
        # crear aristas
        # nodos=Arista.creara(n,matriz0,nodos)
        # nodos=self.compconn(self,nodos,n)
        # print(nodos)
        return nodos
    
    def modeloBarabasiAlbert(self,n, d, dirigido=False, auto=False):
        from random import choice, random
        """
        # n=10      #numero de nodos
        # d=1     #numero de aristas a las que se puede conectar cada nodo.
        # pmax=0.5
        """
        nodos={}
        # metodo
        for i in range(0,n,1):
            nodos[i]=[]
            x = [x for x in range(len(nodos)-1)]
            for _ in range(len(x)):
                j = choice(x)
                nn = len(nodos[j])
                p=1-(nn/d)
                if (random() < p) and j != i:
                    nodos[j] = nodos[j] + list([i])
                    x.remove(j)
        print(nodos)
        # crear aristas
        # nodos=Arista.creara(n,matriz0,nodos)
        # nodos=self.compconn(self,nodos,n)
        # print(nodos)
        return nodos
    
    def modelodorogovt(self, n, dirigido=False):
        import random
        
        #crear nodos
        nodos = Nodo.crear(n,[])
        # print(nodos)
        
        # metodo
        from random import choice
        nodos[0] = [1]
        nodos[1] = [2]
        nodos[2] = [0]
        usados = []
        usados.append(list([0,1]))
        usados.append(list([1,2]))
        usados.append(list([2,0]))
        
        for ni in range(3,n,1):
            arislct = choice(usados)
            
            nodos[ni] = nodos[ni] + list([arislct[0]])
            nodos[ni] = nodos[ni] + list([arislct[1]])
            usados.append(list([ni,arislct[0]]))
            usados.append(list([ni,arislct[1]]))
        # crear aristas
        # nodos=Arista.creara(n,matriz0,nodos)
        # nodos=self.compconn(self,nodos,n)
        # print(nodos)
        return nodos
    
    def savegraph(self,savegf,nombre):
        # text_file = open("E:\sample.gv", "wt")
        text_file = open(nombre, "wt")
        text_file.write(savegf)
        text_file.close()
        
    def textfil(self,nodos):
        header = "graph {\n"
        nodost = ""
        aristast =""
        cierre = "}"
        tmpi=[]
        for i in nodos:
            nodost += str("\t"+str(i)+"\n")
            if (len(nodos[i])>0):
                var = nodos[i]
                for j in var:
                    tmpi.append([i,j])
        for i in tmpi:
            if (list(np.flip(i)) in tmpi):
                tmpi.remove(list(np.flip(i)))
        for i in tmpi:
            var = i
            aristast += "\t"+str(var[0])+" -- " + str(var[1]) + ";\n"
        
        savegf = header + nodost + aristast + + cierre
        return savegf
    
    def textfilpesos(self,nodos,camino):
        header = "graph {\n"
        nodost = ""
        aristast =""
        cierre = "}"
        tmpi=[]
        for i in nodos:
            nodost += str("\t"+str(i)+"\n")
        for i in camino:
            if (len(i)>0):
                var = i[0]
                var2 = i[1]
                # for j in range(len(var)):
                tmpi.append([var[0],var[1],var2])
        for i in tmpi:
            if (list(np.flip(i)) in tmpi):
                tmpi.remove(list(np.flip(i)))
        for i in tmpi:
            var=i
            aristast += "\t"+str(var[0])+" -- " + str(var[1]) + "[weight=" + str(var[2]) +"];\n"
        
        savegf = header + nodost + aristast + cierre
        return savegf
    
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
        """
        Te regresa un arbol inducido por Breadth First Search
        a partir de un nodo s
        """
        nodos = self.arreglarnodos(self,nodos)
        n = len(nodos)
        ni = s
        Capas = {}
        Capas[0] = list(nodos[0])
        Discovered = Nodo.crear(n, False)
        Tree = Nodo.crear(n,[])
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
        """
        Te regresa un arbol inducido por Depth First Search
        a partir de un nodo s
        Funcion recursiva
        """
        nodos = self.arreglarnodos(self,nodos)
        n = len(nodos)
        ni = s
        Discovered = Nodo.crear(n, False)
        Tree = Nodo.crear(n,[])
        
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
    
    def pesospagrafo(self, nodos):
        import random
        n = len(nodos)
        pesos = Nodo.crear(n,[])
        for i in nodos:
            long = len(nodos[i])
            pesos[i] = random.sample([i for i in range(500)], k=long)
            # pesos[i] = random.choices([i for i in range(500)], k=long)
        return pesos
    
    def sortbyweight(self,nodes,weights):
        """
        nodes temp
        weights temp2
        """
        a = np.argsort(weights)
        temp = []
        temp2 = []
        for i in a:
            temp.append(nodes[i])
            temp2.append(weights[i])
        return temp,temp2
    
    def arreglarnodoswweight(self,nodos,pesos):
        prenodos = {}
        prepesos = {}
        for i in nodos:
            vec = []
            vec2 = []
            if len(nodos[i]) > 0:
                for k in range(len(nodos[i])):
                    vec.append(nodos[i][k])
                    vec2.append(pesos[i][k])
            for j in nodos:
                if ((i in nodos[j]) == True) and ((j in nodos[i]) == False):
                    vec.append(j)
                    vec2.append(pesos[j][np.argwhere(np.array(nodos[j])== i)[0][0]])
            prenodos[i] = vec
            prepesos[i] = vec2
        return prenodos, prepesos
    
    def creararbol(self, S, nodos, pesos):
        """
        Esta funcion crea un arbol a partir de un camino dado
        """
        costo = 0
        camino = []
        for i in range(len(S)-1):
            if (S[i+1] in nodos[S[i]]) == True:
                costo = costo + pesos[S[i]][np.argwhere(np.array(nodos[S[i]]) == S[i+1])[0][0]]
                camino.append([[S[i],S[i+1]],costo])
            elif (S[i+1] not in nodos[S[i]]) == True:
                temp = S[0:i+1]
                pesoactual = np.inf
                d = nodos[S[i+1]]
                p = pesos[S[i+1]]
                for j in range(len(temp)-1,0,-1):
                    x = temp[j]
                    if (x in d) == True:
                        posactual = np.argwhere(np.array(d) == x)[0][0]
                        if p[posactual] < pesoactual:
                            pesoactual = p[posactual]
                            posiactu = posactual
                        else:
                            pesoactual = pesoactual
                            posiactu = posiactu
                costo = costo + pesos[d[posiactu]][np.argwhere(np.array(nodos[d[posiactu]]) == S[i+1])[0][0]]
                camino.append([[d[posiactu],S[i+1]],costo])
            return camino
    
    def ordinaris(self, nodos,n,pesos):
        ordenaris = []
        for i in nodos:
            for j in range(len(nodos[i])):
                ordenaris.append(list([i,nodos[i][j],pesos[i][j]]))
        ordenaris = np.array(ordenaris)
        ordenaris2 = ordenaris[np.argsort(ordenaris[:,2])]
        ordenaris2=np.flip(ordenaris2,0)
        return ordenaris2
    
    def djkstra(self, s, grafo):
        nodos = grafo
        q = []
        n = len(nodos)
        S = []
        prioq = Nodo.crear(n, np.inf)
        
        prioq[s] = 0
        q.append(s)
        pesos = Grafo.pesospagrafo(self, nodos)
        ordenaris2 = Grafo.ordinaris(self, nodos,n,pesos)
        while len(q) > 0:
            u = q[0]
            S.append(u)
            temp = ordenaris2[np.argwhere(ordenaris2[:,0] == u)[:,0]]
            for i in temp:
                cn = i[1]
                if (cn in S) == False:
                    if (prioq[cn] > i[2]):
                        if (cn in q) == False:
                            q.insert(0,cn)
                            prioq[cn] = i[2]
                        elif (cn in q) == True:
                            q.remove(cn)
                            q.insert(0,cn)
            q.remove(u)
        return S, pesos
    
    def arboldjsktra(self,s,grafo):
        S, pesos = self.djkstra(self, s, grafo)
        camino = self.creararbol(self, S, grafo, pesos)
        arboldjkstra = self.textfilpesos(self, grafo, camino)
        header = "graph {\n"
        nodost = ""
        aristast =""
        cierre = "}"
        tmpi=[]
        nodos = grafo
        n=len(grafo)
        cosssss = Nodo.crear(n, 0)
        
        for i in camino:
            if (len(i)>0):
                var = i[0]
                var2 = i[1]
                # for j in range(len(var)):
                tmpi.append([var[0],var[1],var2])
                cosssss[var[1]]=var2
        for i in tmpi:
            if (list(np.flip(i)) in tmpi):
                tmpi.remove(list(np.flip(i)))
        
        for i in nodos:
            if i == s:
                cos = 0
            else:
                cos =cosssss[i]
            nodost += str("\t"+str(i)+"  [label=nodo_"+str(i)+"("+ str(cos)+")]\n")
        
        for i in tmpi:
            var=i
            aristast += "\t"+str(var[0])+" -- " + str(var[1]) + "[weight=" + str(var[2]) +"];\n"
        
        savegf = header + nodost + aristast + cierre
        
        print(savegf)
        text_file = open("E:\grafof.gv", "wt")
        # text_file = open("arboldij", "wt")
        text_file.write(savegf)
        text_file.close()
        return arboldjkstra


# dec = input()
grafo = Grafo.menuini(Grafo,'mll')
Grafo.savegraph(Grafo,grafo)

s = 5 #que sea aleatorio?
arboldjst = Grafo.arboldjsktra(Grafo, s, grafo)
print(arboldjst)
print("archivo del arbol guardado automaticamente")