"""
Universidad del Valle de Guatemala
Seccion 10
Ing. Cristian Castro
Mario Perdomo  18029
NearestNeighbors.py
Proposito: Modelo Nearest Neighbour para ubicacion de imagenes
"""
import os
from os.path import join
from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt
import numpy as np

#Nearest neighbout model used by the main
class NearestNeighborsModel:
    def __init__(self):
        currentDirectory = os.path.dirname(__file__)
        self.path = os.path.join(currentDirectory,'DB')
        #10 neighbours for the model
        self.model = NearestNeighbors(n_neighbors=10)
        #the iamges founded
        self.images = []
        #images dictionary that includes the name
        self.imagesNames = {}

    def trainModel(self):
        images = os.listdir(self.path)
        counter = 0
        for img in images:
            #Gets the 
            imageName = plt.imread(os.path.join(self.path,img))
            #Pixels equal de 1920000 are functional to this program.
            if imageName.size == 1920000:
                #Reshappes the image's pixels arrays in one whole array with 
                #an arrange of pixel by pixel of 1600 x 1200
                image = np.reshape(imageName,(1600*1200))
                self.images.append(image)
                #gets the name archive of the image
                self.imagesNames[counter] = img
                #repeats
                counter += 1
        #tranining data is assamble for all for photos
        self.model.fit(self.images)

    def searchImage(self,path):
        image = plt.imread(path)
        if image.size == 1920000:
            #Same function as the reshape of the training function
            image = [np.reshape(image,(1600*1200))]
            #Here, we look for the k-neighbours of the model, without returning the distance
            #We're only interested in the index
            results = self.model.kneighbors(image,10,return_distance=False)
            resultArr = []
            for result in results[0]:
                #Here, we get the indexes of the orde rof each image and appened on resultArr
                x = self.imagesNames[result]
                resultArr.append(x)
            return resultArr
        else:
            return []
