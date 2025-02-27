import os

 #Function to retrieve the content of a specified file
def read_file_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Function to write content into a file
def write_to_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

# Function to identify the longest word in a file
def find_longest_word(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        words = file.read().split()
    return max(words, key=len) if words else None

# Function to check if a file is empty
def check_file_empty(file_path):
    return os.stat(file_path).st_size == 0  # Returns True if file size is 0

# Function to reverse the content of a file and save it to a new file
def reverse_file_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()[::-1]  # Reverse content

    new_file_path = os.path.join(os.path.dirname(file_path), "reversed_content.txt")
    with open(new_file_path, 'w', encoding='utf-8') as new_file:
        new_file.write(content)

# Function to convert a list of strings to uppercase using lambda
def convert_to_uppercase(words):
    return list(map(lambda word: word.upper(), words))

# Function to filter words with even lengths using lambda
def filter_even_length_words(words):
    return list(filter(lambda word: len(word) % 2 == 0, words))

# Function to process a file and convert its words to uppercase using lambda
def process_file_with_lambda(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    processed_lines = [" ".join(map(lambda word: word.upper(), line.split())) for line in lines]

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write("\n".join(processed_lines))

# Example Usage
if __name__ == "__main__":
    file_path = r"/Users/Sans/Public/sans.txt"

    # Read and display the file content
    print("Displaying File Content:")
    print(read_file_content(file_path))

    # Write new content to the file
    write_to_file(file_path, "I love rootkits.")

    # Find the longest word in the file
    print("Identifying the Longest Word:")
    print("Longest Word Found:", find_longest_word(file_path))

    # Check if the file is empty
    print("Checking File Status:")
    print("Is File Empty?", check_file_empty(file_path))

    # Reverse the file content and save it to 'reversed_content.txt'
    reverse_file_content(file_path)
    print("Reversed Content Saved Successfully.")

    # Convert a list of words to uppercase
    words_list = ["code", "development", "programming", "lambda"]
    print("Converting Words to Uppercase:")
    print("Uppercase Words:", convert_to_uppercase(words_list))

    # Filter words with even lengths
    print("Filtering Even-Length Words:")
    print("Even-Length Words:", filter_even_length_words(words_list))

    # Process the file and convert its content to uppercase
    process_file_with_lambda(file_path)
    print("File Content Converted to Uppercase Successfully.")
