"""
Python and NumPy Fundamentals for CrashLens Project.
This script demonstrates core Python and NumPy concepts using crash data examples.
Tasks: List/Tuple/Dict, Conditionals, Loops, Functions, PEP8, NumPy Fundamentals.
"""

import numpy as np

def categorize_severity(impact_value):
    """
    Categorizes the severity of a crash based on its impact value.
    Demonstrates: Functions, Conditional Statements, and Result Returning.
    """
    if impact_value >= 80:
        return "Critical"
    elif impact_value >= 50:
        return "Major"
    elif impact_value >= 20:
        return "Minor"
    else:
        return "Negligible"

def process_crash_data(crash_list):
    """
    Processes a list of crash impact values and returns categorized results.
    Demonstrates: Lists, Loops (for), and Function calls.
    """
    results = []
    for impact in crash_list:
        severity = categorize_severity(impact)
        results.append(severity)
    return results

def simulate_data_threshold(start_value, threshold):
    """
    Simulates decreasing impact values until a threshold is met.
    Demonstrates: While Loops and Data Logic.
    """
    current_value = start_value
    steps = 0
    while current_value > threshold:
        current_value -= 5
        steps += 1
    return steps

def run_numpy_analysis(data_list):
    """
    Performs numerical analysis using NumPy on the provided data.
    Demonstrates: NumPy Arrays, Shapes, Dimensions, Indexing, and Math Operations.
    """
    # 1. Creating NumPy Arrays from Python Lists
    impact_array = np.array(data_list)
    
    print("\n--- NumPy Analysis ---")
    # 2. Understanding Array Shape, Dimensions, and Index Positions
    print(f"Array: {impact_array}")
    print(f"Shape: {impact_array.shape}")
    print(f"Dimensions: {impact_array.ndim}")
    print(f"First Element (Index 0): {impact_array[0]}")
    print(f"Last Element (Index -1): {impact_array[-1]}")
    
    # 3. Performing Basic Mathematical Operations on NumPy Arrays
    # Scaling all impact values by 1.1 (e.g., adding a safety factor)
    scaled_impacts = impact_array * 1.1
    print(f"Scaled Impacts (* 1.1): {scaled_impacts.round(2)}")
    
    # Calculating mean and total impact
    print(f"Mean Impact: {np.mean(impact_array):.2f}")
    print(f"Total Impact Sum: {np.sum(impact_array)}")

def main():
    """
    Main entry point for the script.
    Demonstrates: Code structuring for readability and reuse.
    """
    print("--- CrashLens: Python & NumPy Fundamentals ---")
    
    # 1. Working with Python Lists, Tuples, and Dictionaries
    # List of impact values
    impact_values = [15, 42, 88, 55, 10, 95, 30] 
    
    # Tuple representing metadata (immutable)
    crash_metadata = ("Region-A", "2026-Q1", "Sector-7")
    
    # Dictionary mapping crash IDs to their respective impact
    crash_records = {
        "CR-001": 15,
        "CR-002": 42,
        "CR-003": 88
    }
    
    print(f"\nMetadata: {crash_metadata}")
    print(f"Sample Records Dict: {crash_records}")
    
    # 2. Processing Data with Functions and Logic
    severity_categories = process_crash_data(impact_values)
    print(f"\nProcessed Severities: {severity_categories}")
    
    # 3. Running while loop simulation
    initial_impact = 40
    limit = 12
    steps_needed = simulate_data_threshold(initial_impact, limit)
    print(f"\nSimulation: Starting at {initial_impact}, it took {steps_needed} steps to drop below {limit}.")
    
    # 4. Running NumPy Analysis
    run_numpy_analysis(impact_values)
    
    print("\nExecution complete. All tasks demonstrated successfully!")

if __name__ == "__main__":
    main()
