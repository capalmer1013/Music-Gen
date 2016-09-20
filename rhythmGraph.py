from music21 import *
import objects

# Rhythm graph stuff
states = []
startingStates = {}

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

    states = getRhythmicStates(flatStream)

    # second pass create edges
    # adjacency matrix[exit node][enter node]
    adjacencyMatrix = [[0 for x in range(len(states)+1)] for x in range(len(states)+1)]

    for i in range(len(adjacencyMatrix)):
        for j in range(len(adjacencyMatrix)):
            adjacencyMatrix[i][j] = objects.rational()

    # should make a square adjacency matrix
    for i in measureNumbers:
        if i > 1:
            try:
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
            except KeyError:
                print 'damn a key error fuck it'

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
