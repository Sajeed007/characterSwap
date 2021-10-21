input_string=input("Enter the string to swap: ")

def oddswap(s):
    char = list(s)
    length = len(char)
    middle = length//2
    if length>3:
        i = 1
        while(i<length-2):
            if (i+1 == middle):
                char[i], char[i+2] = char[i+2], char[i]
                i = i + 1
            elif(i == middle):
                i +=1
                continue
            elif (i != middle):
                char[i], char[i+1] = char[i+1], char[i]
            i += 2
    else:
        return s
    return ''.join(char)

def evenswap(s):
    char = list(s)
    length = len(char)
    # middle = length//2
    if length>3:
        for i in range(1, length-2, 2):
            char[i], char[i+1] = char[i+1], char[i]
    else:
        return s
    return ''.join(char)

if len(input_string)%2 == 0:
    print(evenswap(input_string))
else:
    print(oddswap(input_string))
