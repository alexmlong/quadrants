import json
from pprint import pprint
import random
import numpy as np

# sigmoid function
def nonlin(x,deriv=False):
    if(deriv==True):
        return x*(1-x)
    return 1/(1+np.exp(-x))
    
def calcBestDecision(trainingData, decisions):
    if len(trainingData) == 0 or random.randint(0, 9) < 2:
        return random.choice(range(9))

## input dataset
    trainingData = np.array(trainingData)
    trainingInputs = trainingData[0:,range(trainingData.shape[1] - 1)]
## output dataset            
    trainingOutputs = trainingData[0:,[trainingData.shape[1] - 1]]

# seed random numbers to make calculation
# deterministic (just a good practice)
    np.random.seed(1)

# initialize weights randomly with mean 0
    syn0 = 2*np.random.random((trainingInputs.shape[1],1)) - 1

    for iter in xrange(10000):

        # forward propagation
        layer0 = trainingInputs
        layer1 = nonlin(np.dot(layer0,syn0))

        # how much did we miss?
        layer1Error = trainingOutputs - layer1

        # multiply how much we missed by the 
        # slope of the sigmoid at the values in layer1
        layer1Delta = layer1Error * nonlin(layer1,True)

        # update weights
        syn0 += np.dot(layer0.T,layer1Delta)

    unknownInput = np.array(decisions).T

    prediction = np.dot(syn0.T, unknownInput)
    return random.choice([k for k, v in enumerate(prediction[0]) if v == max(prediction[0])])

creatures = []
for i in range(20):
    creatures.append({"id": i, "loc": random.randint(0, 8), "data": [], "popOfLastChoice": 0})

pprint(creatures)

worldI = 0
while worldI < 20:
    print worldI
    locCounts = np.array(
            [len([c for c in creatures if c["loc"] == locI])
                for locI in range(9)]) \
            .reshape((3, 3))


    for creature in creatures:
        decisions = [[i, c] for i, c in enumerate(locCounts.flatten())]
        bestDecision = range(9)[calcBestDecision(creature["data"], decisions)]
        creature["popOfLastChoice"] = locCounts.flatten()[bestDecision]
        creature["loc"] = bestDecision

        locCounts = np.array(
                [len([c for c in creatures if c["loc"] == locI])
                    for locI in range(9)]) \
                .reshape((3, 3))

    for creature in creatures:
        reward = 1 * creature["popOfLastChoice"]
        creature["data"].append([creature["loc"], creature["popOfLastChoice"], reward])

    json.dump(creatures, open("creatures.json", "w"))
    worldI += 1
    print locCounts
    pprint(creatures)

pprint(creatures)
print locCounts

decisions = [
    [5,],
    [77,],
    [3,],
    ]

#print decisions[calcBestDecision(trainingData, decisions)]
