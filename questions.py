from pprint import pprint as pp
from random import uniform

class Question:

    def __init__(self, stem, expression="m*v"):
        """

        :param stem: a str of the question stem
        :param ranges: a list of ranges of values for each variable in the stem
        :param expression: a str of a math expression computing the answer
        """
        self._stem = stem
        self._expression = expression

        #self._limits = []
        self._values = {}
        self.parse()
        self._answer = self.calc_answer()

    def calc_answer(self):
        return None

    def randomize(self):
        for variable, limits in self._limits:
            precision = min(len(str(limits[0]).split('.')[1]),  # precision of low limit
                            len(str(limits[1]).split('.')[1]))  # precision of high limit
            #TODO: use precision variable in this
            self._values.update({variable: uniform(limits[0], limits[1])})


    def parse(self):
        """
        sets self._limits to a list of tuples for each variable
        :return:
        """
        self._limits = {line[0:line.find(':')]:   # variable name is the dict key
                            (float(line[line.find(':') + 2:line.find(',')]),  # first number in ordered pair
                             float(line[line.find(',') + 2:line.find(']]')]))  # second number
                        for line in self._stem.split('[[') if ']]' in line}  # first line in split is part of stem

        #self.expression =

q = Question("what is [[a: 1.3, 1.5]] times [[b: 4.5, 4.9]]?", "a*b")
pp(q._limits)
print(q._expression)