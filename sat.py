import random, math
from convertArray import convertSat

def sat(fileName):
    vars, statements = convertSat(fileName)
    numVars = len(vars)
    varBoolean = {}

    for i in range(round(math.log(numVars, 2))):
        # Random assign
        for var in vars:
            randomBoolean = random.randint(0,1)
            if randomBoolean == 0:
                varBoolean[var] = False
            else:
                varBoolean[var] = True

        for i in range(numVars):
            invalidState = []
            for statement in statements:
                first, second = statement
        
                firstBoolean = varBoolean[first] if first > 0 else not varBoolean[first * -1]
                secondBoolean = varBoolean[second] if second > 0 else not varBoolean[second * -1]
                if not (firstBoolean or secondBoolean):
                    invalidState.append(statement)
            
            if len(invalidState) == 0:
                return True
            else:
                randomPick = random.randint(0, len(invalidState) -1)
                randomFlip = random.randint(0,1)
                ft, sd = invalidState[randomPick]
                if randomFlip == 0:
                    varBoolean[abs(ft)] = False if varBoolean[abs(ft)] else True
                else:
                    varBoolean[abs(sd)] = False if  varBoolean[abs(sd)] else True
    
    return False
# print(sat('testCase/sat.txt'))
#print(sat('problem_set/course4/sat1.txt')) #ans: True
print(sat('problem_set/course4/sat2.txt'))
# print(sat('problem_set/course4/sat3.txt'))
# print(sat('problem_set/course4/sat4.txt'))


#ans:101100