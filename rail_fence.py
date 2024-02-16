railFStr = input("Enter the string : ")

def removeWSpacwe(railFStr):
    railFStr = railFStr.replace(" ", "")
    return railFStr

def railFence(railFStr):
    l1 = ""
    l2 = ""
    for i in range(len(railFStr)):
        if i%2 == 0:
            l1 = l1 + railFStr[i]
        else:
            l2 = l2 + railFStr[i]
    return l1+l2

def decrypt(railFStr):
    l1 = ""
    l2 = ""
    if len(railFStr) % 2 != 0:
        railFStr = railFStr + "#"
        midpoint = len(railFStr) // 2
        l1 = railFStr[:midpoint]
        l2 = railFStr[midpoint:(len(railFStr))]

        for i in range(len(l1)):
            print(l1[i])
            if i != len(l1) - 1:
                print(l2[i])
    else:
        midpoint = len(railFStr) // 2
        l1 = railFStr[:midpoint]
        l2 = railFStr[midpoint:]
        for i in range(len(l1)):
            print(l1[i])
            print(l2[i])

railFStr = removeWSpacwe(railFStr)
railFStr = railFence(railFStr)

decrypt(railFStr)