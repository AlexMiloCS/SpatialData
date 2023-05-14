"AM 3045 ONOMA: ALEXANDROS MILONAKIS"

class my_grid:

    def __init__(self,road_list,csv_manager,number_of_rows):
        self.road_list =road_list
        self.csv_manager = csv_manager
        self.minX = csv_manager.getMinX()
        self.minY = csv_manager.getMinY()
        self.maxX = csv_manager.getMaxX()
        self.maxY = csv_manager.getMaxY()
        self.cell_width = (self.maxX - self.minX) / number_of_rows
        self.cell_height = (self.maxY - self.minY) / number_of_rows
        self.grid_map = {}
        self.number_of_rows =number_of_rows
        for y_coord in range(number_of_rows):
            for x_coord in range(number_of_rows):
                coord = '({},{})'.format(y_coord,x_coord)
                self.grid_map[coord] = []

    def split_minXY_maxXY(self,minXY_maxXY):
        min_values = minXY_maxXY[0].split()
        max_values = minXY_maxXY[1].split()
        minX = float(min_values[0])
        minY = float(min_values[1])
        maxX = float(max_values[0])
        maxY = float(max_values[1])
        minmax_values = [minX,minY,maxX,maxY]
        return minmax_values
    
    
    def find_vertice_cell(self,x,y):
        row = int((y - self.minY) // self.cell_height)
        col = int((x - self.minX) // self.cell_width)
        if(col == self.number_of_rows):
            col -=1
        if(row == self.number_of_rows):
            row -=1
        cell_value = [row,col]
        return cell_value

    def find_MBR_cells(self, elem_minXY_maxXY, index):
        bottom_left = self.find_vertice_cell( elem_minXY_maxXY[0], elem_minXY_maxXY[1])
        top_right = self.find_vertice_cell( elem_minXY_maxXY[2], elem_minXY_maxXY[3])
        for row in range(bottom_left[1],top_right[1]+1):
            for col in range(bottom_left[0],top_right[0]+1):
                map_key =  '({},{})'.format(row,col)
                self.grid_map[map_key].append(index)      
   
        

    def create_grid(self):

        for row in range(len(self.road_list[0])):
            self.find_MBR_cells(self.split_minXY_maxXY(self.road_list[1][row]),self.road_list[0][row])
        
        with open('C:\\Users\\Alekos\\Desktop\\projects\\Diaxeirisi\\assignment2\\grid.grd', 'w') as f:
            for key in self.grid_map:
                value = self.grid_map[key]
                if len(value)>0:
                    for element in range(len(value)):
                        x =value[element]
                        identifier =self.road_list[0][x-1]
                        mbr_str = ' '.join(map(str, self.road_list[1][x-1]))
                        vertex_str = ','.join([''.join(map(str, vertex)) for vertex in self.road_list[2][x-1]])
                        f.write('{},{},{}\n'.format(identifier,mbr_str,vertex_str))

        with open('C:\\Users\\Alekos\\Desktop\\projects\\Diaxeirisi\\assignment2\\grid.dir', 'w') as f:

            f.write('{} {} {} {}'.format(self.minX,self.maxX, self.minY,self.maxY ))
            for key in self.grid_map:
                elements = len(self.grid_map[key])
                x_coord=(key[1])
                y_coord=(key[3])
                f.write('\n{} {} {}'.format(x_coord,y_coord,elements))
    
    def get_number_of_rows(self):
        return self.number_of_rows
    