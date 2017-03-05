import unittest
import sys
import os
solution = __import__("solution")

class SolutionTestCase(unittest.TestCase):
    def test_sampledata(self):
        solution.main()

        path = os.path.join("data")

        for item in os.scandir(path):
            if item.name.endswith(".in"):
                in_path = os.path.join(path, item.name)
                answer_path = os.path.join(path, item.name[0:-3] + ".ans")
                if os.path.isfile(answer_path):
                    print(answer_path)
                    self.assertTrue(self,"wee!")


if __name__ == '__main__':
    unittest.main()
