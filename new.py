class Logic(object):
  def _init_(self):
        
        self.l0 = [1, 35, 36]
        self.l1 = [0, 8, 2]
        self.l2 = [1, 6, 3]
        self.l3 = [4, 5, 2]
        self.l4 = [3, 5]
        self.l5 = [3, 4, 6, 12]
        self.l6 = [2, 5, 7, 11]
        self.l7 = [6, 8, 10]
        self.l8 = [1, 7, 9]
        self.l9 = [8, 18, 30, 31, 34]
        self.l10 = [7, 9, 11]
        self.l11 = [6, 10, 12, 17]
        self.l12 = [5, 11, 13]
        self.l13 = [12, 14]
        self.l14 = [13, 15, 17]
        self.l15 = [14, 16]
        self.l16 = [15, 17, 18]
        self.l17 = [11, 14, 16]
        self.l18 = [9, 11, 16, 19]
        self.l19 = [18, 20]
        self.l20 = [19, 21, 22, 30]
        self.l21 = [20]
        self.l22 = [20, 23]
        self.l23 = [22, 24]
        self.l24 = [23, 25]
        self.l25 = [24, 26, 29]
        self.l26 = [25, 27, 28]
        self.l27 = [26, 28, 33]
        self.l28 = [26, 27, 29, 33]
        self.l29 = [25, 28, 30, 33]
        self.l30 = [20, 29, 31]
        self.l31 = [9, 29, 30, 35]
        self.l32 = [29, 33, 35]
        self.l33 = [27, 28, 32]
        self.l34 = [9, 35]
        self.l35 = [31, 32, 34, 36]
        self.l36 = [0, 35]
        
        #Neighbour's Graph  Ends
        
        self.adjList = [self.l0, self.l1, self.l2, self.l3, self.l4, self.l5,
                        self.l6, self.l7, self.l8, self.l9, self.l10, self.l11,
                        self.l12, self.l13, self.l14, self.l15, self.l16, self.l17,
                        self.l18, self.l19, self.l20, self.l21, self.l22, self.l23,
                        self.l24, self.l25, self.l26, self.l27, self.l28, self.l29,
                        self.l30, self.l31, self.l32, self.l33, self.l34, self.l35, 
                        self.l36]
         
        self.pos[2]={}
        self.priority[36] = {0}

    #Neighbours List  

    # Neighbour's Graph  Ends


    #Adjacency List for all Nodes


    #Function for Updatinig The Priority Layer Wise:
  def updatePriority(self):
        self.priority[36] = 0

        for i in range(0, 2):
            self.layering(self.pos[i])


  def layering(self, val):
        readyQueue = queue()
        readyQueue.push(val)
        visited = [False, False, False, False, False, False, False, False,
                   False, False, False, False, False, False, False, False, 
                   False, False, False, False, False, False, False, False, 
                   False, False, False, False, False, False, False, False,
                   False, False, False, False, False]
        visited[val] = True
        p[36] = 0
        while not readyQueue.empty():
            current = readyQueue.front()
            readyQueue.pop()
            print(current, end = '')
            print("\n", end = '')
            for x in self.adjList[current]:
                if not visited[x]:

                    readyQueue.push(x)
                    visited[x] = True
                    p[x] = p[current] + 1
                    print(x, end = '')
                    print(" ", end = '')
                    print(p[x], end = '')
                    print("\n", end = '')

        print("*********", end = '')
        print("\n", end = '')
        for i in range(0, 36):
            self.priority[i] += p[i]
        #        for(int i=0;i<10;i++)
        #      {
        #          cout<<i<<" - "<<priority[i]<<endl
        #      }
  def print(self):
        for i in range(0, 36):
            print(i, end = '')
            print(" - ", end = '')
            print(self.priority[i], end = '')
            print("\n", end = '')
        self.findMax()
  def findMax(self):
        max = 0
        m = 0
        for i in range(0, 36):
            if self.priority[i] > max:
                max = self.priority[i]
                m = i
        print(m, end = '')
        print(":", end = '')
        print(max, end = '')
        print("\n", end = '')
        
  def AssignPos(self):
    p1,p2,p3
    max = 36
    while True:
      p1 = randint()%max
      p2 = randint()%max
      p3 = randint()%max
      if p1 == p2 or p2 == p3 or p3 == p1:
        continue
      else:
        pos[0]=p1
        pos[1]=p2
        Xpos = p3
        break

    print("The  Position of police(1) is-::", end = '')
    print(pos[0], end = '')
    print("\n", end = '')
    print("The  Position of police(2) is-::", end = '')
    print(pos[1], end = '')
    print("\n", end = '')
    print("The  Position of Mr. X is-::", end = '')
    print(Xpos, end = '')
    print("\n", end = '')
    #Now After assigning it for the first time 

  def UpdatePolicePos(self):
        
    # int nxtNeighbours[]
    #police (1&2)

        for i in range(0, 2):
            choice = adjList[pos[i]][rand()%adjList[pos[i]].size()]
        # cout<<"The choice is ::"<<choice
            pos[i]=choice


  def PoliceCaughtmrX(self):
    #if x has been caught ?

        for i in range(0, 2):
            if pos[i]==Xpos:
                return True
        return False



  def updateXpos(self):
    #updates the pos of Mr. X
        max = 0
        maxPos = 0
        for x in adjList[Xpos]:
            if priority[x]> max:
                max = priority[x]
                maxPos = x
        Xpos=maxPos


  def printPos(self):
    # prints the updated postion
        print("The Updated Position of police(1) is-::", end = '')
        print(pos[0], end = '')
        print("\n", end = '')
        print("The Updated Position of police(2) is-::", end = '')
        print(pos[1], end = '')
        print("\n", end = '')
        print("The Updated Position of Mr. X is-:::", end = '')
        print(Xpos, end = '')
        print("\n", end = '')


  def GameLoop(self):
        AssignPos()
        while not PoliceCaughtmrX():
            updatePriority()
            updateXpos()
            UpdatePolicePos()
            printPos()






  def main():
        one = Logic()
        one.GameLoop()