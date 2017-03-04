import sys
import os
from shutil import copyfile

arguments = sys.argv
if len(arguments) != 2:
    print("Missing problem name")
    print("Usage: init.py problem_name")
    quit()

problem_name = arguments[1]
print("Fetching problem: " + problem_name)

# create a directory structure for the problem under this
problem_path = os.path.join(".", problem_name)
if(os.path.exists(problem_path)):
    print("Problem already initialized")
    quit()

os.makedirs(problem_path)

test_path = os.path.join(problem_path, "tests")

copyfile(os.path.join(".", "solution.py"), os.path.join(problem_path, "solution.py"))
copyfile(os.path.join())


# download the test data
# launch IDE