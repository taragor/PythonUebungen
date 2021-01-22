#!/usr/bin/python3


import string

def main():
    pass

def check_format(doc):
    lines = doc.splitlines()
    if lines[0][0:14] != "\\input texinfo":
        return (None,1)

    linesBeforeText = []

    for line in lines[1:]:
        if len(line)> 0:
            if line[0] != "@":
                break
            linesBeforeText.append(line)

    if len(list(filter(lambda x: x[0:10] == "@settitle ", linesBeforeText))) == 0:
        return (None, 2)

    if lines[-1] != "@bye":
        return (None, 3)

    zeilen = len(list(filter(lambda x: False if len(x)<=0 else x[0] != "@", lines[1:])))
    
    befehle = [x.split(" ")[0][1:] for x in lines if len(x)>0 and x[0]=="@"]

    dic = {}
    for befehl in befehle:
        dic[befehl] = dic.get(befehl,0)+1



    return (zeilen, dic)





def check_structure(doc):
    lines = doc.split("\n")

    stack = []
    liste = []

    endBefehle = list(map(lambda x: x[5:], filter(lambda x: x.startswith("@end "), lines)))

    for i in range(0, len(lines)):
        if lines[i].startswith("@"):
            befehl = lines[i]
            if befehl[1:] in endBefehle:
                stack.append(befehl[1:])
                liste.append(befehl[1:])
            elif befehl.startswith("@end "):
                if len(stack) == 0:
                    return(None, i)
                letzterBefehl = stack.pop()
                if letzterBefehl != befehl.split(" ")[1]:
                    return(None, i)



    return (True, list(sorted(liste)))

if __name__ == "__main__":
    pass


