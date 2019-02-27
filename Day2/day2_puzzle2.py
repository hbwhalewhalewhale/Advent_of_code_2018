import numpy as np

def check_for_two_strings_if_only_one_char_is_different (s1,s2):
    if s1==s2:
        return ("","")
    difference_count = 0
    index = 0
    for index in range(len(s1)):
        if difference_count>1:
            return ("","")
        if s1[index] != s2[index]:
            difference_count+=1
    return s1,s2


if __name__ == "__main__":

    #----load input string to list---#
    file = open("input.txt","r")
    string = file.read()
    #test_string = "aabcde\nfghij\nklmno\npqrst\nfguij\naxcye\nwvxyz"   
    list = string.split("\n")
    line1 = 0
    line2 = 0
    for line1 in range(len(list)):
        for line2 in range(len(list)):
            s1,s2 = check_for_two_strings_if_only_one_char_is_different(list[line1],list[line2])
            if (s1 != ""):
                print(line1)
                print(line2)
                print(s1)
                print(s2)

