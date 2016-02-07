from music21 import *
import random
import learnMusic
import writeRhythm
import writeNotes
outputStream = stream.Stream()

keys = {'C': 0, 'C#': 7, 'D': 2, 'E-': -3, 'E': 4, 'F': -1, 'F#': 6, 'G': 1, 'A-': -4, 'A': 3, 'B-': -2, 'B': 5}
keyIndex = ['C', 'C#', 'D', 'E-', 'E', 'F', 'F#', 'G', 'A-', 'A', 'B-', 'B']

# assign random key signature
songKey = key.KeySignature(keys[keyIndex[random.randint(0, 11)]])

if random.randint(0, 1) % 2:
    # major
    scaleOfNotes = songKey.getScale('major')
else:
    # minor
    scaleOfNotes = songKey.getScale('minor')

timeSignature = random.randint(3, 4)
timeSignature = str(timeSignature) + '/4'
outputStream.append(meter.TimeSignature(timeSignature))

# listOfNotes.chord._notes
# thats how i wanna get a list of notes cause it's a hackathon

outputStream.append(songKey)
outputStream.append(meter.TimeSignature(timeSignature))

dictOfMeasures = writeRhythm.fillRhythmicDissonance(learnMusic.rhythmMatrix, learnMusic.states, meter.TimeSignature(timeSignature))

listOfMeasures = []
for keyOfDict in dictOfMeasures:
    listOfMeasures.append(keyOfDict)

for measureNumber in listOfMeasures:
    for l in dictOfMeasures[measureNumber]:
        if type(l) is note.Note:
            outputStream.append(l)

writeNotes.adjustNotes(outputStream, learnMusic.noteGraph, learnMusic.noteStates, scaleOfNotes.chord._notes)

outputStream.show()


