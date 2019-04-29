from scipy.stats import chisquare
from generate import features



def getCounts(feature):
    file = open("langout.txt", 'r')
    index = features[feature]
    vals = []
    for line in file:
        lang = (eval(line))
        vals.append(lang[index])
        
    counts = [0,0,0]
    for item in vals:
        if item == '+':
            counts[0] += 1
        elif item == '-':
            counts[1] += 1
        else:
            counts[2] += 1
    file.close()
    print(counts)
    return counts


def chi():
    outfile = open("chiout.txt", 'w')
    for feature in features:
        counts = getCounts(feature)
        outfile.write(feature)
        outfile.write(str(counts))
        outfile.write(str(chisquare(counts)))
        outfile.write('\n')
   
    outfile.close()

chi()
