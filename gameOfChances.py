#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 16:47:17 2018

@author: nithish k
"""

import  itertools as itr
import sys

"""
I have genearlised such that for any number of dies this works 
and you also have an option to define different probababilities of the states in thhe diess to take care of biased dies
This also works when you roll dies having more than 6 sides , i.e n sides
PLease pass the cmd line arguments, if the die faces are 1, 3 and 4 just pass cmd argument as '134'
"""
try:
    input_state = sys.argv[1] # give input string as the die states 666
    input_state = [int(i) for i in input_state]
except:
    input_state = [3,3,4] # change here

    

numDies = len(input_state)
diePositions = [i for i in range(numDies)]
# change the number of sides here if you need
eachDieStates = [1,2,3,4,5,6]
# change for a biased die
probOfEachState = {1:1/6,2:1/6,3:1/6,4:1/6,5:1/6,6:1/6}



def maxChoose():

    pass

def variableTimesProb(eachState,rollCombination): 
    # eachstate  = (die1,die2,die3...) and rollCom = pisitons (0,2)
    #check for all positions equal , then return 25
#    intersectionProb = [eachState[i]*probOfEachState[eachState[i]] if i in rollCombination else 1*eachState[i] for i in range(numDies) ]
    
    if len(set(eachState)) == 1 :
        randomVar = 25
    else:
        randomVar = sum(eachState)   
        
    probabiltyOfState = 1
    for i in range(numDies):
        if i in rollCombination:
            probabiltyOfState = probabiltyOfState * probOfEachState[eachState[i]]
        else :
            probabiltyOfState = probabiltyOfState * 1 ##sure probability
        
    #return expected value for each state
    return randomVar*probabiltyOfState  


def minChoose():
    pass


def MinMaxSuccessors(state):
    ##combinatioons of dies I could roll
    allCombs = []
    for i in range(numDies+1): #iterate till all the dies
        #all posible positions that could be changed
         allCombs.append([i for i in itr.combinations(diePositions,i)])
    ##reduce complexity
    return [i for i in itr.chain.from_iterable(allCombs)] # list of tuples

def chanceSucc(state,rollCombination):
#    constantPositions = list(set(diePositions)-set(rollCombination))
#    #think for any number of dies 
#    constantPositions.sort()
    #prepare tuple arange constant and non constant items roll combination is already sorted
    args = tuple((eachDieStates if i in rollCombination else [state[i]] for i in range(numDies)))
    allCartProducts = itr.product(*args)
    return [i for i in allCartProducts]


#
#chanceSucc((1,2,3),(1,2))
def expectedValue(states,rollCombination):
    # sigma(X*f(x))
    return sum([variableTimesProb(state,rollCombination) for state in states])



# for each minmax successor generate chance succeosrs, for each chance successor generate expected value
def getBestMove(state,player = 'Max'):
    possibleCombinationOfRolls = MinMaxSuccessors(state)
    if player == 'Max':
        AllExpectedValues = []
        for roll in possibleCombinationOfRolls:
            
            AllExpectedValues.append(expectedValue(chanceSucc(state,roll),roll))
            
        ##get the maximum
        
#        return AllExpectedValues,possibleCombinationOfRolls
        return possibleCombinationOfRolls[AllExpectedValues.index(max(AllExpectedValues))]
            
print("Working to get the best move")
bestPossibleRoll =  getBestMove(input_state)
#"-".join(map(str,bestPossibleRoll))
print("Please choose to roll die/s in the position : ")
if bool(bestPossibleRoll):
    print([i+1 for i in bestPossibleRoll])
else: 
    print("Dont roll any die")            
            
            
            