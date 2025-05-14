#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        print([])  # Return an empty list for non-positive length
        return
    
    fibonacci = [0, 1]
    
    while len(fibonacci) < length:
        next_number = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(next_number)
    
    print(fibonacci[:length])  # Ensure only the requested length is printed

   