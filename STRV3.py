import arcpy

# Define a new function for judging neighborhood cubes
# X == 1, X > 1 and X < 6, X == 6
# Y == 1, Y > 1 and Y < 6, Y == 6
# Z == 1, Z > 1 and Z < 6, Z == 6
def NeighborCubes(X, Y, Z):

    if X == 1 and Y == 1 and Z == 1:
        NeighborList = [[X+1,Y,Z],[X,Y+1,Z],[X,Y,Z+1],[X+1,Y+1,Z],[X+1,Y,Z+1],[X,Y+1,Z+1],[X+1,Y+1,Z+1]]
    if X == 6 and Y == 1 and Z == 1:
        NeighborList = [[X-1,Y,Z],[X,Y+1,Z],[X,Y,Z+1],[X-1,Y+1,Z],[X-1,Y,Z+1],[X,Y+1,Z+1],[X-1,Y+1,Z+1]]
    if X == 1 and Y == 6 and Z == 1:
        NeighborList = [[X+1,Y,Z],[X,Y-1,Z],[X,Y,Z+1],[X+1,Y-1,Z],[X+1,Y,Z+1],[X,Y-1,Z+1],[X+1,Y-1,Z+1]]
    if X == 1 and Y == 1 and Z == 6:
        NeighborList = [[X+1,Y,Z],[X,Y+1,Z],[X,Y,Z-1],[X+1,Y+1,Z],[X+1,Y,Z-1],[X,Y+1,Z-1],[X+1,Y+1,Z-1]]
    if X == 6 and Y == 6 and Z == 1:
        NeighborList = [[X-1,Y,Z],[X,Y-1,Z],[X,Y,Z+1],[X-1,Y-1,Z],[X-1,Y,Z+1],[X,Y-1,Z+1],[X-1,Y-1,Z+1]]
    if X == 6 and Y == 1 and Z == 6:
        NeighborList = [[X-1,Y,Z],[X,Y+1,Z],[X,Y,Z-1],[X-1,Y+1,Z],[X-1,Y,Z-1],[X,Y+1,Z-1],[X-1,Y+1,Z-1]]
    if X == 1 and Y == 6 and Z == 6:
        NeighborList = [[X+1,Y,Z],[X,Y-1,Z],[X,Y,Z-1],[X+1,Y-1,Z],[X+1,Y,Z-1],[X,Y-1,Z-1],[X+1,Y-1,Z-1]]
    if X == 6 and Y == 6 and Z == 6:
        NeighborList = [[X-1,Y,Z],[X,Y-1,Z],[X,Y,Z-1],[X-1,Y-1,Z],[X-1,Y,Z-1],[X,Y-1,Z-1],[X-1,Y-1,Z-1]]

    if X > 1 and X < 6 and Y == 1 and Z == 1:
        NeighborList = [[X+1,Y,Z],[X,Y+1,Z],[X,Y,Z+1],[X+1,Y+1,Z],[X+1,Y,Z+1],[X,Y+1,Z+1],[X+1,Y+1,Z+1],
                        [X-1,Y,Z],[X-1,Y+1,Z],[X-1,Y,Z+1],[X-1,Y+1,Z+1]]
    if X > 1 and X < 6 and Y == 6 and Z == 1:
        NeighborList = [[X+1,Y,Z],[X,Y-1,Z],[X,Y,Z+1],[X+1,Y-1,Z],[X+1,Y,Z+1],[X,Y-1,Z+1],[X+1,Y-1,Z+1],
                        [X-1,Y,Z],[X-1,Y-1,Z],[X-1,Y,Z+1],[X-1,Y-1,Z+1]]
    if X > 1 and X < 6 and Y == 1 and Z == 6:
        NeighborList = [[X+1,Y,Z],[X,Y+1,Z],[X,Y,Z-1],[X+1,Y+1,Z],[X+1,Y,Z-1],[X,Y+1,Z-1],[X+1,Y+1,Z-1],
                        [X-1,Y,Z],[X-1,Y+1,Z],[X-1,Y,Z-1],[X-1,Y+1,Z-1]]
    if X > 1 and X < 6 and Y == 6 and Z == 6:
        NeighborList = [[X+1,Y,Z],[X,Y-1,Z],[X,Y,Z-1],[X+1,Y-1,Z],[X+1,Y,Z-1],[X,Y-1,Z-1],[X+1,Y-1,Z-1],
                        [X-1,Y,Z],[X-1,Y-1,Z],[X-1,Y,Z-1],[X-1,Y-1,Z-1]]

    if X == 1 and Y > 1 and Y < 6 and Z == 1:
        NeighborList = [[X+1,Y,Z],[X,Y+1,Z],[X,Y,Z+1],[X+1,Y+1,Z],[X+1,Y,Z+1],[X,Y+1,Z+1],[X+1,Y+1,Z+1],
                        [X,Y-1,Z],[X+1,Y-1,Z],[X,Y-1,Z+1],[X+1,Y-1,Z+1]]
    if X == 6 and Y > 1 and Y < 6 and Z == 1:
        NeighborList = [[X-1,Y,Z],[X,Y+1,Z],[X,Y,Z+1],[X-1,Y+1,Z],[X-1,Y,Z+1],[X,Y+1,Z+1],[X-1,Y+1,Z+1],
                        [X,Y-1,Z],[X-1,Y-1,Z],[X,Y-1,Z+1],[X-1,Y-1,Z+1]]
    if X == 1 and Y > 1 and Y < 6 and Z == 6:
        NeighborList = [[X+1,Y,Z],[X,Y+1,Z],[X,Y,Z-1],[X+1,Y+1,Z],[X+1,Y,Z-1],[X,Y+1,Z-1],[X+1,Y+1,Z-1],
                        [X,Y-1,Z],[X+1,Y-1,Z],[X,Y-1,Z-1],[X+1,Y-1,Z-1]]
    if X == 6 and Y > 1 and Y < 6 and Z == 6:
        NeighborList = [[X-1,Y,Z],[X,Y+1,Z],[X,Y,Z-1],[X-1,Y+1,Z],[X-1,Y,Z-1],[X,Y+1,Z-1],[X-1,Y+1,Z-1],
                        [X,Y-1,Z],[X-1,Y-1,Z],[X,Y-1,Z-1],[X-1,Y-1,Z-1]]

    if X == 1 and Y == 1 and Z > 1 and Z < 6:
        NeighborList = [[X+1,Y,Z],[X,Y+1,Z],[X,Y,Z+1],[X+1,Y+1,Z],[X+1,Y,Z+1],[X,Y+1,Z+1],[X+1,Y+1,Z+1],
                        [X,Y,Z-1],[X+1,Y,Z-1],[X,Y+1,Z-1],[X+1,Y+1,Z-1]]
    if X == 6 and Y == 1 and Z > 1 and Z < 6:
        NeighborList = [[X-1,Y,Z],[X,Y+1,Z],[X,Y,Z+1],[X-1,Y+1,Z],[X-1,Y,Z+1],[X,Y+1,Z+1],[X-1,Y+1,Z+1],
                        [X,Y,Z-1],[X-1,Y,Z-1],[X,Y+1,Z-1],[X-1,Y+1,Z-1]]
    if X == 1 and Y == 6 and Z > 1 and Z < 6:
        NeighborList = [[X+1,Y,Z],[X,Y-1,Z],[X,Y,Z+1],[X+1,Y-1,Z],[X+1,Y,Z+1],[X,Y-1,Z+1],[X+1,Y-1,Z+1],
                        [X,Y,Z-1],[X+1,Y,Z-1],[X,Y-1,Z-1],[X+1,Y-1,Z-1]]
    if X == 6 and Y == 6 and Z > 1 and Z < 6:
        NeighborList = [[X-1,Y,Z],[X,Y-1,Z],[X,Y,Z+1],[X-1,Y-1,Z],[X-1,Y,Z+1],[X,Y-1,Z+1],[X-1,Y-1,Z+1],
                        [X,Y,Z-1],[X-1,Y,Z-1],[X,Y-1,Z-1],[X-1,Y-1,Z-1]]

    if X > 1 and X < 6 and Y > 1 and Y < 6 and Z == 1:
        NeighborList = [[X+1,Y,Z],[X,Y+1,Z],[X,Y,Z+1],[X+1,Y+1,Z],[X+1,Y,Z+1],[X,Y+1,Z+1],[X+1,Y+1,Z+1],
                        [X-1,Y,Z],[X-1,Y+1,Z],[X-1,Y,Z+1],[X-1,Y+1,Z+1],
                        [X,Y-1,Z],[X+1,Y-1,Z],[X,Y-1,Z+1],[X+1,Y-1,Z+1],
                        [X-1,Y-1,Z],[X-1,Y-1,Z+1]]
    if X > 1 and X < 6 and Y > 1 and Y < 6 and Z == 6:
        NeighborList = [[X+1,Y,Z],[X,Y+1,Z],[X,Y,Z-1],[X+1,Y+1,Z],[X+1,Y,Z-1],[X,Y+1,Z-1],[X+1,Y+1,Z-1],
                        [X-1,Y,Z],[X-1,Y+1,Z],[X-1,Y,Z-1],[X-1,Y+1,Z-1],
                        [X,Y-1,Z],[X+1,Y-1,Z],[X,Y-1,Z-1],[X+1,Y-1,Z-1],
                        [X-1,Y-1,Z],[X-1,Y-1,Z-1]]

    if X > 1 and X < 6 and Y == 1 and Z > 1 and Z < 6:
        NeighborList = [[X+1,Y,Z],[X,Y+1,Z],[X,Y,Z+1],[X+1,Y+1,Z],[X+1,Y,Z+1],[X,Y+1,Z+1],[X+1,Y+1,Z+1],
                        [X-1,Y,Z],[X-1,Y+1,Z],[X-1,Y,Z+1],[X-1,Y+1,Z+1],
                        [X,Y,Z-1],[X+1,Y,Z-1],[X,Y+1,Z-1],[X+1,Y+1,Z-1],
                        [X-1,Y,Z-1],[X-1,Y+1,Z-1]]
    if X > 1 and X < 6 and Y == 6 and Z > 1 and Z < 6:
        NeighborList = [[X+1,Y,Z],[X,Y-1,Z],[X,Y,Z+1],[X+1,Y-1,Z],[X+1,Y,Z+1],[X,Y-1,Z+1],[X+1,Y-1,Z+1],
                        [X-1,Y,Z],[X-1,Y-1,Z],[X-1,Y,Z+1],[X-1,Y-1,Z+1],
                        [X,Y,Z-1],[X+1,Y,Z-1],[X,Y-1,Z-1],[X+1,Y-1,Z-1],
                        [X-1,Y,Z-1],[X-1,Y-1,Z-1]]

    if X == 1 and Y > 1 and Y < 6 and Z > 1 and Z < 6:
        NeighborList = [[X+1,Y,Z],[X,Y+1,Z],[X,Y,Z+1],[X+1,Y+1,Z],[X+1,Y,Z+1],[X,Y+1,Z+1],[X+1,Y+1,Z+1],
                        [X,Y-1,Z],[X+1,Y-1,Z],[X,Y-1,Z+1],[X+1,Y-1,Z+1],
                        [X,Y,Z-1],[X+1,Y,Z-1],[X,Y+1,Z-1],[X+1,Y+1,Z-1],
                        [X,Y-1,Z-1],[X+1,Y-1,Z-1]]
    if X == 6 and Y > 1 and Y < 6 and Z > 1 and Z < 6:
        NeighborList = [[X-1,Y,Z],[X,Y+1,Z],[X,Y,Z+1],[X-1,Y+1,Z],[X-1,Y,Z+1],[X,Y+1,Z+1],[X-1,Y+1,Z+1],
                        [X,Y-1,Z],[X-1,Y-1,Z],[X,Y-1,Z+1],[X-1,Y-1,Z+1],
                        [X,Y,Z-1],[X-1,Y,Z-1],[X,Y+1,Z-1],[X-1,Y+1,Z-1],
                        [X,Y-1,Z-1],[X-1,Y-1,Z-1]]

    if X > 1 and X < 6 and Y > 1 and Y < 6 and Z > 1 and Z < 6:
        NeighborList = [[X+1,Y,Z],[X,Y+1,Z],[X,Y,Z+1],[X+1,Y+1,Z],[X+1,Y,Z+1],[X,Y+1,Z+1],[X+1,Y+1,Z+1],
                        [X-1,Y,Z],[X-1,Y+1,Z],[X-1,Y,Z+1],[X-1,Y+1,Z+1],
                        [X,Y-1,Z],[X+1,Y-1,Z],[X,Y-1,Z+1],[X+1,Y-1,Z+1],
                        [X,Y,Z-1],[X+1,Y,Z-1],[X,Y+1,Z-1],[X+1,Y+1,Z-1],
                        [X-1,Y-1,Z],[X-1,Y-1,Z+1],
                        [X-1,Y,Z-1],[X-1,Y+1,Z-1],
                        [X,Y-1,Z-1],[X+1,Y-1,Z-1],
                        [X-1,Y-1,Z-1]]

    NeighborListStr = []
    for i in NeighborList:
        Str = [str(j) for j in i]
        StrKey = '_'.join(Str)
        NeighborListStr.append(StrKey)

    return NeighborListStr

