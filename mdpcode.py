from PyQt5.QtWidgets import QDesktopWidget, QApplication, QDialog, QWidget
from PyQt5 import  QtWidgets
from PyQt5 import uic
from db import *
from motor import motorRun
from nfc import NFC
from led.led import Arduino_NeoPixel
from audio import Audio
import sys

order_form = uic.loadUiType("./gui.ui")[0]
admin_form_login = uic.loadUiType("./login.ui")[0]
admin_form_data = uic.loadUiType("./admin.ui")[0]
payment_form = uic.loadUiType("./payment.ui")[0]
chipcounter = 0
peperocounter = 0
total = 0

nfc = NFC()
audio = Audio()

db = snacksql('localhost','snack')
db.dbConnect()

neo = Arduino_NeoPixel()

#GUI 초기화면
class orderWindow(QDialog, order_form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btChip.clicked.connect(self.ChipClick)
        self.btPepero.clicked.connect(self.PePeroClick)
        self.CANCEL.clicked.connect(self.cancelClick)
        self.ORDER.clicked.connect(self.orderClick)
        self.btAdmin.clicked.connect(self.adminClick)
        neo.neoOn()
    def closeEvent(self, event):
        neo.neoOff()
    def ChipClick(self):
        global chipcounter
        dbStock = db.SnackStockCnt('chip')
        if chipcounter < dbStock:
            chipcounter += 1
            self.lbChipCnt.setText('감자칩 ' + str(chipcounter)+'개')
            self.TOTALPRICE.setText('결제 금액\n' + str((chipcounter + peperocounter) * 1500) + '원')
    def clear(self):
        self.lbChipCnt.setText('감자칩 0개')
        self.lbPeperoCnt.setText('빼빼로 0개')
        self.TOTALPRICE.setText('결제 금액\n'+'0원')

    #뺴뺴로 버튼 이벤트
    def PePeroClick(self):
        global peperocounter
        dbStock = db.SnackStockCnt('pepero')
        if peperocounter < dbStock:
            peperocounter += 1
            self.lbPeperoCnt.setText('빼빼로 ' + str(peperocounter)+'개')
            self.TOTALPRICE.setText('결제 금액\n' + str((chipcounter + peperocounter) * 1500) + '원')

    #취소 버튼 이벤트
    def cancelClick(self):
        global chipcounter
        global peperocounter
        chipcounter = 0
        peperocounter = 0
        self.clear()

    #관리자 버튼 이벤트 - 비밀번호 GUI 표시
    def adminClick(self):
        admin_widget.setFixedWidth(800)
        admin_widget.setFixedHeight(460)
        admin_widget.show()

    #결제 버튼 이벤트 - 결제 GUI 표시
    def orderClick(self):
        paymentWin.setFixedWidth(521)
        paymentWin.setFixedHeight(344)

        paymentWin.show()


#GUI 결제화면
class uiPayment(QDialog, payment_form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.btCancel.clicked.connect(self.btCancelClick)
        self.btCheck.clicked.connect(self.btCheckClick)
        self.btCheck.setEnabled(True)
        self.center()
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    #결제 버튼 이벤트
    def btCheckClick(self):
        nfcId = nfc.nfcRun()
        motor = motorRun()
        nfcFind = nfcId.rfind('UID')
        if nfcFind == -1:
            print("실패")
            self.lbPayment.setText("결제 실패")
        else:
            print("성공")
            self.btCheck.setDisabled(True)
            audio.start()
            self.lbPayment.setText("결제 성공 \n 상품이 나올때 까지 기다려 주세요")
            db.SnackSell('chip',db.SnackStockCnt('chip')-chipcounter)
            db.SnackSell('pepero', db.SnackStockCnt('pepero') - peperocounter)
            db.SnackSellUpdate('chip',chipcounter,chipcounter*1500)
            db.SnackSellUpdate('pepero', peperocounter, peperocounter * 1500)
            motor.cRun(chipcounter)
            motor.pRun(peperocounter)
            orderWin.cancelClick()

    #나가기 버튼 이벤트
    def btCancelClick(self):
        self.lbPayment.setText("확인 버튼을 누르신 다음 \n카드를 대고 기다려 주세요")
        self.btCheck.setEnabled(True)
        orderWin.cancelClick()
        paymentWin.close()

#GUI 관리자 비밀번호 입력 화면
class uiLogin(QDialog, admin_form_login):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.retranslateUi(self)
        self.btNum0.clicked.connect(self.btNum0Click)
        self.btNum1.clicked.connect(self.btNum1Click)
        self.btNum2.clicked.connect(self.btNum2Click)
        self.btNum3.clicked.connect(self.btNum3Click)
        self.btNum4.clicked.connect(self.btNum4Click)
        self.btNum5.clicked.connect(self.btNum5Click)
        self.btNum6.clicked.connect(self.btNum6Click)
        self.btNum7.clicked.connect(self.btNum7Click)
        self.btNum8.clicked.connect(self.btNum8Click)
        self.btNum9.clicked.connect(self.btNum9Click)

        self.btPwCancel.clicked.connect(self.btPwCancelClick)
        self.btPwCheck.clicked.connect(self.btPwCheckClick)


    def tbPwPlainText(self, String):
        self.tbPwShow.setPlainText(self.tbPwGetText()+String)
    #텍스트 브라우져
    def tbPwClear(self):
        self.tbPwShow.clear()
    # 비밀번호 텍스트 브라우저에 적힌 텍스트 가져오기
    def tbPwGetText(self):
        return str(self.tbPwShow.toPlainText()) #쓰여진 글자 가져옴

    #비밀번호 초기화 버튼
    def btPwCancelClick(self):
        self.tbPwShow.clear()

    # 비밀번호 확인 버튼 클릭
    def btPwCheckClick(self):
        row = db.login()
        check = row['password']
        if check == self.tbPwGetText():
            admin_widget.setFixedWidth(800)
            admin_widget.setFixedHeight(460)
            admin_widget.setCurrentIndex(admin_widget.currentIndex()+1)
            self.lbGuide.setText('비밀번호를 입력해 주세요')
            self.tbPwClear()
        else:
            self.lbGuide.setText('비밀번호가 틀렸습니다.')

    #넘패드
    def btNum0Click(self):
        num='0'
        self.tbPwPlainText(num)

    def btNum1Click(self):
        num='1'
        self.tbPwPlainText(num)

    def btNum2Click(self):
        num='2'
        self.tbPwPlainText(num)

    def btNum3Click(self):
        num='3'
        self.tbPwPlainText(num)

    def btNum4Click(self):
        num='4'
        self.tbPwPlainText(num)

    def btNum5Click(self):
        num='5'
        self.tbPwPlainText(num)

    def btNum6Click(self):
        num='6'
        self.tbPwPlainText(num)

    def btNum7Click(self):
        num='7'
        self.tbPwPlainText(num)

    def btNum8Click(self):
        num='8'
        self.tbPwPlainText(num)

    def btNum9Click(self):
        num='9'
        self.tbPwPlainText(num)

#GUI 데이터 표시 화면
class uiData(QDialog,admin_form_data):
    def __init__(self):
        global StockSum, checkSnack
        super().__init__()
        self.StockSum = 0
        self.setupUi(self)
        self.retranslateUi(self)
        self.btBack.clicked.connect(self.btBackClick)
        self.tbSnackDataUpload()
        self.btDataRefresh.clicked.connect(self.btDataRefreshClick)
        #과자 업데이트 이벤트 연결
        self.radioChip.clicked.connect(self.groupBoxDef)
        self.radioPepero.clicked.connect(self.groupBoxDef)
        self.btPlus.clicked.connect(self.btPlusClick)
        self.btMinus.clicked.connect(self.btMinusClick)
        self.btUpdateCheck.clicked.connect(self.btUpdateCheckClick)
        self.btSellRefresh.clicked.connect(self.btSellRefreshClick)
        self.tbSnackSellDataUpload()
    #gui 과자 업데이트 목록
    def groupBoxDef(self):
        if self.radioChip.isChecked():
            self.checkSnack = 'chip' #snackTitle 적기
        elif self.radioPepero.isChecked():
            self.checkSnack = 'pepero' #snackTitle 적기

    #화살표 버튼 이벤트 (+)
    def btPlusClick(self):
        self.StockSum = self.StockSum+1
        self.lbsetText()

    #화살표 버튼 이벤트 (-)
    def btMinusClick(self):
        if self.StockSum > 0:
            self.StockSum = self.StockSum-1
        self.lbsetText()

    #텍스트 변경
    def lbsetText(self):
        self.lbStock.setText(str(self.StockSum)+"개")

    #확인 버튼 이벤트
    def btUpdateCheckClick(self):
        db.SnackUpdate(self.checkSnack,self.StockSum)
        self.StockSum=0
        self.lbsetText()

    # 돌아가기
    def btBackClick(self):
        admin_widget.close()
        admin_widget.setCurrentIndex(admin_widget.currentIndex() - 1)

    # 과자 정보 목록
    def btDataRefreshClick(self):
        db.close()
        db.dbConnect()
        rows = db.SnackSerch()
        self.tbSnackData.clear()
        for row in rows:
            self.tbSnackData.append(str(row['id'])+' '*10+row['title']+' '*10+str(row['stock']))
    def tbSnackDataUpload(self):
        rows = db.SnackSerch()
        for row in rows:
             self.tbSnackData.append(str(row['id'])+' '*10+row['title']+' '*10+str(row['stock']))
    #과자 판매 목록
    def tbSnackSellDataUpload(self):
        rows = db.SnackSellSerch()
        for row in rows:
            self.tbSnackSellData.append(str(row['id'])+' '*10+row['title']+' '*10+str(row['sell_stock'])+' '*10 +str(row['total_price']))
    def btSellRefreshClick(self):
        db.close()
        db.dbConnect()
        rows =db.SnackSellSerch()
        self.tbSnackSellData.clear()
        for row in rows:
            self.tbSnackSellData.append(str(row['id']) + ' '*10 + row['title'] + ' '*10 + str(row['sell_stock']) + ' '*10 + str(row['total_price']))

if __name__ == "__main__":
    global main_widget, admin_widget, paymentWin
    app = QApplication(sys.argv)
    orderWin = orderWindow()
    loginWin = uiLogin()
    dataWin = uiData()
    paymentWin = uiPayment()
    orderWin.show()
    # 스택

    admin_widget = QtWidgets.QStackedWidget()
    admin_widget.addWidget(loginWin)
    admin_widget.addWidget(dataWin)

    sys.exit(app.exec_())

