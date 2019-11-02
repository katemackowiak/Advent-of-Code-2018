file = open("aoc8.1datatest.txt", "r")
wholeArray = (file.readlines()[0]).split()
for i in range(len(wholeArray)):
    num = wholeArray[i]
    wholeArray[i] = [int(num)]
#labels: numcn, nummd, md
#wholeArray structure: input value, data label, node number
#parentNum structure: parent number, number children left
wholeArray[0].append("numcn")
wholeArray[0].append(0)
parentNum = []
parentNum.append([wholeArray[0][2], wholeArray[0][0]])
currentParent = str(0)
metadata = 0
for i in range(1,len(wholeArray)):  #so going through each number
    lastVal = wholeArray[i-1]   #this is the last number for reference
    if lastVal[1] == "numcn":   #if the last number was the number of child nodes
        wholeArray[i].append("nummd")   #then this number is the number of meta data
        wholeArray[i].append(lastVal[2])    #therefore they have the same parent node
        parentNum[-1].append(wholeArray[i]) #and also the data should be added to the parent node array
    if lastVal[1] == "nummd":   #if the last number was a metadata
        for y in range(len(parentNum)): #then we need to check if there actually are child nodes/meta data for the parent
            x = parentNum[y]
            if x[0] == currentParent:   #so go through the parent nodes and find the one with data which lines up with where we are
                if x[1] > 0:    #if there are child nodes for this parent
                    #THIS IS ALWAYS THE FIRST CHILD NODE 
                    wholeArray[i].append["numcn"]   #then note that we are in a new node
                    wholeArray[i].append[currentParent] #denotes the parent of this node
                    #PARENT NODE STUFF
                    parentNum[y][1] -= 1 #subtract from the number of child nodes left for the parent
                    currentParent = currentParent + x[1] #set the new mode to the current parent
                    parentNum.append([i[0][2]],i[0][0]) #add this node to the list of parent nodes
                else:   #if there arent child nodes then skip to metadata
                    currentParent = currentParent[:-1]  #move up to the prior parent
                    #METADATA
                    if parentNum[currentParent][2] > 0: #if the current parent does have metadata
                        wholeArray[i].append("md")  #set the current type
                        wholeArray[i].append(currentParent) #set the parent of this node
                        metadata += wholeArray[i][0] #add to metadata
                        parentNum[currentParent][2] -= 1 #subtract from metadata left
                    #MODE AGAIN
                    else:   #if there werent any child nodes then we must be on to the next node?
                    #SINCE THERE ARENT ANY MORE CHILD NODES FOR THIS PARENT MOVE UP A PARENT
                        wholeArray[i].append["numcn"]   #then note that we are in a new node
                        #PARENT STUFF
                        currentParent = currentParent[:-1]
                        wholeArray[i].append[currentParent] #denotes the parent of this node
                        parentNum[y][1] -= 1 #subtract from the number of child nodes left for the parent
                        parentNum.append([i[0][2]],i[0][0]) #add this node to the list of parent nodes
    if lastVal[1] == "md":  #if the last was metadata it can either be metadata or the next node
        for y in range(len(parentNum)):
            x = parentNum[y]
            if x[0] == currentParent:   #our current parent node
                if parentNum[currentParent][2] > 0: #if theres more metadata
                    wholeArray[i].append("md")  #set the current type
                    wholeArray[i].append(currentParent) #set the parent of this node
                    metadata += wholeArray[i][0] #add to metadata
                    parentNum[currentParent][2] -= 1 #subtract from metadata left
                else:   #must be the new node
                    print('i give up')

                        





