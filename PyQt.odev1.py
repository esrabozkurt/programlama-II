import sys
from PyQt4 import QtGui
class tabloOdev(QtGui.QWidget):
    
    def __init__(self):
        super(tabloOdev, self).__init__()
        self.initUI()
        
        
    def initUI(self):
        
        self.setWindowTitle('Table')     
        
        
        grid = QtGui.QGridLayout()
        self.setLayout(grid)
        
        
        veriler = {'Adı':['Can','Semih','Büşra'], 
                'Soyadı':['Aydın','Yarar','Demirgüreşçi'], 
                'Bölüm':['YBS','YBS','İktisat'],}
        
        
        table = QtGui.QTableWidget(self)
        table.setRowCount(3)
        table.setColumnCount(3)
        
        
        baslik = []
        for n, key in enumerate(sorted(veriler.keys(), key=lambda kv: kv[1])):
            baslik.append(key)
            for m, item in enumerate(veriler[key]):
                yeniItem = QtGui.QTableWidgetItem(item)
                table.setItem(m, n, yeniItem)
        
        
        table.setHorizontalHeaderLabels(baslik)        

        
        table.resizeColumnsToContents()
        table.resizeRowsToContents()
        
        
        grid.addWidget(table, 0,0)     

        self.show()
        
def main():
    uygulama = QtGui.QApplication(sys.argv)
    w = tabloOdev()
    uygulama.exec_()


if __name__ == '__main__':
    main()
