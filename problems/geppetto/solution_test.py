import unittest
import sys
import os
import io
solution = __import__("solution")


class SolutionTestCase(unittest.TestCase):
    def test_sample_data(self):
        path = "."

        for item in os.scandir(path):
            if item.name.endswith(".in"):
                in_path = os.path.join(path, item.name)
                answer_path = os.path.join(path, item.name[0:-3] + ".ans")
                if os.path.isfile(answer_path):
                    # run the tests
                    with open(in_path, 'r') as input:
                        with open(answer_path, 'r') as expected:
                            sys.stdout.write("Running test " + item.name)
                            actual = io.StringIO()
                            solution.solve(input, actual)
                            self.assertEqual(expected.read().strip(), actual.getvalue().strip())
                            sys.stdout.write(": passed\n")


if __name__ == '__main__':
    unittest.main()
