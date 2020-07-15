from tkinter import*
from PIL import Image,ImageTk
import pytesseract
import tkinter.messagebox
from googletrans import Translator
from gtts import gTTS
import os
from playsound import playsound


root=Tk(className="Language Translator")

#scanning the image
def translate_scan():
    #taking the text
    txt=str(ent1.get())

    #taking image path
    txt_image=str(ent2.get())

    #taking radio button int
    egf=rb_select.get()

    #taking text or image int
    ti=rb_text.get()
    if ti==1:
        translator = Translator()
        if egf == 1:
            dis.delete(1.0, END)
            f = translator.translate(txt, dest='en')
            resu = f.text
            tkinter.messagebox.showinfo("Translator", "Translation Completed....")
            print(resu)
            dis.insert(END, resu)
        elif egf == 2:
            dis.delete(1.0, END)
            f = translator.translate(txt, dest='de')
            resu = f.text
            tkinter.messagebox.showinfo("Translator", "Translation Completed....")
            print(resu)
            dis.insert(END, resu)
        else:
            dis.delete(1.0, END)
            f = translator.translate(txt, dest='fr')
            resu = f.text
            tkinter.messagebox.showinfo("Translator", "Translation Completed....")
            print(resu)
            dis.insert(END, resu)

    else:
        img_open=Image.open(txt_image)
        pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
        result = pytesseract.image_to_string(img_open)

        #translate the text
        translator = Translator()
        if egf==1:
            dis.delete(1.0, END)
            f = translator.translate(result, dest='en')
            resu=f.text
            tkinter.messagebox.showinfo("Translator", "Translation Completed....")
            print(resu)
            dis.insert(END,resu)
        elif egf==2:
            dis.delete(1.0, END)
            f = translator.translate(result, dest='de')
            resu = f.text
            tkinter.messagebox.showinfo("Translator", "Translation Completed....")
            print(resu)
            dis.insert(END, resu)
        else:
            dis.delete(1.0, END)
            f = translator.translate(result, dest='fr')
            resu = f.text
            tkinter.messagebox.showinfo("Translator", "Translation Completed....")
            print(resu)
            dis.insert(END, resu)
#save function

def save_trans():
    txt = str(ent1.get())
    txt_image = str(ent2.get())
    t1=rb_text.get()
    if t1==1:
        translator = Translator()
        f = translator.translate(txt, dest='en')
        resu = f.text
        with open('D:/Translated_File.txt', mode='w')as file:
            file.write(resu)
        tkinter.messagebox.showinfo("Translator", "File Saved....")
        print("file saved.....")
    else:
        img_open = Image.open(txt_image)
        pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
        result = pytesseract.image_to_string(img_open)
        translator = Translator()
        f = translator.translate(result, dest='en')
        resu = f.text
        with open('D:/Translated_File.txt', mode='w')as file:
            file.write(resu)
        tkinter.messagebox.showinfo("Translator","File Saved....")
        print("file saved.....")

