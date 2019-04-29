from generate import *

lang = generate(rules)


def consistent(lang, rule):
    cond = readrule(rule[1])
    feature = lang[features[rule[0]]]
    if cond == '':
        return True    
    if not eval(cond):
        if feature != '0':
            return False
    elif feature == '0':
        return False
    return True

def fconsistent(lang, rules):
    
    for rule in rules:
        if not consistent(lang, rule):
            return False
    return True

