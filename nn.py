from pprint import pprint
import random
import numpy as np

# sigmoid function
def nonlin(x,deriv=False):
    if(deriv==True):
        return x*(1-x)
    return 1/(1+np.exp(-x))
    
def calcBestDecision(trainingData, decisions):
## input dataset
#trainingInputs = np.array([
    trainingInputs = trainingData[0:,range(trainingData.shape[1] - 1)]
#                [0,0,1],
#                [0,1,1],
#                [1,0,1],
#                [1,1,1],
#                ])
#    
## output dataset            
#trainingOutputs = np.array([[0,0,1,1]]).T
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
    return list(prediction[0]).index(max(prediction[0]))

trainingData = np.array([
        [20, 10],
        [40, 20],
        [10, 5],
        [2, 1]
        ])

creatures = []
for i in range(10):
    creatures.append({"loc": random.randint(0, 8), "data": trainingData})

worldI = 0
while worldI < 10:
    print worldI
    locCounts = np.array(
            [len([c for c in creatures if c["loc"] == locI])
                for locI in range(9)]) \
            .reshape((3, 3))

    print locCounts

    for creature in creatures:
        decisions = [[c, ] for c in locCounts.flatten()]
        bestDecision = calcBestDecision(creature["data"], decisions)

        try:
            creature["loc"] = range(9)[bestDecision]
        except:
            import ipdb
            ipdb.set_trace()

    worldI += 1
    pass

pprint(creatures)

decisions = [
    [5,],
    [77,],
    [3,],
    ]

print decisions[calcBestDecision(trainingData, decisions)]
