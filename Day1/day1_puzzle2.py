
def first_duplicate_result(list):
    length = len(list)
    result_arr = [0] 
    sum = 0
    for j in range (length**2):
        i = j%length
        sum = sum + eval(list[i])
        if (sum in result_arr):
            print(result_arr.index(sum))
            print(j)                      
            return sum
        result_arr.append(sum)   
    return "nothing found"

if __name__ == "__main__":
    file = open("input.txt","r")
    string = file.read()
    #string="+7, +7, -2, -7, -4"
    string= string.replace(",","\n")
    string = string.replace("+","")
    list = string.split("\n")
    print(first_duplicate_result(list))

    if (3 in [1,4,1]):
        print("True")

            