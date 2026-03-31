def main():
    print("--- First Data Analysis Script ---")
    
    # 1. Define variables and small sample data
    data_points = [12, 45, 23, 67, 34, 89, 21]
    print(f"Sample Data: {data_points}")
    
    # 2. Simple calculations
    total_sum = sum(data_points)
    count = len(data_points)
    average = total_sum / count
    max_val = max(data_points)
    min_val = min(data_points)
    
    # 3. Print results to the console
    print("\n--- Analysis Results ---")
    print(f"Total count: {count} data points")
    print(f"Total sum:   {total_sum}")
    print(f"Average:     {average:.2f}")
    print(f"Maximum:     {max_val}")
    print(f"Minimum:     {min_val}")
    
    # Example logic: filter data
    threshold = 40
    filtered_data = [x for x in data_points if x > threshold]
    print(f"\nValues greater than {threshold}: {filtered_data}")
    
    print("\nScript execution completed successfully!")

if __name__ == "__main__":
    main()
