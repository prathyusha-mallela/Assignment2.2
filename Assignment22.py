# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 22:11:02 2017

@author: Prathyusha Mallela
"""
#assignment 2.2
def print_stars_nested_for(n):
    #increment of * prints
    #outer for loop
    #star='*';
    for i in range(0,n):
        #inner for loop
        for j in range(0,i+1):
            print('*',end='');
            #print(star*j);
        print('\r');
    #decrement of * prints
    #outer for loop
    for i in range((n-1),0,-1):
        #inner for loop
        for j in range(0,i):
            print('*',end='');
            #print(star*j);
        print('\r');

n=5
print_stars_nested_for(5);
