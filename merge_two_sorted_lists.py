def mergeTwoLists(list1, list2):

    output = list1[:]  
    for i in range(len(list2)):
        inserted = False

        for j in range(len(list1)):
            if list2[i] <= list1[j]:
                output.insert(j,list2[i])
                inserted = True
                break

        if not inserted:
            output.append(list2[i])

    return output

print(mergeTwoLists([1,2,4],[1,3,5]))