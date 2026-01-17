class Jammer:
    def __init__(self, name, jammer_type, power, bandwidth):
        self.name = name
        self.jammer_type = jammer_type
        self.power = power
        self.bandwidth = bandwidth

    def interference_level(self):
        if self.jammer_type == "noise":
            return (self.power * self.bandwidth) / 100

        elif self.jammer_type == "spot":
            return (self.power * self.bandwidth) / 150

        elif self.jammer_type == "deceptive":
            return (self.power * 20) / 100

        return 0
