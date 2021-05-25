import tkinter
from tkinter import Label, font, Frame, Button, filedialog, PhotoImage, Canvas
import NearestNeighbors
import os
from os.path import join
from PIL import Image,ImageTk
import cv2

class Main:
    def __init__(self):
        self.root = tkinter.Tk()
        self.resultImages = []
        self.imagesPath = os.getcwd()
        self.imagesPath = os.path.join(self.imagesPath,"DB")
        self.model = NearestNeighbors.NearestNeighborsModel()
        self.model.trainModel()

    def mainWindow(self):
        self.root.geometry("1400x800")
        self.root.configure(bg='#595959')
        self.root.title("Buscador de Imagenes")
        for i in range(5):
            self.root.columnconfigure(i,weight=1)
        button = tkinter.Button(self.root, text="Buscar Imagen",width=20,height=2, command = lambda: self.selectImage())
        button.grid(row=1,column=2)
        self.root.mainloop()

    def displayImages(self,results):
        col_num=5
        imgs = []
        #Se itera por las imagenes colocando $colnnum cada fila
        for row_n in range(0, len(results), col_num):
            for column_n in range(col_num):
                image_path = results[row_n+column_n]
                resized = Image.open("DB/"+image_path).resize((200, 200),Image.ANTIALIAS)
                imgs.append(ImageTk.PhotoImage(resized))
                img = imgs[row_n+column_n]
                panel_image = tkinter.Label(self.root, image = img, height=200, width=200)
                panel_image.grid(row=row_n+2, column=column_n, columnspan=1)
        self.root.mainloop()

    def selectImage(self):
        root = tkinter.Tk()
        root.withdraw()
        image_path = filedialog.askopenfilename()
        if image_path != "":
            results = self.model.searchImage(image_path)
            if len(results) > 0:
                self.displayImages(results)

if __name__=="__main__":
    app = Main()
    app.mainWindow()
