#!/user/bin/env python3
"""mapper4.ipynb"""

import sys
for line in sys.stdin:
    line = line.strip() 
    num = line.split(",")
    
    EmployeeID=""
    Name = "-"
    Salary = "-"
    Country = "-"
    Passcode = "-"

    if len(num) == 2:
        EmployeeID=num[0]
        Name=num[1]
  
    elif len(num) == 4:
        continue

    elif len(num) == 5:
        EmployeeID= num[0]
        Salary = num[1]+num[2]
        Country=num[3]
        Passcode=num[4]
       
    else:
        EmployeeID= num[0]
        Salary = num[1]+num[2]
        Country=num[3]+', '+num[4]
        Passcode=num[5]
 
    print(EmployeeID,Name,Salary,Country,Passcode,sep="\t")
