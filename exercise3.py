"""
exercise3.py

usage:
python exercise3.py

"""

scores = [85.0, 75.0, 95.0, 110.0, 56.0]

total = 0
for item in scores:
    total += item

print total

#alternative:
print sum(scores)

