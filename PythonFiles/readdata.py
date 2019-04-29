def getRules():
    file = open('newdata.csv', 'r')
    features = []
    conds = []
    x = file.readlines()

    for item in x:
        features.append(item.split(',')[1])
        conds.append(item.split(',')[3])

    features = features[1:-1]
    conds = conds[1:-1]

    for i in range (0,len(conds)):
        conds[i] = (conds[i].replace('&', ','))
        conds[i] = (conds[i].replace('"', ''))
    
    rules = []
    
    for i in range (0, len(features)):
        rules.append([features[i], conds[i]])

    file.close()
    return rules,getDict(features)

def getDict(features):
    featuresDict = {}
    for item in features:
        featuresDict[item] = features.index(item)
    return(featuresDict)




    

