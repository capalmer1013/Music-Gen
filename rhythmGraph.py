from music21 import *
import musicAttributes
import objects

# Rhythm graph stuff
states = []


def createRhythmGraph(flatStream):
    measureNumbers = []

    # old stuff
    # dictOfTime = musicAttributes.getTimeSignatures(flatStream)
    # dictOfRhythmicDissonances = measureRhythmicDissonance(flatStream, dictOfTime)

    dictOfRhythmicDissonances = getRhythmicDissonances(flatStream)
    for i in dictOfRhythmicDissonances:
        measureNumbers.append(i)

    measureNumbers.sort()
    # # first pass create states
    # for i in measureNumbers:
    #     if dictOfRhythmicDissonances[i] not in states:
    #         states.append(dictOfRhythmicDissonances[i])

    # create states wow look at that 1 line
    states = getRhythmicStates(flatStream)

    # second pass create edges
    # adjacency matrix[exit node][enter node]
    adjacencyMatrix = [[0 for x in range(len(states))] for x in range(len(states))]

    for i in range(len(adjacencyMatrix)):
        for j in range(len(adjacencyMatrix)):
            adjacencyMatrix[i][j] = objects.rational()

    # should make a square adjacency matrix
    for i in measureNumbers:
        if i > 1:
            previousState = dictOfRhythmicDissonances[i-1]
            currentState = dictOfRhythmicDissonances[i]
            if adjacencyMatrix[states.index(previousState)][states.index(currentState)].denominator == -1:
                adjacencyMatrix[states.index(previousState)][states.index(currentState)].numerator += 1
                for column in adjacencyMatrix[states.index(previousState)]:
                    column.denominator = 1
            else:
                adjacencyMatrix[states.index(previousState)][states.index(currentState)].numerator += 1
                for column in adjacencyMatrix[states.index(previousState)]:
                    column.denominator += 1


    # for row in adjacencyMatrix:
    #     for column in row:
    #         print str(column.numerator) + '/' + str(column.denominator)
    #     print "-----------------------------------------"
    return adjacencyMatrix


def getRhythmicDissonances(flatStream):
    returnDict = {}
    currentMeasureNumber = 1
    currentMeasure = []
    for element in flatStream:
        if element.measureNumber == currentMeasureNumber or element.measureNumber is None:
            if isinstance(element, note.Note) or isinstance(element, chord.Chord):
                currentMeasure.append(element.duration.fullName)

        else:
            if len(currentMeasure) > 0:
                returnDict[currentMeasureNumber] = currentMeasure

            currentMeasureNumber = element.measureNumber
            currentMeasure = []
            if isinstance(element, note.Note) or isinstance(element, chord.Chord):
                    currentMeasure.append(element.duration.fullName)

    returnDict[currentMeasureNumber] = currentMeasure
    return returnDict


def getRhythmicStates(flatStream):
    stateList = []
    currentMeasureNumber = 1
    currentMeasure = []
    for element in flatStream:
        if element.measureNumber == currentMeasureNumber or element.measureNumber is None:
            if isinstance(element, note.Note) or isinstance(element, chord.Chord):
                currentMeasure.append(element.duration.fullName)

        else:
            if len(currentMeasure) > 0:
                if currentMeasure not in stateList:
                    stateList.append(currentMeasure)
            currentMeasureNumber = element.measureNumber
            currentMeasure = []
            if isinstance(element, note.Note) or isinstance(element, chord.Chord):
                    currentMeasure.append(element.duration.fullName)
    if currentMeasure not in stateList:
        stateList.append(currentMeasure)
    return stateList

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
            dictOfDissonances[currentMeasure-1] = measureDissonance
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