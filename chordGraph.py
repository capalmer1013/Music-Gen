from music21 import *
tonic = [0, 2, 4]
supertonnic = [1, 3, 5]
mediant = [2, 4, 6]
subdominant = [3, 5, 7]
dominant = [4, 6, 7]
submendiant = [5, 7, 1]
leadingtone = [6, 1, 2]


def createChordGraph(flatStream):
    chords = flatStream.getElementsByClass(chord.Chord)
    k = flatStream.analyze('key')
    scaleNotes = k.chord._notes
    # k.correlationCoefficient
    listOfChords = []
    for i in chords:
        listOfChords.append(i)

    for singleChord in listOfChords:
        for i in singleChord.pitchNames:
            

    return chords