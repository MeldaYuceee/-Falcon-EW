class EWSimulator:
    def __init__(self, radar):
        self.radar = radar

    def run(self, jammer):
        print("\n⚠️ Jammer Activated:", jammer.name)

        self.radar.apply_jammer(jammer)

        print(f"Radar Signal Quality: {self.radar.signal_quality:.1f}%")
        print(
            "Classification:",
            self.radar.classify_interference(jammer.jammer_type)
        )

        if self.radar.signal_quality > 0:
            print("System Status: Degraded but Operational")
        else:
            print("System Status: Mission Failed")
