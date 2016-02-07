from music21 import *
import random


def fillRhythmicDissonance(rhythmMatrix, states, timeSignature):
    listOfRhythmicDissonances = createRhythmicProgression(rhythmMatrix, states)
    dictOfMeasures = {}
    offset = .25
    for i in range(len(listOfRhythmicDissonances)):
        stream1 = stream.Stream()
        stream1.append(timeSignature)
        maxTries = 7
        increase = 1
        decrease = .5
        while getMeasuresRhythmicDissonance(stream1) != listOfRhythmicDissonances[i]+offset and maxTries > 0:
            if getMeasuresRhythmicDissonance(stream1) > listOfRhythmicDissonances[i]+offset:
                if random.randint(0, 8):
                    tempNote = note.Note('B-4')
                    tempNote.offset = increase
                else:
                    tempNote = note.Note('B-4', type='half')
                    tempNote.offset = 0
                decrease += 1
                stream1.append(tempNote)
                maxTries -= 1
            elif getMeasuresRhythmicDissonance(stream1) < listOfRhythmicDissonances[i]+offset:
                tempNote = note.Note('B-4', type='eighth')
                tempNote.offset = decrease
                increase += 1
                stream1.append(tempNote)
                # print 'thing happened' + str(decrease)
                maxTries -= 1

        dictOfMeasures[i] = stream1
    return dictOfMeasures





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
    if len(listOfNotes) > 0:
        for e in listOfNotes:
            if denominator == -1:
                denominator = 1
                numerator += e.beatStrength
            else:
                numerator += e.beatStrength
                denominator += 1

    return float(numerator)/float(denominator)