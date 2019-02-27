import numpy as np



if __name__ == "__main__":

    #----load input string to list---#
    file = open("input.txt","r")
    string = file.read()
    #test_string = "abcdef\nbababc\nabbcde\nabcccd\naabcdd\nabcdee\nababab"   
    list = string.split("\n")
    #----count twice/thrice occuring letters for all input lines---#
    twice_count = 0
    thrice_count = 0    
    for line in list:
        print(line)
        alphabet = np.zeros(26)
        for character in line:
            char_as_number = ord(character)-97     #convert lower-case alphabet in unicode to 0-25            
            alphabet[char_as_number] += 1
        uniques, counts = np.unique(alphabet,return_counts=True)
        
        #check for double occuring characters
        if 2 in uniques:
            twice_count+=1
            print("----twice +1")
        #check for thrice occuring characters
        if 3 in uniques:
            thrice_count+=1
            print("----thrice +1")
    print("\n\n")
    print(twice_count)
    print(thrice_count)
    checksum = twice_count*thrice_count
    print("checksum: " + str(checksum))