
INF = 922337203685

link=False
_time = 0

class Queue:

  def __init__(self):
    self.queue = []

    # Add an element
  def enqueue(self, item):
    self.queue.append(item)

    # Remove an element
  def dequeue(self):
    if len(self.queue) < 1:
      return None
    return self.queue.pop(0)

    # Display  the queue
  def display(self):
    for i in range(len(self.queue)):
      print("(s,d):",self.queue[i].source,self.queue[i].destination)

  def size(self):
    return len(self.queue)
q = Queue()

class packet():
 
  def __init__(self,source,destination,distance_table):
    self.source= source
    self.destination = destination
    self.distance_table = distance_table

class DVR():
  

  def __init__(self,node,direct_edge_costs):
    self.neignbourcnt = 0
    self.is_happen = []
    self.distance_table = {}
    self.next_hop = {}
    self.direct_edge_costs = direct_edge_costs
    self.A = node
   

  def send_dvr(self):
    global link
    print("send_dvr request recieved....")
    temp_dt = {}
    for i in range(4):
      
      if(i==self.A or self.direct_edge_costs[i]==INF):
       
        continue
      
      
      
      pkt = packet( self.A ,i,self.distance_table)
      print("packet to be delivered(S,D):",self.A,i)
      q.enqueue(pkt)
    
    
    

  def start(self):
    
    self.next_hop = self.direct_edge_costs.copy()
    for i in range(4):
      if(self.direct_edge_costs[i]!=INF):
        self.next_hop[i]=i
        temp_1 = {
          "mincost": 100000,
  
        }


        self.is_happen.append(temp_1)
      else:
        self.next_hop[i]=INF
        temp_1 = {
          "mincost": 100000,
  
        }


        self.is_happen.append(temp_1)        
    self.distance_table = self.direct_edge_costs.copy()
    self.send_dvr()
    print("Printing Distance Vector table....")
    print(self.distance_table)
    print()



      


  def update_table(self,packet):
    global _time
    is_table_updated = False
    _time+=1
    self.neignbourcnt+=1

    print("Update packet recieved... at time:",_time)
    print ("Destination:",packet.destination)
    print ("Source:",packet.source)
   
    
    print(packet)
    print()
    for i in range (4):
      if(self.next_hop[i]== packet.source):
       
        print("In new",i," ",packet.distance_table[i])
        temp = self.distance_table[i]
        
        if(self.is_happen[i]["mincost"]>packet.distance_table[i] +self.direct_edge_costs[packet.source]):
          self.is_happen[i]["mincost"] = packet.distance_table[i] +self.direct_edge_costs[packet.source]
        self.distance_table[i] = packet.distance_table[i] +self.direct_edge_costs[packet.source]
        print(self.distance_table[i])
        self.next_hop[i]=self.next_hop[packet.source]
        if(self.distance_table[i] != temp):
          is_table_updated=True
          print("yes")
      else:
        if(i==self.A):
          continue
        print("in old")
        print(packet.distance_table[i] +self.direct_edge_costs[packet.source])
        print(self.distance_table[i])
        print("//////////////")
        if(self.is_happen[i]["mincost"]>packet.distance_table[i] +self.direct_edge_costs[packet.source]):
          self.is_happen[i]["mincost"] = packet.distance_table[i] +self.direct_edge_costs[packet.source]
        if(self.distance_table[i] > packet.distance_table[i] +self.direct_edge_costs[packet.source]):
          print("enter2")
          self.distance_table[i] = packet.distance_table[i] +self.direct_edge_costs[packet.source]
          self.next_hop[i]=self.next_hop[packet.source]
          is_table_updated=True
    
    temp_3=0
    for i in range(4):
      if(self.direct_edge_costs[i]!=INF):
        temp_3+=1
    if(self.neignbourcnt==temp_3):
      self.neignbourcnt = 0
      for i in range(4):
        if(i!=self.A):
        
          if(self.is_happen[i]["mincost"]!=self.distance_table[i]):
            print(self.distance_table[i])
            print(self.is_happen[i]["mincost"])
            self.distance_table[i]=self.is_happen[i]["mincost"]
            is_table_updated=True
            print("NEv.........................................")
    for i in range(4):
      if(self.direct_edge_costs[i]!=INF):
        self.is_happen[i]["mincost"] = 100000

       



    
  

    if(is_table_updated==True):
      print("Updated distance table")
      print(self.distance_table)
      self.send_dvr()
    
  
  def link_changes(self,target_node):
    global link
    print("target_node:",target_node)

    self.direct_edge_costs[target_node] = INF
  
    self.send_dvr()
   

