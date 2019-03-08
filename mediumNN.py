import numpy as numpy


class NeuralNetwork:
    def __init__(self, inp, outp):
        self.inp = inp
        self.outp = outp
        # this creates a matrix with the height of the input as the x and 4 as the y matrix ( height(input) , 4)
        self.weights1 = numpy.random.rand(self.inp.shape[1], 4)
        # for the second layer we only have a 4 x 1 matrix. 
        self.weights2 = numpy.random.rand(4, 1)
        self.outp = outp

    def __sigmoid(self,x):
        return 1/(1 + exp(-x))

    # we calculate the result for the given problem
    def __feedforward(self):
        layer1 = self.__sigmoid(numpy.dot(self.inp, self.weights1))
        return self.__sigmoid(numpy.dot(layer1, self.weights2))
            
    def __backprop(self):    
        
        
    def train(self, iterations):
        return

    def think(self, problem):
        return
