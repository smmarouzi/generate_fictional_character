# create character background
from rembg import remove
import requests
from PIL import Image
from io import BytesIO
import os
import cv2

class FictionalEnvironment:
    def __init__(self, background_dir = "images/background") -> None:
        
        self.background_dir = background_dir
        self.createBackgroundPath()
        
    def inputBackgroundIndex(self):
        background_index = input("Enter a number between 1 to 4: ")   
        return background_index
        
    def createBackgroundPath(self):
        self.background_path = os.path.join(self.background_dir,  self.inputBackgroundIndex() + '.' + "jpg")
    
    def show_image(self, image, image_name = "character_final_image"):
        cv2.imshow(image_name, image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    def loadBackground(self):
        image_with_bg = cv2.imread(self.background_path)  
        self.show_image(image_with_bg, "background_image")
        return image_with_bg
    
    def loadCharacter(self, character_path = "images/final/character_with_custom/final_character.jpg"):
        character_image = cv2.imread(character_path)  
        self.show_image(character_image, "character")
        return character_image
        
    def changeBackground(self, 
                         original_image = "images/final/character_with_custom/final_character.jpg", 
                         background_image = [], 
                         final_image_path = "images/final/character_with_background/character_with_background.jpg"):
        with open(final_image_path, 'wb') as f:
            input = open(original_image, 'rb').read()
            subject = remove(input, alpha_matting=True, alpha_matting_foreground_threshold=50)
            f.write(subject)
        """
        background_image = 'https://iso.500px.com/wp-content/uploads/2014/07/big-one.jpg'
        background_image = Image.open(BytesIO(requests.get(background_image).content))
        """
        with open(background_image, 'rb') as f:
            image_data = f.read()
        background_image = Image.open(BytesIO(image_data))
        """
        foreground_img = Image.open(final_image_path)
        """
        with open(final_image_path, 'rb') as f:
            image_data = f.read()
        foreground_img = Image.open(BytesIO(image_data))
        background_image.paste(foreground_img, (0,0), foreground_img)
        background_image.save(final_image_path, format='jpeg')
        self.final_image = cv2.imread(final_image_path)
        
        
if __name__=="__main__":
    fe = FictionalEnvironment()
    fe.changeBackground(background_image = fe.background_path)