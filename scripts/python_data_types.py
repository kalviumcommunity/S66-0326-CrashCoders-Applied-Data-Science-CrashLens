def main():
    print("--- 1. Working with Numeric Data Types ---")
    
    # Integers and floating-point numbers
    total_samples = 150        # integer representing count
    average_speed = 45.5       # float representing speed in km/h
    
    print(f"Total samples: {total_samples}")
    print(f"Average speed: {average_speed} km/h")
    
    # Basic arithmetic and division
    distance = total_samples * average_speed
    print(f"Total simulated distance (samples * speed): {distance}")
    
    # Observing division (always returns float in Python 3)
    half_samples = total_samples / 2
    print(f"Half samples (Standard Division): {half_samples}")
    
    # Integer division
    exact_half_samples = total_samples // 2
    print(f"Half samples (Integer Division): {exact_half_samples}\n")
    
    print("--- 2. Understanding String Data Types ---")
    
    # Creating string variables
    dataset_name = "Crash Statistics 2026"
    region = "North District"
    
    # Concatenating strings
    full_title = dataset_name + " - " + region
    print(f"Dataset Title: {full_title}")
    
    # Accessing string values
    print(f"First character of dataset name: '{dataset_name[0]}'")
    print(f"First word of dataset name: '{dataset_name.split()[0]}'\n")
    
    print("--- 3. Mixing Numbers and Strings Safely ---")
    
    # Intentional conversion to prevent errors
    # Incorrect way: combined_info = region + total_samples (Would cause TypeError)
    
    # Safe conversion numbers to strings
    combined_info = region + " has " + str(total_samples) + " samples documented."
    print("Safe string concatenation:", combined_info)
    
    # Safe conversion strings to numbers
    string_number = "1024"
    numeric_value = int(string_number)
    print(f"String converted to int, doubled: {numeric_value * 2}\n")
    
    print("--- 4. Inspecting Data Types ---")
    
    # Checking types during execution
    print(f"Type of total_samples (150): {type(total_samples)}")
    print(f"Type of average_speed (45.5): {type(average_speed)}")
    print(f"Type of dataset_name ('Crash Statistics 2026'): {type(dataset_name)}")
    print("Type awareness guarantees your variables behave as expected!")

if __name__ == "__main__":
    main()
