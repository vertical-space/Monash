from DNASequence import DNASequence

valid = False

while valid != True:
    input = raw_input("Enter a DNA Sequence:")
    try:
        x = DNASequence(input)
        valid = True
    except:
        print "sequence not valid"

print '\n\n', x.reverse_complement()
