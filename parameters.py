# Optimized physical parameters for Gbps performance
PARAMS = {
    "fermi_level": 0.5,         # eV: Maximizes phase transition sharpness
    "relaxation_time": 0.2e-12,  # 0.2 ps: Suppresses jitter for high-speed switching
    "group_index": 30,          # Enhances nonlinear interaction via slow-light
    "nonlinearity_sigma": 1.2,  # Nonlinear coefficient for singularity formation[cite: 2]
    "bit_rate": 10e9            # Target base rate: 10 Gbps[cite: 2]
}
