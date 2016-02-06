from music21 import *
import musicAttributes

# Rhythm graph stuff


def createRhythmGraph(flatStream):
    dictOfTime = musicAttributes.getTimeSignatures(flatStream)
    listOfRhythmicDissonances = measureRhythmicDissonance(flatStream, dictOfTime)


# def createRhythmGraph(flatStream):
#
#
# def noteRhythmicDissonance(note):


def measureRhythmicDissonance(flatStream, timeSigs):
    listOfNotes = []
    listOfOffsets = []
    dictOfNotes = {}

    for element in flatStream:
        if isinstance(element, note.Note) or isinstance(element, chord.Chord):
            listOfNotes.append(element)

    for element in listOfNotes:
        dictOfNotes[element.offset] = element

    for i in dictOfNotes:
        listOfOffsets.append(i)

    listOfOffsets.sort()

    # measureNumber
    currentMeasure = dictOfNotes[listOfOffsets[0]].measureNumber
    tempMeasureList = []

    for offset in listOfOffsets:
        element = dictOfNotes[offset]
        if element.measureNumber == currentMeasure:
            tempMeasureList.append(element)
        else:
            currentMeasure = element.measureNumber
            # figure out the rhythmic dissonance for the previous measure
            for i in tempMeasureList:
                noteRhythmicDissonance(i, timeSigs)
            # get the next measure started

    heresAlist = []
    return heresAlist
    # return list of rhythmic dissonances for measures


def noteRhythmicDissonance(noteElement, timeSigs):

