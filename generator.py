import random
from typing import Literal


def select_words(num: int) -> list:
    """
    Selects a number of words from the dictionary file.
    """
    # While this would be slow if the dictionary was *huge*, it's only 3.5mb or so.
    with open("dictionary", "r") as f:
        words = f.read().splitlines()
    return random.sample(words, num)


def generate_password(words: list, separators: list) -> str:
    """
    Generates a password from the selected words and joins it with random
    separators selected from a provided list.
    """
    password = ""
    for word in words:
        # Toss a random separator from the list into the password.
        # It's possible to only use one separator on the user end
        password += word + random.choice(separators)
    return password[:-1]


def add_special_characters(password: str, level: Literal[1, 2]) -> str:
    """
    Adds special characters to the password.
    """

    # These are defined as functions so that there isn't a lot of duplicate code
    # for invoking the level 1 and level 2 special character functions.
    # Otherwise, I'd have to duplicate the L1 block in the L2 area and that would
    # just make no sense when I can indent and add a def line.
    def one(p: str) -> str:
        if "a" in p.lower():
            p = p.replace("a", "@")
        if "s" in p.lower():
            p = p.replace("s", "$")
        if "d" in p.lower():
            p = p.replace("d", "#")
        if "i" in p.lower():
            p = p.replace("i", "!")
        if "o" in p.lower():
            p = p.replace("o", "0")
        return p

    def two(p: str) -> str:
        if "l" in p.lower():
            p = p.replace("l", "|")
        if "e" in p.lower():
            p = p.replace("e", "{")
        return p

    if level == 1:
        password = one(password)
    elif level == 2:
        password = one(password)
        password = two(password)

    return password


def main():
    """
    Function for main program control.
    """
    print("Password Generator v1.0")
    print("========================")
    while True:
        while True:
            try:
                num_words = int(input("How many words long? "))
                break
            except ValueError:
                print("Please enter a number.")

        separators = []
        print("Enter your separator options, one at a time. Enter 'done' when finished.")
        while True:
            separator = input("Separator: ")
            if separator.lower().strip() == "done":
                break
            separators.append(separator)

        ival = input("Would you like to add special characters? (y/n)")
        if ival.lower().strip() == "y":
            level = int(input("Enter level (1 or 2): "))
            if level > 2:
                level = 2
        else:
            level = 0

        words = select_words(num_words)
        password = generate_password(words, separators)
        if level > 0:
            # noinspection PyTypeChecker
            password = add_special_characters(password, level)
        print("Your password is: " + password)
        ival = input("Would you like to generate another password? (y/n)")
        if ival.lower().strip() == "y":
            continue
        else:
            break


if __name__ == "__main__":
    main()