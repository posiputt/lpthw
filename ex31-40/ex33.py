def makeList(threshold, increment):
    i = 0
    numbers = []

    for i in range(0, threshold, increment):
        print "At the top i is %d" % i
        numbers.append(i)

        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    print "The numbers: "

    for num in numbers:
        print num

listSize = 0
increment = 1

print "Hey... you wanna buy a list?"

buyAList = raw_input("> ").lower()

if buyAList == "yes":
    print "How big should the biggest number be?"
    listSize = int(raw_input("> "))
    if listSize < 2:
        exit("That's not a list!")
    print "By how much should I increment between elements?"
    increment = int(raw_input("> "))
    if increment < 1:
        exit("I will not increment by that number, it is scratched.")
else:
    exit("Suit yourself.")

makeList(listSize, increment)
