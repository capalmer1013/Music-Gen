from music21 import *
import random


def createMeasuresOfRhythm(rhythmMatrix, states, timeSignature):
    stream1 = stream.Stream()

    stateProgression = getStateProgression(rhythmMatrix, states)

    for state in stateProgression:
        i = states.index(state)
        for noteLength in states[i]:
            if 'dotted' in noteLength.lower():
                stream1.append(note.Note('B-4', type=noteLength.lower()[7:], dots=1))
            else:
                stream1.append(note.Note('B-4', type=noteLength.lower()))

    return stream1


def getStateProgression(rhythmMatrix, states):
    currentState = 0
    stateProgression = []
    stateProgression.append(states[0])

    while currentState != len(states)-1:
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
