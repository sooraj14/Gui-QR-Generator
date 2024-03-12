from tkinter import *
from tkinter import ttk
from tkinter.font import Font
from tkinter import filedialog
import shutil
import qrcode
from PIL import Image, ImageTk


class QR:
    def pathSelector(self):
        self.path = filedialog.askdirectory()
        self.path_display = ttk.Label(root,text=self.path, font=font_4 , background='spring green')
        self.path_display.place(x= 120, y=200)
        
        # image name input and label
        self.name = ttk.Label(root, text= "Enter the image name", font=font_3, background="spring green")
        self.name.place(x= 30, y= 240)
        
        self.name_input = ttk.Entry(root, width=50)
        self.name_input.place(x=280, y=240)
    
    
    def qrGenerate(self):
        self.link = self.link_field.get()
        try:
            self.button.config(text="Generating...")
            self.path_loc = self.path_display.cget('text')
            self.img_name = self.name_input.get()
            
            self.img = qrcode.make(self.link)
            self.img.save(f"{self.img_name}.png", "PNG")
            
            shutil.move(f"{self.imag_name}.png", self.path_loc)
            
            self.button.config(text="generated")
        except:
            self.button.config(text="Generated")
            self.img = qrcode.make(self.link)
            self.img.save("trial.png", "PNG")
            
            # 
            self.imageOpen = Image.open("trial.png")
            
            # Resize the image using resize() method
            self.resize_image = self.imageOpen.resize((250, 250))
            
            self.image_view = ImageTk.PhotoImage(self.resize_image)
            canvas.create_image(2, 2,anchor=NW , image=self.image_view)
            
    
    
    def create_widgets(self):
        # setting up root as global to use it from the main
        global root
        # heading label 
        self.heading = ttk.Label(root, text="QR Generator", font= font_2, background='spring green')
        self.heading.pack()
        
        # Link Label and Entry part
        self.link_label = ttk.Label(root, text="Enter your link below: ", font=font_3, background='spring green')
        self.link_label.place(x= 30, y = 100)
        
        self.link_field = ttk.Entry(root, width=50)
        self.link_field.place(x=30 ,y=130)
        
        # Path Label and browse button
        self.path_label = ttk.Label(root, text="Enter the path to Download or Skip to just generate QR: ", font=font_3, background='spring green')
        self.path_label.place(x=30, y=170)
        
        self.path_button = ttk.Button(root, text='Browse', command=self.pathSelector)
        self.path_button.place(x=30, y=200)
        
        # QR generator button
        self.button = ttk.Button(root, text="Generate QR", command=self.qrGenerate)
        self.button.place(x= 310, y=300)




if __name__ == "__main__":
    q = QR()
    root = Tk()
    canvas = Canvas(root, width=250, height=250)
    canvas.configure(bg="spring green")
    canvas.place(x= 225, y= 370)
    root.title("QR Genenrator")
    root.geometry('700x700')
    root.configure(bg="spring green")
    # setting up fonts
    font_1 = Font(family='Arial', size=24,weight='normal',slant='italic',underline=1,overstrike=0)
    font_2 = Font(family='Helvetica',size=32,weight='bold',slant='italic',underline=1,overstrike=0)
    font_3 = Font(family='Courier', size=14, weight='normal', slant='roman', underline=0, overstrike=0)
    font_4 = Font(family='Times', size=12, weight='normal', slant='roman', underline=1, overstrike=0)
    
    q.create_widgets()
    root.mainloop()
