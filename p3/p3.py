import random


#1
def knapsack(V, W, MAX, popSize, mut, maxGen, percent):
    generation = 0
    pop = generate(V, popSize) #2
    fitness = getFitness(pop, V, W, MAX) #3
    while (not test(fitness, percent) and generation < maxGen): #4
        generation += 1
        pop = newPopulation(pop, fitness, mut) #5
        fitness = getFitness(pop, V, W, MAX) #6
    # print fitness
    # print generation
    return str(selectElite(pop, fitness))+" Fitness is "+str(selectEliteW(pop, fitness))

#2
def generate(V, popSize):
    length = len(V)
    pop = [[random.randint(0, 1) for i in range(length)] for j in range(popSize)]
    # print pop
    return pop

#3,   #6
def getFitness(pop, V, W, MAX):
    fitness = []
    for i in range(len(pop)):
        weight = 0
        volume = MAX + 1
        while (volume > MAX):
            weight = 0
            volume = 0
            ones = []
            for j in range(len(pop[i])):
                if pop[i][j] == 1:
                    volume += V[j]
                    weight += W[j]
                    ones += [j]
            if volume > MAX:
                pop[i][ones[random.randint(0, len(ones) - 1)]] = 0
        fitness += [weight]
    print ("Modified Population:")
    print(pop)
    print("Fitness of Population:")
    print( fitness)
    return fitness

#4
def test(fit, rate):
    maxCount = mode(fit)
    if float(maxCount) / float(len(fit)) >= rate:
        return True
    else:
        return False
#4.1
def mode(fit):
    values = set(fit)
    maxCount = 0
    for i in values:
        if maxCount < fit.count(i):
            maxCount = fit.count(i)
    return maxCount

#5
def newPopulation(pop, fit, mut):
    popSize = len(pop)
    newPop = []
    newPop += [selectElite(pop, fit)] #5.1
    print("Elite:")
    print(newPop)
    while (len(newPop) < popSize):
        (mate1, mate2) = select(pop, fit) #5.2
        newPop += [mutate(crossover(mate1, mate2), mut)] #5.3,  #5.4

    print("After Selection")
    print(newPop)
    return newPop

#5.1,   #7
def selectElite(pop, fit):
    elite = 0
    for i in range(len(fit)):
        if fit[i] > fit[elite]:
            elite = i
    return pop[elite]

def selectEliteW(pop, fit):
    elite = 0
    for i in range(len(fit)):
        if fit[i] > fit[elite]:
            elite = i
    return fit[elite]



#5.2
##Roulette-wheel
def select(pop, fit):
    size = len(pop)
    totalFit = sum(fit)
    lucky = random.randint(0, totalFit)
    tempSum = 0
    mate1 = []
    fit1 = 0
    for i in range(size):
        tempSum += fit[i]
        if tempSum >= lucky:
            mate1 = pop.pop(i)
            fit1 = fit.pop(i)
            break
    tempSum = 0
    lucky = random.randint(0, sum(fit))
    for i in range(len(pop)):
        tempSum += fit[i]
        if tempSum >= lucky:
            mate2 = pop[i]
            pop += [mate1]
            fit += [fit1]
            return (mate1, mate2)


def tournament_selection(pop, K):
    """
    Takes population list of binary lists and tournament size and returns a winning binary list.
    """
    tBest = 'None'
    P = len(pop)
    for i in range(K):
        contestant = pop[random.randint(0, P-1)]
        if (tBest == 'None') or vFitness(contestant) > vFitness(tBest):
            tBest = contestant[:]
    return tBest




#5.3
def crossover(mate1, mate2):
    lucky = random.randint(0, len(mate1) - 1)
    # print "Lucky: " + str(lucky)
    return mate1[:lucky] + mate2[lucky:]


#5.4
def mutate(gene, mutate):
    for i in range(len(gene)):
        lucky = random.randint(1, mutate)
        if lucky == 1:
            # print "MUTATED!"
            gene[i] = bool(gene[i]) ^ 1
    return gene




##main
volume = [135, 139, 149, 150, 156, 163, 173, 184, 192, 201, 210, 214, 221, 229, 240]
weights = [70, 73, 77, 80, 82, 87, 90, 94, 98, 106, 110, 113, 115, 118, 120]
maxVolume = 750
popSize = 20
mut = 1
maxGen = 20
percent = 0.8

#print(crossover(volume, weights))
#print(mutate([1, 1, 1, 1, 1, 1, 1, 1, 1]))

print("FINAL SOLUTION: " + str(knapsack(volume, weights, maxVolume, popSize,2,10,50)))