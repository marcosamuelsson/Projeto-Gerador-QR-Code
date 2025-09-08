import qrcode
import qrcode.constants
import pandas as pd
from customtkinter import filedialog
import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO

class GenerateQR:
    def __init__(self):     
            self.file = ""
            self.qr = ""
            self.image_path = ""

    def SelectFile(self):
        self.file = filedialog.askopenfilename(title="Select the file to generate QR Code", filetypes=[("Text Files", ".txt"), ("Excel Files", ".xlsx"), ("Excel Files", ".xlsm"), ("Excel Files", ".xlsb")]).replace("/", "\\")
        return self.file
        
    def Read_File(self):
        name, extension = os.path.splitext(os.path.basename(self.file))
        
        if extension.lower() == ".txt":
            with open(self.file, 'r', encoding='utf-8') as file:
                information = file.read()
            return information
        
        elif extension in [".xlsx",".xlsm", ".xlsb"]:
            information = pd.read_excel(self.file)
            return information
    
    def Select_Save(self):
        self.image_path = filedialog.asksaveasfilename(title="Select the name and folder to save", filetypes=[("PNG Files", ".png")]).replace("/", "\\") #+ ".png"
        return self.image_path
    
    def Generate(self):
        self.image_path = self.image_path + ".png"
        self.qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4
        )
        self.qr.add_data(self.Read_File())
        self.qr.make(fit=True)
        
        img = self.qr.make_image(fill_color="black", back_color='white')
        img.save(self.image_path)

if __name__ == "__main__":
    gerar = GenerateQR()
    gerar.SelectFile()
    gerar.Select_Save()
    gerar.Generate()