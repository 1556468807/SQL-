from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import mysql.connector
from select_function import select_function
class LandIn(QMainWindow):
    def __init__(self):
        super().__init__()
        self.id = ''
        self.password = ''
        self.landIn_window()
    def landIn_window(self):
        # 创建窗口
        self.resize(380, 200)
        # 设置窗口标题
        self.setWindowTitle("登录")
        # 创建按钮
        btn = QPushButton("登录", self)
        btn.setGeometry(120, 140, 100, 35)
        # 创建“眼睛”按钮
        self.eye_btn = QPushButton(self)
        self.eye_btn.setGeometry(340, 45, 20, 20)
        self.eye_btn.setIcon(QIcon("closed_eye.png"))  # 使用闭合的眼睛图标
        self.eye_btn.setCheckable(True)
        self.eye_btn.setChecked(False)  # 初始状态为未选中，即闭合眼睛
        self.eye_btn.clicked.connect(self.toggle_eye)
        # 创建label（纯文本），在创建时指定父亲
        label1 = QLabel("账号", self)
        label2 = QLabel("密码", self)
        # 设置显示位置与大小  x，y，w，h
        label1.setGeometry(20, 20, 35, 20)
        label2.setGeometry(20, 45, 35, 20)
        # 显示文本框
        self.edit1 = QLineEdit(self)
        self.edit1.setPlaceholderText("输入账号")
        self.edit1.setGeometry(85, 20, 250, 20)
        self.edit2 = QLineEdit(self)
        self.edit2.setPlaceholderText("输入密码")
        self.edit2.setGeometry(85, 45, 250, 20)
        self.edit2.setEchoMode(QLineEdit.Password)  # 设置密码模式
        # 程序进入循环等待状态
        btn.clicked.connect(self.button_press)

    def button_press(self):
        self.id = self.edit1.text()
        self.password = self.edit2.text()
        self.connectDB()

    def toggle_eye(self):
        if self.eye_btn.isChecked():
            self.eye_btn.setIcon(QIcon("open_eye.png"))  # 切换到睁开眼睛图标
            self.edit2.setEchoMode(QLineEdit.Normal)  # 可见密码
        else:
            self.eye_btn.setIcon(QIcon("closed_eye.png"))  # 切换到闭合眼睛图标
            self.edit2.setEchoMode(QLineEdit.Password)  # 隐藏密码

    def connectDB(self):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user=self.id,
                password=self.password,
                database="supermarket"
            )
            cursor = conn.cursor()
            if conn.is_connected():
                # print("成功登录")
                self.close()  # 关闭登录窗口
                # select_function必须为类的一个属性，否则程序会一闪而过，必须带self.
                self.w1 = select_function(cursor,conn)
                # conn.close() # 断开数据库连接
            else:
                print("连接成功，但登录失败")
        except mysql.connector.Error as err:
            print("登录失败:", err)
            QMessageBox.warning(self, '登录失败', '用户名或密码错误！')
            # 清空输入的账号和密码
            self.edit1.clear()
            self.edit2.clear()