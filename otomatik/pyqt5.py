import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QVBoxLayout, QSpinBox, QPushButton, QComboBox
import time
import os

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Veri Giriş Formu")
        self.setGeometry(50, 50, 300, 300)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Gonderilecek mail alanı
        toemail_label = QLabel("toemail:")
        self.toemail_input = QLineEdit()
        layout.addWidget(toemail_label)
        layout.addWidget(self.toemail_input)

        # firma alanı
        firma_label = QLabel("firma:")
        self.firma_input = QLineEdit()
        layout.addWidget(firma_label)
        layout.addWidget(self.firma_input)

        indikator_label = QLabel("indikator:")
        self.combo_box1 = QComboBox()
        self.combo_box1.addItem("ABS-B3")
        self.combo_box1.addItem("ABS-I1")
        # self.combo_box1.addItem("")
        self.combo_box1.currentIndexChanged.connect(self.onSelectionChange1)
        layout.addWidget(indikator_label)
        layout.addWidget(self.combo_box1)

        yazar_label = QLabel("yazar:")
        self.combo_box2 = QComboBox()
        self.combo_box2.addItem("Erhan ATALAN")
        self.combo_box2.addItem("Serdar BULUT")
        self.combo_box2.addItem("Davut ATALAN")
        self.combo_box2.currentIndexChanged.connect(self.onSelectionChange2)
        layout.addWidget(yazar_label)
        layout.addWidget(self.combo_box2)

        usmodel_label = QLabel("usmodel:")
        self.combo_box5 = QComboBox()
        self.combo_box5.addItem("B")
        self.combo_box5.addItem("C")
        self.combo_box5.addItem("CB")
        self.combo_box5.addItem("CC")
        self.combo_box5.addItem("V")
        self.combo_box5.addItem("I")
        self.combo_box5.currentIndexChanged.connect(self.onSelectionChange5)
        layout.addWidget(usmodel_label)
        layout.addWidget(self.combo_box5)

        # uzunluk alanı
        uzunluk_label = QLabel("uzunluk:") 
        self.uzunluk_input = QSpinBox()
        layout.addWidget(uzunluk_label)
        layout.addWidget(self.uzunluk_input)

        tonaj_label = QLabel("tonaj:")
        self.combo_box6 = QComboBox()
        self.combo_box6.addItem("60")
        self.combo_box6.addItem("80")
        self.combo_box6.addItem("100")
        self.combo_box6.addItem("120")
        self.combo_box6.addItem("30")
        self.combo_box6.currentIndexChanged.connect(self.onSelectionChange6)
        layout.addWidget(tonaj_label)
        layout.addWidget(self.combo_box6)

        # teslimatgun alanı
        teslimatgun_label = QLabel("teslimatgun: ") 
        self.teslimatgun_input = QSpinBox()
        layout.addWidget(teslimatgun_label)
        layout.addWidget(self.teslimatgun_input)

        insaatkimtarafindanyapilacak_label = QLabel("insaatkimtarafindanyapilacak: A Alici S Satici")
        self.combo_box7 = QComboBox()
        self.combo_box7.addItem("A")
        self.combo_box7.addItem("S")
        self.combo_box7.currentIndexChanged.connect(self.onSelectionChange7)
        layout.addWidget(insaatkimtarafindanyapilacak_label)
        layout.addWidget(self.combo_box7)

        vinckimtarafindanyapilacak_label = QLabel("vinckimtarafindanyapilacak: A Alici S Satici")
        self.combo_box8 = QComboBox()
        self.combo_box8.addItem("A")
        self.combo_box8.addItem("S")
        self.combo_box8.currentIndexChanged.connect(self.onSelectionChange8)
        layout.addWidget(vinckimtarafindanyapilacak_label)
        layout.addWidget(self.combo_box8)

        nakliyekimtarafindanyapilacak_label = QLabel("nakliyekimtarafindanyapilacak: A Alici S Satici")
        self.combo_box9 = QComboBox()
        self.combo_box9.addItem("A")
        self.combo_box9.addItem("S")
        self.combo_box9.currentIndexChanged.connect(self.onSelectionChange9)
        layout.addWidget(nakliyekimtarafindanyapilacak_label)
        layout.addWidget(self.combo_box9)


        # onodeme alanı
        onodeme_label = QLabel("onodeme: %40") 
        self.onodeme_input = QSpinBox()
        layout.addWidget(onodeme_label)
        layout.addWidget(self.onodeme_input)

        cekvade_label = QLabel("cekvade: 60 90 30")
        self.combo_box10 = QComboBox()
        self.combo_box10.addItem("60")
        self.combo_box10.addItem("90")
        self.combo_box10.addItem("30")
        self.combo_box10.currentIndexChanged.connect(self.onSelectionChange10)
        layout.addWidget(cekvade_label)
        layout.addWidget(self.combo_box10)

        # teklifsuresi alanı
        teklifsuresi_label = QLabel("teklifsuresi: 5 ") 
        self.teklifsuresi_input = QSpinBox()
        layout.addWidget(teklifsuresi_label)
        layout.addWidget(self.teklifsuresi_input)

        # ekmasraf alanı
        ekmasraf_label = QLabel("ekmasraf: ") 
        self.ekmasraf_input = QSpinBox()
        layout.addWidget(ekmasraf_label)
        layout.addWidget(self.ekmasraf_input)

        # insaatucret alanı
        insaatucret_label = QLabel("insaatucret: 0") 
        self.insaatucret_input = QSpinBox()
        layout.addWidget(insaatucret_label)
        layout.addWidget(self.insaatucret_input)

        # vincucret alanı
        vincucret_label = QLabel("vincucret: 0") 
        self.vincucret_input = QSpinBox()
        layout.addWidget(vincucret_label)
        layout.addWidget(self.vincucret_input)

        # nakliyeucret alanı
        nakliyeucret_label = QLabel("nakliyeucret: 0") 
        self.nakliyeucret_input = QSpinBox()
        layout.addWidget(nakliyeucret_label)
        layout.addWidget(self.nakliyeucret_input)


        
        # Onayla butonu
        self.onay_button = QPushButton("Onayla")
        self.onay_button.clicked.connect(self.onayla)
        layout.addWidget(self.onay_button)

        self.setLayout(layout)
        self.show()
    
    def onSelectionChange1(self, index):
        selected_item = self.combo_box1.currentText()
        print(f"combo_box1: {selected_item}")

    def onSelectionChange2(self, index):
        selected_item = self.combo_box2.currentText()
        print(f"combo_box2: {selected_item}")

    # def onSelectionChange3(self, index):
    #     selected_item = self.combo_box3.currentText()
    #     print(f"combo_box3: {selected_item}")

    # def onSelectionChange4(self, index):
    #     selected_item = self.combo_box4.currentText()
    #     print(f"combo_box4: {selected_item}")

    def onSelectionChange5(self, index):
        selected_item = self.combo_box5.currentText()
        print(f"combo_box5: {selected_item}")

    def onSelectionChange6(self, index):
        selected_item = self.combo_box6.currentText()
        print(f"combo_box6: {selected_item}")

    def onSelectionChange7(self, index):
        selected_item = self.combo_box7.currentText()
        print(f"combo_box7: {selected_item}")

    def onSelectionChange8(self, index):
        selected_item = self.combo_box8.currentText()
        print(f"combo_box8: {selected_item}")

    def onSelectionChange9(self, index):
        selected_item = self.combo_box9.currentText()
        print(f"combo_box9: {selected_item}")

    def onSelectionChange10(self, index):
        selected_item = self.combo_box10.currentText()
        print(f"combo_box10: {selected_item}")

    def onayla(self):

        toemail = self.toemail_input.text()
        firma = self.firma_input.text()
        indikator = self.combo_box1.currentText()
        insaatkimtarafindanyapilacak = self.combo_box7.currentText()
        vinckimtarafindanyapilacak = self.combo_box8.currentText()
        nakliyekimtarafindanyapilacak = self.combo_box9.currentText()
        usmodel = self.combo_box5.currentText()
        yazar = self.combo_box2.currentText()
        # tel = self.combo_box4.currentText()
        uzunluk = self.uzunluk_input.value()
        tonaj = self.combo_box6.currentText()
        teslimatgun = self.teslimatgun_input.value()
        onodeme = self.onodeme_input.value()
        cekvade = self.combo_box10.currentText()
        teklifsuresi = self.teklifsuresi_input.value()
        ekmasraf = self.ekmasraf_input.value()
        insaatucret = self.insaatucret_input.value()
        vincucret = self.vincucret_input.value()
        nakliyeucret = self.nakliyeucret_input.value()

        self.kaydet(toemail, firma, usmodel, uzunluk,tonaj, teslimatgun ,insaatkimtarafindanyapilacak, vinckimtarafindanyapilacak,nakliyekimtarafindanyapilacak,onodeme,cekvade,teklifsuresi,ekmasraf,indikator,insaatucret,vincucret,nakliyeucret,yazar)
        from run import run
        run()
        self.close()  # Pencereyi kapat
    
    def kaydet(self, toemail, firma, usmodel, uzunluk,tonaj, teslimatgun,insaatkimtarafindanyapilacak, vinckimtarafindanyapilacak,nakliyekimtarafindanyapilacak,onodeme,cekvade,teklifsuresi,ekmasraf,indikator,insaatucret,vincucret,nakliyeucret,yazar):
        ana_klasor_yolu = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        # Yeni dosyanın tam yolu
        yeni_dosya_yolu = os.path.join(ana_klasor_yolu, 'veri1.py')
        # Verileri veri.py dosyasına kaydetme işlemleri
        with open(yeni_dosya_yolu, "w") as file:
            file.write(f"A = 'ALICI FIRMA TARAFINDAN'\n")
            file.write(f"S = 'SATICI FIRMA TARAFINDAN'\n")
            file.write(f"toemail = '{toemail}'\n")
            file.write(f"firma = '{firma}'\n")
            file.write(f"usmodel = '{usmodel}'\n")
            file.write(f"indikator = '{indikator}'\n")
            file.write(f"yazar = '{yazar}'\n")
            # file.write(f"tel = '{tel}'\n")
            file.write(f"insaat = {insaatkimtarafindanyapilacak}\n")
            file.write(f"vinc = {vinckimtarafindanyapilacak}\n")
            file.write(f"nakliye = {nakliyekimtarafindanyapilacak}\n")
            file.write(f"uzunluk = {uzunluk}\n")
            file.write(f"tonaj = {tonaj}\n") 
            file.write(f"teslimatgun = {teslimatgun}\n") 
            file.write(f"onodeme = {onodeme}\n") 
            file.write(f"cekvade = {cekvade}\n") 
            file.write(f"teklifsuresi = {teklifsuresi}\n") 
            file.write(f"ekmasraf = {ekmasraf}\n") 
            file.write(f"insaatucret = {insaatucret}\n") 
            file.write(f"vincucret = {vincucret}\n") 
            file.write(f"nakliyeucret = {nakliyeucret}\n") 

app = QApplication(sys.argv)
widget = MyWidget()
widget.show()
sys.exit(app.exec_())

