"""
Python Fundamentals: Working with Lists, Tuples, and Dictionaries.
This script demonstrates the creation and use of core Python data structures.
"""

def main():
    # 1. Lists: Ordered and mutable collection of items
    # Represents a list of crash impact magnitudes
    impact_list = [25.5, 40.2, 10.8, 88.0, 55.4]
    print(f"Initial Impact List: {impact_list}")
    
    # Modifying the list (mutability)
    impact_list.append(12.3)
    print(f"Updated Impact List (added member): {impact_list}")
    
    # 2. Tuples: Ordered and immutable records
    # Represents metadata for a specific dataset
    dataset_metadata = ("CrashLens_v1", "2026-04-01", "Region-North")
    print(f"\nDataset Metadata (Tuple): {dataset_metadata}")
    # dataset_metadata[0] = "New_Version"  # This would raise a TypeError
    
    # 3. Dictionaries: Key-Value pairs for structured data
    # Mapping crash hazard codes to their descriptions
    hazard_descriptions = {
        "H01": "Frontal Collision",
        "H02": "Side Impact",
        "H03": "Rollover"
    }
    print(f"\nHazard Descriptions (Dictionary): {hazard_descriptions}")
    print(f"Description for H02: {hazard_descriptions['H02']}")
    
    # Adding a new entry to the dictionary
    hazard_descriptions["H04"] = "Rear-end Collision"
    print(f"Updated Hazard Descriptions: {hazard_descriptions}")

if __name__ == "__main__":
    main()
