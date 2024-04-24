#!/usr/bin/env python3

import random
import json

# Import the methods to fuzz from their respective modules
from method1 import add as method1
from method2 import subtract as method2
from method3 import multiply as method3
from method4 import divide as method4
from method5 import concatenate_strings as method5

# Load the input data from blns.json
with open('blns.json', 'r') as f:
    input_data = json.load(f)

# List of methods to fuzz
methods_to_fuzz = [method1, method2, method3, method4, method5]

# Fuzzes each method in methods_to_fuzz with random inputs and checks for bugs
def fuzz_methods():
    # Iterate over the methods and fuzz each one
    for method in methods_to_fuzz:
        # Select a random input from the loaded data
        random_input = random.choice(input_data)

        # Generate two random values
        if method.__name__ in ['add', 'subtract', 'multiply', 'divide']:
            input_a = random.choice(input_data)
            input_b = random.choice(input_data)
            # Attempt to call the method with the generated inputs
            try:
                result = method(input_a, input_b)
            except Exception as e:
                # If an exception occurs, report it
                report_bug(method.__name__, random_input, f"Error occurred: {e}")
                continue

        # Check if the result contains any unexpected behavior (e.g., exceptions, crashes, incorrect output)
        if is_bug_detected(method.__name__, random_input, result):
            # Report the bug or log the issue
            report_bug(method.__name__, random_input, result)


# Checks if the result of the method indicates a bug.
def is_bug_detected(method_name, input_data, result):

    if method_name == 'add':
        # Check if the result is the sum of the input numbers
        return result != input_data[0] + input_data[1]

    elif method_name == 'subtract':
        # Check if the result is the difference of the input numbers
        return result != input_data[0] - input_data[1]

    elif method_name == 'multiply':
        # Check if the result is the product of the input numbers
        return result != input_data[0] * input_data[1]

    elif method_name == 'divide':
        # Check if dividing by zero raises a ValueError
        if input_data[1] == 0:
            return not isinstance(result, ValueError)
        # Check if the result is the quotient of the input numbers
        return result != input_data[0] / input_data[1]

    elif method_name == 'concatenate_strings':
        # Check if the result is the concatenation of the input strings
        return result != input_data[0] + input_data[1]

    else:
        # If the method name is not recognized, assume no bug detected
        return False

# Reports a bug detected in a method
def report_bug(method_name, input_data, result):
    print(f"Bug detected in method {method_name}:")
    print(f"Input data: {input_data}")
    print(f"Result: {result}")
    print("Please investigate and fix the issue.")

# Entry point to run the fuzzing process
if __name__ == "__main__":
    fuzz_methods()
