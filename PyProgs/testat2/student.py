def readcsv(filename, *filterstrings):
    file = open(filename,"r")
    lines = file.readlines()
    file.close()
    headersLine = lines[0][:-1]
    allHeader = headersLine.split(";")
    headingsWithNumbers = {}
    filteredHeaders = []
    colDicts = []

    for i,heading in enumerate(allHeader):
        if any([True for x in filterstrings if x in heading]):
            filteredHeaders.append(heading)
            headingsWithNumbers[i] = heading

    lengths = [len(el) for el in lines[0][:-1].split(";")]

    for line in lines:
        for i, element in enumerate(line[:-1].split(";")):
            lengths[i] = max([lengths[i], len(element)])

    for line in lines[1:]:
        colDicts.append({})
        for col, heading in headingsWithNumbers.items():
            elements = line[:-1].split(";")
            if col >= len(elements):
                colDicts[-1][heading] = "".ljust(lengths[col])
            else:
                colDicts[-1][heading] = elements[col].ljust(lengths[col])


    return(filteredHeaders, colDicts)
    pass