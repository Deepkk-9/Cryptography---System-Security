def findIndex(c, matrix):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == c or c in matrix[i][j]:
                return (i, j)
    return None

def genMatrix(key):
    matrix = [[0 for i in range(5)] for j in range(5)]
    temp = key
    rows = 0
    cols = 0

    while temp:
        if temp[0] == 'I':
            matrix[cols][rows] = temp[0] + 'J'
        else:
            matrix[cols][rows] = temp[0]
        temp = temp[1:]
        rows += 1

        if rows == 5:
            rows = 0
            cols += 1

    code = 65
    while code < 91:
        if chr(code) in key:
            code += 1
            if 'I' in key and chr(code) == 'J':
                code += 1
            continue
        else:
            if chr(code) == 'I':
                matrix[cols][rows] = chr(code) + chr(code + 1)
                code += 1
            else:
                matrix[cols][rows] = chr(code)
        code += 1
        rows += 1

        if rows == 5:
            rows = 0
            cols += 1

        if cols > 4:
            break

    return matrix

def encrypt(pt, matrix):
    temp = pt
    cipher = ''
    while temp:
        a = temp[0:2]
        temp = temp[2:]
        a0 = findIndex(a[0], matrix)
        a1 = findIndex(a[1], matrix)

        if a0[0] == a1[0]:
            cipher += matrix[a0[0]][(a0[1] + 1) % 5]
            cipher += matrix[a1[0]][(a1[1] + 1) % 5]
        elif a0[1] == a1[1]:
            cipher += matrix[(a0[0] + 1) % 5][a0[1]]
            cipher += matrix[(a1[0] + 1) % 5][a1[1]]
        else:
            cipher += matrix[a0[0]][a1[1]]
            cipher += matrix[a1[0]][a0[1]]
        a = ''

    return cipher

pt = input('Enter plain text: ').upper()
if len(pt) % 2 != 0:
    pt += 'Z'

key = input('Enter key: ').upper()
matrix = genMatrix(key)
cipher = encrypt(pt, matrix)

print()
for row in matrix:
    print(row)
print('\nPlain Text:  ', pt)
print('Cipher Text: ', cipher, '\n')
