#!/bin/usr/python3



def main():
    dic = {'abcd': "Hallo", 12345: (1,7), 12349: 4}
    #123: ((1,7),4), (4,(1,7))
    print(shorter(dic))
    pass

def shorter(dic):
    #erzeuge neues dictionary
    newDic = {}

    #iteriere durch das alte dictionary
    for keyOrig in dic:

        #erstelle den neuen Schlüssel
        strKey = str(keyOrig)[:3]

        #Wenn der neue schlüssel noch nicht im neuen dict enthalten ist
        if strKey not in newDic.keys():

            #füge den alten wert unter dem neuen schlüssel ins neue dict ein
            newDic[strKey] = dic[keyOrig]
        else:
            #Wenn unter dem neuen schlüssel im neuen dict schon ein tupel steht
            if type(newDic[strKey]) is tuple:

                #füge den einzufügenden wert zum bestehenden tupel hinzu und sortiere das tupel
                newDic[strKey] = tuple(sorted(newDic[strKey] + (dic[keyOrig],)))
            else:

                #erstelle ein tupel aus dem bereits unter dem neuen Schlüssel gespeicherten Wert und dem abzuspeichernden Wert
                newDic[strKey] = tuple(sorted((newDic[strKey],dic[keyOrig])))
    return newDic


if __name__ == '__main__':
    main()