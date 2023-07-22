import pygsheets
import sys
sys.stdout.reconfigure(encoding='utf-8')




def getinfo(key, cell):
    from .veri import model
    # Kimlik doğrulama için JSON kimlik bilgilerini yükleyin
    gc = pygsheets.authorize(service_file='abs.json')

    # Hedeflenen Google Sheets belgesini açın
    spreadsheet = gc.open_by_key(key)
    # Sayfa adını belirtin veya indeks kullanın
    # worksheet = spreadsheet.sheet1
    worksheet = spreadsheet.sheet1
    # Hücrenin değerini alın
    cell_value = worksheet.get_value(cell)
    cell_without_symbol = cell_value.replace('₺', '').replace('.', '')
    intcell = int(cell_without_symbol)
    round_cell = round(intcell, -3)
    print(f'{model} Model Fiyat: {round_cell}')
    return round_cell

def getinfoz(key,cell):
    # Kimlik doğrulama için JSON kimlik bilgilerini yükleyin
    gc = pygsheets.authorize(service_file='abs.json')

    # Hedeflenen Google Sheets belgesini açın
    spreadsheet = gc.open_by_key(key)
    # Sayfa adını belirtin veya indeks kullanın
    # worksheet = spreadsheet.sheet1
    worksheet = spreadsheet.sheet1
    # Hücrenin değerini alın
    cell_value = worksheet.get_value(cell)
    return cell_value