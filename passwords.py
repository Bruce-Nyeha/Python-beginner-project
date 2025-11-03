LOWER=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS=["0","1","2","3","4","5","6","7","8","9"]
SPECIAL=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", """, """, ",", ".", "<", ">", "?", "/", "`", "~"]

"""
Create a function definition for each of the functions defined by Sven. Since you won't have any 
code in your functions yet just add the word pass as the body of your function.
"""

#word_in_file function
def word_in_file(word, filename, case_sensitive=False):
    with open(filename, "r", encoding="utf-8") as file:
        for f in file:
             f = f.strip()
             if case_sensitive:
                 if word==f:
                     return True
             else:
                if word.lower() == f.lower():
                    return True
    return False

#word_has_character function with its parameters
def word_has_character(word, character_list):
    for w in word:
        if w in character_list:
            return True
        return False

#word_complexity function also with its parameter
def word_complexity(word):
    complexity = 0
    if word_has_character(word, UPPER):
        complexity += 1

    if word_has_character(word, LOWER):
        complexity += 1

    if word_has_character(word, DIGITS):
        complexity += 1

    if word_has_character(word, SPECIAL):
        complexity += 1

    return complexity
    
#password_strength function with its parameter
def password_strength(password, min_length=10, strong_length=16):
    if word_in_file(password, "wordlist.txt"):
        print("Password is a dictionary word and is not secure.")
        return 0
    
    #we check the toppasswords.txt file to see if password exist in that file too
    if word_in_file(password, "toppasswords.txt"):
        print("Password is commonly used password and is not secure.")
        return 0
    
    #we check the length of the password to make sure the passwor is strong enough

    if len(password) < min_length:
        print("Password is too short and is not secure.")
        return 1
    
    if len(password) >= strong_length:
        print("Password is long, lenght trumps complexity this is a good password.")
        return 5

    complexity = word_complexity(password)
    strength = 1 + complexity
    return strength
#main function
def main():
    print("Welcome to the Password Strength Checker!")
    print("Enter 'q' to quit.\n")

    while True:
        password = input("Enter a password to test: ")

        if password.lower() == 'q':
            print("Goodbye! Program quiting...")
            break

        strength = password_strength(password)
        print(f"Password strength score: {strength} \n")

if __name__== "__main__":
    main()


