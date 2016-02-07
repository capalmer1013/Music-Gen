from music21 import *
import random

def adjustNotes(musicStream, noteGraph, noteStates, scaleOfNotes):
    currentState = 0
    firstTime = True
    firstNone = True
    for element in musicStream:
        if noteStates[currentState].nextNoteInterval is not None:
            if type(element) is note.Note:
                if firstTime:
                    element.nameWithOctave = scaleOfNotes[0].name + '4'
                    nextNote = element.transpose(noteStates[currentState].nextNoteInterval)
                    currentState = findNextState(currentState, noteGraph)
                    firstTime = False
                else:
                    element.nameWithOctave = nextNote.nameWithOctave
                    nextNote = element.transpose(noteStates[currentState].nextNoteInterval)
                    currentState = findNextState(currentState, noteGraph)
        else:
            currentState = 0
            nextNote = element.transpose(noteStates[currentState].nextNoteInterval)
            currentState = findNextState(currentState, noteGraph)
            # if firstNone:
            #     element.nameWithOctave = scaleOfNotes[0].name + '4'
            #     firstNone = False
            # else:
            #     del element


def findNextState(currentState, noteGraph):
    randomFloat = random.random()
    for i in range(len(noteGraph[currentState])):
        if noteGraph[currentState][i].getFloat() > 0:
            if noteGraph[currentState][i].getFloat() > randomFloat:
                return i
            else:
                randomFloat = randomFloat - noteGraph[currentState][i].getFloat()