if __name__ == "__main__":
    file = open("input.txt","r")
    string = file.read()
    string = string.replace("+","")
    list =string.split("\n")
    sum = 0
    for i in list:
        sum = sum + eval(i)
    print(sum)