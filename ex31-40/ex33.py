def makeList(threshold):
    i = 0
    numbers = []

    while i < threshold:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    print "The numbers: "

    for num in numbers:
        print num

listSize = 0

print "Hey... you wanna buy a list?"

buyAList = raw_input("> ").lower()

if buyAList == "yes":
    print "How big should it be?"
    listSize = int(raw_input("> "))
    if listSize < 2:
        exit("That's not a list!")
else:
    exit("Suit yourself.")

makeList(listSize)