#listen function
def listen():
    txt = str(ent1.get())
    txt_image = str(ent2.get())
    ti1=rb_text.get()
    ti2=rb_select.get()
    if ti1==1:
        translator = Translator()
        if ti2 == 1:
            f = translator.translate(txt, dest='en')
            resu = f.text
            mytext = resu
            language = 'en'
            myobj = gTTS(text=mytext, lang=language, slow=False)
            myobj.save("D:\Translated.mp3")
            os.system("mpg321 Translated.mp3")
            tkinter.messagebox.showinfo("Translator", "Audio File Created....")
            print("audio file created...")
            answer=tkinter.messagebox.askquestion("Listen","Do you want to hear the file")
            if answer=="yes":
                playsound('D://Translated.mp3')
                print(answer)

        elif ti2 == 2:
            f = translator.translate(txt, dest='de')
            resu = f.text
            language = 'de'
            mytext=resu
            myobj = gTTS(text=mytext, lang=language, slow=False)
            myobj.save("D:\Translated.mp3")
            os.system("mpg321 Translated.mp3")
            tkinter.messagebox.showinfo("Translator", "Audio File Created....")
            print("audio file created...")
            answer = tkinter.messagebox.askquestion("Listen", "Do you want to hear the file")
            if answer == "yes":
                playsound('D://Translated.mp3')
                print(answer)

        else:
            f = translator.translate(txt, dest='fr')
            resu = f.text
            mytext = resu
            language = 'fr'
            myobj = gTTS(text=mytext, lang=language, slow=False)
            myobj.save("D:\Translated.mp3")
            os.system("mpg321 Translated.mp3")
            tkinter.messagebox.showinfo("Translator", "Audio File Created....")
            print("audio file created...")
            answer = tkinter.messagebox.askquestion("Listen", "Do you want to hear the file")
            if answer == "yes":
                playsound('D://Translated.mp3')
                print(answer)

    else:
        translator = Translator()
        img_open=Image.open(txt_image)
        pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
        result = pytesseract.image_to_string(img_open)
        if ti2 == 1:
            f = translator.translate(result, dest='en')
            resu = f.text
            mytext = resu
            language = 'en'
            myobj = gTTS(text=mytext, lang=language, slow=False)
            myobj.save("D:\Translated.mp3")
            os.system("mpg321 Translated.mp3")
            tkinter.messagebox.showinfo("Translator", "Audio File Created....")
            print("audio file created...")
            answer = tkinter.messagebox.askquestion("Listen", "Do you want to hear the file")
            if answer == "yes":
                playsound('D://Translated.mp3')
                print(answer)

        elif ti2 == 2:
            f = translator.translate(result, dest='de')
            resu = f.text
            language = 'de'
            mytext=resu
            myobj = gTTS(text=mytext, lang=language, slow=False)
            myobj.save("D:\Translated.mp3")
            os.system("mpg321 Translated.mp3")
            tkinter.messagebox.showinfo("Translator", "Audio File Created....")
            print("audio file created...")
            answer = tkinter.messagebox.askquestion("Listen", "Do you want to hear the file")
            if answer == "yes":
                playsound('D://Translated.mp3')
                print(answer)

        elif ti2==3:
            f = translator.translate(result, dest='fr')
            resu = f.text
            mytext = resu
            language = 'fr'
            myobj = gTTS(text=mytext, lang=language, slow=False)
            myobj.save("D:\Translated.mp3")
            os.system("mpg321 Translated.mp3")
            tkinter.messagebox.showinfo("Translator", "Audio File Created....")
            print("audio file created...")
            answer = tkinter.messagebox.askquestion("Listen", "Do you want to hear the file")
            if answer == "yes":
                playsound('D://Translated.mp3')
                print(answer)



    #####################################################################################
    # if ti1==1:
    #     translator = Translator()
    #     f = translator.translate(txt, dest='fr')
    #     resu = f.text
    #     mytext = resu
    #     if ti2==1:
    #         language = 'en'
    #         myobj = gTTS(text=mytext, lang=language, slow=False)
    #         myobj.save("D:\\Translated.mp3")
    #         os.system("mpg321 Translated.mp3")
    #     elif ti2==2:
    #         language = 'de'
    #         myobj = gTTS(text=mytext, lang=language, slow=False)
    #         myobj.save("D:\\Translated.mp3")
    #         os.system("mpg321 Translated.mp3")
    #     else:
    #         language = 'fr'
    #         myobj = gTTS(text=mytext, lang=language, slow=False)
    #         myobj.save("D:\\Translated.mp3")
    #         os.system("mpg321 Translated.mp3")
    # else:
    #     img_open = Image.open(txt_image)
    #     pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
    #     result = pytesseract.image_to_string(img_open)
    #     translator = Translator()
    #     f = translator.translate(result, dest='en')
    #     resu = f.text
    #     mytext = resu
    #     if ti2 == 1:
    #         language = 'en'
    #         myobj = gTTS(text=mytext, lang=language, slow=False)
    #         myobj.save("D:\\Translated.mp3")
    #         os.system("mpg321 Translated.mp3")
    #     elif ti2 == 2:
    #         language = 'de'
    #         myobj = gTTS(text=mytext, lang=language, slow=False)
    #         myobj.save("D:\\Translated.mp3")
    #         os.system("mpg321 Translated.mp3")
    #     else:
    #         language = 'fr'
    #         myobj = gTTS(text=mytext, lang=language, slow=False)
    #         myobj.save("D:\\Translated.mp3")
    #         os.system("mpg321 Translated.mp3")
########################################################################################

#main frame
frame=Frame(root)
frame.pack()

#Trans
tra=Label(frame,text="Translator",font=("Pristina",25),height=1)
tra.grid(row=0,columnspan=4)

####adding image
# img_label=Image.open("‪E:\\translator\\gui\\Picture1.png")
# photo=ImageTk.PhotoImage(img_label)
# ph_label=Label(frame,image=photo)
# ph_label.grid(row=0,column=3)

#text radiobutton
rb_text=IntVar()
r1=Radiobutton(frame,text="Text",variable=rb_text,value=1)
r1.grid(row=1,columnspan=2)

#Image radiobutton
r2=Radiobutton(frame,text="Image",variable=rb_text,value=2)
r2.grid(row=1,column=2)

#taking text input
text=Label(frame,text='Text')
text.grid(row=2,column=0,sticky=E)

#or
or_label=Label(frame,text="OR")
or_label.grid(row=3,columnspan=3)

#taking image name
image=Label(frame,text='Image Name')
image.grid(row=4,column=0,sticky=E)



#taking text
ent1=Entry(frame)
ent1.grid(row=2,column=1)

#taking image
ent2=Entry(frame)
ent2.grid(row=4,column=1)

#english radiobutton
rb_select=IntVar()
r1=Radiobutton(frame,text="English",variable=rb_select,value=1)
r1.grid(row=5)

#german radiobutton
r2=Radiobutton(frame,text="German",variable=rb_select,value=2)
r2.grid(row=5,column=1)

#french radiobutton

r3=Radiobutton(frame,text="French",variable=rb_select,value=3)
r3.grid(row=5,column=3)

#translate button
tran=Button(frame,text="Translate",bg="black",fg="white",command=translate_scan)
tran.grid(row=6,columnspan=4)

#Quit button
bhar=Button(frame,text="Quit",bg="red",fg="black",command=frame.quit)
bhar.grid(row=8,column=3)

#text box
#dis=Entry(frame,width=35)
dis=Text(frame,width=35,height=10,wrap=WORD)
dis.grid(row=7,columnspan=5)

#save button
sav=Button(frame,text="Save",bg="black",fg="white",command=save_trans)
sav.grid(row=8,columnspan=1)


#listen button
lis=Button(frame,text="Listen",bg="black",fg="white",command=listen)
lis.grid(row=8,columnspan=4)



root.mainloop()