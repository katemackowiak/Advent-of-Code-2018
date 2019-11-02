file = open("aoc8.1datatest.txt", "r")
wholeArray = (file.readlines()[0]).split()
for i in range(len(wholeArray)):
    num = wholeArray[i]
    wholeArray[i] = [int(num)]
#labels: numcn, nummd, md
#wholeArray structure: input value, data label, current parent, 2nd part value (-1 if not done)
#parentNum structure: parent number, number children left, number metadata left
#each parent number add a value at the end as a string, thats what is stored for each val in parentnum
#for instance the top is 1, then in the next layer theres 11 and 12 and so on
#in the wholeArray, the parent number is used to identify a specific node with its header and its metadata
#any time a new cn or md is added, the parent node values must be decreased by 1
currentParent = 1
parentNum = []
metadataCount = 0
longestParent = 0
parentNum.append([currentParent, wholeArray[0][0]]) #starts tree with top layer and num children
wholeArray[0].append("numcn")
wholeArray[0].append(currentParent)
wholeArray[0].append(-1)
for curValNum in range(1,len(wholeArray)):
    curVal = wholeArray[curValNum][0]
    lastVal = wholeArray[curValNum-1]   #gets data of last value to determine what the current one is
    if lastVal[1] == "numcn":
        #our current number is a nummd
        #the parent is also the same as the numcn
        wholeArray[curValNum].append("nummd")
        wholeArray[curValNum].append(currentParent)
        for i in range(len(parentNum)): #jump through each parent number
            if parentNum[i][0] == currentParent:
                parentNum[i].append(curVal) 
    if lastVal[1] == "nummd":
        #our current number has three options:
            #it is the first child node of our current parent
            #it is the first metadata of our current parent
            #it is the next child of the parent above the current parent
        for parNum in range(len(parentNum)):
            par = parentNum[parNum]
            if par[0] == currentParent:    #check the data for the current parent, this is for cn and md
                if par[1] > 0: #if there are children for this parent
                    #need to update both wholeArray and parentNum
                    wholeArray[curValNum].append("numcn")
                    currentParent = str(currentParent) + str(par[1]) 
                    parentNum[parNum][1] = parentNum[parNum][1] - 1 #decreases number child nodes left for the current parent
                    wholeArray[curValNum].append(currentParent)
                    parentNum.append([currentParent, curVal])
                elif par[2] > 0: #if there arent children but theres metadata
                    wholeArray[curValNum].append("md")
                    wholeArray[curValNum].append(currentParent)
                    metadataCount += curVal
                    parentNum[parNum][2] = parentNum[parNum][2] - 1
                else:
                    #must be the next child of the above parent
                    notDone = True
                    while (notDone):  
                        wholeArray[curValNum].append("numcn")
                        currentParent = str(currentParent)[:-1]
                        for i in parentNum: #loop through and see if there are still children for the parent
                            if i[1] > 0:    #if there are children then break the loop
                                notDone = False
                                currentParent = str(currentParent) + str(i[1]) #determine new current parent
                                parentNum.append(currentParent,curVal-1)
                                wholeArray[curValNum].append(currentParent)                                
    if lastVal[1] == "md":
        #there are three options for our current number:
            #it is the next metadata of the current parent
            #it is the next child of the parent above the current parent
            #it is the metadata of the above parent
        for parNum in range(len(parentNum)):
            par = parentNum[parNum]
            if str(par[0]) == str(currentParent):    #check the data for the current parent, this is for cn and md
                if par[2] > 0: #if there is more metadata for this parent
                    wholeArray[curValNum].append("md")
                    wholeArray[curValNum].append(currentParent)
                    metadataCount += curVal
                    parentNum[parNum][2] = parentNum[parNum][2] - 1
                else:   #check to see if theres children for the next parent
                    notDone = True
                    while (notDone):  
                        currentParent = str(currentParent)[:-1]
                        for i in range(len(parentNum)): #loop through and see if there are still children for the parent
                            if str(parentNum[i][0]) == str(currentParent):
                                numberToAddToCurPar = parentNum[i][1]
                                if parentNum[i][1] > 0:    #if there are children then break the loop
                                    notDone = False      
                                    parentNum[i][1] -= 1
                                    currentParent = str(currentParent) + str(numberToAddToCurPar)
                                    wholeArray[curValNum].append("numcn")
                                    wholeArray[curValNum].append(currentParent)
                                    parentNum.append([currentParent, curVal])
                                elif parentNum[i][2] > 0: #if theres md for that parent
                                    notDone = False 
                                    parentNum[i][2] -= 1
                                    metadataCount += curVal
                                    wholeArray[curValNum].append("md")
                                    wholeArray[curValNum].append(currentParent)
    wholeArray[curValNum].append(-1)
    if int(currentParent) > longestParent:
        longestParent = int(currentParent)
#PART TWO
while longestParent > 0:
    longestValues = []
    for curVal in wholeArray:
        if curVal[1] == "numcn": #if we are at a parent node
            if curVal[3] > -1: #and its value hasnt already been determined
                if len(curVal[2]) == longestParent:
                    longestValues.append(int(curVal[2]))
    longestValues = longestValues.sort()
    for curVal in wholeArray:
        for par in longestValues:
            if int(curVal[1]) == par: #go through the list of children
                if int(curVal[0]) == 0: #if there arent any child nodes add all the metadata
                    print("go through and add metadata")
    longestParent -= 1
'''
CURRENT PROBLEMS:
everything
take data and actually arrange it in a tree? thatd be interesting?
'''
