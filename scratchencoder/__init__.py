import logging

class Encoder():
    def __init__(self):
        self.chars = """AabBCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789 -_`~!@#$%^&*()+=[];:'"\|,.<>/?}{"""

    def decode(self, text):
        decoded = ""
        text = str(text)
        y = 0
        for i in range(0, len(text)//2):
            x = self.chars[int(str(text[y])+str(text[int(y)+1]))-1]
            decoded = str(decoded)+str(x)
            y += 2
        return decoded

    def encode(self, text):
        encoded = ""
        length = int(len(text))
        for i in range(0,length):
            try:
                x = int(self.chars.index(text[i])+1)
                if x < 10:
                    x = str(0)+str(x)
                encoded = encoded + str(x)
            except ValueError:
                logging.error('Character not supported')
        return encoded    
