# create the character
import numpy as np
import os
import cv2
import insightface
from insightface.app import FaceAnalysis
from insightface.data import get_image as ins_get_image
import matplotlib.pyplot as plt


class FictionalCharacter:
    def __init__(self, character_face_path = "images/character_face/face.jpg", custom_dir = "images/customs" ) -> None:
        
        self.initializeInsightFace()
        
        self.custom_dir = custom_dir
        self.character_face_path = character_face_path
        
        self.prepareCharacterFace()
        self.createCustomPath()
        # self.character_face = self.applyChangesOnFace(self.character_face)
        self.final_character = self.createCharacter()
    
    def initializeInsightFace(self):
        model_pack_name = 'buffalo_l'
        self.app = FaceAnalysis(name=model_pack_name)
        self.app.prepare(ctx_id=0, det_size=(640, 640))
        
        self.swapper = insightface.model_zoo.get_model('models/face_swapper/inswapper_128.onnx',
                                download=False,
                                download_zip=False)
        
    def inputCustomIndex(self):
        custom_index = input("Enter a number between 1 to 13: ")   
        return custom_index
    
    def createCustomPath(self):
        self.custom_path = os.path.join(self.custom_dir,  self.inputCustomIndex() + '.' + "jpg")
    
    def loadFace(self):
        image_with_character_face = cv2.imread(self.character_face_path)  
        self.show_image(image_with_character_face, "original_face_image")
        return image_with_character_face
    
    def prepareCharacterFace(self):
        img = self.loadFace()
        character_faces = self.app.get(img)
        assert len(character_faces) == 1
        self.character_face = character_faces[0]
        # self.show_image(character_face, "croped_face_image")
        bbox = self.character_face['bbox']
        bbox = [int(b) for b in bbox]
        plt.imshow(img[bbox[1]:bbox[3],bbox[0]:bbox[2],::-1])
        plt.show()
    
    def show_image(self, image, image_name = "test"):
        cv2.imshow(image_name, image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    def loadCustom(self):
        image_with_custom = cv2.imread(self.custom_path)  
        self.show_image(image_with_custom, "custom_image")
        return image_with_custom
    
    def createCharacter(self):
        img = self.loadCustom()
        faces = self.app.get(img)
        res = img.copy()
        for face in faces:
            res = self.swapper.get(res, face, self.character_face, paste_back=True)
        self.show_image(res, "final_image")
        return res

    def imwrite(self, 
                fictional_character,
                final_fictional_character_path = "images/final/character_with_custom/final_character.jpg"):
        
        cv2.imwrite(final_fictional_character_path,self.final_character)
        
if __name__ == "__main__":
    fc = FictionalCharacter()
    print(type(fc.final_character))
    print(fc.final_character.shape)
    fc.imwrite(fc.final_character)
    
        