from music21 import *
import random


def adjustNotesNormal(musicStream, noteGraph, noteStates):
    currentState = 0
    i = 0
    for element in musicStream:
        if type(element) is stream.Stream:
            for songNote in element:
                i += 1
                if type(songNote) is note.Note:
                    if i == len(element)-1:
                        songNote.nameWithOctave = noteStates[len(noteStates)-1]
                    else:
                        songNote.nameWithOctave = noteStates[currentState]
                    currentState = findNextState(currentState, noteGraph)

def findNextState(currentState, noteGraph):
    randomFloat = random.random()
    for i in range(len(noteGraph[currentState])):
        if noteGraph[currentState][i].getFloat() > 0:
            if noteGraph[currentState][i].getFloat() > randomFloat:
                return i
            else:
                randomFloat = randomFloat - noteGraph[currentState][i].getFloat()
