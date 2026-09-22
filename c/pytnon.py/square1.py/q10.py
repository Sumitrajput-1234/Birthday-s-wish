import argparse

def main():
    # Create the parser
    parser = argparse.ArgumentParser(description="Calculate the square of a given number.")
    
    # Add argument
    parser.add_argument("number", type=float, help="The number to be squared")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Compute square
    result = args.number ** 2
    
    # Display result
    print(f"The square of {args.number} is {result}")

if __name__ == "__main__":
    main()
