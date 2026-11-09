#getting the english words
import re


def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())
    return valid_words



class Rotating_CC:
    ALPHA_upper = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
    ALPHA_lower = ('a', 'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
    EnglishWords = load_words()
    
    def RCC_encrypt(self, msg, shift):
        return self.RCC(msg, shift)
    

    def RCC_decrypt(self, msg, shift=1):
        if shift > 26:
            return None
        new_msg = self.RCC(msg, -shift)
        if self.test_accuracy(new_msg) > .75:
            return new_msg
        return self.RCC_decrypt(msg, shift+1)
                
                
    def test_accuracy(self, msg):
        msg = msg.lower()
        msg_words = re.findall(r'\w+', msg)
        whole = len(msg_words)
        part = 0
        for word in msg_words:
            if word in self.EnglishWords:
                part +=1
        return part/whole
        
      
    def RCC (self, msg, shift):
        new_msg = ""
        new_shift = shift
        for ch in msg:
            if ch in self.ALPHA_upper:
                i = self.ALPHA_upper.index(ch)
                ch = self.ALPHA_upper[(i + new_shift)%26]
                new_shift+=shift
            elif ch in self.ALPHA_lower:
                i = self.ALPHA_lower.index(ch)
                ch = self.ALPHA_lower[(i + new_shift)%26]
                new_shift+=shift
            new_msg += ch
        return new_msg
