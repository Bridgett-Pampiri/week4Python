
# week4Python



## File Read & Write Challenge

This Python program reads the content of a file, modifies it, and writes the result into a new file.  
It also includes error handling to deal with cases where the file does not exist or cannot be read.

## How it Works
1. The user is asked to enter a filename.
2. The program attempts to read the file.
3. The contents are modified (in this example, converted to uppercase).
4. The modified content is written to a new file called `modified_<original_filename>`.
5. If the file does not exist or cannot be opened, the program displays a clear error message.

## Example

Suppose you have a file named `example.txt` with the following content:
Hello world

### Running the Program
```bash
python file_modifier.py
```

Input
Enter the filename to read: example.txt

Output
File has been read successfully
Modified content written to: modified_example.txt

## New File Created
The new file modified_example.txt will contain:
HELLO WORLD



