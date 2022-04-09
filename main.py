# 2022/04/09 v1.0 developed by Seok Ho Lee
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from pytube import YouTube
import os,sys,glob,webbrowser
class MainClass(QMainWindow):
    def check(self,status,num):
        exec('Name'+num+'.setDisabled('+str(not status)+')')
        exec('Link'+num+'.setDisabled('+str(not status)+')')
    def __init__(self):
        super().__init__()
        self.setFixedSize(615,213)
        self.setWindowTitle('기상송 다운로드 매니저')
        def info():
            info=QMessageBox()
            info.setWindowTitle('정보')
            info.setIcon(QMessageBox.Information)
            info.setText('v1.0 developed by Seok Ho Lee')
            info.setStandardButtons(QMessageBox.Yes|QMessageBox.Close)
            info.button(QMessageBox.Yes).setText('Github')
            info.exec_()
            if info.clickedButton()==info.button(QMessageBox.Yes): webbrowser.open('https://github.com/Mercen-Lee')
        def download(num):
            exec('global temp; temp=Check'+num+'.isChecked()')
            if temp:
                exec('global FLink; FLink=Link'+num+'.text()')
                YouTube(FLink).streams.filter(only_audio=True).first().download()
                for x in glob.glob('*.mp4'):
                    if not os.path.isdir(x):
                        exec('global FName; FName=Name'+num+'.text()')
                        os.rename(x,FName+'.mp3')
            else: return
        def warning(num):
            exec('global temp; temp=Check'+num+'.isChecked()')
            if temp:
                if exec('global temp; temp=Name'+num+'.text()==\'\'') or temp:
                    QMessageBox.warning(self,'경고',num+'번째 음악의 파일명이 공백입니다.')
                    return False
                elif exec('global temp; temp=Link'+num+'.text()==\'\'') or temp:
                    QMessageBox.warning(self,'경고',num+'번째 음악의 링크가 공백입니다.')
                    return False
                elif exec('global temp; temp=\'youtu\' not in Link'+num+'.text()') or temp:
                    QMessageBox.warning(self,'경고',num+'번째 음악의 링크가 올바르지 않습니다.')
                    return False
                else: return True
            else: return True
        def start():
            if not Check1.isChecked() and not Check2.isChecked() and not Check3.isChecked():
                QMessageBox.warning(self,'경고','음악이 선택되지 않았습니다.')
                return
            for i in range(1,4):
                if not warning(str(i)): return
            try:
                for i in range(1,4): download(str(i))
                QMessageBox.information(self,'알림','다운로드가 완료되었습니다.')
            except: QMessageBox.warning(self,'경고','오류가 발생했습니다.')
        for i in range(1,4):
            j='Check'+str(i)
            exec(j+'=QCheckBox(self)')
            exec(j+'.resize(21,31)')
            exec(j+'.move(15,'+str(i*40)+')')
            exec(j+'.toggle()')
            j='Name'+str(i)
            exec(j+'=QLineEdit(\''+str(i-1)+'\','+'self)')
            exec(j+'.resize(69,31)')
            exec(j+'.move(43,'+str(i*40)+')')
            exec(j+'.setAlignment(Qt.AlignCenter)')
            j='Link'+str(i)
            exec(j+'=QLineEdit(self)')
            exec(j+'.resize(481,31)')
            exec(j+'.move(120,'+str(i*40)+')')
            exec('globals().update(locals())')
        Name=QLabel('파일명',self)
        Name.resize(69,31)
        Name.move(43,6)
        Name.setAlignment(Qt.AlignCenter)
        Link=QLabel('유튜브 링크',self)
        Link.resize(481,31)
        Link.move(120,6)
        Link.setAlignment(Qt.AlignCenter)
        Button=QPushButton('다운로드',self)
        Button.resize(491,41)
        Button.move(115,160)
        Info=QPushButton('정보',self)
        Info.resize(106,41)
        Info.move(10,160)
        Info.clicked.connect(lambda:info())
        Button.clicked.connect(lambda:start())
        Check1.stateChanged.connect(lambda:self.check(Check1.isChecked(),'1'))
        Check2.stateChanged.connect(lambda:self.check(Check2.isChecked(),'2'))
        Check3.stateChanged.connect(lambda:self.check(Check3.isChecked(),'3'))
if __name__=='__main__':
    app=QApplication(sys.argv)
    myWindow=MainClass()
    myWindow.show()
    app.exec_()
