from fictional_character import FictionalCharacter
from character_background import FictionalEnvironment
from chat import ChatBot

# original face image of the character is saved at images/character_face/face.jpg
# There are 13 different witch custums, we can choose from the list of 1 to 13
# There are 4 different backgrounds, we can choose from 1 to 4 
# by calling ChatBot class and providing ChatGPT API KEY we can run a conversation with imaginary costumer representative witch

def main():

    fc = FictionalCharacter()
    fc.imwrite(fc.final_character)
    fe = FictionalEnvironment()
    fe.changeBackground(background_image = fe.background_path)
    fe.show_image(fe.final_image)
    
    # chat
    API_KEY = input("Please enter your chatGPT API key: ")
    cb = ChatBot(API_KEY)
    cb.start_chat()

if __name__ == "__main__":
    main()
        

        

        
        