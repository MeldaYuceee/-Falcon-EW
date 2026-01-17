from jammer import Jammer
from radar import Radar
from simulator import EWSimulator

print("--- Falcon-EW Jammer Training Simulation ---")

radar = Radar()
simulator = EWSimulator(radar)

print(f"Initial Radar Signal Quality: {radar.signal_quality}%")

noise = Jammer("Noise Jammer", "noise", 45, 60)
spot = Jammer("Spot Jammer", "spot", 40, 30)
deceptive = Jammer("Deceptive Jammer", "deceptive", 30, 10)

simulator.run(noise)
simulator.run(spot)
simulator.run(deceptive)
