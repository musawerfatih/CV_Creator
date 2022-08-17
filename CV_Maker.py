from tkinter import *
from tkinter import IntVar
from PIL import Image, ImageDraw, ImageFont
from PIL import Image

root = Tk()
root.geometry('1066x580')
root.title('My CV Maker')
root.resizable(0,0)

def openimgae():
    global cv
    cv = Image.open('cvv.jpg')
openimgae()

global fnt, namefnt

fnt = ImageFont.truetype("GOTHIC.TTF", 54)
moredfnt = ImageFont.truetype("GOTHIC.TTF", 45)
d = ImageDraw.Draw(cv)


# Defining Frames
BasicFrame = LabelFrame(root, text='Basic Information')
LangFrame = LabelFrame(root, text='Select Options')
DetailFrame = LabelFrame(root, text='More Details')

EducationFrame = LabelFrame(DetailFrame, text='Education Details')
ObjectiveFrame = LabelFrame(DetailFrame, text='Your Objectives')
WorkFrame = LabelFrame(DetailFrame, text='Work Experience & Short Courses')

# Griding Frames
BasicFrame.grid(row=0, column=0, padx=10)

DetailFrame.grid(row=0, column=1, rowspan=2,)
LangFrame.grid(row=1, column=0, ipadx=50, ipady=10)


EducationFrame.grid(row=0, column=0, padx=10, pady=5)
ObjectiveFrame.grid(row=1, column=0, padx=10, pady=5)
WorkFrame.grid(row=2, column=0, padx=10, pady=5, rowspan=3)


# Basic Frame Details
name = Label(BasicFrame,text='Enter your Name')
fname = Label(BasicFrame,text='Enter your F/Name')
dob = Label(BasicFrame,text='Enter your DOB')
phone = Label(BasicFrame,text='Enter your Phone#')
email = Label(BasicFrame,text='Enter your Email')
nationality = Label(BasicFrame,text='Enter your Nationality')
address = Label(BasicFrame,text='Enter your Address')
nfontsize = Label(BasicFrame,text='Enter name font size dflt : 160 ')

# Status Label
status_label = Label(LangFrame)
status_label.grid(row=3, column=0, columnspan=4, padx=(20,5), pady=(25,0))

size = IntVar()
size.set(160)
# Basic Details Entry Widgets
nameEntry = Entry(BasicFrame)
fnameEntry = Entry(BasicFrame)
dobEntry = Entry(BasicFrame)
phoneEntry = Entry(BasicFrame)
emailEntry = Entry(BasicFrame)
nationalityEntry = Entry(BasicFrame)
addressEntry = Entry(BasicFrame)
nfontsizeEntry = Entry(BasicFrame, textvariable=size)


# Basic Detail Grading
name.grid(row=0, column=0, padx=0, pady=10)
nameEntry.grid(row=0, column=1)

fname.grid(row=0, column=2, padx=10, pady=10)
fnameEntry.grid(row=0, column=3, padx=10)

dob.grid(row=1, column=0, padx=10, pady=10)
dobEntry.grid(row=1, column=1)

phone.grid(row=1, column=2, padx=10, pady=10)
phoneEntry.grid(row=1, column=3)

email.grid(row=2, column=0, padx=10, pady=10)
emailEntry.grid(row=2, column=1)

nationality.grid(row=2, column=2, padx=10, pady=10)
nationalityEntry.grid(row=2, column=3)

address.grid(row=3, column=0, padx=10, pady=10)
addressEntry.grid(row=3, column=1)

nfontsize.grid(row=3, column=2, padx=10, pady=10)
nfontsizeEntry.grid(row=3, column=3)
# Message Boxes
msg = Label(BasicFrame, text= 'Enter your language details')
msg.grid(row=4, column=0, pady=(15,5))

langbox = Text(BasicFrame, height=8, width=20)
langbox.grid(row=5, column=0, columnspan=3, pady=(0,10))


edubox = Text(EducationFrame, height=10, width=55)
edubox.grid(row=0, column=0)


