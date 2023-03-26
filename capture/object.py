class Object:
    def __init__(self, imgurl:str, text:str, threshold:float, relative_position:tuple):
        self.imgurl = imgurl
        self.text = text
        self.threshold = threshold
        self.relative_position = relative_position