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
with open('Fuzz/blns.json', 'r') as f:
    input_data = json.load(f)

# List of methods to fuzz
methods_to_fuzz = [method1, method2, method3, method4, method5]


# Fuzzes each method in methods_to_fuzz with random inputs and checks for bugs
def fuzz_methods():
    # Iterate over the methods and fuzz each one
    for method in methods_to_fuzz:

        # Generate two random values
        if method.__name__ in ['add', 'subtract', 'multiply', 'divide', 'concatenate_strings']:
            input_a = random.choice(input_data)
            input_b = random.choice(input_data)
            error = None
            # Attempt to call the method with the generated inputs
            try:
                result = method(input_a, input_b)
            except Exception as e:
                # If an exception occurs, report it
                error = str(e)  # Convert the exception to a string
                report_bug(method.__name__, result, input_a, input_b, error)
                continue

            # Check if the result contains any unexpected behavior (e.g., exceptions, crashes, incorrect output)
            if is_bug_detected(method.__name__, input_a, input_b, result):
                # Report the bug or log the issue
                report_bug(method.__name__, result, input_a, input_b, error)
            else:
                # If no bugs are detected, print "No bugs detected" for the current method
                print(f"No bugs detected for method {method.__name__}.")
                print(f"Input data 1: {input_a}")
                print(f"Input data 2: {input_b}")
                print(f"Result: {result}")
                print()


# Checks if input is a number
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


# Checks if the result of the method indicates a bug.
def is_bug_detected(method_name, input_a, input_b, result):
    if method_name == 'add':
        # Check if both inputs can be converted to numbers
        if is_number(input_a) and is_number(input_b):
            # Convert input strings to numbers and check if they can be converted successfully
            float_input_a = float(input_a)
            float_input_b = float(input_b)
            # Check if the result is equal to the sum of the input numbers
            if result == float_input_a + float_input_b: return False
        else:
            # Bug detected
            return True

    elif method_name == 'subtract':
        # Check if the result is the difference of the input numbers
        if is_number(input_a) and is_number(input_b):
            if result == float(input_a) - float(input_b): return False
        else:
            return True  # Bug detected

    elif method_name == 'multiply':
        # Check if the result is the product of the input numbers
        if is_number(input_a) and is_number(input_b):
            if result == float(input_a) * float(input_b): return False
        else:
            return True  # Bug detected

    elif method_name == 'divide':
        # Check if dividing by zero raises a ValueError
        if float(input_b) == 0:
            if not isinstance(result, ValueError): return True
        # Check if the result is the quotient of the input numbers
        if is_number(input_a) and is_number(input_b):
            if result == float(input_a) / float(input_b): return False
        else:
            return True  # Bug detected

    elif method_name == 'concatenate_strings':
        # Check if the result is not the concatenation of the input strings
        if isinstance(input_a, str) and isinstance(input_b, str) and isinstance(result, str):
            if result == input_a + input_b: return False
        else:
            return True  # Bug detected

    else:
        # If the method name is not recognized, assume no bug detected
        return False


# Reports a bug detected in a method
def report_bug(method_name, result, input_a, input_b, error):
    print(f"Bug detected in method {method_name}:")
    print(f"Input data 1: {input_a}")
    print(f"Input data 2: {input_b}")
    print(f"Result: {result}")
    print("Error message:", error)  # Assuming the variable `error` contains the error message
    print("Please investigate and fix the issue.")
    print()


# Entry point to run the fuzzing process
if __name__ == "__main__":
    fuzz_methods()
