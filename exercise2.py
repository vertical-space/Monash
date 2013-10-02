"""
intsize.py

usage:
python intsize.py int

"""



from sys import argv
input = argv[1]

if 0 < int(input) < 50:
    print 'Minor'
elif 50 < int(input) < 1000:
    print 'Major'
else:
    print 'Severe'
    
