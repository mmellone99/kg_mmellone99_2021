#Kargo Software Engineer Intern Assesment
#Michael Mellone

import sys

def charMap(*argv):
    if len(sys.argv[1]) == len(sys.argv[2]):  
        dict = {}   
        for i in range(len(sys.argv[1])):  
            if sys.argv[1][i] not in dict:
                dict[sys.argv[1][i]] = sys.argv[2][i]
            if dict[sys.argv[1][i]] != sys.argv[2][i]:
                return False
        return True
    return False  


print(charMap())

