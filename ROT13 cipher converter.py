# Today we are going to make a ROT13 cipher translator. 
# ROT13 is a simple letter substitution cipher that replaces a letter with the 13th letter after it in the alphabet. 
# For example, 'A' becomes 'N', 'B' becomes 'O', and so on. The same applies to lowercase letters.



rot13_cipher_list = {'A': 'N', 'B': 'O', 'C': 'P', 'D': 'Q', 'E': 'R', 'F': 'S', 'G': 'T', 'H': 'U', 'I': 'V', 'J': 'W', 
                     'K': 'X', 'L': 'Y', 'M': 'Z', 'N': 'A', 'O': 'B', 'P': 'C', 'Q': 'D', 'R': 'E', 'S': 'F', 'T': 'G', 
                     'U': 'H', 'V': 'I', 'W': 'J', 'X': 'K', 'Y': 'L', 'Z': 'M', ' ': ' ','!': '!', '?': '?', '.': '.',
                     ',': ','}

# First, we will create a function that takes user input to determine whether they want to enter a string or 
# read from a file.


def file_or_string(choice):
        if choice == 'f':
            print("(\nMac Users: /Users/yourusername/Desktop/filename.txt",
                  "\nWindows User: C:\\Users\\yourusername\\Desktop\\filename.txt)")
            file_name = input("Enter the file name path: ")
            try:
                with open(file_name, 'r') as file:
                    content = file.read()
                    print(f"\nCiphered content:\n{text_to_rot13_case(content)}")
            except FileNotFoundError:
                print("File not found.")
                
        elif choice == 's':
            user_text = input("Enter the string to convert: ")
            print(f"Result: {text_to_rot13_case(user_text)}")
            
        elif choice == 'e':
            return
        else:
            print("Invalid choice.")


# Now we will create a function that takes a string as input and returns the ROT13 ciphered version of that string.
# First we want to see the user input if its uppercase or lowercase and we want to be the output in whatever case the user
# inputs like both uppercase and lowercase letters should be converted to their respective ROT13 counterparts 
# while preserving the case.

def text_to_rot13_case(text):
    result = []
    for char in text:
        if char.isupper():
            result.append(rot13_cipher_list.get(char, char))
        elif char.islower():
            mapped = rot13_cipher_list.get(char.upper(), char)
            result.append(mapped.lower() if mapped.isalpha() else mapped)
        else:
            result.append(rot13_cipher_list.get(char, char))
    return ''.join(result)

# Now we will test our function with some examples.

def text_to_rot13_convert(text):
    return ''.join(
        rot13_cipher_list.get(char.upper(), char).lower() if char.islower()
        else rot13_cipher_list.get(char.upper(), char)
        for char in text
    )

# Finally, we will create a main function that will take user input and call the text_to_rot13_case function 
# to convert the input to ROT13 and print the result.


def main():
    while True:
        User_choice = input("Do you want to enter a string or a file? (Enter 's for string', 'f for file', or 'e' to exit): ").strip().lower()
        if User_choice == 'e':
            break
            print("Exiting the program.")
        file_or_string(User_choice)
        User_text = input("Enter a string to be converted to ROT13: ")
        rot13_text = text_to_rot13_case(User_text)
        print(f"\nROT13 ciphered version: {rot13_text}\n")
    
        file_or_string(User_choice)
    
main()
    

