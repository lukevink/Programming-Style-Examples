# Verify that we can open and read the election results CSV correctly
# Showing a "test-driven" style

from electiondata import ElectionResults
import unittest

class ElectionResultsTest(unittest.TestCase):

    def setUp(self):
        self.results = ElectionResults('electiondata.py')

    def testVotes(self):
        self.results.load()
        votes = self.results.votes()
        #Check that the first state is correct
        #Check with teacher why this syntax is incorrect (and object oriented.py)
        assert all_votes[0] == 212930
        


# if this file is run directly, run the tests
if __name__ == "__main__":
    unittest.main()
