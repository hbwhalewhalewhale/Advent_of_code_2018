import numpy as np

def parse(line):    
    at_index = line.find("@")
    colon_index = line.find(":")
    comma_index = line.find(",")
    x_index = line.find("x")
    
    line_number = int(line[1:at_index-1])
    x_offset = int(line[at_index+2:comma_index])
    y_offset = int(line[comma_index+1:colon_index])
    x_size = int(line[colon_index+2:x_index])
    y_size = int(line[x_index+1:])

    return line_number,x_offset,y_offset,x_size,y_size

def count_marked (grid):
    counter = 0
    for x in range(grid.shape[0]):
        for y in range(grid.shape[1]):
            if grid[x,y]==-1:
                counter+=1
    return counter

if __name__ == "__main__":
    file = open("input.txt","r")
    string = file.read()    
    #string = "#1 @ 1,3: 4x5\n#1 @ 1,3: 4x5"
    list = string.split("\n")
    grid = np.zeros((1100,11000))

    

    for line in list:
        line_number,x_offset,y_offset,x_size,y_size = parse (line)
        print(grid[x_offset,y_offset])
        for x in range(x_size):
            for y in range(y_size):
                val = grid[x_offset+x,y_offset+y]
                if val==0 :
                    grid[x_offset+x,y_offset+y] = line_number
                else:
                    grid[x_offset+x,y_offset+y] = -1
                   
        print(grid[x_offset,y_offset])
        print("\nline number:  "+str(line_number))
        print("x_off:        " + str(x_offset))
        print("y_off:        " + str(y_offset))
        print("x:            " + str(x_size))
        print("y:            " + str(y_size))
    print("Counter:      " + str(count_marked(grid))      
      