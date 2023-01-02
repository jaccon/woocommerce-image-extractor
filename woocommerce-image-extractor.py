import csv
import os
import re

downloadPath = "./downloads"
dataFile = "data.csv"

with open('data.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)

    for row in reader:
        imagePath = row[29]
        arr = re.split(',', imagePath)
        
        for x in range(len(arr)):
          filename = arr[x]
          print(filename)
          command = "wget -nd -H -p -A jpg,jpeg,png,gif -e robots=off -x --force-directories " + filename + " -P " + downloadPath
          os.system(command)
                
        

