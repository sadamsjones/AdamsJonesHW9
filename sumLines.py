# sumLines.py
 
"""
sumLines.py - A script that reads a text file, computes the sum, number of integers, and the average of all numbers.

Usage:
  python3 sumLines.py <filename>

Example:
  python3 sumLines.py dataInput.txt

Where sum = 917, Number of Elements = 26, and Average = 35.26923076923077
"""

import sys
file_path = "/home/debian/datainput.txt"
def process_file(file_path):
    """
    Process the given file to compute the sum, number of integers, and the average of all numbers.

    Args:
        file_path (str): Path to the input text file.

    Returns:
        tuple: A tuple containing the sum, number of integers, and the average.
    """
    try:
        with open(file_path, 'r') as file:
            total_sum = 0
            num_elements = 0

            # Iterate through each line in the file
            for line in file:
                # Split the line into a list of integers
                numbers = list(map(int, line.split()))

                # Update total_sum and num_elements
                total_sum += sum(numbers)
                num_elements += len(numbers)
 # Calculate the average
            average = total_sum / num_elements if num_elements > 0 else 0

            return total_sum, num_elements, average

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

def main():
    # Check if the correct number of command line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python3 sumLines.py <filename>")
        sys.exit(1)

    file_path = sys.argv[1]

    # Process the file and get the result
    result = process_file(file_path)

    # Print the result
    print(f"Where sum = {result[0]}, Number of Elements = {result[1]}, and Average = {result[2]}")

if __name__ == "__main__":
    main()

