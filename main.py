import re

with open('essay.txt', 'r') as file:
    essaystr = file.read()

class ZipfLaw:
    def __init__(self, string: str):
        self.string = string
        self.words = [i.lower() for i in re.findall(r'(\b[A-Za-z][a-z]{2,9}\b)', self.string)]
        self.frequency = {}
        self.counts = []
    def getRank(self):
        for i in self.words:
            if i in self.frequency:
                self.frequency[i] += 1
            else:
                self.frequency[i] = 1
        for i in self.frequency:
            self.counts.append(frequency[i])
        return self.counts.sort(reverse=True)
    def plotRank(self):
        pass
    def exportJSON(self):
        pass

test = ZipfLaw(string=essaystr)
print(test.getRank())

