#!Clustering Algorithms

## Design clustering algorithms here to
## be tested on the data.

## Each clustering algorithm should be specified
## as a function that takes as arguments
## a list of longitude coordinates, a list of
## latitude coordinates and the longitude and
## latitude coordinates of the city, and returns
## a list of "clusters", each cluster being a list
## of indices of the coordinates involved...


## imports:
import math
from sklearn.cluster import KMeans
import numpy as np
import os

## used to find distances between points:
import geopy
from geopy import distance

import csv

## function to translate between
## cluster labels and nested indices
def labels_to_index(cluster_labels):
    cluster_indices=[]
    for label in list(set(cluster_labels)):
        cluster_index = (cluster_labels==label).nonzero()[0].tolist()
        cluster_indices.append(cluster_index)
    return cluster_indices

## here's k-means clustering as an example of
## how to construct the clustering algorithm
def k_means_clustering(lngs,lats,city_lng,city_lat):
    ## scale the longitudinal axis to appriximate
    ## cartesian coordinates...
    lngs = np.array(lngs)*math.cos(city_lat)

    ## using n_issues/5 to determine k
    ## not the most objective method, but its a start...
    kmeans = KMeans(n_clusters=int(len(lngs)/5.))
    kmeans.fit(np.array([lngs,lats]).transpose())

    cluster_labels = np.array(kmeans.labels_)
    ## use labels_to_index function to get
    ## output from cluster labels...
    return labels_to_index(cluster_labels)

def mcl(lngs,lats,city_lng,city_lat):
    ## generate graph
    graph=[]
    used_inds=[]
    for i in range(len(lngs)):
        for j in range(i,len(lngs)):
            distance=geopy.distance.vincenty(
					tuple(lngs[i],lats[i]]),
					tuple(lngs[j],lats[j])).feet
            if distance<200
                graph.append[[i,j,distance]]
    with open("mcl_data/mcl_input_data.tsv","w") as f:
		for row in graph:
			f.write(str(row[0])+"\t"+str(row[1])+"\t"+str(row[2])+"\n")
    "mcl mcl_data/mcl_input_data.tsv --abc -o mcl_data/mcl_output_data.tsv"
    output_data=[]
    with open("mcl_data/mcl_output_data.tsv","r") as f:
        tsvin = csv.reader(tsvin,delimiter='\t')
        for row in tsvin:
            output_data.append(row)
    return output_data
