"""
exercise4.py

usage:
python exercise4.py

"""

infile = 'uniprot_sprot.fasta'

input = open (infile, 'r').readlines()

count = 0

for line in input:
    if ">" in line and "OS=Homo sapiens" in line:
        count += 1

print count
# count = 20272

# alternative:
# less uniprot_sprot.fasta | grep ">" | grep sapiens | wc -l



input2 = open(infile, 'r').read().split(">")

best = 0
name = ""
for item in input2:
    lines = item.split("\n")
    head = lines[0]
    tail = ''.join(lines[1:]
    if len(tail) > best:
        best = len(tail)
        name = head

print "longest protein:", best
print "name:", name

    
