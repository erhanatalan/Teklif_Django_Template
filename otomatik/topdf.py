
def wordtopdf(docxPathName,pdfPathName ):
    from docx2pdf import convert
    import time
    # Word belgesini PDF'ye dönüştürmek için dosya yolunu belirtin
    docx_path = docxPathName
    pdf_path = pdfPathName

    # Word belgesini PDF'ye dönüştürün
    convert(docx_path, pdf_path)

    print(f"{pdf_path} dosyası oluşturuldu.")
    time.sleep(2)
