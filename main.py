"AM 3045 ONOMA: ALEXANDROS MILONAKIS"

from csv_manager import csv_manager
from my_grid import my_grid
from selection_queries import selection_queries
from manage_files import manage_files

manager1 = csv_manager("C:\\Users\\Alekos\\Desktop\\projects\\Diaxeirisi\\assignment2\\tiger_roads.csv")
road_list = manager1.create_mylist() 
grid1 = my_grid(road_list,manager1,10)
this_grid = grid1.create_grid()

my_selection_queries = selection_queries(grid1.get_number_of_rows())
my_manager = manage_files()
my_grid_dir = my_manager.read_file_and_split('grid.dir')
the_grid = my_manager.read_grd_file('grid.grd')
my_selection_queries.create_structure(the_grid,my_grid_dir)

queries=my_manager.read_queries('queries.txt')
counter = 1

for query in queries:
    minX,maxX,minY,maxY = my_manager.split_line(query)
    identifiers,refined_identifiers,cells = my_selection_queries.selection_query(minX,maxX,minY,maxY)
    """
    identifiers_str = ' '.join(map(str,identifiers))
    #print("Pre refinement stage results")
    print("Query {} results:".format(counter))
    print(identifiers_str)
    print("Cells:",cells)
    print("Results:",len(identifiers))
    print('----------') 
    #print("Post refinement stage results")
    """
    ref_identifiers_str = ' '.join(map(str, refined_identifiers))
    print("Query {} results:".format(counter))
    print(ref_identifiers_str)
    print("Cells:",cells)
    print("Results:",len(refined_identifiers))
    print('----------')       
    counter += 1
    