leading = " " * 3
blank = " " * 4
wire = "-" * 4
resistor_side = "v^v^"
left = "|   "
right = "   |"
terminal_pos = "  _ + "
terminal_neg = "  - - "


class Circuit:

    def __init__(self, power="5 V", load="5 Ohm"):
        """

        :type power: str
        :type load: str
        """
        self.power = power.split(" ")[0]  # ditch the units, assume V
        self.comp = [load.split(" ")[0]]  # ditch the units, assume Ohm
        self.equiv = int(self.comp[0])
        self.schematic = [leading + blank + self.comp[0] + blank * 3,
                          leading + blank + "Ohm" + blank * 3,
                          leading + wire + resistor_side + wire * 3,
                          leading + left + blank * 3 + right,
                          self.power + terminal_pos + blank * 3 + right,
                          "V" + terminal_neg + blank * 3 + right,
                          leading + left + blank * 3 + right,
                          leading + wire * 5]

        if len(self.power) > 1:
            self.schematic[4] = self.schematic[4][0:2] + self.schematic[4][3:]

    def draw(self):
        for line in self.schematic:
            print(line)

    def addComp(self, new_comp):
        self.comp.append(new_comp.split(" ")[0])   # ditch the units
        self.schematic[0] = self.schematic[0][0:15] + self.comp[-1]
        self.schematic[1] = self.schematic[1][0:15] + "Ohm"
        self.schematic[2] = self.schematic[2][0:15] + resistor_side + wire
        self.equiv = sum(int(resistor) for resistor in self.comp)


    def calc(self, variable):
        if variable == "R":
            return self.equiv
        elif variable == "V":
            return self.power
        elif variable == "I":
            return int(self.power) / self.equiv

    def summarize(self):

        print(f"Resistance is {c.calc('R')} Ohm")
        print(f"Voltage is {c.calc('V')} V")
        print(f"Current is {c.calc('I'):.3f} A")


c = Circuit(power="10 V", load="10 Ohm")
c.draw()
c.summarize()
c.addComp("10 Ohm")
c.draw()
c.summarize()