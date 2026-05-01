from simulator import PhaseSingularitySimulator
from parameters import PARAMS

# 1. Initialize Simulator
sim = PhaseSingularitySimulator(PARAMS)

# 2. Generate Signal and Analyze Trajectory
signal = sim.generate_cheyne_stokes()
d_phase, singularities = sim.analyze_trajectory(signal)

# 3. Output Results (Example target bitstream)
target_bitstream = [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
error_rate = sim.calculate_ber(singularities, target_bitstream)

print(f"Simulation Successful.")
print(f"Target Bitrate: {PARAMS['bit_rate']/1e9} Gbps")
print(f"Measured BER: {error_rate:.4f}")
