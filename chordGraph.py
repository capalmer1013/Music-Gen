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


def createChordGraph(flatStream):
    chords = flatStream.getElementsByClass(chord.Chord)
    k = flatStream.analyze('key')
    scaleNotes = k.chord.notes
    # k.correlationCoefficient
    listOfChords = []
    for i in chords:
        listOfChords.append(i)

    for singleChord in listOfChords:
        listOfRankings = []
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




    return chords