# Language Frames
def submit_data():
    global namefnt
    namefnt = ImageFont.truetype("GOTHIC.TTF", size.get())

    global d, cv
    if ' ' in nameEntry.get():
        try:
            fn, ln = nameEntry.get().split(' ')
            d.text((1010, 390), fn.upper(), font=namefnt, fill="black")
            d.text((1010, 570), ln.upper(), font=namefnt, fill="black")
        except:
            fn, mn, ln = nameEntry.get().split(' ')
            ffn = fn + ' ' + mn
            d.text((1010, 390), ffn.upper(), font=namefnt, fill="black")
            d.text((1010, 570), ln.upper(), font=namefnt, fill="black")
    else:
        d.text((1010, 400), nameEntry.get().upper(), font=namefnt, fill="black")
        
    d.text((155, 795), fnameEntry.get(), font=fnt, fill="black")
    d.text((155, 1080), addressEntry.get(), font=fnt, fill="black")
    d.text((155, 1555), phoneEntry.get(), font=fnt, fill="black")
    d.text((155, 1835), dobEntry.get(), font=fnt, fill="black")
    d.text((155, 2100), emailEntry.get(), font=fnt, fill="black")
    d.text((155, 2355), nationalityEntry.get(), font=fnt, fill="black")

    # Language Text Box
    d.text((155, 2625), langbox.get(1.0, END), font=fnt, fill="black", spacing=20)
    d.text((1010,970), edubox.get(1.0, END), font=moredfnt, fill="black", spacing=20)
    d.text((1010,1910), objbox.get(1.0, END), font=moredfnt, fill="black", spacing=20)
    d.text((1010,2380), workbox.get(1.0, END), font=moredfnt, fill="black", spacing=20)
   
    status_label.config(text='Data submitted.')


def get_cv():
    cv.save(f'{nameEntry.get()}_cv.jpg')
    cv.show()
    status_label.config(text='Successfully exported CV in JPG format.')

def get_as_pdf():
    cv.save(f'{nameEntry.get()}_cv_Pdf.pdf')
    status_label.config(text='Successfully exported CV in pdf format.')

def clear_data():
    nameEntry.delete(0,END)
    fnameEntry.delete(0,END)
    addressEntry.delete(0,END)
    phoneEntry.delete(0,END)
    dobEntry.delete(0,END)
    emailEntry.delete(0,END)
    nationalityEntry.delete(0,END)
    size.set(160)
    langbox.delete(0.0,END)
    edubox.delete(0.0,END)
    workbox.delete(0.0,END)


    status_label.config(text='Data Cleared')

SubmitData = Button(LangFrame, text='Submit Data', command=submit_data, bg='green', fg='white', relief=RIDGE)
SubmitData.grid(row=1, column=0, padx=(90,40), pady=(10,10), sticky=W)

jpg_button = Button(LangFrame, text='Get CV as JPG', command=get_cv, bg='#448ee4', fg='white', relief=RIDGE)
jpg_button.grid(row=1, column=1, padx=10, pady=(10,10), sticky=W)

cv_button = Button(LangFrame, text='Get CV as PDF', command=get_as_pdf, bg='#448ee4', fg='white', relief=RIDGE)
cv_button.grid(row=1, column=2, padx=(10,0), pady=(10,10), sticky=W)

clear_button = Button(LangFrame, text='  Clear Data ', command=clear_data, bg='gray', fg='white', relief=RIDGE)
clear_button.grid(row=2, column=0, padx=(90,0), pady=10, sticky=W)

quit_button = Button(LangFrame, text='Exit', command=root.quit, bg='red', fg='white', relief=RIDGE)
quit_button.grid(row=2, column=1, padx=(10,5), pady=10, sticky=W)


# Inside Frames in Details Frames
objctv = """To work in a challenging environment in any government
and non-government organization for career growth
through sincere, achievement and skill and where
evaluation is based on performance and where is an
equal chance of career development."""

objbox = Text(ObjectiveFrame, height=8, width=55, wrap=WORD)
objbox.grid(row=1, column=0)
objbox.insert('end',objctv,)

workbox = Text(WorkFrame, height=10, width=55)
workbox.grid(row=2, column=0, rowspan=3)


root.mainloop()
