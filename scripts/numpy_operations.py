"""
NumPy Fundamentals: Performing Basic Mathematical Operations on NumPy Arrays.
This script demonstrates element-wise and aggregate math operations for data analysis.
"""

import numpy as np

def main():
    # 1. Element-wise operations
    initial_impacts = np.array([20.5, 45.0, 12.8, 88.3, 35.1, 56.4])
    print("--- Original Impact Magnitudes ---")
    print(initial_impacts)
    
    # Multiplying by a scalar (e.g., universal safety multiplier)
    safety_factor = 1.15
    increased_impacts = initial_impacts * safety_factor
    print(f"\nIncreased Impacts (Factor {safety_factor}):\n{increased_impacts.round(2)}")
    
    # Adding a constant offset (e.g., baseline sensor noise)
    baseline_noise = 2.0
    adjusted_impacts = initial_impacts + baseline_noise
    print(f"\nAdjusted Impacts (Baseline +{baseline_noise}):\n{adjusted_impacts.round(2)}")
    
    # 2. Aggregate Mathematical Operations
    print("\n--- Aggregate Statistics ---")
    print(f"Total Combined Impact: {np.sum(initial_impacts):.2f}")
    print(f"Mean Impact Score:     {np.mean(initial_impacts):.2f}")
    print(f"Maximum Recorded:      {np.max(initial_impacts):.2f}")
    print(f"Minimum Recorded:      {np.min(initial_impacts):.2f}")
    print(f"Standard Deviation:    {np.std(initial_impacts):.2f}")
    
    # 3. Array-to-Array Operations
    weights = np.array([0.8, 1.2, 0.9, 1.5, 1.0, 1.1])
    weighted_results = initial_impacts * weights
    print("\n--- Weighted Analysis (Impact * Weight) ---")
    print(f"Weighted Scores: {weighted_results.round(2)}")

if __name__ == "__main__":
    main()
