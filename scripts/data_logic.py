"""
Python Fundamentals: Writing Conditional Statements for Data Logic.
This script demonstrates how to use if, elif, and else statements to process crash data.
"""

def main():
    # Sample crash severity value (range 0 to 100)
    impact_severity = 72
    
    print(f"Analyzing Crash with Severity Score: {impact_severity}")
    
    # Using Conditional Statements (if-elif-else) to categorize severity
    if impact_severity >= 90:
        category = "Critical"
        print("ALERT: Immediate emergency response required.")
    elif impact_severity >= 70:
        category = "High"
        print("Note: Significant damage localized; medical attention needed.")
    elif impact_severity >= 40:
        category = "Moderate"
        print("Note: Damage detected; standard protocol applies.")
    else:
        category = "Low"
        print("Note: Minor impact; monitoring only.")
        
    print(f"\nFinal Classification: {category}")
    
    # Logical Operators in Conditionals
    hazard_present = True
    speed_mph = 65
    
    print(f"\nContextual Check: Hazard={hazard_present}, Speed={speed_mph} mph")
    if hazard_present and speed_mph > 60:
        print("Warning: High-risk condition detected.")
    elif hazard_present or speed_mph > 60:
        print("Caution: Elevated risk factors present.")
    else:
        print("All parameters within normal safety range.")

if __name__ == "__main__":
    main()
