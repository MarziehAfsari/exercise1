
# Finding distance which vehicle path

from optparse import Values
import math
from numpy import array, reshape
from tabulate import tabulate
import numpy as np
#Read Data from file : AlgorithmStatusNew.JSON
import json

# Opening JSON file
mainFile = open('AlgorithStatusNew.json')
VehicleIDlist=[]
NumofBlocklist=[]
disofVehList=[]
# returns JSON object as a dictionary
data = json.loads(mainFile.read())
vehiclePath=data['vehiclesPath']
for path in vehiclePath.values():
  pathOfBlocks=path['path']  
  VehicleID=int(path['vehicleId'])
  
  if pathOfBlocks!=[[]]:
    VehicleIDlist.append(VehicleID)
    numOfBlock=0  
    disofVeh=0
    for block in pathOfBlocks:
      #empty block
      numOfBlock+=1    
      for k in block:
         dis=0
         j=1
         while j< len(k):
          lat1=k[j-1]["Latitude"]/(180/math.pi)
          lat2=k[j]["Latitude"]/(180/math.pi)
          long1=k[j-1]["Longitude"]/(180/math.pi)
          long2=k[j]["Longitude"]/(180/math.pi)
          dlon = long2 - long1
          dlat = lat2 - lat1
          a = (math.sin(dlat/2))**2 + math.cos(lat1) * math.cos(lat2) * (math.sin(dlon/2))**2
          c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
          dis += 6378.8 * c
          j+=1
         disofVeh+=dis
    NumofBlocklist.append(numOfBlock)
    disofVehList.append(disofVeh)

##### tables
# Headers=["Id vehicle","Number of Block","Distance"]
Data=(VehicleIDlist,NumofBlocklist,disofVehList)
print("Rows: Id vehicle & ","Number of Block & ","Distance")
print(tabulate(Data, tablefmt="grid"))


