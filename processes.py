#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 13:59:48 2017

@author: piotr
"""

from multiprocessing import Process, Queue
import networkx as nx
import time
from random import random

def f(graph):
    time.sleep(15)
    print(nx.info(graph))
def stopien_wierzcholka_graf(graph, q):
    lista=[]
    for x in range(1000000):
        lista.append(random())
    stopien_wierzcholka=nx.degree_centrality(graph)
    q.put(stopien_wierzcholka)
def posrednictwo_graf(graph, q):
    lista=[]
    for x in range(1000000):
        lista.append(random())
    posrednictwo=nx.betweenness_centrality(graph)
    q.put(posrednictwo)
if __name__ == '__main__':
    lista=[]
    q=Queue()
    G=nx.complete_graph(100)
    p = Process(target=f, args=(G,q))
    stopien=Process(target=stopien_wierzcholka_graf, args=(G, q))
    posrednictwo=Process(target=posrednictwo_graf, args=(G, q))
#    slownik_process=Process(target=zwroc_slownik)
    stopien.start()
    posrednictwo.start()
    for i in range(2):
        lista.append(q.get(True))
        
        