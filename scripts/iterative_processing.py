"""
Python Fundamentals: Using for and while Loops for Iterative Data Processing.
This script demonstrates how to process collections of data using loops.
"""

def main():
    # 1. Processing a list of crash impact scores with a 'for' loop
    impact_scores = [12, 45, 67, 23, 89, 34, 56]
    print(f"Original Impact Scores: {impact_scores}")
    
    threshold = 50
    high_impact_count = 0
    
    print(f"\nScanning for impacts above {threshold}:")
    for score in impact_scores:
        if score > threshold:
            print(f"High-impact detected: {score}")
            high_impact_count += 1
        else:
            print(f"Minor impact: {score}")
            
    print(f"Total High Impact Scores Found: {high_impact_count}")
    
    # 2. Simulating distance decay during impact with a 'while' loop
    initial_velocity = 60
    stop_velocity = 5
    current_velocity = initial_velocity
    deceleration_steps = 0
    
    print(f"\nSimulating vehicle deceleration (Target = {stop_velocity} mph):")
    while current_velocity > stop_velocity:
        # Simulate velocity reduction per unit of time/distance
        current_velocity -= 12
        deceleration_steps += 1
        print(f"Step {deceleration_steps}: Velocity = {current_velocity} mph")
        
    print(f"Deceleration Simulation complete in {deceleration_steps} steps.")

if __name__ == "__main__":
    main()
