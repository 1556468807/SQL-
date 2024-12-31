from PyQt5.QtWidgets import QApplication
import sys
from LandIn import LandIn
def main():
    app = QApplication(sys.argv)
    window = LandIn()
    window.show()  # 显示窗口
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()


