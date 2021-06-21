import logging
class Encoder():
    global chars
    chars = "abcdefghijklmnopqrstuvwxyz0123456789+-. _"
    def encode(self, text):
        global chars
        text = text.lower()
        encoded = ""
        length = int(len(text))
        for i in range(0,length):
            try:
                x = int(chars.index(text[i])+int(9))
                encoded = encoded + str(x)
            except ValueError:
                logging.error('Character not supported')
        return encoded
    def decode(self, text):
        decoded = ""
        y = 0
        for i in range(0,len(text)//2):
            x = chars[int(str(text[y])+str(text[int(y)+1]))-9]
            decoded = str(decoded)+str(x)
            y += 2
        return decoded
