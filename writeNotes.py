from music21 import *
import random

def adjustNotes(musicStream, noteGraph, noteStates, scaleOfNotes):
    currentState = 0
    firstTime = True
    firstNone = True
    previousNote = None
    for element in musicStream:
        if type(element) is note.Note:
            if noteStates[currentState].nextNoteInterval is not None:
                    if firstTime:
                        element.nameWithOctave = scaleOfNotes[0].name + '4'  # 4 when its single part 2 when its all parts
                        nextNote = element.transpose(noteStates[currentState].nextNoteInterval)
                        currentState = findNextState(currentState, noteGraph)
                        firstTime = False
                    else:
                        element.nameWithOctave = nextNote.nameWithOctave
                        if element.transpose(noteStates[currentState].nextNoteInterval).octave > 6 or element.transpose(noteStates[currentState].nextNoteInterval).octave < 2:
                            nextNote = element.transpose(noteStates[currentState].nextNoteInterval*-1)
                        else:
                            nextNote = element.transpose(noteStates[currentState].nextNoteInterval)
                        currentState = findNextState(currentState, noteGraph)
                    previousNote = element.name
            else:
                currentState = 0
                element.nameWithOctave = previousNote+'4'
                nextNote = element.transpose(noteStates[currentState].nextNoteInterval)
                currentState = findNextState(currentState, noteGraph)
                # if firstNone:
                #     element.nameWithOctave = scaleOfNotes[0].name + '4'
                #     firstNone = False
                # else:
                #     del element
            if not checkIfNoteInScale(element, scaleOfNotes): #and random.randint(0,50):
                element.transpose(-1)
                if len(element.pitch.getAllCommonEnharmonics(alterLimit=1)) > 0:
                    element.name = element.pitch.getAllCommonEnharmonics(alterLimit=1)[0].name
                print element.name


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


def checkIfNoteInScale(element, scaleOfNotes):
    for i in scaleOfNotes:
        if i.name == element.name:
            return True

    return False

def trueIfSharp(element, scaleOfNotes):
    for i in scaleOfNotes:
        if i.name == element.name+'#':
            return True
    return False