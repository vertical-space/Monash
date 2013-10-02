class Rodent:
    def __init__(self, tag_id):
        self.tag_id = tag_id
        self.weights = []
        
    def plot(self):
        return self.tag_id[0]
        
    def add_weight(self,weight):
        self.weights.append(float(weight)) 

rodents = {}
for line in open("rodents.csv"):
    tag_id, weight = line.split(',')
    if tag_id not in rodents:
        my_rodent = Rodent(tag_id)
        my_rodent.add_weight(weight)
        rodents[tag_id] = my_rodent
    else:
        rodents[tag_id].add_weight(weight)

print rodents

for key in rodents:
    print rodents[key].tag_id, rodents[key].weights
