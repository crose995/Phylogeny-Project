import random
import readdata

rules, features = readdata.getRules()

def readrule(rule):
    rule = rule.replace('¬', 'not ')
    rule = rule.replace(',', ' and')
    rule = rule.replace('+', '("+" == ')
    rule = rule.replace('-', '("-" == ')
    for key, value in features.items():
        rule = rule.replace(key, 'lang['+str(value)+'])') 
    
    return rule

def assign():
    x = random.randint(0,1)
    if x:
        return '-'
    else:
        return '+'
    
def generate(rules):
    lang = ['?']*len(rules)
    for rule in rules:
        feature = features[rule[0]]
        if rule[1] == "":
           lang[feature] = assign()
        else:
            cond = readrule(rule[1])
            if eval(cond):
                lang[feature] = assign()
            else:
                lang[feature] = '0'
    return lang

def genMul(num):
    file = open('langout.txt', 'w')
    for i in range (0,num):
        file.write(str(generate(rules)))
        file.write('\n')
    file.close()







