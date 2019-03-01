import numpy as np

def parse(line):  # parse: "1 @ 1,3: 4x4" into integers: 1 1 3 4 4
    at_index = line.find("@")
    colon_index = line.find(":")
    comma_index = line.find(",")
    x_index = line.find("x")
    
    claim_number = int(line[1:at_index-1])
    x_offset = int(line[at_index+2:comma_index])
    y_offset = int(line[comma_index+1:colon_index])
    x_size = int(line[colon_index+2:x_index])
    y_size = int(line[x_index+1:])

    return claim_number,x_offset,y_offset,x_size,y_size

def count_marked (grid):
    counter = 0
    for x in range(grid.shape[0]):
        for y in range(grid.shape[1]):
            if grid[x,y]==-1:
                counter+=1
    return counter

if __name__ == "__main__":
    file = open("input2.txt","r")
    string = file.read()    
    #string = "#1 @ 1,3: 4x4\n#2 @ 3,1: 4x4\n#3 @ 5,5: 2x2"
    list = string.split("\n")
    grid = np.zeros((1100,11000))
    print("First run:")    
    for line in list: #for each claim: marks all cells a claim mentions. if marked again it will assign -1.
        claim_number,x_offset,y_offset,x_size,y_size = parse (line)
        for x in range(x_size):
            for y in range(y_size):
                val = grid[x_offset+x,y_offset+y]
                if val==0 :
                    grid[x_offset+x,y_offset+y] = claim_number
                else:
                    grid[x_offset+x,y_offset+y] = -1
                    valid = 0
    print("Counter: " + str(count_marked(grid)))
    print("Second run:")       
    for line in list:   #checks in the grid if a claim mentions only cells that are marked by himself.
        valid = 1
        claim_number,x_offset,y_offset,x_size,y_size = parse (line)
        for x in range(x_size):
            for y in range(y_size):
                val = grid[x_offset+x,y_offset+y]
                if val==claim_number:
                    continue
                else:                    
                    valid = 0
        if valid==1:
            print(str(claim_number) + " is the valid claim!")               
      