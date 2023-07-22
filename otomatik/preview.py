import fitz
import tkinter as tk
from PIL import Image, ImageTk

class PDFPreviewWindow(tk.Toplevel):
    def __init__(self, parent, pdf_path):
        super().__init__(parent)
        self.title("PDF Preview")
        self.parent = parent
        self.pdf_path = pdf_path
        self.canvas = tk.Canvas(self)
        self.canvas.pack()
        self.preview_pdf()

    def preview_pdf(self):
        doc = fitz.open(self.pdf_path)
        page = doc[0]
        pix = page.get_pixmap()
        image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        image_tk = ImageTk.PhotoImage(image)
        self.canvas.config(width=image.width, height=image.height)
        self.canvas.create_image(0, 0, anchor='nw', image=image_tk)
        self.canvas.image = image_tk  # Referansı tutmak için
        self.update_idletasks()

def prew(path1, path2):
    root = tk.Tk()
    root.title("Main Window")

    pdf_window1 = PDFPreviewWindow(root, path1)
    pdf_window2 = PDFPreviewWindow(root, path2)

    root.mainloop()