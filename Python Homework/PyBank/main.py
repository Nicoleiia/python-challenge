import csv 
import os

#csv file
with open("Resources/budget_data.csv") as file:
    #print(file.read())
  
    reader = csv.reader(file)
    header = next(reader)
    
    total_months = 0
    net_total_losses = 0
    
    #read header row
    for row in reader: 
        print(row)
        total_months = total_months + 1
        
        net_total_losses = net_total_losses + int(row[1])
        
    print(total_months)
    print(net_total_losses)
    
    
    
    
        
   
    

    

    


 