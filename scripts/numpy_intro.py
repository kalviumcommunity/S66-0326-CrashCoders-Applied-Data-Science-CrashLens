"""
NumPy Fundamentals: Creating Arrays, Dimensions, Shape, and Indexing.
This script demonstrates core NumPy functionality for data science.
"""

import numpy as np

def main():
    # 1. Creating NumPy Arrays from Python Lists
    crash_data_list = [102, 345, 233, 98, 412, 187, 305, 521]
    crash_array = np.array(crash_data_list)
    print("--- NumPy Array Creation ---")
    print(f"Original List: {crash_data_list}")
    print(f"NumPy Array:   {crash_array}")
    
    # 2. Understanding Array Shape and Dimensions
    print(f"\n--- Array Properties ---")
    print(f"Shape: {crash_array.shape}")
    print(f"Dimensions: {crash_array.ndim}")
    print(f"Total Elements: {crash_array.size}")
    print(f"Data Type: {crash_array.dtype}")
    
    # 3. Understanding Index Positions
    print(f"\n--- Array Indexing ---")
    print(f"First element (index 0): {crash_array[0]}")
    print(f"Last element (index -1): {crash_array[-1]}")
    print(f"Slice (indices 2 to 5): {crash_array[2:5]}")
    
    # 4. Multi-dimensional Array Example
    multi_dim_data = [[1, 2, 3], [4, 5, 6]]
    matrix = np.array(multi_dim_data)
    print(f"\n--- Matrix Properties ---")
    print(f"Matrix:\n{matrix}")
    print(f"Matrix Shape: {matrix.shape}")
    print(f"Matrix Dimensions: {matrix.ndim}")

if __name__ == "__main__":
    main()
