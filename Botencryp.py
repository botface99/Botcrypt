#BOTFACE Encryption Program by hritik
import os
botinput=""
looper="1"
while looper == '1':
    s = 'ENCRYPTION DECRYPTION BY BOTFACE'
    l=s.center(120,'-')
    print("\n\n",l)
    botinput = input("\n\n\n\t\tEnter 1 to Encrypt , 0 to Decrypt your selected file : ")   
    if botinput == '1':
        filer=''
        key=''
        result=''
        try:
            filer = input("\n\n\t\tEnter your text file name : ")
            bot=open(filer,"r")
        except FileNotFoundError:
            print("File not found or enter your filename with absolute path location")
        else:
            content=bot.read()
            key=input("\n\t\tEnter your key to Encrypt your file : ")
            v=int(key)
            s=" "
            for i in range(0,len(content)):
                if " " in content[i]:
                    result=result + s 
                else:
                    result=result + chr(ord(content[i])-v)
            bot.close()
            bot=open(filer,"w")
            bot.write(result)
            bot.close()
            print("\n\t\tYou are successfully Encrypted your selected text file. \n") 
    elif botinput == '0':
        filer=''
        key=''
        result=''
        try:
            filer = input("\n\n\t\tEnter your text file name : ")
            bot=open(filer,"r")
        except FileNotFoundError:
            print("\n\t\tFile not found or enter your filename with absolute path location")
        else:
            content=bot.read()
            key=input("\n\t\tEnter your key to Decrypt your file : ")
            v=int(key)
            s=" "
            for i in range(0,len(content)):
                if " " in content[i]:
                    result=result + s
                else:
                        result=result + chr(ord(content[i])+v)
            bot.close()
            bot=open(filer,"w")
            bot.write(result)
            bot.close()
            print("\n\t\tYou are successfully Decrypted your selected text file. \n") 
    else:
        print("\n\n\t\tSomething Wrong \n")
        
    
