# 🌟 File Read & Write with Error Handling (Beginner Version)

# Using pre-defined input and output file names
input_filename = "example.txt"   # The file we will read
output_filename = "output.txt"   # The new file we will create

try:
    # Step 2: Open the input file and read content
    with open(input_filename, "r") as infile:
        content = infile.read()
    print(f"File '{input_filename}' successfully read!\n")

    # Step 3: Modify the content
    # Example modification: convert all text to uppercase
    modified_content = content.upper()

    # Step 4: Write the modified content to a new file
    with open(output_filename, "w") as outfile:
        outfile.write(modified_content)
    print(f"Modified content has been written to '{output_filename}' successfully!")

except FileNotFoundError:
    print(f"Error: The file '{input_filename}' does not exist. Please create it first.")

except PermissionError:
    print(f"Error: You do not have permission to read '{input_filename}'.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
