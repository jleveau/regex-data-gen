from coverage.annotate import os

from dataGenerator.contraints.MaxLength import MaxLength
from dataGenerator.contraints.MinLength import MinLength
from dataGenerator.contraints.RegexContraint import RegexConstraint
from dataGenerator.generator import DataGenerator
import time


def printData(data) -> str:
    s = ""
    i = 0
    for test_data in data:
        s += "TEST CAST " + str(i) + "\n"
        s += "CONSTRAINTS \n"
        s += test_data[0]
        s += "DATA TEST \n"
        s += test_data[1]
        s += '\n\n\n'
        i += 1
    return s

if __name__ == "__main__":

    start_time = time.time()

    generator = DataGenerator()
    generator.addConstraint(MinLength(6))
    generator.addConstraint(MaxLength(30))
    generator.addConstraint(RegexConstraint("/([[:alpha:]])*/"))

    data = generator.generate()
    print("--- %s seconds ---" % (time.time() - start_time))

    file = open(os.path.join("output", "data.txt"), "w")
    file.write(printData(data))
    file.close()

