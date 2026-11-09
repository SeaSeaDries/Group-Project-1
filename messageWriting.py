import os
from Decrypt import Rotating_CC
from random import randint
    
class Message:
    
    def __init__(self):
        self.cipher = Rotating_CC()
        
        
    def get_chat_name(self):
        self.user = input("Username: ")
        recipient = input("Chat with: ")
        chat_name = [self.user, recipient]
        chat_name.sort()
        chat_file = f"[{chat_name[0]}]-[{chat_name[1]}].txt"
        return chat_file
        
    
    def write_msg(self):
        chat_file  = self.get_chat_name()
        
        if os.path.exists(chat_file):
            chat_history = self.read_msg(chat_file)
            print(chat_history)
        else:
            chat_history = ""
        
        msg = input("Message: ")
        
        if chat_history:
            chat_history = chat_history + f"\n[{self.user}]: {msg}"
        else:
            chat_history = f"[{self.user}]: {msg}"
        
        with open(chat_file, "w") as file:
            updated_chat = self.cipher.RCC_encrypt(chat_history, randint(1, 25))
            file.write(updated_chat)
            
            
            
    def read_msg(self, chat_file):
        if os.path.exists(chat_file):
            with open(chat_file, "r") as file:
                encrypted = file.read()
                decrypted = self.cipher.RCC_decrypt(encrypted)
                return decrypted
        else:
            print("No chat history found.")
            return ''
