from music21 import *
import random


def fillRhythmicDissonance(rhythmMatrix, states, timeSignature):
    listOfRhythmicDissonances = createRhythmicProgression(rhythmMatrix, states)
    dictOfMeasures = {}

    for i in range(len(listOfRhythmicDissonances)):
        measureList = []
        tempBeatStrength = 1
        tempNote = note.Note('B-4')
        measureList.append(tempNote)

        while True:

            stream1 = stream.Stream()
            stream1.append(timeSignature)
            for item in measureList:
                stream1.append(item)

            if getMeasuresRhythmicDissonance(stream1) < listOfRhythmicDissonances[i]*.90:
                tempNote = note.Note('B-4')
                measureList.append(tempNote)
                tempBeatStrength = tempBeatStrength * 1.5
                measureList.append(tempNote)
            elif getMeasuresRhythmicDissonance(stream1) > listOfRhythmicDissonances[i]*1.10:
                tempNote = note.Note('B-4')
                tempNote.offset += 1
                measureList.append(tempNote)
                tempBeatStrength = tempBeatStrength * .5

            stream1 = stream.Stream()
            stream1.append(timeSignature)
            for item in measureList:
                stream1.append(item)

            if getMeasuresRhythmicDissonance(stream1) < listOfRhythmicDissonances[i]*.90 or getMeasuresRhythmicDissonance(measureList) > listOfRhythmicDissonances[i]*1.10:
                break
        dictOfMeasures[i] = measureList





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