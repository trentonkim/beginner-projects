bottleNumber = 99

while bottleNumber > 1:
    print(str(bottleNumber) + " bottles of beer on the wall, " + str(bottleNumber) + " bottles of beer. Take one down, pass it around.")
    bottleNumber = bottleNumber - 1

if bottleNumber == 1:
    print(str(bottleNumber) + " bottle of beer on the wall, " + str(bottleNumber) + " bottle of beer. Take it down, pass it around.")
    bottleNumber = bottleNumber - 1

if bottleNumber == 0:
    print(str(bottleNumber) + " bottles of beer on the wall, " + str(bottleNumber) + " bottles of beer. We've taken them down, and passed them around; now we're drunk and passed out!")
    bottleNumber = bottleNumber - 1