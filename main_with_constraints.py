from dataGenerator.contraints.lengthConstraint import LengthConstraint
from dataGenerator.contraints.regexContraint import RegexConstraint
from dataGenerator.generator import DataGenerator


if __name__ == "__main__":

    generator = DataGenerator()
    generator.addConstraint(RegexConstraint("/ac/"))
    generator.addConstraint(LengthConstraint(6))
    print(generator.generate())