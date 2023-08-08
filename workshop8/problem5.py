# problem5, 12/05/21, Cordelia Jiang
# write a program that reports the names and number of club members infected up
# to each meeting from the first meeting where anyone was infected.

fileHandle = open(input("Enter file name:  "))

oldInfectedList = []
newInfectedList = []
meetingNum = []

for line in fileHandle:
    words = line.split()
    names = words[1:]  # every person in current line/meeting
    for i in range(len(names)):
        meetingNum = words[0]
        # search for the infected person and people sitting next to the infected
        if names[i][-1] == "*":  # last character in name of current position
            oldInfectedList.append(names[i][0:-1])
            newInfectedList.append(names[i-1])
            newInfectedList.append(names[i+1])

        # round cafe table: to check whether new infected is sitting next to
        # old infected
        if names[i] in oldInfectedList:
            if i+1 > len(names)-1:
                if names[0] in newInfectedList:
                    print(names[0], "in already")
                else:
                    newInfectedList.append(names[0])
            else:
                if names[i+1] in newInfectedList:
                    print(names[i+1], "in already")
                else:
                    newInfectedList.append(names[i+1])
            if i-1 < 0:
                if names[-1] in newInfectedList:
                    print(names[-1], "in already")
                else:
                    newInfectedList.append(names[-1])
            else:
                if names[i-1] in newInfectedList:
                    print(names[i-1], "in already")
                else:
                    newInfectedList.append(names[i-1])

        # clear newInfectedList
        if i == len(names)-1:
            for newInfected in newInfectedList:
                oldInfectedList.append(newInfected)
            newInfectedList.clear()

    if len(oldInfectedList) > 0:
        print(meetingNum, " ".join(oldInfectedList), len(oldInfectedList))
