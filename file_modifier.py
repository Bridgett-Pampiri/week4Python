def modify_content(content):
    """
    Modify the file content.
    Example: convert all text to uppercase.
    You can change this function to apply different modifications.
    """
    return content.upper()


# Ask user for input file
filename = input("Enter the filename to read: ")

try:
    # Read the file
    with open(filename, "r") as infile:
        content = infile.read()

    # Modify content
    modified_content = modify_content(content)

    # Write to new file
    new_filename = "modified_" + filename
    with open(new_filename, "w") as outfile:
        outfile.write(modified_content)

    print("File has been read successfully")
    print("Modified content written to:", new_filename)

except FileNotFoundError:
    print("Error: The file was not found. Please check the filename and try again.")
except PermissionError:
    print("Error: You don't have permission to read this file.")
except Exception as e:
    print("An unexpected error occurred:", e)
