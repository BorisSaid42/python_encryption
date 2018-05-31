from cryptography.fernet import Fernet
from tkinter import *
from tkinter import filedialog
from functools import partial







def menu():
    fileLabel = Label(root, text="Welcome to Boris Said's encrypter \n It uses AES 256  \n The buttons are fairly obvious \n If you loose your key you loose your files")
    fileLabel.config(width=35)
    fileLabel.pack();


    encryptButton = Button(root, text="Encrypt", command=encrypt_helper)
    encryptButton.pack()

    newKeyButton = Button(root, text="New Key", command=new_key)
    newKeyButton.pack()

    decryptButton = Button(root, text="Decrypt", command=decrypt_helper)
    decryptButton.pack()

def new_key():
    

    key = Fernet.generate_key()
    print(key)
    keyLabel = Label(root, text="Here is your new key. \n Store it somewhere safe. \n You need it to unlock file.")
    newKeyDisplay = Entry(root, state='readonly', readonlybackground='white', fg='black')
    newKeyDisplay.config(width = 50)
    var = StringVar()
    var.set(key)
    newKeyDisplay.config(textvariable=var)
    newKeyDisplay.pack()
    keyLabel.pack();

    return key


def clear():
    for widget in root.winfo_children():
        widget.destroy()
        

  
    
def callback(encrypt_or_decrypt):
    clear()
        
    
    keyLabel = Label(root, text="Enter your key")
    global key
    key = Entry(root)
    key.pack()
    middle_with_arg = partial(middle, encrypt_or_decrypt)

    submitButton = Button(root, text="Submit Key", command=middle_with_arg)
    submitButton.pack();
    keyLabel.pack()
    global filePath
        
    filePath =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))



def encrypt_helper():
    callback("encrypt")

    
def decrypt_helper():
    callback("decrypt")

    
def middle(enc_or_dec):
    print(enc_or_dec)
    keyValue = key.get()
    if enc_or_dec == "encrypt":
        encrypt(keyValue, filePath)
        
    if enc_or_dec  == "decrypt":
        decrypt(keyValue, filePath)
    else:
        print('there has been a failure')


def encrypt(key, filePath):
    
    print('the function to encrypt has ran')
    print(filePath)
    localKey=  key
    print(localKey)
    f = Fernet(key)
    
    
    with open(filePath, mode='rb') as data_fh:
        encrypted_data = f.encrypt(data_fh.read())

    with open(filePath, mode="wb") as encdata_fh:
        print("encryption %75")
        encdata_fh.write(encrypted_data)
        print('me thinks the file be encrypted')

        
    clear()
    menu()

def decrypt(key, filePath):
    print('The function to decrypt ahs ranm')
    print(filePath)
    f = Fernet(key)
    with open(filePath, mode='rb') as encrypted_data:
        decrypted_data =  f.decrypt(encrypted_data.read())

    with open(filePath, mode="wb") as encrypted_data:
        encrypted_data.write(decrypted_data)



    clear()
    menu()
    


root = Tk()



menu()
mainloop()


    


