#!/user/bin/env python3
"""reducer4.ipynb"""

import sys
import string

dict1 = {}
dict2 = {}


for line in sys.stdin:
    line = line.strip() #remove the blank spaces
    EmployeeID,Name,Salary,Country,Passcode = line.split('\t')

    if Salary == "-":
        dict1[EmployeeID] = Name
    else:
        dict2[EmployeeID] = [Salary,Country,Passcode]

for val1 in dict1.keys():
    EmployeeID=val1
    for val2 in dict2.keys():
        if val1==val2:
            Name=dict1[val1]
            Salary=dict2[val2][0]
            Country=dict2[val2][1]
            Passcode=dict2[val2][2]
            print(EmployeeID,Name,Salary,Country,Passcode,sep="\t")
