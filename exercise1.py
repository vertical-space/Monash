"""
even.py

usage:
python even.py int

"""



from sys import argv
input = argv[1]

if int(input) % 2 == 0:
    print 'even'
else:
    print 'odd'
    
