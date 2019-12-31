import csv
import matplotlib.pyplot as plt
import random


# load irist dataset and put  it into test set and training set

def loadDataset(Trainingfilename,Testfilename, trainingSet=[], testSet=[]):
    ##trainset section
    with open(Trainingfilename, 'rt') as csvfile:
        next(csvfile)
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(len(dataset) ):
            for y in range(1):
                dataset[x][y] = float(dataset[x][y])
                trainingSet.append(dataset[x])
    ##testset section
    with open(Testfilename, 'rt') as csvfile:
        next(csvfile)
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(len(dataset) ):
            for y in range(1):
                dataset[x][y] = float(dataset[x][y])
                testSet.append(dataset[x])

   # print(trainingSet)
   # print(testSet)


#############################
# SIMILARITY CHECK FUNCTION #
#############################

# euclidean distance calcualtion

import math


def euclideanDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        distance += pow((float(instance1[x]) - float(instance2[x])), 2)
    return math.sqrt(distance)


############################################################
# NEIGHBOURS - selecting subset with the smallest distance #
############################################################

import operator


def getNeighbors(trainingSet, testInstance, k):
    distances = []
    length = len(testInstance) - 1
    for x in range(len(trainingSet)):
        dist = euclideanDistance(testInstance, trainingSet[x], length)
        distances.append((trainingSet[x], dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors


######################
# PREDICTED RESPONSE #
######################

import operator


def getResponse(neighbors):
    classVotes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
    return sortedVotes[0][0]


######################
# MEASURING ACCURACY #
######################

def getAccuracy(testSet, predictions):
    correct = 0
    for x in range(len(testSet)):
        if testSet[x][-1] in predictions[x]:
            correct = correct + 1

    return (correct / float(len(testSet)) * 100)


def main():
    # Setup arrays to store train and test accuracies
    neighborsNumber = range(1, 11)
    p_accuracy = []

    # prepare data
    trainingSet = []
    testSet = []
    loadDataset('train.csv',"test.csv", trainingSet, testSet)
    print('Train set: ' + repr(len(trainingSet)))
    print('Test set: ' + repr(len(testSet)))
    print("Please waiting for processing, It will continue about 4 min")
    # generate predictions
    for k in neighborsNumber:
        predictions = []
        for x in range(len(testSet)):
            neighbors = getNeighbors(trainingSet, testSet[x], k)
            result = getResponse(neighbors)
            predictions.append(result)
            # print('> predicted=' + repr(result) + ', actual=' + repr(testSet[x][-1]))
        accuracy = getAccuracy(testSet, predictions)
        print("k:"+str(k))
        print('Accuracy: ' + repr(accuracy) + '%')
        p_accuracy.append(float(accuracy))
        print(p_accuracy)
    # Generate plot
    f = plt.figure()
    plt.title('k-NN: Varying Number of Neighbors')
    plt.plot(neighborsNumber, p_accuracy, label=' Accuracy')
    plt.legend()
    plt.xlabel('Number of Neighbors')
    plt.ylabel('Accuracy')
    plt.show()
    f.savefig("plot.pdf", bbox_inches='tight')

main()