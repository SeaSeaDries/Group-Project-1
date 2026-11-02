name = "Leigha VanOrsdol"

message_file = input("What is the message file name? (file_name.txt) ")

with open(message_file, "a") as file:
    print("Got it!")
    
with open(message_file, "r") as file:
    print(file.read())
    
message = input("What would you like to say? ")

with open(message_file, "a") as file:
    file.write(f"[{name}]: {message} \n")