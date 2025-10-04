def simple_file_processor():
    """Simple version focusing on core requirements"""

    # Get input filename with error handling
    while True:
        input_file = input("Enter the input filename: ")

        try:
            with open(input_file, 'r') as file:
                content = file.read()
            break

        except FileNotFoundError:
            print(f"Error: File '{input_file}' not found. Please try again.")
        except PermissionError:
            print(
                f"Error: No permission to read '{input_file}'. Please try another file.")
        except Exception as e:
            print(f"Error reading file: {e}. Please try again.")

    # Modify content (simple uppercase conversion)
    modified_content = content.upper()

    # Get output filename
    output_file = input("Enter the output filename: ")

    try:
        with open(output_file, 'w') as file:
            file.write(modified_content)
        print(f"Success! Modified file saved as '{output_file}'")

    except Exception as e:
        print(f"Error writing file: {e}")


# Run the simple version
simple_file_processor()