# Define a new function to calculate the distance between two cubes
def Distance(list1,list2):
    distance = float(((list1[0]-list2[0])**2 + (list1[1]-list2[1])**2 + (list1[2]-list2[2])**2)**0.5)
    return distance

# Define a new function to calculate the average vector of two old vectors
def MeanVec(list):
    vec1 = list[0]
    vec2 = list[1]
    newvec = []
    for i in range(0, len(vec1)):
        newvec.append((vec1[i]+vec2[i])/len(list))
    return newvec

# Define a new function to delete element of dictionary
def DelDicElem(dictionary, pointID1, pointID2):
    key1 = '{0}-{1}'.format(pointID1, pointID2)
    key2 = '{1}-{0}'.format(pointID1, pointID2)
    if key1 in dictionary:
        del (dictionary[key1])
    else:
        del (dictionary[key2])

def ScriptTool(InputCubes, Variables, STR_numbers, OutputCubes):

    # Construct a dictionary of cube features
    # e.g. {'1':[V1, V2, V3]}
    FeatureDic = {}
    fields = ['OBJECTID','V1', 'V2', 'V3', 'X', 'Y', 'Z']
    with arcpy.da.SearchCursor(InputCubes, fields) as cursor:
        for row in cursor:
            FeatureVector = [row[1],row[2],row[3]]
            ObjectID = row[0]
            FeatureDic[str(ObjectID)] = [row[i] for i in range(len(FeatureVector))]
    # arcpy.AddMessage('FeatureDic is:')
    # arcpy.AddMessage(FeatureDic)

    # Construct a dictionary of positions and objectID
    # e.g. {'1_1_1':'1', '1_1_2':'2'}
    ObjectDic = {}
    with arcpy.da.SearchCursor(InputCubes, fields) as cursor:
        for row in cursor:
            PositionList = [row[4], row[5], row[6]]
            PositionListStr = [str(i) for i in PositionList]
            NeighborKey = '_'.join(PositionListStr)
            ObjectID = row[0]
            ObjectDic[NeighborKey] = str(ObjectID)
    # arcpy.AddMessage('ObjectDic is:')
    # arcpy.AddMessage(ObjectDic)

    # Construct a dictionary of neighbor cubes
    # e.g. {'1':[2, 3, 4, 5], '2':[1, 3, 4, 5]}
    NeighborDic = {}
    with arcpy.da.SearchCursor(InputCubes, fields) as cursor:
        for row in cursor:
            PositionList = [row[4], row[5], row[6]]
            PositionListStr = [str(i) for i in PositionList]
            NeighborList = NeighborCubes(PositionList[0], PositionList[1], PositionList[2])
            NeighborKey = '_'.join(PositionListStr)
            NeighborListID = []
            for i in NeighborList:
                NeighborListID.append(ObjectDic[i])
                NeighborListIDStr = [str(i) for i in NeighborListID]
            NeighborDic[ObjectDic[NeighborKey]] = NeighborListIDStr
    # arcpy.AddMessage('NeighborDic is:')
    # arcpy.AddMessage(NeighborDic)

    # Construct a dictionary of distance matrix
    # e.g. {'1-2': 0.5, '1-3': 0.4, '1-4': 0.8}
    DistanceDic = {}
    for k in NeighborDic.keys():
        for v in NeighborDic[k]:
            InverseKey = '{0}-{1}'.format(str(v), str(k))
            if InverseKey not in DistanceDic:
                PositiveKey = '{0}-{1}'.format(str(k), str(v))
                distance = Distance(FeatureDic[k],FeatureDic[v])
                DistanceDic[PositiveKey] = distance
    # arcpy.AddMessage('DistanceDic is:')
    # arcpy.AddMessage(DistanceDic)

    # Start the hierarchical clustering loop
    cycles = 1
    while len(FeatureDic) > STR_numbers:
        # arcpy.AddMessage('Start the {0}th cycles'.format(cycles))
        # e.g. MinDistanceDicKey is '29-30'
        # e.g. MinDisDicKeySplit is [29,30]
        MinDistanceDicKey = min(DistanceDic, key=DistanceDic.get)  # Find the key with the smallest value in DistanceDic
        MinDisDicKeySplit = MinDistanceDicKey.split('-')
        # MinDisDicKeySplitInt = [int(i) for i in MinDisDicKeySplit]  # Convert str to int, beacause keys and values in the dictionary are int.
        # arcpy.AddMessage('MinDistanceDicKey is:')
        # arcpy.AddMessage(MinDistanceDicKey)

        # Add new element and delete old element from FeatureDic
        # Calculate the value of new element
        OldVecList = [FeatureDic[e] for e in MinDisDicKeySplit]
        # Mean vector of two old vectors, which is new element.
        NewValue = MeanVec(OldVecList)
        # arcpy.AddMessage('Old element list is:')
        # arcpy.AddMessage(OldVecList)
        # arcpy.AddMessage('New element is:')
        # arcpy.AddMessage(NewValue)

        # Add new element and delete the old one of FeatureDic
        MinDistanceDicKey = MinDistanceDicKey.replace('-','_')
        FeatureDic[MinDistanceDicKey] = NewValue
        for e in MinDisDicKeySplit:
            del(FeatureDic[e])
        # arcpy.AddMessage('New FeatureDic is:')
        # arcpy.AddMessage(FeatureDic)

        # Add new element and delete the old one of NeighborDic
        NewNeighbor = []
        for e in MinDisDicKeySplit:
            NewNeighbor = NewNeighbor + NeighborDic[e]
        NewNeighbor = list(set(NewNeighbor))
        for e in MinDisDicKeySplit:
            NewNeighbor.remove(e)
        # arcpy.AddMessage('The union set is:')
        # arcpy.AddMessage(NewNeighbor)
        NeighborDic[MinDistanceDicKey] = NewNeighbor  # Add new element to NeighborDic keys
        for e in MinDisDicKeySplit:  # Delete old element of NeighborDic keys
            del(NeighborDic[e])
        # arcpy.AddMessage('New NeighborDic is:')
        # arcpy.AddMessage(NeighborDic)
        # Replace old element to new element in NeighborDic values
        for e in NeighborDic.keys():
            CurrentValueList = NeighborDic[e]
            for i in range(0, len(CurrentValueList)):
                if CurrentValueList[i] in MinDisDicKeySplit:
                    CurrentValueList[i] = MinDistanceDicKey
            NeighborDic[e] = list(set(CurrentValueList))
        # arcpy.AddMessage('New NeighborDic is:')
        # arcpy.AddMessage(NeighborDic)

        # Remove current MinDisDicKey from DistanceDic
        del(DistanceDic[str(MinDisDicKeySplit[0] + '-' + MinDisDicKeySplit[1])])
        # arcpy.AddMessage('New DistanceDic is:')
        # arcpy.AddMessage(DistanceDic)
        # Replace old element contained in DistanceDic keys to new element
        for e in list(DistanceDic.keys()):
            CurrentKeyList = e.split('-')
            if CurrentKeyList[0] in MinDisDicKeySplit:
                CurrentKeyList[0] = MinDistanceDicKey
                DelDicElem(DistanceDic, e.split('-')[0], e.split('-')[1])
            if CurrentKeyList[1] in MinDisDicKeySplit:
                CurrentKeyList[1] = MinDistanceDicKey
                DelDicElem(DistanceDic, e.split('-')[0], e.split('-')[1])
            # Update DistanceDic
            DistanceDic['{0}-{1}'.format(CurrentKeyList[0],CurrentKeyList[1])] = Distance(FeatureDic[CurrentKeyList[0]],FeatureDic[CurrentKeyList[1]])
        DelKeyList = []
        ResKeyList = []
        for e in list(DistanceDic.keys()):
            KeyO = e.split('-')[0]
            KeyD = e.split('-')[1]
            KeyDO = '{0}-{1}'.format(KeyD, KeyO)
            if KeyDO in DistanceDic.keys() and KeyDO not in ResKeyList:
                DelKeyList.append(KeyDO)  # Store inverse keys
                ResKeyList.append(e)  # Store positive keys
        for e in DelKeyList:
            del(DistanceDic[e])

        cycles = cycles + 1

        # arcpy.AddMessage('New DistanceDic is:')
        # arcpy.AddMessage(DistanceDic)
        # arcpy.AddMessage('STR result is:')
        # arcpy.AddMessage(FeatureDic)

    # Write the STR result into a new field
    ClusterCode = 0
    ClusterCodeDic = {}
    # Code the points with same cluster
    for e in FeatureDic.keys():
        ClusterCode = ClusterCode + 1
        CodeList = e.split('_')
        for e in CodeList:
            ClusterCodeDic[int(e)] = ClusterCode
    # arcpy.AddMessage(ClusterCodeDic)
    arcpy.management.AddField(InputCubes, "cluster_id", "LONG", None, None, None, '', "NULLABLE", "NON_REQUIRED", '')
    NewFields = ['OBJECTID','cluster_id']
    with arcpy.da.UpdateCursor(InputCubes, NewFields) as cursor:
        for row in cursor:
            row[1] = ClusterCodeDic[int(row[0])]
            cursor.updateRow(row)

    return

if __name__ == '__main__':
    # ScriptTool parameters
    # Get the data in tool box
    InputCubes = arcpy.GetParameterAsText(0)  # Get input cubes
    Variables = arcpy.GetParameterAsText(1)  # Variables of input cubes
    STR_numbers = int(arcpy.GetParameterAsText(2))  # Numbers of spatiotemporal regionalization
    OutputCubes = arcpy.GetParameterAsText(3)  # Build output cubes
    # arcpy.AddMessage('Main function success!')
    # Run ScriptTool function
    ScriptTool(InputCubes, Variables, STR_numbers, OutputCubes)