from music21 import *
import random


def fillRhythmicDissonance(rhythmMatrix, states):
    listOfMeasures = []
    listOfRhythmicDissonances = createRhythmicProgression(rhythmMatrix, states)

    for i in range(len(listOfRhythmicDissonances)):
        while getMeasuresRhythmicDissonance(listOfMeasures[i]) < listOfRhythmicDissonances[i]*.90 or getMeasuresRhythmicDissonance(listOfMeasures[i]) > listOfRhythmicDissonances[i]*1.10:
            if getMeasuresRhythmicDissonance(listOfMeasures[i]) < listOfRhythmicDissonances[i]*.90

            elif getMeasuresRhythmicDissonance(listOfMeasures[i]) > listOfRhythmicDissonances[i]*1.10:
            listOfMeasures.append()


def createRhythmicProgression(rhythmMatrix, states):
    currentState = 0
    stateProgression = []
    stateProgression.append(states[0])

    while currentState != len(rhythmMatrix)-1:
        randomFloat = random.random()
        for i in range(len(rhythmMatrix[currentState])):
            if rhythmMatrix[currentState][i].getFloat() > 0:
                if rhythmMatrix[currentState][i].getFloat() > randomFloat:
                    currentState = i
                    stateProgression.append(states[i])
                    break
                else:
                    randomFloat = randomFloat - rhythmMatrix[currentState][i].getFloat()
    return stateProgression


def getMeasuresRhythmicDissonance(listOfNotes):
    numerator = 0
    denominator = -1
    for e in listOfNotes:
        if denominator == -1:
            denominator = 1
            numerator += e.beatStrength
        else:
            numerator += e.beatStrength
            denominator += 1

    return float(numerator)/float(denominator)