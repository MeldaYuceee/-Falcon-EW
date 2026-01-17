class Radar:
    def __init__(self):
        self.signal_quality = 100

    def apply_jammer(self, jammer):
        interference = jammer.interference_level()
        self.signal_quality -= interference

        if self.signal_quality < 0:
            self.signal_quality = 0

    def classify_interference(self, jammer_type):
        if jammer_type == "deceptive":
            return "Suspicious Signal Behavior"

        if self.signal_quality > 70:
            return "Normal Operation"
        elif 40 < self.signal_quality <= 70:
            return "Possible Noise Jamming"
        else:
            return "High Interference Detected"
