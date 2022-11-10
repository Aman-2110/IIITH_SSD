from datetime import datetime as dt

inputFile = open('Readings for 126x25 mat.txt', 'r')

data = []
matrix = []
timeStamp = []
flag = False

while True:
    line = inputFile.readline()
    
    if not line:
        data.append(matrix)
        break
    elif len(line) != 1 :
        elements = line.split('\t')
        matrix.append(elements[1:-1])
        if len(matrix) == 21 :
            timeStamp.append(elements[0])
        flag = True
    elif flag :
        data.append(matrix)
        matrix = []
        flag = False

leftFoot = False
rightFoot = False
leftX = []
rightX = []
leftTime = []
rightTime = []
isLeftMat = True
isRightMat = True

for frame, mat in enumerate(data) :
    noRightLegInMat = True
    noLeftLegInMat = True
    for row, line in enumerate(mat) :
        for col, element in enumerate(line) :
            if element != '0' :
                if not leftFoot and col <= 12 and isLeftMat: 
                    if row != 125 and data[frame][row + 1][col - 1] != '0' or data[frame][row + 1][col] != '0' or data[frame][row + 1][col + 1] != '0' : 
                        leftX.append(row)
                        leftTime.append(timeStamp[frame])                
                        leftFoot = True
                        rightFoot = False
                        isLeftMat = False
                elif not rightFoot and col > 12 and isRightMat:
                    if row != 125 and data[frame][row + 1][col - 1] != '0' or data[frame][row + 1][col] != '0' or data[frame][row + 1][col + 1] != '0' : 
                        rightX.append(row)
                        rightTime.append(timeStamp[frame])                   
                        rightFoot = True
                        leftFoot = False
                        isRightMat = False
                        
                if col <= 12 :
                    noLeftLegInMat = False
                else : 
                    noRightLegInMat = False
                                 
    if noLeftLegInMat : 
        isLeftMat = True
    if noRightLegInMat :
        isRightMat = True
        
print((leftX[0] - rightX[0])*2)
print(((leftX[0] - rightX[0]))/(dt.strptime(rightTime[0], "%H:%M:%S.%f") - dt.strptime(leftTime[0], "%H:%M:%S.%f")).seconds)
print((2/(dt.strptime(rightTime[0], "%H:%M:%S.%f") - dt.strptime(leftTime[0], "%H:%M:%S.%f")).seconds)*60)