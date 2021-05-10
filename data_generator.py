import random

def randomSubset(size=25, jump=1):
    result=[]
    for i in range(0, size+1, jump):
        result.append(random.sample(range(i),i))
    return result

def ascendingSubset(size=25, jump=1):
    result=[]
    for i in range(0, size+1, jump):
        result.append(sorted(random.sample(range(i),i)))
    return result

def descendingSubset(size=25, jump=1):
    result=[]
    for i in range(0, size+1, jump):
        result.append(sorted(random.sample(range(i),i),reverse=True))
    return result

def constantSubset(size=25, jump=1):
    result=[]
    for i in range(0, size+1, jump):
        result.append([random.randint(0,size)]*i)
    return result

def vShapedSubset(size=25,jump=1):
    result=[]
    for i in range(0, size+1, jump):
        result.append(sorted(random.sample(range(i),i//2),reverse=True)+sorted(random.sample(range(i),i//2)))
    return result

def aShapedSubset(size=25,jump=1):
    result=[]
    for i in range(0, size+1, jump):
        result.append(sorted(random.sample(range(i),i//2))+sorted(random.sample(range(i),i//2),reverse=True))
    return result