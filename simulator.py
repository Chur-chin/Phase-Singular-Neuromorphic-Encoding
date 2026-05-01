import numpy as np

class PhaseSingularitySimulator:
    """Simulator for Phase Singularity detection in nonlinear 2D materials[cite: 2]"""
    
    def __init__(self, p):
        self.p = p
        self.dt = 1e-13  # 0.1 ps resolution
        self.time = np.arange(0, 1e-9, self.dt)

    def generate_cheyne_stokes(self, freq=20e9):
        """Generates the nonlinear envelope collapse pattern[cite: 2]"""
        # Periodic 'Apnea-like' suppression for data mapping[cite: 2]
        envelope = (1 + np.sin(2 * np.pi * freq/10 * self.time)) * \
                   np.sin(2 * np.pi * freq * self.time)
        return np.maximum(0, envelope)

    def analyze_trajectory(self, signal):
        """Analyzes the stability of the singularity trajectory[cite: 2]"""
        # Calculate nonlinear phase shift based on intensity[cite: 2]
        phase = np.cumsum(self.p["nonlinearity_sigma"] * (signal**2) * self.dt)
        d_phase_dt = np.gradient(phase, self.dt)
        
        # Detection at the Extraction Point (Group velocity min, Phase jump max)[cite: 2]
        threshold = np.max(d_phase_dt) * 0.7
        return d_phase_dt, d_phase_dt > threshold

    def calculate_ber(self, detected_singularities, target_bits):
        """Computes Bit Error Rate (BER)[cite: 2]"""
        samples_per_bit = int((1/self.p["bit_rate"]) / self.dt)
        detected_bits = []
        for i in range(len(target_bits)):
            chunk = detected_singularities[i*samples_per_bit : (i+1)*samples_per_bit]
            detected_bits.append(1 if np.any(chunk) else 0)
        return np.mean(np.array(detected_bits) != np.array(target_bits))
