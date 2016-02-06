from music21 import *


# def createRhythmGraph(flatStream):
#
#
# def noteRhythmicDissonance(note):


def measureRhythmicDissonance(flatStream, timeSigs):
    listOfNotes = []
    dictOfNotes = {}

    for element in flatStream:
        if isinstance(element, note.Note) or isinstance(element, chord.Chord):
            listOfNotes.append(element)

    for element in listOfNotes:
        dictOfNotes[element.offset] = element

    # return list of rhythmic dissonances for measures
