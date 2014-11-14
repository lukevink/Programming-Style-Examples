class ElectionResults:
  
    def __init__(self, filename):
        self.filename = filename

    def load(self):
        self.file = open(self.filename, 'r')
        self.all_lines = self.file.readlines()[1:]

    def states(self):
        all_names = []
        for line in self.all_lines:
            columns = line.split(',')
            votes = str(int(columns[3]) + int(columns[5]))
            line = str(columns[1]+ " : " + votes)
            all_names.append(line)
        return all_names[0:]

    def votes(self):
        all_votes = []
        for line in self.all_lines:
            columns = line.split(',')
            votes = int(columns[3]) + int(columns[5])
            all_votes.append(votes)
        return all_votes[0:]

    def state_count(self):
        return len(self.states())

  

