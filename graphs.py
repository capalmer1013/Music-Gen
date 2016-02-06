from music21 import *
import musicAttributes

# Rhythm graph stuff


def createRhythmGraph(flatStream):
    dictOfTime = musicAttributes.getTimeSignatures(flatStream)
    dictOfRhythmicDissonances = measureRhythmicDissonance(flatStream, dictOfTime)



def measureRhythmicDissonance(flatStream, timeSigs):
    listOfNotes = []
    listOfOffsets = []
    dictOfNotes = {}
    dictOfDissonances = {}

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
            runningCount = 0
            for i in tempMeasureList:
                runningCount += noteRhythmicDissonance(i, timeSigs)

            if len(tempMeasureList) > 0:
                measureDissonance = runningCount/len(tempMeasureList)
            else:
                # maybe it should be 1 I dont know
                measureDissonance = 0
            tempMeasureList[:] = []
            tempMeasureList.append(element)
            dictOfDissonances[currentMeasure] = measureDissonance
            # get the next measure started

    return dictOfDissonances
    # return list of rhythmic dissonances for measures


def noteRhythmicDissonance(noteElement, timeSigs):
    timeOffsets = []
    for i in timeSigs:
        timeOffsets.append(i)

    timeOffsets.sort(reverse=True)

    for i in timeOffsets:
        # grab the highest time signature that is at or below the
        if timeSigs[i].offset <= noteElement.offset:
            currentTimeSignature = timeSigs[i]
            break

    # TODO handle other denominators like 8
    # possibly not now that I'm gonna try to use beat strengths

    # if currentTimeSignature.numerator % 2 == 0:
    #     # even time signature
    #
    # else:
    #     # probably an odd time signature

    # really it returns beat consonance
    # 1 - 0 ! being most consonant 0 being most dissonant.
    # really this may need rewritten but who knows
    return noteElement.beatStrength