import numpy as np

def find_unique_day_guard_list (list):
    guard = ""
    date_guard = []
    date = ""
    for entry in list:
        if entry[1:11]!=date: #check for a new day
            date = entry[1:11]            
            if entry[25:26]!="#": #checks if a guard takes several-day shifts
                continue
            else:
                guard = entry[26:30]  
            date_guard.append([date,guard])
    return date_guard

def time_between(fell_asleep,wakes_up): 
    #calculates time between two string-times:e.g. 23:30 and 24:50. Only 23 and 24 can occur as hours
    if fell_asleep[0:2] == "23":
        start = int(fell_asleep[3:])
    else:
        start = int(fell_asleep[3:])+60
    if wakes_up[0:2] == "23":
        end = int(wakes_up[3:])
    else:
        end = int(wakes_up[3:])+60

    return end-start

def unique_guards (date_guard):#calculates/returns list of unique guards from the date-guard List
    guards = []
    print("Different dates: " +str(len(date_guard)))
    for entry in date_guard:
        if (entry[1] in guards) == False:
            guards.append(entry[1])
    print("Different guards: " +str(guards),end=" amount: ")
    print(len(guards))  
    return guards

def calc_guard_sleep_array (list) -> ([str],[int]): 
    #calculate for each guard and each of the 60 minutes, how often he was asleep at the specific minute throughout his several duty-days

    #List of all Days, and Guards at the day#
    date_guard = find_unique_day_guard_list(list)
    #Unique Guards#
    guards = unique_guards(date_guard)
    #Calc the array  
    asleep_array = np.zeros((len(guards),60))    
    for entry in list:        
        if entry[19:24] == "Guard":#new Guard found
            current_guard = guards.index(entry[26:30])
            continue
        if entry[19:24] == "falls":#guard falls asleep
            fell_asleep = (entry[12:17])
        if entry[19:24] == "wakes":#guard wakes up
            wakes_up = (entry[12:17])
            for j in range (time_between(fell_asleep,wakes_up)): #calc and write asleep-period
                offset = int(fell_asleep[3:5])
                asleep_array[current_guard,offset+j] += 1            
    return asleep_array

if __name__ == "__main__":
    file = open("input.txt","r")
    string = file.read()    
    #---sort datestamps by date---#    
    string = string.replace("00:","24:")#use 24 instead of 00 for midnight, for easy sorting.
    list = string.split("\n")    
    list = sorted(list)

    asleep_array = calc_guard_sleep_array(list)

    #---Solution Puzzle 1:---#
    guard = np.zeros((15))
    for i in range(15):
        guard[i] = np.sum(asleep_array[i])
        if i==12:#maximum
            print("Puzzle1:")
            #print(asleep_array[i]) 
    print("Guard: " + str(guard.argmax())) #Guard at index 12 has number 523
    print(np.max(asleep_array[12]))#Value 18 occurs at minute 38
    #Solution = 38 * 523

    
    #---Solution Puzzle2:---#
    maximum = asleep_array.argmax()
    index = np.where(asleep_array==maximum)
    file_array = open("arr.txt","w")
    max = 0
    g = 0
    m = 0
    for i in range (15):
        file_array.write("\n")
        for j in range (60):
            if asleep_array[i][j] > max:
                max = asleep_array[i][j]            
            file_array.write(str(asleep_array[i][j]))
            file_array.write(" ")
            if max == 21: #maximum
                max += 1
                g = i
                m = j
    print("Puzzle2:")
    print("Guard: " + str(g)) #Guard at index 3 has number 463
    print("Minute: " + str(m)) #Minute 49  
    #Solution = 463 * 49
    