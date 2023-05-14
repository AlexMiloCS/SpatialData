"AM 3045 ONOMA: ALEXANDROS MILONAKIS"

from manage_files import manage_files

class selection_queries:

    def __init__(self,number_of_rows):
        self.minX =float('inf')
        self.minY=float('inf')
        self.maxX=float('-inf')
        self.maxY=float('-inf')
        self.cell_width = 0
        self.cell_height = 0
        self.file_manager = manage_files()
        self.grid_map = {}
        self.number_of_rows = number_of_rows
        for row in range(number_of_rows):
            for col in range(number_of_rows):
                coord = '({},{})'.format(row,col)
                self.grid_map[coord] = []

    def find_vertice_cell(self,x,y):
        row = int((y - self.minY) // self.cell_height)
        col = int((x - self.minX) // self.cell_width)
        if(col == self.number_of_rows):
            col -=1
        if(row == self.number_of_rows):
            row -=1
        cell_value = [col,row]
        return cell_value
    
    def create_structure(self,my_grid,my_grid_dir):
        flag = False
        counter=0
        for line in my_grid_dir:
            if not flag:
                flag = True
                self.minX,self.maxX,self.minY,self.maxY = self.file_manager.split_line(line)
                self.cell_width = (self.maxX - self.minX) / self.number_of_rows
                self.cell_height = (self.maxY - self.minY) / self.number_of_rows
                continue
            y,x,elements = line.split()
            key = '({},{})'.format(y,x)
            if int(elements)==0:
                continue
            for i in range(int(elements)):
                self.grid_map[key].append(my_grid[counter])
                counter += 1

    def check_window_intersection(self,wx_min , wy_min, wx_max, wy_max, mbrx_min ,mbry_min , mbrx_max , mbry_max):
        if wx_max < mbrx_min or wx_min > mbrx_max:
            return False
        if wy_max < mbry_min or wy_min > mbry_max:
            return False
        return True
    
    def find_refernce_point(self,mbrX,mbrY,windowX,windowY):
        if mbrX>windowX:
            x = mbrX
        else:
            x = windowX
        if mbrY>windowY:
            y= mbrY
        else:
            y=windowY
        return x,y
    
    def point_in_window(self,ref_x,ref_y,row,col):
        cell_value = self.find_vertice_cell(ref_x,ref_y)
        if cell_value[0]==row:
            if cell_value[1]==col:
                return True
        return False
    
    def check_intersection(self,x1,y1,x2,y2,point3,point4):
        x3,y3 = point3.split()
        x4,y4 = point4.split()
        x3 = float(x3)
        y3 = float(y3)
        x4 = float(x4)
        y4 = float(y4)
        t=-1
        u=-1
        if (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)!=0:
            t = ((x1-x3)*(y3-y4)-(y1-y3)*(x3-x4))/((x1-x2)*(y3-y4)-(y1-y2)*(x3-x4))
        if (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4) !=0:
            u = ((x1-x3)*(y1-y2)-(y1-y3)*(x1-x2))/((x1-x2)*(y3-y4)-(y1-y2)*(x3-x4))
        if t>=0 and t<=1 and u>=0 and u<=1:
            return True
        return False 
    
    def line_points_interesction(self,wx_min , wx_max, wy_min,  wy_max,linestring):
        prev_point =linestring[0]
        for point in linestring:
            if point == linestring[0]:
                continue
            if self.check_intersection(wx_min,wy_min,wx_min,wy_max,prev_point,point):
                return True
            if self.check_intersection(wx_min,wy_min,wx_max,wy_min,prev_point,point):
                return True
            if self.check_intersection(wx_max,wy_max,wx_min,wy_max,prev_point,point):
                return True
            if self.check_intersection(wx_max,wy_max,wx_max,wy_min,prev_point,point):
                return True
            prev_point = point
        return False 

    def refinement_step(self,wx_min , wx_max, wy_min,  wy_max,mbrminmax,linestring):
        mbrminX,mbrminY,mbrmaxX,mbrmaxY = self.file_manager.split_line(mbrminmax)
        if wx_min< mbrminX and  wx_max > mbrmaxX:
            return True
        if wy_min < mbrminY and wy_max > mbrmaxY:
            return True
        if self.line_points_interesction(wx_min , wx_max, wy_min,  wy_max,linestring):
            return True
        return False
    

    def selection_query(self, wx_min , wx_max, wy_min,  wy_max):
        bottom_left =  self.find_vertice_cell(wx_min, wy_min)
        top_right = self.find_vertice_cell(wx_max, wy_max)
        identifiers =[]
        refined_identifiers = []
        cells = 0
        for row in range(bottom_left[0],top_right[0]+1):
            for col in range(bottom_left[1],top_right[1]+1):
                coord =  '({},{})'.format(row, col)
                elements = self.grid_map.get(coord)
                if len(elements)==0:                  
                    continue 
                cells += 1               
                for element in elements:
                    mbrminX,mbrminY,mbrmaxX,mbrmaxY = self.file_manager.split_line(element[1])
                    if not self.check_window_intersection(wx_min , wy_min, wx_max, wy_max,mbrminX,mbrminY,mbrmaxX,mbrmaxY):
                            continue
                    ref_x,ref_y =self.find_refernce_point(mbrminX,mbrminY,mbrmaxX,mbrmaxY)
                    if self.point_in_window(ref_x,ref_y,row,col):
                        if self.refinement_step(wx_min , wx_max, wy_min, wy_max,element[1],element[2]):
                            refined_identifiers.append(element[0])
                        identifiers.append(element[0])
        return identifiers,refined_identifiers,cells
    
    