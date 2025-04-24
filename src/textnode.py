from enum import Enum
class TextType(Enum):
    BOLD = 'bold'
    ITALIC = 'italic'
    CODE = 'code'

def TextNode():
    def __init__(self, text, text_type, url):
        self.text = text
        self.text_type = text_type
        self.url = url
        