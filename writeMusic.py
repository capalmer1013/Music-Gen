from music21 import *
import random
import learnMusic
import writeRhythm

outputStream = stream.Stream()

keys = {'C': 0, 'C#': 7, 'D': 2, 'E-': -3, 'E': 4, 'F': -1, 'F#': 6, 'G': 1, 'A-': -4, 'A': 3, 'B-': -2, 'B': 5}
keyIndex = ['C', 'C#', 'D', 'E-', 'E', 'F', 'F#', 'G', 'A-', 'A', 'B-', 'B']

# assign random key signature
songKey = key.KeySignature(keys[keyIndex[random.randint(0, 11)]])

if random.randint(0, 1) % 2:
    # major
    listOfNotes = songKey.getScale('major')
else:
    # minor
    listOfNotes = songKey.getScale('minor')

# listOfNotes.chord._notes
# thats how i wanna get a list of notes cause it's a hackathon

outputStream.append(songKey)

writeRhythm.fillRhythmicDissonance(learnMusic.rhythmMatrix, learnMusic.states)

#outputStream.show()


