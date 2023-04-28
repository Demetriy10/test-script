import os

# Open the input file
with open('input.txt', 'r') as input_file:
    # Read the content of the input file
    content = input_file.read()
    # Split the content into lines
    lines = content.splitlines()
    # Initialize the current file name to None
    current_file_name = None
    # Initialize the current file content to an empty string
    current_file_content = ''
    # Loop through the lines
    for line in lines:
        # If the line starts with a "#" character
        if line.startswith('#'):
            # If there is a current file name and content
            if current_file_name and current_file_content:
                # Write the current file content to a file with the current file name
                with open(current_file_name + '.txt', 'w') as output_file:
                    output_file.write(current_file_content)
            # Set the current file name to the rest of the line after the "#" character
            current_file_name = line[1:].strip()
            # Reset the current file content to an empty string
            current_file_content = ''
        # Otherwise, add the line to the current file content with a newline character
        else:
            current_file_content += line + '\n'
    # If there is a current file name and content
    if current_file_name and current_file_content:
        # Write the current file content to a file with the current file name
        with open(current_file_name + '.txt', 'w') as output_file:
            output_file.write(current_file_content)
