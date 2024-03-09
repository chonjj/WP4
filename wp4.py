import memecreator
import memegenerator


def main():
    while True:
        user_input = input("Welcome to the ICS Meme Generator. "
                           "Would you like to generate a meme or create your "
                           "own? (type 'g' to generate, 'c' to create,"
                           "or 'q' to quit):\n")
        if user_input.lower() == "g":
            print("Generating your meme...")
            meme = memegenerator.get_memes()
            memegenerator.parse_memes(meme)
            memegenerator.display_meme()
            print("Successfully generated your meme.")
            break
        elif user_input.lower() == "c":
            top_text = str(input("What would you like the top text to be?\n"))
            bottom_text = str(input("What would you like the bottom text to "
                                    "be?\n"))
            print("Generating your meme...")
            memecreator.get_memes()
            memecreator.make_meme(top_text, bottom_text)
            print("Successfully generated your meme.")
            break
        elif user_input.lower() == "q":
            break
        else:
            user_input = input("This is not a valid input, please try again.")


if __name__ == "__main__":
    main()
