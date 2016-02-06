from music21 import *
import objects
toneChords = [[0, 2, 4], [1, 3, 5], [2, 4, 6], [3, 5, 7], [4, 6, 1], [5, 7, 2], [6, 1, 3]]

tonic = []
supertonnic = []
mediant = []
subdominant = []
dominant = []
submendiant = []
leadingtone = []

chordDegree = {}

def createChordGraph(flatStream):
    chords = flatStream.getElementsByClass(chord.Chord)
    k = flatStream.analyze('key')
    scaleNotes = k.chord._notes
    # k.correlationCoefficient
    listOfChords = []
    for i in chords:
        listOfChords.append(i)

    for singleChord in listOfChords:
        listOfRankings = []
        listOfRankingsFloat = []
        for chordFunction in toneChords:
            matchingNotes = objects.rational()
            for tempPitch in singleChord.pitchNames:
                for scaleDegree in chordFunction:
                    if tempPitch == scaleNotes[scaleDegree].name:
                        if matchingNotes.denominator == -1:
                            matchingNotes.denominator = 1
                            matchingNotes.numerator += 1
                        else:
                            matchingNotes.denominator += 1
                            matchingNotes.numerator += 1
                    else:
                        matchingNotes.denominator += 1
            listOfRankings.append(matchingNotes)
        for e in listOfRankings:
            listOfRankingsFloat.append(e.getFloat())
        if listOfRankingsFloat.index(max(listOfRankingsFloat)) not in chordDegree:
            chordDegree[listOfRankingsFloat.index(max(listOfRankingsFloat))] = []
            chordDegree[listOfRankingsFloat.index(max(listOfRankingsFloat))].append(singleChord)
        else:
            chordDegree[listOfRankingsFloat.index(max(listOfRankingsFloat))].append(singleChord)

    adjacencyMatrix = [[0 for x in range(len(toneChords))] for x in range(len(toneChords))]
    for i in range(len(adjacencyMatrix)):
        for j in range(len(adjacencyMatrix)):
            adjacencyMatrix[i][j] = objects.rational()


    print "BALLS"



    return chords