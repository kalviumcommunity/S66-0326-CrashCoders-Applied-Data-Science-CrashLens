"""
Python Fundamentals: Defining and Calling Functions, Passing Data, and Results.
This script demonstrates functions for modular and reusable crash data analysis.
"""

def calculate_impact_force(mass, velocity_initial, velocity_final, time_delta):
    """
    Calculates the average impact force of a collision.
    Demonstrates: Defining functions, passing multiple parameters, and return values.
    """
    # Force = Mass * (Delta Velocity) / Delta Time
    delta_v = velocity_initial - velocity_final
    if time_delta <= 0:
        return 0.0
    
    force = (mass * delta_v) / time_delta
    return round(force, 2)

def generate_report(crash_id, force_result):
    """
    Format a simple report based on crash ID and calculated force.
    Demonstrates: Functions for data logic and reuse.
    """
    report = f"Crash ID: {crash_id}\nEstimated Impact Force: {force_result} Newtons"
    
    if force_result > 5000:
        report += "\nSeverity Note: High Force Impact detected."
    else:
        report += "\nSeverity Note: Standard Force Impact detected."
        
    return report

def main():
    """
    Main entry point to execute the analysis logic.
    Demonstrates: Structuring code for readability (PEP8 Basics).
    """
    print("--- Vehicle Collision Analysis Software ---\n")
    
    # Example 1: Calculating impact for Crash-A
    # Data: 1500kg car, 30 m/s to 0 m/s in 0.2 seconds
    case_a_id = "CRA-001"
    case_a_force = calculate_impact_force(1500, 30, 0, 0.2)
    
    # Example 2: Generating and printing the report
    case_a_report = generate_report(case_a_id, case_a_force)
    print(case_a_report)
    
    print("\nProcessing complete for current simulation.")

if __name__ == "__main__":
    main()
