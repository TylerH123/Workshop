import random, sys
def printRandName(dict):
    ##print dict.keys()
    teams = list(dict)
    #print(teams)
    team = teams[random.randint(0,2)]
    ##print team
    ##print len(dict[team])
    ##print(dict[team])
    print(dict[team][(random.randint(0,len(dict[team])-1))])

KREWES = {
    'orpheus': ['Emily', 'Kevin', 'Vishwaa', 'Eric', 'ray', 'Jesse', 'Tiffany', 'Amanda', 'Junhee', 'Jackie', 'Tyler', 'Emory', 'Ivan', 'Elizabeth', 'Pratham'],
    'rex': ['William','Joesph','Calvin','Ethan','Moody'],
    'endymion': ['Grace','Nahi','Derek','Jun Tao','Connor','Jason','Tammy'] }
printRandName(KREWES)
##print(sys.version)
