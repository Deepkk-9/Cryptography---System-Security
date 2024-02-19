
def removeWSpacwe(strdata):
    strdata = strdata.replace(" ", "")
    return strdata

keyLenght = int(input("Enter the lenght of the key : "))

# print(keyLenght)

key = []

print("Enter the keys : ")
for i in range(keyLenght):
    key.append(int(input()))

print("The key is : ",key)

strData = input("Enter the string data : ")
strData = removeWSpacwe(strData)


strLsts = []

for i in range(len(strData)):
    if i%keyLenght == 0:
        newList = []
        strLsts.append(newList)       

# print(strLsts)

addVal = len(strLsts) * keyLenght
addVal = addVal - len(strData)

for i in range(addVal):
    strData+="$"

# print(strData)

counter = 0

for i in range(len(strLsts)):
    for j in range(counter, keyLenght+counter):
        strLsts[i].append(strData[j])
        
    counter += keyLenght

# print(strLsts)

cipherTxt = ""

for i in range(keyLenght):
    fVal = key.index(i+1)
    
    for i in range(len(strLsts)):
        getLst = strLsts[i]
        cipherTxt = cipherTxt+getLst[fVal]

print("Encrypted Cipher text : ", cipherTxt)

    

def decryption(cipherTxt, key):

    nRows = len(cipherTxt) // len(key)

    dLists = [[] for i in range(0,nRows)]

    # print(dLists)

    #This gives me the indexes of the key values:
    getIndex = []
    for i in range(len(key)):
        getIndex.append(key.index(i+1))
    # print(getIndex)


    #divides the cipher text into lists 
    d = [list(cipherTxt[i:i + nRows]) for i in range(0, len(cipherTxt), nRows)]
    # print(d)

    #Decryption
    t=0

    for i in d:
        getI = getIndex[t]
        b = 0
        for j in i:
            dLists[b].insert(getI, j)
            b = b+1
        t = t+1

    # print(dLists)

    decryptedTxt = ''.join([''.join(sublist) for sublist in dLists])

    print("Decrypted text: ", decryptedTxt)



decryption(cipherTxt, key)
