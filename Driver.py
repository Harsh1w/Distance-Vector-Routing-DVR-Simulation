from Node import *
import Node


def Start_DVR():

  A = DVR(0,{0:0,1:1,2:INF,3:INF})
  B = DVR(1,{0:1,1:0,2:1,3:INF})
  C = DVR(2,{0:INF,1:1,2:0,3:1})
  D = DVR(3,{0:INF,1:INF,2:1,3:0})
  
  
  A.start()
  B.start()
  C.start()
  D.start()

  
  while(1):

      
    if(q.size() == 0):
      print("No packets DVR halts...")
      print("final distance tables....")
      print("Distance table at 0:",A.distance_table)
      print("Distance table at 1:",B.distance_table)
      print("Distance table at 2:",C.distance_table)
      print("Distance table at 3:",D.distance_table)
      print("fineshed at time:",Node._time)

      print("final next_hop tables....")
      print("Distance table at 0:",A.next_hop)
      print("Distance table at 1:",B.next_hop)
      print("Distance table at 2:",C.next_hop)
      print("Distance table at 3:",D.next_hop)

      # if(Node._time==17):
      #   B.link_changes(0)
      #   A.link_changes(1)
      #   continue

     
      exit()
      
     
    else:
      print("Pending Packets status...")
      q.display()
      print("In else!!! and qsize:",q.size())
      event = q.dequeue()
      print("test:",event.destination)
      if(event.destination == 0 ):
        print("In 0")
        A.update_table(event)
      elif(event.destination == 1):
        print("In 1")
        B.update_table(event)
      elif(event.destination == 2 ):
        print("In 2")
        C.update_table(event)
      elif(event.destination == 3 ):
        print("In 3")
        D.update_table(event)
  
    print("Popped event...and qsize:",q.size(),)
    print ("Destination:",event.destination)
    print ("Source:",event.source)
    print("Pending Packets status...")
    q.display()
  
    
    # for i in range (q.size()):
      
    #   print("At (s,d)",i,q.display()[i])
    


Start_DVR()
  
