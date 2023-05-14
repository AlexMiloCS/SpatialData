"AM 3045 ONOMA: ALEXANDROS MILONAKIS"

import csv

class csv_manager:  

    def __init__(self, csv_path):
        self.csv_path= csv_path
        self.minX =float('inf')
        self.minY=float('inf')
        self.maxX=float('-inf')
        self.maxY=float('-inf')

    def find_line_minmax(self,row):
        minX =float('inf')
        minY=float('inf')
        maxX=float('-inf')
        maxY=float('-inf')
        for column in row:
            values = column.split()
            x = float(values[0])
            y = float(values[1])
            if(minX > x):
                minX=x
                if(x<self.minX):
                    self.minX=x
            if(minY > y):
                minY=y
                if(y<self.minY):
                    self.minY=y
            if(maxX < x):
                maxX=x
                if(x>self.maxX):
                    self.maxX=x
            if(maxY < y):
                maxY=y
                if(y>self.maxY):
                    self.maxY=y
        s1 = '{} {}'.format(minX, minY)
        s2 = '{} {}'.format(maxX, maxY)
        s3 = [s1,s2]
        return s3
    
    def create_mylist(self):
        road_list = [[] for i in range(3)]

        with open(self.csv_path) as csvfile:
            reader = csv.reader(csvfile)
            identifier = 1
            for row in reader:
                if len(row) > 1:
                    road_list[0].append(identifier)
                    road_list[1].append(self.find_line_minmax(row))
                    road_list[2].append(row)
                    identifier+=1
        return road_list    

    def getMinX(self):
        return self.minX

    def getMinY(self):
        return self.minY
    
    def getMaxX(self):
        return self.maxX
    
    def getMaxY(self):
        return self.maxY