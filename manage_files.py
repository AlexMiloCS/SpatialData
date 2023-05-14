"AM 3045 ONOMA: ALEXANDROS MILONAKIS"

class manage_files:
    def read_file_and_split(self,file_name):
        with open(file_name, 'r') as f:
            contents = f.read()
            lines = contents.splitlines()
            return lines

    def read_grd_file(self,file_name):
        with open(file_name) as f:
            my_list = []
            for line in f:
                fields = line.strip().split(",")
                my_grid_to_list = []
                my_grid_to_list.append(fields[0])
                my_grid_to_list.append(fields[1])
                my_grid_to_list.append(fields[2:])
                my_list.append(my_grid_to_list)
        return my_list

        
    def read_queries(self,file_name):
        with open(file_name, 'r') as f:
            contents = f.read()
            lines = contents.splitlines()
            for i in range(len(lines)):
                lines[i] = lines[i][2:]
        return lines
            
    def split_line(self,line):
        n1,n2,n3,n4 =line.split()
        n1 = float(n1)
        n2 = float(n2)
        n3 = float(n3)
        n4= float(n4)
        return  n1,n2,n3,n4
    
    
