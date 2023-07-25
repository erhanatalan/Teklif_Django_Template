import subprocess

def wordtopdf(docxPathName, pdfPathName):
    try:
        # LibreOffice komutunu çalıştırarak DOCX dosyasını PDF'ye dönüştürün
        subprocess.run(['libreoffice', '--headless', '--convert-to', 'pdf', docxPathName, '--outdir', pdfPathName])
        print(f"{pdfPathName} dosyası oluşturuldu.")
    except Exception as e:
        print(f"Dönüştürme hatası: {e}")


def wordtopdfforwindows(docxPathName,pdfPathName ):
    from docx2pdf import convert
    import time
    # Word belgesini PDF'ye dönüştürmek için dosya yolunu belirtin
    docx_path = docxPathName
    pdf_path = pdfPathName

    # Word belgesini PDF'ye dönüştürün
    convert(docx_path, pdf_path)

    print(f"{pdf_path} dosyası oluşturuldu.")
    time.sleep(2)
