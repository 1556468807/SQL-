from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from supermarket import supermarket
from employee import employee
from customer import customer
from Product import Product
from Supplier import Supplier
from Orderdetail import Orderdetail
from Saleorder import Saleorder
from Market import Market
from Purchase import Purchase
from Supply import Supply
import datetime
from decimal import Decimal
class ClickCounter: # 点击次数
    def __init__(self):
        self.count = 0
    def increment(self):
        self.count += 1
    def decrement(self):
        self.count -= 1
    def get_count(self):
        return self.count
class select_function(QWidget):
    def __init__(self, cursor,conn):
        super().__init__()
        self.cursor = cursor
        self.conn = conn
        self.widgets_to_delete = []
        self.select_window()
    def select_window(self):
        screen = QDesktopWidget().screenGeometry()
        width = screen.width()
        height = screen.height()
        self.resize(width, height)
        self.setWindowTitle("连锁超市管理系统")

        btn1 = QPushButton("员工", self)
        btn2 = QPushButton("连锁店", self)
        btn3 = QPushButton("顾客", self)
        btn4 = QPushButton("商品", self)
        btn5 = QPushButton("供应商", self)
        btn6 = QPushButton("订单细节", self)
        btn7 = QPushButton("销售订单", self)
        btn8 = QPushButton("销售", self)
        btn9 = QPushButton("采购", self)
        btn10 = QPushButton("供应", self)
        btn1.setGeometry(50, 25 + 30, 200, 58)
        btn2.setGeometry(50, 115 + 30, 200, 58)
        btn3.setGeometry(50, 205 + 30, 200, 58)
        btn4.setGeometry(50, 295 + 30, 200, 58)
        btn5.setGeometry(50, 385 + 30, 200, 58)
        btn6.setGeometry(50, 475 + 30, 200, 58)
        btn7.setGeometry(50, 565 + 30, 200, 58)
        btn8.setGeometry(50, 655 + 30, 200, 58)
        btn9.setGeometry(50, 745 + 30, 200, 58)
        btn10.setGeometry(50, 835 + 30, 200, 58)

        btn1.clicked.connect(self.staff)
        btn2.clicked.connect(self.supermarket)
        btn3.clicked.connect(self.customer)
        btn4.clicked.connect(self.goods)
        btn5.clicked.connect(self.vendor)
        btn6.clicked.connect(self.order)
        btn7.clicked.connect(self.salesNum)
        btn8.clicked.connect(self.sale)
        btn9.clicked.connect(self.purchase)
        btn10.clicked.connect(self.apply)
        self.show()
    def staff(self):
        self.delete_widgets_in_range(400, 0, self.width(), self.height())
        # 创建label（纯文本），在创建时指定父亲
        self.label1 = QLabel("姓名", self)
        self.label2 = QLabel("年龄", self)
        self.label3 = QLabel("工号", self)
        # 设置显示位置与大小  x，y，w，h
        self.label1.setGeometry(500, 100, 50, 30)
        self.label2.setGeometry(500, 200, 50, 30)
        self.label3.setGeometry(500, 300, 50, 30)
        self.label1.show()
        self.label2.show()
        self.label3.show()
        self.widgets_to_delete.append(self.label1)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.label2)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.label3)  # 将新按钮添加到删除列表中
        # 显示文本框
        self.edit1 = QLineEdit(self)
        self.edit1.setPlaceholderText("输入姓名")
        self.edit1.setGeometry(600, 100, 300, 30)
        self.edit2 = QLineEdit(self)
        self.edit2.setPlaceholderText("输入年龄")
        self.edit2.setGeometry(600, 200, 300, 30)
        self.edit3 = QLineEdit(self)
        self.edit3.setPlaceholderText("输入工号")
        self.edit3.setGeometry(600, 300, 300, 30)
        self.edit1.show()
        self.edit2.show()
        self.edit3.show()
        self.widgets_to_delete.append(self.edit1)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.edit2)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.edit3)  # 将新按钮添加到删除列表中
        # 创建label（纯文本），在创建时指定父亲
        self.label4 = QLabel("工资", self)
        self.label5 = QLabel("职位", self)
        self.label6 = QLabel("入职时间", self)
        self.label7 = QLabel("工作店号", self)
        # 设置显示位置与大小  x，y，w，h
        self.label4.setGeometry(920, 100, 70, 30)
        self.label5.setGeometry(920, 200, 70, 30)
        self.label6.setGeometry(920, 300, 70, 30)
        self.label7.setGeometry(1350, 100, 70, 30)
        self.label4.show()
        self.label5.show()
        self.label6.show()
        self.label7.show()
        self.widgets_to_delete.append(self.label4)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.label5)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.label6)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.label7)  # 将新按钮添加到删除列表中
        # 显示文本框
        self.edit4 = QLineEdit(self)
        self.edit4.setPlaceholderText("输入工资")
        self.edit4.setGeometry(1000, 100, 300, 30)
        self.edit5 = QLineEdit(self)
        self.edit5.setPlaceholderText("输入职位")
        self.edit5.setGeometry(1000, 200, 300, 30)
        self.edit6 = QLineEdit(self)
        self.edit6.setPlaceholderText("输入入职时间")
        self.edit6.setGeometry(1000, 300, 300, 30)
        self.edit7 = QLineEdit(self)
        self.edit7.setPlaceholderText("输入工作店号")
        self.edit7.setGeometry(1425, 100, 300, 30)
        self.edit4.show()
        self.edit5.show()
        self.edit6.show()
        self.edit7.show()
        self.widgets_to_delete.append(self.edit4)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.edit5)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.edit6)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.edit7)  # 将新按钮添加到删除列表中
        # 创建按钮
        self.btn1 = QPushButton("查询")
        self.btn1.setGeometry(600, 400, 90, 35)
        self.btn2 = QPushButton("删除")
        self.btn2.setGeometry(800, 400, 90, 35)
        self.btn3 = QPushButton("修改")
        self.btn3.setGeometry(1000, 400, 90, 35)
        self.btn4 = QPushButton("增加")
        self.btn4.setGeometry(1200, 400, 90, 35)
        # 设置按钮的父亲为当前窗口，相当于添加到W窗口中
        self.btn1.setParent(self)
        self.btn2.setParent(self)
        self.btn3.setParent(self)
        self.btn4.setParent(self)
        self.btn1.show()
        self.btn2.show()
        self.btn3.show()
        self.btn4.show()
        self.widgets_to_delete.append(self.btn1)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.btn2)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.btn3)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.btn4)  # 将新按钮添加到删除列表中

        self.t01 = employee() # 创建一个员工表实例
        self.click_counter01 = ClickCounter() # 创建一个点击计数器实例
        def select():
            self.click_counter01.increment()  # 点击计数器加1
            if self.click_counter01.get_count() > 0:  # 如果点击次数大于0
                self.ls = []
                self.t01.select_search(self.ls,self.cursor,self.conn,self.edit3.text(),
                                      self.edit1.text(),int(self.edit2.text()),
                                      self.edit4.text(),self.edit5.text(),
                                      self.edit6.text(),self.edit7.text())
                self.click_counter01.decrement() # 计数器置0
                length = len(self.ls[0])
                data = []
                age = []
                for record_tuple in self.ls[0]:
                    # 获取 Decimal 对象
                    decimal_value = record_tuple[2]
                    # 将 Decimal 对象转换为字符串并去除单引号，然后转换为整数
                    integer_value = int(str(decimal_value))
                    # 转换后的整数
                    age.append(integer_value)
                # 遍历列表中的每个元组
                for record_tuple in self.ls[0]:
                    # 获取日期对象
                    date_obj = record_tuple[5]
                    # 将日期对象转换为 'YYYY-MM-DD' 格式的字符串
                    formatted_date = date_obj.strftime('%Y-%m-%d')
                    # 输出格式化后的日期
                    data.append(formatted_date)
                for i in range(length):
                    # 显示数据
                    self.item0 = QTableWidgetItem(self.ls[0][i][0])
                    self.table_widget.setItem(i, 0, self.item0)
                    self.item1 = QTableWidgetItem(self.ls[0][i][1])
                    self.table_widget.setItem(i, 1, self.item1)
                    self.item2 = QTableWidgetItem(str(age[i]))
                    self.table_widget.setItem(i, 2, self.item2)
                    self.item3 = QTableWidgetItem(self.ls[0][i][3])
                    self.table_widget.setItem(i, 3, self.item3)
                    self.item4 = QTableWidgetItem(self.ls[0][i][4])
                    self.table_widget.setItem(i, 4, self.item4)
                    self.item5 = QTableWidgetItem(data[i])
                    self.table_widget.setItem(i, 5, self.item5)
                    self.item6 = QTableWidgetItem(self.ls[0][i][6])
                    self.table_widget.setItem(i, 6, self.item6)
                self.table_widget.setGeometry(0, 0, 1000, 400)
                self.table_widget.setParent(self.edit_result)
                self.table_widget.show()

        self.btn1.clicked.connect(select)

        self.t02 = employee() # 创建一个员工表实例
        self.click_counter02 = ClickCounter() # 创建一个点击计数器实例
        def delete():
            self.click_counter02.increment()  # 点击计数器加1
            if self.click_counter02.get_count() > 0:  # 如果点击次数大于0
                self.t02.delete_employee(self.cursor,self.conn,self.edit3.text(),
                                        self.edit1.text(),int(self.edit2.text()),
                                        self.edit4.text(),self.edit5.text(),
                                        self.edit6.text(),self.edit7.text())
                self.click_counter02.decrement() # 计数器置0
        self.btn2.clicked.connect(delete)

        self.t03 = employee() # 创建一个员工表实例
        self.click_counter03 = ClickCounter() # 创建一个点击计数器实例
        def update():
            self.click_counter03.increment()  # 点击计数器加1
            if self.click_counter03.get_count() > 0:  # 如果点击次数大于0
                self.t03.update_employee(self.cursor,self.conn,self.edit3.text(),
                                        self.edit1.text(),int(self.edit2.text()),
                                        self.edit4.text(),self.edit5.text(),
                                        self.edit6.text(),self.edit7.text())
                self.click_counter03.decrement() # 计数器置0
                # 显示数据
                self.item0 = QTableWidgetItem(self.edit3.text())
                self.table_widget.setItem(0, 0, self.item0)
                self.item1 = QTableWidgetItem(self.edit1.text())
                self.table_widget.setItem(0, 1, self.item1)
                self.item2 = QTableWidgetItem(self.edit2.text())
                self.table_widget.setItem(0, 2, self.item2)
                self.item3 = QTableWidgetItem(self.edit4.text())
                self.table_widget.setItem(0, 3, self.item3)
                self.item4 = QTableWidgetItem(self.edit5.text())
                self.table_widget.setItem(0, 4, self.item4)
                self.item5 = QTableWidgetItem(self.edit6.text())
                self.table_widget.setItem(0, 5, self.item5)
                self.item6 = QTableWidgetItem(self.edit7.text())
                self.table_widget.setItem(0, 6, self.item6)
                self.table_widget.setGeometry(0, 0, 1000, 400)
                self.table_widget.setParent(self.edit_result)
                self.table_widget.show()
        self.btn3.clicked.connect(update)

        self.t04 = employee() # 创建一个员工表实例
        self.click_counter04 = ClickCounter() # 创建一个点击计数器实例
        def addemp():
            self.click_counter04.increment()  # 点击计数器加1
            if self.click_counter04.get_count() > 0:  # 如果点击次数大于0
                self.t04.addemployee(self.cursor,self.conn,self.edit3.text(),
                                        self.edit1.text(),int(self.edit2.text()),
                                        self.edit4.text(),self.edit5.text(),
                                        self.edit6.text(),self.edit7.text())
                self.click_couclick_counter04nter.decrement()  # 计数器置0
                # 显示数据
                self.item0 = QTableWidgetItem(self.edit3.text())
                self.table_widget.setItem(0, 0, self.item0)
                self.item1 = QTableWidgetItem(self.edit1.text())
                self.table_widget.setItem(0, 1, self.item1)
                self.item2 = QTableWidgetItem(self.edit2.text())
                self.table_widget.setItem(0, 2, self.item2)
                self.item3 = QTableWidgetItem(self.edit4.text())
                self.table_widget.setItem(0, 3, self.item3)
                self.item4 = QTableWidgetItem(self.edit5.text())
                self.table_widget.setItem(0, 4, self.item4)
                self.item5 = QTableWidgetItem(self.edit6.text())
                self.table_widget.setItem(0, 5, self.item5)
                self.item6 = QTableWidgetItem(self.edit7.text())
                self.table_widget.setItem(0, 6, self.item6)
                self.table_widget.setGeometry(0, 0, 1000, 400)
                self.table_widget.setParent(self.edit_result)
                self.table_widget.show()
        self.btn4.clicked.connect(addemp)



        self.edit_result = QLineEdit(self)
        self.edit_result.setPlaceholderText("查询结果")
        self.edit_result.setGeometry(600, 500, 1000, 600)
        self.edit_result.show()
        self.widgets_to_delete.append(self.edit_result)  # 将新按钮添加到删除列表中
        # 创建表格
        self.table_widget = QTableWidget(20, 7)
        # 设置数据标题
        self.table_widget.setHorizontalHeaderLabels(['员工号', '姓名', '年龄', '工资', '职称', '聘用日期', '店号'])
        # 显示表格
        self.table_widget.setGeometry(0, 0, 1000, 400)
        self.table_widget.setParent(self.edit_result)
        self.table_widget.show()
        self.widgets_to_delete.append(self.table_widget)

    def supermarket(self):
        self.delete_widgets_in_range(400, 0, self.width(), self.height())
        # 创建label（纯文本），在创建时指定父亲
        self.label1 = QLabel("店名", self)
        self.label2 = QLabel("地址", self)
        # 设置显示位置与大小  x，y，w，h
        self.label1.setGeometry(500 + 120, 100+30, 50, 30)
        self.label2.setGeometry(500 + 120, 300-30, 50, 30)
        self.label1.show()
        self.label2.show()
        self.widgets_to_delete.append(self.label1)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.label2)  # 将新按钮添加到删除列表中
        # 显示文本框
        self.edit1 = QLineEdit(self)
        self.edit1.setPlaceholderText("输入店名")
        self.edit1.setGeometry(600 + 120, 100+30, 300, 30)
        self.edit2 = QLineEdit(self)
        self.edit2.setPlaceholderText("输入地址")
        self.edit2.setGeometry(600 + 120, 300-30, 300, 30)
        self.edit1.show()
        self.edit2.show()
        self.widgets_to_delete.append(self.edit1)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.edit2)  # 将新按钮添加到删除列表中
        # 创建label（纯文本），在创建时指定父亲
        self.label3 = QLabel("店号", self)
        self.label4 = QLabel("营业时间", self)
        # 设置显示位置与大小  x，y，w，h
        self.label3.setGeometry(920+50+ 120, 100+30, 70, 30)
        self.label4.setGeometry(920+50+ 120, 300-30, 70, 30)
        self.label3.show()
        self.label4.show()
        self.widgets_to_delete.append(self.label3)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.label4)  # 将新按钮添加到删除列表中
        # 显示文本框
        self.edit3 = QLineEdit(self)
        self.edit3.setPlaceholderText("输入店号")
        self.edit3.setGeometry(1000+70+ 120, 100+30, 300, 30)
        self.edit4 = QLineEdit(self)
        self.edit4.setPlaceholderText("输入营业时间")
        self.edit4.setGeometry(1000+70+ 120, 300-30, 300, 30)
        self.edit3.show()
        self.edit4.show()
        self.widgets_to_delete.append(self.edit3)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.edit4)  # 将新按钮添加到删除列表中

        # 创建按钮
        self.btn1 = QPushButton("查询")
        self.btn1.setGeometry(600+ 140, 400, 90, 35)
        self.btn2 = QPushButton("删除")
        self.btn2.setGeometry(800+ 140, 400, 90, 35)
        self.btn3 = QPushButton("修改")
        self.btn3.setGeometry(1000+ 140, 400, 90, 35)
        self.btn4 = QPushButton("增加")
        self.btn4.setGeometry(1200+ 140, 400, 90, 35)
        # 设置按钮的父亲为当前窗口，相当于添加到W窗口中
        self.btn1.setParent(self)
        self.btn2.setParent(self)
        self.btn3.setParent(self)
        self.btn4.setParent(self)
        self.btn1.show()
        self.btn2.show()
        self.btn3.show()
        self.btn4.show()
        self.widgets_to_delete.append(self.btn1)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.btn2)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.btn3)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.btn4)  # 将新按钮添加到删除列表中

        self.t1 = supermarket()  # 创建一个超市表实例
        self.click_counter01 = ClickCounter()  # 创建一个点击计数器实例
        def select():
            self.click_counter01.increment()  # 点击计数器加1
            if self.click_counter01.get_count() > 0:  # 如果点击次数大于0
                self.ls = []
                self.t1.myselect(self.ls, self.cursor, self.conn, self.edit3.text(),
                                       self.edit1.text(), self.edit2.text(),
                                       self.edit4.text())
                self.click_counter01.decrement()  # 计数器置0
                length = len(self.ls[0])
                for i in range(length):
                    # 显示数据
                    self.item0 = QTableWidgetItem(self.ls[0][i][0])
                    self.table_widget.setItem(i, 0, self.item0)
                    self.item1 = QTableWidgetItem(self.ls[0][i][1])
                    self.table_widget.setItem(i, 1, self.item1)
                    self.item2 = QTableWidgetItem(self.ls[0][i][2])
                    self.table_widget.setItem(i, 2, self.item2)
                    self.item3 = QTableWidgetItem(self.ls[0][i][3])
                    self.table_widget.setItem(i, 3, self.item3)
                self.table_widget.setGeometry(0, 0, 1000, 400)
                self.table_widget.setParent(self.edit_result)
                self.table_widget.show()
        self.btn1.clicked.connect(select)

        self.t2 = supermarket()  # 创建一个超市表实例
        self.click_counter02 = ClickCounter()  # 创建一个点击计数器实例
        def delete():
            self.click_counter02.increment()  # 点击计数器加1
            if self.click_counter02.get_count() > 0:  # 如果点击次数大于0
                self.t2.mydelete(self.cursor, self.conn, self.edit3.text(),
                                       self.edit1.text(), self.edit2.text(),
                                       self.edit4.text())
                self.click_counter02.decrement()  # 计数器置0
        self.btn2.clicked.connect(delete)

        self.t3 = supermarket()  # 创建一个超市表实例
        self.click_counter03 = ClickCounter()  # 创建一个点击计数器实例
        def update():
            self.click_counter03.increment()  # 点击计数器加1
            if self.click_counter03.get_count() > 0:  # 如果点击次数大于0
                self.t3.myupdate(self.cursor, self.conn, self.edit3.text(),
                                       self.edit1.text(), self.edit2.text(),
                                       self.edit4.text())
                self.click_counter03.decrement()  # 计数器置0
                # 显示数据
                self.item0 = QTableWidgetItem(self.edit3.text())
                self.table_widget.setItem(0, 0, self.item0)
                self.item1 = QTableWidgetItem(self.edit1.text())
                self.table_widget.setItem(0, 1, self.item1)
                self.item2 = QTableWidgetItem(self.edit2.text())
                self.table_widget.setItem(0, 2, self.item2)
                self.item3 = QTableWidgetItem(self.edit4.text())
                self.table_widget.setItem(0, 3, self.item3)
                self.table_widget.setGeometry(0, 0, 1000, 400)
                self.table_widget.setParent(self.edit_result)
                self.table_widget.show()
        self.btn3.clicked.connect(update)

        self.t4 = supermarket()# 创建一个超市表实例
        # 创建一个点击计数器实例
        self.click_counter04 = ClickCounter()
        def addsup():
            self.click_counter04.increment()  # 点击计数器加1
            if self.click_counter04.get_count() > 0:  # 如果点击次数大于0
                self.t4.addSupermarket(self.cursor,self.conn,
                    self.edit3.text(), self.edit1.text(), self.edit2.text(), self.edit4.text())
                self.click_counter04.decrement() # 计数器置0
                # 显示数据
                self.item0 = QTableWidgetItem(self.edit3.text())
                self.table_widget.setItem(0, 0, self.item0)
                self.item1 = QTableWidgetItem(self.edit1.text())
                self.table_widget.setItem(0, 1, self.item1)
                self.item2 = QTableWidgetItem(self.edit2.text())
                self.table_widget.setItem(0, 2, self.item2)
                self.item3 = QTableWidgetItem(self.edit4.text())
                self.table_widget.setItem(0, 3, self.item3)
                self.table_widget.setGeometry(0, 0, 1000, 400)
                self.table_widget.setParent(self.edit_result)
                self.table_widget.show()
        self.btn4.clicked.connect(addsup)



        self.edit_result = QLineEdit(self)
        self.edit_result.setPlaceholderText("查询结果")
        self.edit_result.setGeometry(600, 500, 1000, 400)
        self.edit_result.show()
        self.widgets_to_delete.append(self.edit_result)  # 将新按钮添加到删除列表中
        # 创建表格
        self.table_widget = QTableWidget(20, 4)
        # 设置数据标题
        self.table_widget.setHorizontalHeaderLabels(['店号', '店名', '地址', '营业时间'])
        # 显示表格
        self.table_widget.setGeometry(0, 0, 1000, 400)
        self.table_widget.setParent(self.edit_result)
        self.table_widget.show()
        self.widgets_to_delete.append(self.table_widget)

    def customer(self):
        self.delete_widgets_in_range(400, 0, self.width(), self.height())
        # 创建label（纯文本），在创建时指定父亲
        self.label1 = QLabel("会员号", self)
        self.label2 = QLabel("姓名", self)
        self.label3 = QLabel("id号", self)
        # 设置显示位置与大小  x，y，w，h
        self.label1.setGeometry(500 + 110, 100, 60, 30)
        self.label1.show()
        self.widgets_to_delete.append(self.label1)  # 将新按钮添加到删除列表中
        self.label2.setGeometry(500 + 110, 200, 60, 30)
        self.label2.show()
        self.widgets_to_delete.append(self.label2)  # 将新按钮添加到删除列表中
        self.label3.setGeometry(500 + 110, 300, 60, 30)
        self.label3.show()
        self.widgets_to_delete.append(self.label3)  # 将新按钮添加到删除列表中
        # 显示文本框
        self.edit1 = QLineEdit(self)
        self.edit1.setPlaceholderText("输入会员号")
        self.edit1.setGeometry(600 + 110, 100, 300, 30)
        self.edit1.show()
        self.widgets_to_delete.append(self.edit1)  # 将新按钮添加到删除列表中
        self.edit2 = QLineEdit(self)
        self.edit2.setPlaceholderText("输入姓名")
        self.edit2.setGeometry(600 + 110, 200, 300, 30)
        self.edit2.show()
        self.widgets_to_delete.append(self.edit2)  # 将新按钮添加到删除列表中
        self.edit3 = QLineEdit(self)
        self.edit3.setPlaceholderText("输入id号")
        self.edit3.setGeometry(600 + 110, 300, 300, 30)
        self.edit3.show()
        self.widgets_to_delete.append(self.edit3)  # 将新按钮添加到删除列表中
        # 创建按钮
        self.btn1 = QPushButton("查询")
        self.btn1.setGeometry(600 + 140, 400, 90, 35)
        self.btn2 = QPushButton("删除")
        self.btn2.setGeometry(800 + 140, 400, 90, 35)
        self.btn3 = QPushButton("修改")
        self.btn3.setGeometry(1000 + 140, 400, 90, 35)
        self.btn4 = QPushButton("增加")
        self.btn4.setGeometry(1200 + 140, 400, 90, 35)
        # 设置按钮的父亲为当前窗口，相当于添加到W窗口中
        self.btn1.setParent(self)
        self.btn2.setParent(self)
        self.btn3.setParent(self)
        self.btn4.setParent(self)
        self.btn1.show()
        self.btn2.show()
        self.btn3.show()
        self.btn4.show()
        self.widgets_to_delete.append(self.btn1)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.btn2)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.btn3)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.btn4)  # 将新按钮添加到删除列表中

        self.t1 = customer()  # 创建一个实例
        self.click_counter01 = ClickCounter()  # 创建一个点击计数器实例

        def select():
            self.click_counter01.increment()  # 点击计数器加1
            if self.click_counter01.get_count() > 0:  # 如果点击次数大于0
                self.ls = []
                self.t1.myselect(self.ls, self.cursor, self.conn, self.edit1.text(),
                                 self.edit2.text(), self.edit3.text())
                self.click_counter01.decrement()  # 计数器置0
                length = len(self.ls[0])
                for i in range(length):
                    # 显示数据
                    self.item0 = QTableWidgetItem(self.ls[0][i][0])
                    self.table_widget.setItem(i, 0, self.item0)
                    self.item1 = QTableWidgetItem(self.ls[0][i][1])
                    self.table_widget.setItem(i, 1, self.item1)
                    self.item2 = QTableWidgetItem(self.ls[0][i][2])
                    self.table_widget.setItem(i, 2, self.item2)
                self.table_widget.setGeometry(0, 0, 1000, 400)
                self.table_widget.setParent(self.edit_result)
                self.table_widget.show()

        self.btn1.clicked.connect(select)

        self.t2 = customer()
        self.click_counter02 = ClickCounter()  # 创建一个点击计数器实例

        def delete():
            self.click_counter02.increment()  # 点击计数器加1
            if self.click_counter02.get_count() > 0:  # 如果点击次数大于0
                self.t2.mydelete(self.cursor, self.conn,
                                 self.edit1.text(), self.edit2.text(), self.edit3.text())
                self.click_counter02.decrement()  # 计数器置0

        self.btn2.clicked.connect(delete)

        self.t3 = customer()
        self.click_counter03 = ClickCounter()  # 创建一个点击计数器实例

        def update():
            self.click_counter03.increment()  # 点击计数器加1
            if self.click_counter03.get_count() > 0:  # 如果点击次数大于0
                self.t3.myupdate(self.cursor, self.conn,
                                 self.edit1.text(), self.edit2.text(), self.edit3.text())
                self.click_counter03.decrement()  # 计数器置0
                # 显示数据
                self.item0 = QTableWidgetItem(self.edit1.text())
                self.table_widget.setItem(0, 0, self.item0)
                self.item1 = QTableWidgetItem(self.edit2.text())
                self.table_widget.setItem(0, 1, self.item1)
                self.item2 = QTableWidgetItem(self.edit3.text())
                self.table_widget.setItem(0, 2, self.item2)
                self.table_widget.setGeometry(0, 0, 1000, 400)
                self.table_widget.setParent(self.edit_result)
                self.table_widget.show()

        self.btn3.clicked.connect(update)

        self.t4 = customer()
        # 创建一个点击计数器实例
        self.click_counter04 = ClickCounter()

        def addsup():
            self.click_counter04.increment()  # 点击计数器加1
            if self.click_counter04.get_count() > 0:  # 如果点击次数大于0
                self.t4.addSupermarket(self.cursor, self.conn,
                                       self.edit1.text(), self.edit2.text(), self.edit3.text())
                self.click_counter04.decrement()  # 计数器置0
                # 显示数据
                self.item1 = QTableWidgetItem(self.edit1.text())
                self.table_widget.setItem(0, 1, self.item1)
                self.item2 = QTableWidgetItem(self.edit2.text())
                self.table_widget.setItem(0, 2, self.item2)
                self.item0 = QTableWidgetItem(self.edit3.text())
                self.table_widget.setItem(0, 0, self.item0)
                self.table_widget.setGeometry(0, 0, 1000, 400)
                self.table_widget.setParent(self.edit_result)
                self.table_widget.show()

        self.btn4.clicked.connect(addsup)




        # 显示查询结果文本框
        self.edit_result = QLineEdit(self)
        self.edit_result.setPlaceholderText("查询结果")
        self.edit_result.setGeometry(600, 500, 1000, 600)
        self.edit_result.show()
        self.widgets_to_delete.append(self.edit_result)  # 将新按钮添加到删除列表中
        # 创建表格
        self.table_widget = QTableWidget(20, 3)
        # 设置数据标题
        self.table_widget.setHorizontalHeaderLabels(['会员号', '顾客名', '顾客号'])
        # 显示表格
        self.table_widget.setGeometry(0, 0, 1000, 400)
        self.table_widget.setParent(self.edit_result)
        self.table_widget.show()
        self.widgets_to_delete.append(self.table_widget)

    def goods(self):
        self.delete_widgets_in_range(400, 0, self.width(), self.height())
        # 创建label（纯文本），在创建时指定父亲
        self.label1 = QLabel("商品名", self)
        self.label2 = QLabel("商品号", self)
        self.label3 = QLabel("分类名", self)
        # 设置显示位置与大小  x，y，w，h
        self.label1.setGeometry(500 + 110, 100, 60, 30)
        self.label2.setGeometry(500 + 110, 200, 60, 30)
        self.label3.setGeometry(500 + 110, 300, 60, 30)
        self.label1.show()
        self.label2.show()
        self.label3.show()
        self.widgets_to_delete.append(self.label1)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.label2)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.label3)  # 将新按钮添加到删除列表中
        # 显示文本框
        self.edit1 = QLineEdit(self)
        self.edit1.setPlaceholderText("输入商品名")
        self.edit1.setGeometry(600 + 110, 100, 300, 30)
        self.edit2 = QLineEdit(self)
        self.edit2.setPlaceholderText("输入商品号")
        self.edit2.setGeometry(600 + 110, 200, 300, 30)
        self.edit3 = QLineEdit(self)
        self.edit3.setPlaceholderText("输入分类名")
        self.edit3.setGeometry(600 + 110, 300, 300, 30)
        self.edit1.show()
        self.edit2.show()
        self.edit3.show()
        self.widgets_to_delete.append(self.edit1)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.edit2)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.edit3)  # 将新按钮添加到删除列表中
        # 创建按钮
        self.btn1 = QPushButton("查询")
        self.btn1.setGeometry(600 + 140, 400, 90, 35)
        self.btn2 = QPushButton("删除")
        self.btn2.setGeometry(800 + 140, 400, 90, 35)
        self.btn3 = QPushButton("修改")
        self.btn3.setGeometry(1000 + 140, 400, 90, 35)
        self.btn4 = QPushButton("增加")
        self.btn4.setGeometry(1200 + 140, 400, 90, 35)
        # 设置按钮的父亲为当前窗口，相当于添加到W窗口中
        self.btn1.setParent(self)
        self.btn2.setParent(self)
        self.btn3.setParent(self)
        self.btn4.setParent(self)
        self.btn1.show()
        self.btn2.show()
        self.btn3.show()
        self.btn4.show()
        self.widgets_to_delete.append(self.btn1)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.btn2)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.btn3)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.btn4)  # 将新按钮添加到删除列表中

        self.t1 = Product()  # 创建一个实例
        self.click_counter01 = ClickCounter()  # 创建一个点击计数器实例

        def select():
            self.click_counter01.increment()  # 点击计数器加1
            if self.click_counter01.get_count() > 0:  # 如果点击次数大于0
                self.ls = []
                self.t1.myselect(self.ls, self.cursor, self.conn, self.edit2.text(),
                                 self.edit1.text(), self.edit3.text())
                self.click_counter01.decrement()  # 计数器置0
                length = len(self.ls[0])
                for i in range(length):
                    # 显示数据
                    self.item0 = QTableWidgetItem(self.ls[0][i][0])
                    self.table_widget.setItem(i, 0, self.item0)
                    self.item1 = QTableWidgetItem(self.ls[0][i][1])
                    self.table_widget.setItem(i, 1, self.item1)
                    self.item2 = QTableWidgetItem(self.ls[0][i][2])
                    self.table_widget.setItem(i, 2, self.item2)
                self.table_widget.setGeometry(0, 0, 1000, 400)
                self.table_widget.setParent(self.edit_result)
                self.table_widget.show()

        self.btn1.clicked.connect(select)

        self.t2 = Product()
        self.click_counter02 = ClickCounter()  # 创建一个点击计数器实例

        def delete():
            self.click_counter02.increment()  # 点击计数器加1
            if self.click_counter02.get_count() > 0:  # 如果点击次数大于0
                self.t2.mydelete(self.cursor, self.conn,
                                 self.edit2.text(),self.edit1.text(), self.edit3.text())
                self.click_counter02.decrement()  # 计数器置0

        self.btn2.clicked.connect(delete)

        self.t3 = Product()
        self.click_counter03 = ClickCounter()  # 创建一个点击计数器实例

        def update():
            self.click_counter03.increment()  # 点击计数器加1
            if self.click_counter03.get_count() > 0:  # 如果点击次数大于0
                self.t3.myupdate(self.cursor, self.conn,
                                 self.edit2.text(),self.edit1.text(), self.edit3.text())
                self.click_counter03.decrement()  # 计数器置0
                # 显示数据
                self.item0 = QTableWidgetItem(self.edit2.text())
                self.table_widget.setItem(0, 0, self.item0)
                self.item1 = QTableWidgetItem(self.edit1.text())
                self.table_widget.setItem(0, 1, self.item1)
                self.item2 = QTableWidgetItem(self.edit3.text())
                self.table_widget.setItem(0, 2, self.item2)
                self.table_widget.setGeometry(0, 0, 1000, 400)
                self.table_widget.setParent(self.edit_result)
                self.table_widget.show()

        self.btn3.clicked.connect(update)

        self.t4 = Product()
        # 创建一个点击计数器实例
        self.click_counter04 = ClickCounter()

        def addsup():
            self.click_counter04.increment()  # 点击计数器加1
            if self.click_counter04.get_count() > 0:  # 如果点击次数大于0
                self.t4.addSupermarket(self.cursor, self.conn,
                                       self.edit2.text(),self.edit1.text(), self.edit3.text())
                self.click_counter04.decrement()  # 计数器置0
                # 显示数据
                self.item1 = QTableWidgetItem(self.edit2.text())
                self.table_widget.setItem(0, 1, self.item1)
                self.item2 = QTableWidgetItem(self.edit1.text())
                self.table_widget.setItem(0, 2, self.item2)
                self.item0 = QTableWidgetItem(self.edit3.text())
                self.table_widget.setItem(0, 0, self.item0)
                self.table_widget.setGeometry(0, 0, 1000, 400)
                self.table_widget.setParent(self.edit_result)
                self.table_widget.show()

        self.btn4.clicked.connect(addsup)


        # 显示查询结果文本框
        self.edit_result = QLineEdit(self)
        self.edit_result.setPlaceholderText("查询结果")
        self.edit_result.setGeometry(600, 500, 1000, 600)
        self.edit_result.show()
        self.widgets_to_delete.append(self.edit_result)  # 将新按钮添加到删除列表中
        # 创建表格
        self.table_widget = QTableWidget(20, 3)
        # 设置数据标题
        self.table_widget.setHorizontalHeaderLabels([ '商品号', '商品名','分类号'])
        # 显示表格
        self.table_widget.setGeometry(0, 0, 1000, 400)
        self.table_widget.setParent(self.edit_result)
        self.table_widget.show()
        self.widgets_to_delete.append(self.table_widget)

    def vendor(self):
        self.delete_widgets_in_range(400, 0, self.width(), self.height())
        # 创建label（纯文本），在创建时指定父亲
        self.label1 = QLabel("供应商号", self)
        self.label2 = QLabel("供应商名", self)

        # 设置显示位置与大小  x，y，w，h
        self.label1.setGeometry(500+110, 100, 80, 30)
        self.label2.setGeometry(500+110, 200, 80, 30)
        self.label1.show()
        self.label2.show()
        self.widgets_to_delete.append(self.label1)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.label2)  # 将新按钮添加到删除列表中

        # 显示文本框
        self.edit1 = QLineEdit(self)
        self.edit1.setPlaceholderText("输入供应商号")
        self.edit1.setGeometry(600+110, 100, 300, 30)
        self.edit2 = QLineEdit(self)
        self.edit2.setPlaceholderText("输入供应商名")
        self.edit2.setGeometry(600+110, 200, 300, 30)
        self.edit1.show()
        self.edit2.show()
        self.widgets_to_delete.append(self.edit1)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.edit2)  # 将新按钮添加到删除列表中

        # 创建按钮
        self.btn1 = QPushButton("查询")
        self.btn1.setGeometry(600 + 140, 400, 90, 35)
        self.btn2 = QPushButton("删除")
        self.btn2.setGeometry(800 + 140, 400, 90, 35)
        self.btn3 = QPushButton("修改")
        self.btn3.setGeometry(1000+ 140, 400, 90, 35)
        self.btn4 = QPushButton("增加")
        self.btn4.setGeometry(1200+ 140, 400, 90, 35)
        # 设置按钮的父亲为当前窗口，相当于添加到W窗口中
        self.btn1.setParent(self)
        self.btn2.setParent(self)
        self.btn3.setParent(self)
        self.btn4.setParent(self)
        self.btn1.show()
        self.btn2.show()
        self.btn3.show()
        self.btn4.show()
        self.widgets_to_delete.append(self.btn1)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.btn2)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.btn3)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.btn4)  # 将新按钮添加到删除列表中

        self.t1 = Supplier()  # 创建一个实例
        self.click_counter01 = ClickCounter()  # 创建一个点击计数器实例

        def select():
            self.click_counter01.increment()  # 点击计数器加1
            if self.click_counter01.get_count() > 0:  # 如果点击次数大于0
                self.ls = []
                self.t1.myselect(self.ls, self.cursor, self.conn,
                                 self.edit1.text(), self.edit2.text())
                self.click_counter01.decrement()  # 计数器置0
                length = len(self.ls[0])
                for i in range(length):
                    # 显示数据
                    self.item0 = QTableWidgetItem(self.ls[0][i][0])
                    self.table_widget.setItem(i, 0, self.item0)
                    self.item1 = QTableWidgetItem(self.ls[0][i][1])
                    self.table_widget.setItem(i, 1, self.item1)
                self.table_widget.setGeometry(0, 0, 1000, 400)
                self.table_widget.setParent(self.edit_result)
                self.table_widget.show()

        self.btn1.clicked.connect(select)

        self.t2 = Supplier()
        self.click_counter02 = ClickCounter()  # 创建一个点击计数器实例

        def delete():
            self.click_counter02.increment()  # 点击计数器加1
            if self.click_counter02.get_count() > 0:  # 如果点击次数大于0
                self.t2.mydelete(self.cursor, self.conn,
                                 self.edit1.text(), self.edit2.text())
                self.click_counter02.decrement()  # 计数器置0

        self.btn2.clicked.connect(delete)

        self.t3 = Supplier()
        self.click_counter03 = ClickCounter()  # 创建一个点击计数器实例

        def update():
            self.click_counter03.increment()  # 点击计数器加1
            if self.click_counter03.get_count() > 0:  # 如果点击次数大于0
                self.t3.myupdate(self.cursor, self.conn,
                                 self.edit1.text(), self.edit2.text())
                self.click_counter03.decrement()  # 计数器置0
                # 显示数据
                self.item0 = QTableWidgetItem(self.edit1.text())
                self.table_widget.setItem(0, 0, self.item0)
                self.item1 = QTableWidgetItem(self.edit2.text())
                self.table_widget.setItem(0, 1, self.item1)
                self.table_widget.setGeometry(0, 0, 1000, 400)
                self.table_widget.setParent(self.edit_result)
                self.table_widget.show()

        self.btn3.clicked.connect(update)

        self.t4 = Supplier()
        # 创建一个点击计数器实例
        self.click_counter04 = ClickCounter()

        def addsup():
            self.click_counter04.increment()  # 点击计数器加1
            if self.click_counter04.get_count() > 0:  # 如果点击次数大于0
                self.t4.addSupermarket(self.cursor, self.conn,
                                 self.edit1.text(), self.edit2.text())
                self.click_counter04.decrement()  # 计数器置0
                # 显示数据
                self.item1 = QTableWidgetItem(self.edit1.text())
                self.table_widget.setItem(0, 1, self.item1)
                self.item2 = QTableWidgetItem(self.edit2.text())
                self.table_widget.setItem(0, 2, self.item2)
                self.table_widget.setGeometry(0, 0, 1000, 400)
                self.table_widget.setParent(self.edit_result)
                self.table_widget.show()

        self.btn4.clicked.connect(addsup)


        # 显示查询结果文本框
        self.edit_result = QLineEdit(self)
        self.edit_result.setPlaceholderText("查询结果")
        self.edit_result.setGeometry(600, 500, 1000, 600)
        self.edit_result.show()
        self.widgets_to_delete.append(self.edit_result)  # 将新按钮添加到删除列表中
        # 创建表格
        self.table_widget = QTableWidget(20, 2)
        # 设置数据标题
        self.table_widget.setHorizontalHeaderLabels(['供应商号', '供应商名称'])
        # 显示表格
        self.table_widget.setGeometry(0, 0, 1000, 400)
        self.table_widget.setParent(self.edit_result)
        self.table_widget.show()
        self.widgets_to_delete.append(self.table_widget)

    def order(self):
        self.delete_widgets_in_range(400, 0, self.width(), self.height())
        # 创建label（纯文本），在创建时指定父亲
        self.label1 = QLabel("订单号", self)
        self.label2 = QLabel("总金额", self)
        self.label3 = QLabel("日期", self)
        # 设置显示位置与大小  x，y，w，h
        self.label1.setGeometry(500 + 110, 100, 60, 30)
        self.label2.setGeometry(500 + 110, 200, 60, 30)
        self.label3.setGeometry(500 + 110, 300, 60, 30)
        self.label1.show()
        self.label2.show()
        self.label3.show()
        self.widgets_to_delete.append(self.label1)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.label2)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.label3)  # 将新按钮添加到删除列表中
        # 显示文本框
        self.edit1 = QLineEdit(self)
        self.edit1.setPlaceholderText("输入订单号")
        self.edit1.setGeometry(700 + 10, 100, 300, 30)
        self.edit2 = QLineEdit(self)
        self.edit2.setPlaceholderText("输入总金额")
        self.edit2.setGeometry(700 + 10, 200, 300, 30)
        self.edit3 = QLineEdit(self)
        self.edit3.setPlaceholderText("输入日期")
        self.edit3.setGeometry(700 + 10, 300, 300, 30)
        self.edit1.show()
        self.edit2.show()
        self.edit3.show()
        self.widgets_to_delete.append(self.edit1)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.edit2)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.edit3)  # 将新按钮添加到删除列表中
        # 创建按钮
        self.btn1 = QPushButton("查询")
        self.btn1.setGeometry(600 + 140, 400, 90, 35)
        self.btn2 = QPushButton("删除")
        self.btn2.setGeometry(800 + 140, 400, 90, 35)
        self.btn3 = QPushButton("修改")
        self.btn3.setGeometry(1000 + 140, 400, 90, 35)
        self.btn4 = QPushButton("增加")
        self.btn4.setGeometry(1200 + 140, 400, 90, 35)
        # 设置按钮的父亲为当前窗口，相当于添加到W窗口中
        self.btn1.setParent(self)
        self.btn2.setParent(self)
        self.btn3.setParent(self)
        self.btn4.setParent(self)
        self.btn1.show()
        self.btn2.show()
        self.btn3.show()
        self.btn4.show()
        self.widgets_to_delete.append(self.btn1)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.btn2)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.btn3)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.btn4)  # 将新按钮添加到删除列表中

        self.t01 = Orderdetail()  # 创建一个员工表实例
        self.click_counter01 = ClickCounter()  # 创建一个点击计数器实例

        def select():
            self.click_counter01.increment()  # 点击计数器加1
            if self.click_counter01.get_count() > 0:  # 如果点击次数大于0
                self.ls = []
                self.t01.select_search(self.ls, self.cursor, self.conn,
                                       self.edit1.text(), self.edit2.text(),self.edit3.text())
                self.click_counter01.decrement()  # 计数器置0
                length = len(self.ls[0])
                data = []
                # 遍历列表中的每个元组
                for record_tuple in self.ls[0]:
                    # 获取日期对象
                    date_obj = record_tuple[2]
                    # 将日期对象转换为 'YYYY-MM-DD' 格式的字符串
                    formatted_date = date_obj.strftime('%Y-%m-%d')
                    # 输出格式化后的日期
                    data.append(formatted_date)
                for i in range(length):
                    # 显示数据
                    self.item0 = QTableWidgetItem(self.ls[0][i][0])
                    self.table_widget.setItem(i, 0, self.item0)
                    self.item1 = QTableWidgetItem(self.ls[0][i][1])
                    self.table_widget.setItem(i, 1, self.item1)
                    self.item5 = QTableWidgetItem(data[i])
                    self.table_widget.setItem(i, 5, self.item5)
                self.table_widget.setGeometry(0, 0, 1000, 400)
                self.table_widget.setParent(self.edit_result)
                self.table_widget.show()

        self.btn1.clicked.connect(select)

        self.t02 = Orderdetail()  # 创建一个员工表实例
        self.click_counter02 = ClickCounter()  # 创建一个点击计数器实例

        def delete():
            self.click_counter02.increment()  # 点击计数器加1
            if self.click_counter02.get_count() > 0:  # 如果点击次数大于0
                self.t02.delete_employee(self.cursor, self.conn,
                                       self.edit1.text(), self.edit2.text(),self.edit3.text())
                self.click_counter02.decrement()  # 计数器置0

        self.btn2.clicked.connect(delete)

        self.t03 = Orderdetail()  # 创建一个员工表实例
        self.click_counter03 = ClickCounter()  # 创建一个点击计数器实例

        def update():
            self.click_counter03.increment()  # 点击计数器加1
            if self.click_counter03.get_count() > 0:  # 如果点击次数大于0
                self.t03.update_employee(self.cursor, self.conn,
                                       self.edit1.text(), self.edit2.text(),self.edit3.text())
                self.click_counter03.decrement()  # 计数器置0
                # 显示数据
                self.item0 = QTableWidgetItem(self.edit1.text())
                self.table_widget.setItem(0, 0, self.item0)
                self.item1 = QTableWidgetItem(self.edit2.text())
                self.table_widget.setItem(0, 1, self.item1)
                self.item2 = QTableWidgetItem(self.edit3.text())
                self.table_widget.setItem(0, 2, self.item2)
                self.table_widget.setGeometry(0, 0, 1000, 400)
                self.table_widget.setParent(self.edit_result)
                self.table_widget.show()

        self.btn3.clicked.connect(update)

        self.t04 = Orderdetail()  # 创建一个员工表实例
        self.click_counter04 = ClickCounter()  # 创建一个点击计数器实例

        def addemp():
            self.click_counter04.increment()  # 点击计数器加1
            if self.click_counter04.get_count() > 0:  # 如果点击次数大于0
                self.t04.addemployee(self.cursor, self.conn,
                                       self.edit1.text(), self.edit2.text(),self.edit3.text())
                self.click_couclick_counter04nter.decrement()  # 计数器置0
                # 显示数据
                self.item1 = QTableWidgetItem(self.edit1.text())
                self.table_widget.setItem(0, 1, self.item1)
                self.item2 = QTableWidgetItem(self.edit2.text())
                self.table_widget.setItem(0, 2, self.item2)
                self.item0 = QTableWidgetItem(self.edit3.text())
                self.table_widget.setItem(0, 0, self.item0)
                self.table_widget.setGeometry(0, 0, 1000, 400)
                self.table_widget.setParent(self.edit_result)
                self.table_widget.show()

        self.btn4.clicked.connect(addemp)



        # 显示查询结果文本框
        self.edit_result = QLineEdit(self)
        self.edit_result.setPlaceholderText("查询结果")
        self.edit_result.setGeometry(600, 500, 1000, 600)
        self.edit_result.show()
        self.widgets_to_delete.append(self.edit_result)  # 将新按钮添加到删除列表中
        # 创建表格
        self.table_widget = QTableWidget(20, 3)
        # 设置数据标题
        self.table_widget.setHorizontalHeaderLabels(['订单号', '总金额','日期'])
        # 显示表格
        self.table_widget.setGeometry(0, 0, 1000, 400)
        self.table_widget.setParent(self.edit_result)
        self.table_widget.show()
        self.widgets_to_delete.append(self.table_widget)

    def salesNum(self):
        self.delete_widgets_in_range(400, 0, self.width(), self.height())
        # 创建label（纯文本），在创建时指定父亲
        self.label1 = QLabel("订单号", self)
        self.label2 = QLabel("折扣", self)
        self.label3 = QLabel("商品号", self)
        # 设置显示位置与大小  x，y，w，h
        self.label1.setGeometry(500+110, 100, 60, 30)
        self.label2.setGeometry(500+110, 200, 60, 30)
        self.label3.setGeometry(500+110, 300, 60, 30)
        self.label1.show()
        self.label2.show()
        self.label3.show()
        self.widgets_to_delete.append(self.label1)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.label2)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.label3)  # 将新按钮添加到删除列表中
        # 显示文本框
        self.edit1 = QLineEdit(self)
        self.edit1.setPlaceholderText("输入订单号")
        self.edit1.setGeometry(600+110, 100, 300, 30)
        self.edit2 = QLineEdit(self)
        self.edit2.setPlaceholderText("输入折扣")
        self.edit2.setGeometry(600+110, 200, 300, 30)
        self.edit3 = QLineEdit(self)
        self.edit3.setPlaceholderText("输入商品号")
        self.edit3.setGeometry(600+110, 300, 300, 30)
        self.edit1.show()
        self.edit2.show()
        self.edit3.show()
        self.widgets_to_delete.append(self.edit1)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.edit2)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.edit3)  # 将新按钮添加到删除列表中

        # 创建label（纯文本），在创建时指定父亲
        self.label4 = QLabel("消费金额", self)
        self.label5 = QLabel("销售日期", self)

        # 设置显示位置与大小  x，y，w，h
        self.label4.setGeometry(1020+110, 100, 70, 30)
        self.label5.setGeometry(1020+110, 200, 70, 30)
        self.label4.show()
        self.label5.show()
        self.widgets_to_delete.append(self.label4)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.label5)  # 将新按钮添加到删除列表中

        # 显示文本框
        self.edit4 = QLineEdit(self)
        self.edit4.setPlaceholderText("输入消费金额")
        self.edit4.setGeometry(1100+110, 100, 300, 30)
        self.edit5 = QLineEdit(self)
        self.edit5.setPlaceholderText("输入销售日期")
        self.edit5.setGeometry(1100+110, 200, 300, 30)
        self.edit4.show()
        self.edit5.show()
        self.widgets_to_delete.append(self.edit4)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.edit5)  # 将新按钮添加到删除列表中

        # 创建按钮
        self.btn1 = QPushButton("查询")
        self.btn1.setGeometry(600+140, 400, 90, 35)
        self.btn2 = QPushButton("删除")
        self.btn2.setGeometry(800+140, 400, 90, 35)
        self.btn3 = QPushButton("修改")
        self.btn3.setGeometry(1000+140, 400, 90, 35)
        self.btn4 = QPushButton("增加")
        self.btn4.setGeometry(1200+140, 400, 90, 35)
        # 设置按钮的父亲为当前窗口，相当于添加到W窗口中
        self.btn1.setParent(self)
        self.btn2.setParent(self)
        self.btn3.setParent(self)
        self.btn4.setParent(self)
        self.btn1.show()
        self.btn2.show()
        self.btn3.show()
        self.btn4.show()
        self.widgets_to_delete.append(self.btn1)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.btn2)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.btn3)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.btn4)  # 将新按钮添加到删除列表中

        self.t01 = Saleorder()  # 创建一个员工表实例
        self.click_counter01 = ClickCounter()  # 创建一个点击计数器实例

        def select():
            self.click_counter01.increment()  # 点击计数器加1
            if self.click_counter01.get_count() > 0:  # 如果点击次数大于0
                self.ls = []
                self.t01.select_search(self.ls, self.cursor, self.conn, self.edit1.text(),
                                       self.edit2.text(), int(self.edit4.text()),
                                       self.edit5.text(),  self.edit3.text())
                self.click_counter01.decrement()  # 计数器置0
                length = len(self.ls[0])
                data = []
                age = []
                for record_tuple in self.ls[0]:
                    # 获取 Decimal 对象
                    decimal_value = record_tuple[2]
                    # 将 Decimal 对象转换为字符串并去除单引号，然后转换为整数
                    integer_value = int(str(decimal_value))
                    # 转换后的整数
                    age.append(integer_value)
                # 遍历列表中的每个元组
                for record_tuple in self.ls[0]:
                    # 获取日期对象
                    date_obj = record_tuple[3]
                    # 将日期对象转换为 'YYYY-MM-DD' 格式的字符串
                    formatted_date = date_obj.strftime('%Y-%m-%d')
                    # 输出格式化后的日期
                    data.append(formatted_date)
                for i in range(length):
                    # 显示数据
                    self.item0 = QTableWidgetItem(self.ls[0][i][0])
                    self.table_widget.setItem(i, 0, self.item0)
                    self.item1 = QTableWidgetItem(self.ls[0][i][1])
                    self.table_widget.setItem(i, 1, self.item1)
                    self.item2 = QTableWidgetItem(str(age[i]))
                    self.table_widget.setItem(i, 2, self.item2)
                    self.item3 = QTableWidgetItem(self.ls[0][i][3])
                    self.item5 = QTableWidgetItem(data[i])
                    self.table_widget.setItem(i, 5, self.item5)
                self.table_widget.setGeometry(0, 0, 1000, 400)
                self.table_widget.setParent(self.edit_result)
                self.table_widget.show()

        self.btn1.clicked.connect(select)

        self.t02 = Saleorder()  # 创建一个员工表实例
        self.click_counter02 = ClickCounter()  # 创建一个点击计数器实例

        def delete():
            self.click_counter02.increment()  # 点击计数器加1
            if self.click_counter02.get_count() > 0:  # 如果点击次数大于0
                self.t02.delete_employee(self.cursor, self.conn, self.edit1.text(),
                                       self.edit2.text(), int(self.edit4.text()),
                                       self.edit5.text(),  self.edit3.text())
                self.click_counter02.decrement()  # 计数器置0

        self.btn2.clicked.connect(delete)

        self.t03 = Saleorder()  # 创建一个员工表实例
        self.click_counter03 = ClickCounter()  # 创建一个点击计数器实例

        def update():
            self.click_counter03.increment()  # 点击计数器加1
            if self.click_counter03.get_count() > 0:  # 如果点击次数大于0
                self.t03.update_employee(self.cursor, self.conn, self.edit1.text(),
                                       self.edit2.text(), int(self.edit4.text()),
                                       self.edit5.text(),  self.edit3.text())
                self.click_counter03.decrement()  # 计数器置0
                # 显示数据
                self.item0 = QTableWidgetItem(self.edit1.text())
                self.table_widget.setItem(0, 0, self.item0)
                self.item1 = QTableWidgetItem(self.edit2.text())
                self.table_widget.setItem(0, 1, self.item1)
                self.item2 = QTableWidgetItem(self.edit4.text())
                self.table_widget.setItem(0, 2, self.item2)
                self.item3 = QTableWidgetItem(self.edit5.text())
                self.table_widget.setItem(0, 3, self.item3)
                self.item4 = QTableWidgetItem(self.edit3.text())
                self.table_widget.setItem(0, 4, self.item4)
                self.table_widget.setGeometry(0, 0, 1000, 400)
                self.table_widget.setParent(self.edit_result)
                self.table_widget.show()

        self.btn3.clicked.connect(update)

        self.t04 = Saleorder()  # 创建一个员工表实例
        self.click_counter04 = ClickCounter()  # 创建一个点击计数器实例

        def addemp():
            self.click_counter04.increment()  # 点击计数器加1
            if self.click_counter04.get_count() > 0:  # 如果点击次数大于0
                self.t04.addemployee(self.cursor, self.conn, self.edit1.text(),
                                       self.edit2.text(), int(self.edit4.text()),
                                       self.edit5.text(),  self.edit3.text())
                self.click_couclick_counter04nter.decrement()  # 计数器置0
                # 显示数据
                self.item0 = QTableWidgetItem(self.edit1.text())
                self.table_widget.setItem(0, 0, self.item0)
                self.item1 = QTableWidgetItem(self.edit2.text())
                self.table_widget.setItem(0, 1, self.item1)
                self.item2 = QTableWidgetItem(self.edit4.text())
                self.table_widget.setItem(0, 2, self.item2)
                self.item3 = QTableWidgetItem(self.edit5.text())
                self.table_widget.setItem(0, 3, self.item3)
                self.item4 = QTableWidgetItem(self.edit6.text())
                self.table_widget.setItem(0, 4, self.item4)
                self.table_widget.setGeometry(0, 0, 1000, 400)
                self.table_widget.setParent(self.edit_result)
                self.table_widget.show()

        self.btn4.clicked.connect(addemp)


        # 显示查询结果文本框
        self.edit_result = QLineEdit(self)
        self.edit_result.setPlaceholderText("查询结果")
        self.edit_result.setGeometry(600, 500, 1000, 600)
        self.edit_result.show()
        self.widgets_to_delete.append(self.edit_result)  # 将新按钮添加到删除列表中
        # 创建表格
        self.table_widget = QTableWidget(20, 5)
        # 设置数据标题
        self.table_widget.setHorizontalHeaderLabels(['销售订单号','折扣','消费金额','销售日期','商品号'])
        # 显示表格
        self.table_widget.setGeometry(0, 0, 1000, 400)
        self.table_widget.setParent(self.edit_result)
        self.table_widget.show()
        self.widgets_to_delete.append(self.table_widget)

    def sale(self):
        self.delete_widgets_in_range(400, 0, self.width(), self.height())
        # 创建label（纯文本），在创建时指定父亲
        self.label1 = QLabel("商品号", self)
        self.label2 = QLabel("订单号", self)

        # 设置显示位置与大小  x，y，w，h
        self.label1.setGeometry(500 + 110, 100, 60, 30)
        self.label2.setGeometry(500 + 110, 200, 60, 30)
        self.label1.show()
        self.label2.show()
        self.widgets_to_delete.append(self.label1)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.label2)  # 将新按钮添加到删除列表中

        # 显示文本框
        self.edit1 = QLineEdit(self)
        self.edit1.setPlaceholderText("输入商品号")
        self.edit1.setGeometry(600 + 110, 100, 300, 30)
        self.edit2 = QLineEdit(self)
        self.edit2.setPlaceholderText("输入订单号")
        self.edit2.setGeometry(600 + 110, 200, 300, 30)
        self.edit1.show()
        self.edit2.show()
        self.widgets_to_delete.append(self.edit1)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.edit2)  # 将新按钮添加到删除列表中

        # 创建label（纯文本），在创建时指定父亲
        self.label3 = QLabel("顾客号", self)
        self.label4 = QLabel("店号", self)

        # 设置显示位置与大小  x，y，w，h
        self.label3.setGeometry(920 + 210, 100, 70, 30)
        self.label4.setGeometry(920 + 210, 200, 70, 30)
        self.label3.show()
        self.label4.show()
        self.widgets_to_delete.append(self.label3)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.label4)  # 将新按钮添加到删除列表中

        # 显示文本框
        self.edit3 = QLineEdit(self)
        self.edit3.setPlaceholderText("输入顾客号")
        self.edit3.setGeometry(1000 + 210, 100, 300, 30)
        self.edit4 = QLineEdit(self)
        self.edit4.setPlaceholderText("输入店号")
        self.edit4.setGeometry(1000 + 210, 200, 300, 30)
        self.edit3.show()
        self.edit4.show()
        self.widgets_to_delete.append(self.edit3)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.edit4)  # 将新按钮添加到删除列表中

        # 创建按钮
        self.btn1 = QPushButton("查询")
        self.btn1.setGeometry(600 + 140, 400, 90, 35)
        self.btn2 = QPushButton("删除")
        self.btn2.setGeometry(800 + 140, 400, 90, 35)
        self.btn3 = QPushButton("修改")
        self.btn3.setGeometry(1000 + 140, 400, 90, 35)
        self.btn4 = QPushButton("增加")
        self.btn4.setGeometry(1200 + 140, 400, 90, 35)
        # 设置按钮的父亲为当前窗口，相当于添加到W窗口中
        self.btn1.setParent(self)
        self.btn2.setParent(self)
        self.btn3.setParent(self)
        self.btn4.setParent(self)
        self.btn1.show()
        self.btn2.show()
        self.btn3.show()
        self.btn4.show()
        self.widgets_to_delete.append(self.btn1)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.btn2)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.btn3)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.btn4)  # 将新按钮添加到删除列表中





        self.t1 = Market()  # 创建一个实例
        self.click_counter01 = ClickCounter()  # 创建一个点击计数器实例

        def select():
            self.click_counter01.increment()  # 点击计数器加1
            if self.click_counter01.get_count() > 0:  # 如果点击次数大于0
                self.ls = []
                self.t1.myselect(self.ls, self.cursor, self.conn, self.edit1.text(),
                                 self.edit3.text(), self.edit2.text(), self.edit4.text())
                self.click_counter01.decrement()  # 计数器置0
                length = len(self.ls[0])
                for i in range(length):
                    # 显示数据
                    self.item0 = QTableWidgetItem(self.ls[0][i][0])
                    self.table_widget.setItem(i, 0, self.item0)
                    self.item1 = QTableWidgetItem(self.ls[0][i][1])
                    self.table_widget.setItem(i, 1, self.item1)
                    self.item2 = QTableWidgetItem(self.ls[0][i][2])
                    self.table_widget.setItem(i, 2, self.item2)
                    self.item12 = QTableWidgetItem(self.ls[0][i][3])
                    self.table_widget.setItem(i, 2, self.item12)
                self.table_widget.setGeometry(0, 0, 1000, 400)
                self.table_widget.setParent(self.edit_result)
                self.table_widget.show()

        self.btn1.clicked.connect(select)

        self.t2 = Market()
        self.click_counter02 = ClickCounter()  # 创建一个点击计数器实例

        def delete():
            self.click_counter02.increment()  # 点击计数器加1
            if self.click_counter02.get_count() > 0:  # 如果点击次数大于0
                self.t2.mydelete(self.cursor, self.conn,self.edit1.text(),
                                 self.edit3.text(), self.edit2.text(), self.edit4.text())
                self.click_counter02.decrement()  # 计数器置0

        self.btn2.clicked.connect(delete)

        self.t3 = Market()
        self.click_counter03 = ClickCounter()  # 创建一个点击计数器实例

        def update():
            self.click_counter03.increment()  # 点击计数器加1
            if self.click_counter03.get_count() > 0:  # 如果点击次数大于0
                self.t3.myupdate(self.cursor, self.conn,self.edit1.text(),
                                 self.edit3.text(), self.edit2.text(), self.edit4.text())
                self.click_counter03.decrement()  # 计数器置0
                # 显示数据
                self.item0 = QTableWidgetItem(self.edit1.text())
                self.table_widget.setItem(0, 0, self.item0)
                self.item1 = QTableWidgetItem(self.edit3.text())
                self.table_widget.setItem(0, 1, self.item1)
                self.item2 = QTableWidgetItem(self.edit2.text())
                self.table_widget.setItem(0, 2, self.item2)
                self.item12 = QTableWidgetItem(self.edit4.text())
                self.table_widget.setItem(0, 2, self.item12)
                self.table_widget.setGeometry(0, 0, 1000, 400)
                self.table_widget.setParent(self.edit_result)
                self.table_widget.show()

        self.btn3.clicked.connect(update)

        self.t4 = Market()
        # 创建一个点击计数器实例
        self.click_counter04 = ClickCounter()

        def addsup():
            self.click_counter04.increment()  # 点击计数器加1
            if self.click_counter04.get_count() > 0:  # 如果点击次数大于0
                self.t4.addSupermarket(self.cursor, self.conn,self.edit1.text(),
                                 self.edit3.text(), self.edit2.text(), self.edit4.text())
                self.click_counter04.decrement()  # 计数器置0
                # 显示数据
                self.item1 = QTableWidgetItem(self.edit1.text())
                self.table_widget.setItem(0, 1, self.item1)
                self.item2 = QTableWidgetItem(self.edit3.text())
                self.table_widget.setItem(0, 2, self.item2)
                self.item0 = QTableWidgetItem(self.edit2.text())
                self.table_widget.setItem(0, 0, self.item0)
                self.item10 = QTableWidgetItem(self.edit4.text())
                self.table_widget.setItem(0, 0, self.item10)
                self.table_widget.setGeometry(0, 0, 1000, 400)
                self.table_widget.setParent(self.edit_result)
                self.table_widget.show()

        self.btn4.clicked.connect(addsup)



        # 显示查询结果文本框
        self.edit_result = QLineEdit(self)
        self.edit_result.setPlaceholderText("查询结果")
        self.edit_result.setGeometry(600, 500, 1000, 600)
        self.edit_result.show()
        self.widgets_to_delete.append(self.edit_result)  # 将新按钮添加到删除列表中
        # 创建表格
        self.table_widget = QTableWidget(20, 4)
        # 设置数据标题
        self.table_widget.setHorizontalHeaderLabels(['商品号', '店号', '销售订单号', '顾客号'])
        # 显示表格
        self.table_widget.setGeometry(0, 0, 1000, 400)
        self.table_widget.setParent(self.edit_result)
        self.table_widget.show()
        self.widgets_to_delete.append(self.table_widget)

    def purchase(self):
        self.delete_widgets_in_range(400, 0, self.width(), self.height())
        # 创建label（纯文本），在创建时指定父亲
        self.label1 = QLabel("员工号", self)
        self.label2 = QLabel("订单号", self)
        self.label3 = QLabel("商品号", self)
        # 设置显示位置与大小  x，y，w，h
        self.label1.setGeometry(500 + 110, 100, 60, 30)
        self.label2.setGeometry(500 + 110, 200, 60, 30)
        self.label3.setGeometry(500 + 110, 300, 60, 30)
        self.label1.show()
        self.label2.show()
        self.label3.show()
        self.widgets_to_delete.append(self.label1)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.label2)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.label3)  # 将新按钮添加到删除列表中
        # 显示文本框
        self.edit1 = QLineEdit(self)
        self.edit1.setPlaceholderText("输入员工号")
        self.edit1.setGeometry(600 + 110, 100, 300, 30)
        self.edit2 = QLineEdit(self)
        self.edit2.setPlaceholderText("输入订单号")
        self.edit2.setGeometry(600 + 110, 200, 300, 30)
        self.edit3 = QLineEdit(self)
        self.edit3.setPlaceholderText("输入商品号")
        self.edit3.setGeometry(600 + 110, 300, 300, 30)
        self.edit1.show()
        self.edit2.show()
        self.edit3.show()
        self.widgets_to_delete.append(self.edit1)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.edit2)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.edit3)  # 将新按钮添加到删除列表中

        # 创建label（纯文本），在创建时指定父亲
        self.label4 = QLabel("供应商号", self)
        self.label5 = QLabel("商品数量", self)
        self.label6 = QLabel("商品单价", self)

        # 设置显示位置与大小  x，y，w，h
        self.label4.setGeometry(920 + 210, 100, 70, 30)
        self.label5.setGeometry(920 + 210, 200, 70, 30)
        self.label6.setGeometry(920 + 210, 300, 70, 30)
        self.label4.show()
        self.label5.show()
        self.label6.show()
        self.widgets_to_delete.append(self.label4)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.label5)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.label6)  # 将新按钮添加到删除列表中

        # 显示文本框
        self.edit4 = QLineEdit(self)
        self.edit4.setPlaceholderText("输入供应商号")
        self.edit4.setGeometry(1000 + 210, 100, 300, 30)
        self.edit5 = QLineEdit(self)
        self.edit5.setPlaceholderText("输入商品数量")
        self.edit5.setGeometry(1000 + 210, 200, 300, 30)
        self.edit6 = QLineEdit(self)
        self.edit6.setPlaceholderText("输入商品单价")
        self.edit6.setGeometry(1000 + 210, 300, 300, 30)
        self.edit4.show()
        self.edit5.show()
        self.edit6.show()
        self.widgets_to_delete.append(self.edit4)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.edit5)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.edit6)  # 将新按钮添加到删除列表中

        # 创建按钮
        self.btn1 = QPushButton("查询")
        self.btn1.setGeometry(600 + 140, 400, 90, 35)
        self.btn2 = QPushButton("删除")
        self.btn2.setGeometry(800 + 140, 400, 90, 35)
        self.btn3 = QPushButton("修改")
        self.btn3.setGeometry(1000 + 140, 400, 90, 35)
        self.btn4 = QPushButton("增加")
        self.btn4.setGeometry(1200 + 140, 400, 90, 35)
        # 设置按钮的父亲为当前窗口，相当于添加到W窗口中
        self.btn1.setParent(self)
        self.btn2.setParent(self)
        self.btn3.setParent(self)
        self.btn4.setParent(self)
        self.btn1.show()
        self.btn2.show()
        self.btn3.show()
        self.btn4.show()
        self.widgets_to_delete.append(self.btn1)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.btn2)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.btn3)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.btn4)  # 将新按钮添加到删除列表中

        self.t01 = Purchase()  # 创建一个员工表实例
        self.click_counter01 = ClickCounter()  # 创建一个点击计数器实例

        def select():
            self.click_counter01.increment()  # 点击计数器加1
            if self.click_counter01.get_count() > 0:  # 如果点击次数大于0
                self.ls = []
                self.t01.select_search(self.ls, self.cursor, self.conn,self.edit1.text(),
                                       self.edit3.text(), self.edit2.text(),
                                       self.edit4.text(), self.edit5.text(),
                                       self.edit6.text())
                self.click_counter01.decrement()  # 计数器置0
                length = len(self.ls[0])
                age1 = []
                for record_tuple in self.ls[0]:
                    # 获取 Decimal 对象
                    decimal_value = record_tuple[4]
                    # 将 Decimal 对象转换为字符串并去除单引号，然后转换为整数
                    integer_value = int(str(decimal_value))
                    # 转换后的整数
                    age1.append(integer_value)
                age2 = []
                for record_tuple in self.ls[0]:
                    # 获取 Decimal 对象
                    decimal_value = record_tuple[5]
                    # 将 Decimal 对象转换为字符串并去除单引号，然后转换为整数
                    integer_value = int(str(decimal_value))
                    # 转换后的整数
                    age2.append(integer_value)
                for i in range(length):
                    # 显示数据
                    self.item0 = QTableWidgetItem(self.ls[0][i][0])
                    self.table_widget.setItem(i, 0, self.item0)
                    self.item1 = QTableWidgetItem(self.ls[0][i][2])
                    self.table_widget.setItem(i, 1, self.item1)
                    self.item3 = QTableWidgetItem(self.ls[0][i][1])
                    self.table_widget.setItem(i, 3, self.item3)
                    self.item4 = QTableWidgetItem(self.ls[0][i][3])
                    self.table_widget.setItem(i, 4, self.item4)
                    self.item2 = QTableWidgetItem(str(age1[i]))
                    self.table_widget.setItem(i, 2, self.item2)
                    self.item12 = QTableWidgetItem(str(age2[i]))
                    self.table_widget.setItem(i, 2, self.item12)
                self.table_widget.setGeometry(0, 0, 1000, 400)
                self.table_widget.setParent(self.edit_result)
                self.table_widget.show()

        self.btn1.clicked.connect(select)

        self.t02 = Purchase()  # 创建一个员工表实例
        self.click_counter02 = ClickCounter()  # 创建一个点击计数器实例

        def delete():
            self.click_counter02.increment()  # 点击计数器加1
            if self.click_counter02.get_count() > 0:  # 如果点击次数大于0
                self.t02.delete_employee(self.cursor, self.conn,self.edit1.text(),
                                       self.edit3.text(), self.edit2.text(),
                                       self.edit4.text(), self.edit5.text(),
                                       self.edit6.text())
                self.click_counter02.decrement()  # 计数器置0

        self.btn2.clicked.connect(delete)

        self.t03 = Purchase()  # 创建一个员工表实例
        self.click_counter03 = ClickCounter()  # 创建一个点击计数器实例

        def update():
            self.click_counter03.increment()  # 点击计数器加1
            if self.click_counter03.get_count() > 0:  # 如果点击次数大于0
                self.t03.update_employee(self.cursor, self.conn, self.edit1.text(),
                                       self.edit3.text(), self.edit2.text(),
                                       self.edit4.text(), self.edit5.text(),
                                       self.edit6.text())
                self.click_counter03.decrement()  # 计数器置0
                # 显示数据
                self.item0 = QTableWidgetItem(self.edit1.text())
                self.table_widget.setItem(0, 0, self.item0)
                self.item1 = QTableWidgetItem(self.edit3.text())
                self.table_widget.setItem(0, 1, self.item1)
                self.item2 = QTableWidgetItem(self.edit2.text())
                self.table_widget.setItem(0, 2, self.item2)
                self.item3 = QTableWidgetItem(self.edit4.text())
                self.table_widget.setItem(0, 3, self.item3)
                self.item4 = QTableWidgetItem(self.edit5.text())
                self.table_widget.setItem(0, 4, self.item4)
                self.item5 = QTableWidgetItem(self.edit6.text())
                self.table_widget.setItem(0, 5, self.item5)
                self.table_widget.setGeometry(0, 0, 1000, 400)
                self.table_widget.setParent(self.edit_result)
                self.table_widget.show()

        self.btn3.clicked.connect(update)

        self.t04 = Purchase()  # 创建一个员工表实例
        self.click_counter04 = ClickCounter()  # 创建一个点击计数器实例

        def addemp():
            self.click_counter04.increment()  # 点击计数器加1
            if self.click_counter04.get_count() > 0:  # 如果点击次数大于0
                self.t04.addemployee(self.cursor, self.conn,self.edit1.text(),
                                       self.edit3.text(), self.edit2.text(),
                                       self.edit4.text(), self.edit5.text(),
                                       self.edit6.text())
                self.click_couclick_counter04nter.decrement()  # 计数器置0
                # 显示数据
                self.item0 = QTableWidgetItem(self.edit1.text())
                self.table_widget.setItem(0, 0, self.item0)
                self.item1 = QTableWidgetItem(self.edit3.text())
                self.table_widget.setItem(0, 1, self.item1)
                self.item2 = QTableWidgetItem(self.edit2.text())
                self.table_widget.setItem(0, 2, self.item2)
                self.item3 = QTableWidgetItem(self.edit4.text())
                self.table_widget.setItem(0, 3, self.item3)
                self.item4 = QTableWidgetItem(self.edit5.text())
                self.table_widget.setItem(0, 4, self.item4)
                self.item5 = QTableWidgetItem(self.edit6.text())
                self.table_widget.setItem(0, 5, self.item5)
                self.table_widget.setGeometry(0, 0, 1000, 400)
                self.table_widget.setParent(self.edit_result)
                self.table_widget.show()

        self.btn4.clicked.connect(addemp)


        # 显示查询结果文本框
        self.edit_result = QLineEdit(self)
        self.edit_result.setPlaceholderText("查询结果")
        self.edit_result.setGeometry(600, 500, 1000, 600)
        self.edit_result.show()
        self.widgets_to_delete.append(self.edit_result)  # 将新按钮添加到删除列表中
        # 创建表格
        self.table_widget = QTableWidget(20, 6)
        # 设置数据标题
        self.table_widget.setHorizontalHeaderLabels(['员工号', '订单号', '商品号', '供应商号', '商品数量', '商品单价'])
        # 显示表格
        self.table_widget.setGeometry(0, 0, 1000, 400)
        self.table_widget.setParent(self.edit_result)
        self.table_widget.show()
        self.widgets_to_delete.append(self.table_widget)

    def apply(self):
        self.delete_widgets_in_range(400, 0, self.width(), self.height())
        # 创建label（纯文本），在创建时指定父亲
        self.label1 = QLabel("商品号", self)
        self.label2 = QLabel("供应商号", self)

        # 设置显示位置与大小  x，y，w，h
        self.label1.setGeometry(500+110, 100, 80, 30)
        self.label2.setGeometry(500+110, 200, 80, 30)
        self.label1.show()
        self.label2.show()
        self.widgets_to_delete.append(self.label1)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.label2)  # 将新按钮添加到删除列表中

        # 显示文本框
        self.edit1 = QLineEdit(self)
        self.edit1.setPlaceholderText("输入商品号")
        self.edit1.setGeometry(600+110, 100, 300, 30)
        self.edit2 = QLineEdit(self)
        self.edit2.setPlaceholderText("输入供应商号")
        self.edit2.setGeometry(600+110, 200, 300, 30)
        self.edit1.show()
        self.edit2.show()
        self.widgets_to_delete.append(self.edit1)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.edit2)  # 将新按钮添加到删除列表中

        # 创建按钮
        self.btn1 = QPushButton("查询")
        self.btn1.setGeometry(600 + 140, 400, 90, 35)
        self.btn2 = QPushButton("删除")
        self.btn2.setGeometry(800 + 140, 400, 90, 35)
        self.btn3 = QPushButton("修改")
        self.btn3.setGeometry(1000 + 140, 400, 90, 35)
        self.btn4 = QPushButton("增加")
        self.btn4.setGeometry(1200 + 140, 400, 90, 35)
        # 设置按钮的父亲为当前窗口，相当于添加到W窗口中
        self.btn1.setParent(self)
        self.btn2.setParent(self)
        self.btn3.setParent(self)
        self.btn4.setParent(self)
        self.btn1.show()
        self.btn2.show()
        self.btn3.show()
        self.btn4.show()
        self.widgets_to_delete.append(self.btn1)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.btn2)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.btn3)  # 将新按钮添加到删除列表中
        self.widgets_to_delete.append(self.btn4)  # 将新按钮添加到删除列表中






        self.t1 = Supply()  # 创建一个实例
        self.click_counter01 = ClickCounter()  # 创建一个点击计数器实例

        def select():
            self.click_counter01.increment()  # 点击计数器加1
            if self.click_counter01.get_count() > 0:  # 如果点击次数大于0
                self.ls = []
                self.t1.myselect(self.ls, self.cursor, self.conn, self.edit2.text(),
                                 self.edit1.text())
                self.click_counter01.decrement()  # 计数器置0
                length = len(self.ls[0])
                for i in range(length):
                    # 显示数据
                    self.item0 = QTableWidgetItem(self.ls[0][i][0])
                    self.table_widget.setItem(i, 0, self.item0)
                    self.item1 = QTableWidgetItem(self.ls[0][i][1])
                    self.table_widget.setItem(i, 1, self.item1)
                self.table_widget.setGeometry(0, 0, 1000, 400)
                self.table_widget.setParent(self.edit_result)
                self.table_widget.show()

        self.btn1.clicked.connect(select)

        self.t2 = Supply()
        self.click_counter02 = ClickCounter()  # 创建一个点击计数器实例

        def delete():
            self.click_counter02.increment()  # 点击计数器加1
            if self.click_counter02.get_count() > 0:  # 如果点击次数大于0
                self.t2.mydelete(self.cursor, self.conn,self.edit2.text(),
                                 self.edit1.text())
                self.click_counter02.decrement()  # 计数器置0

        self.btn2.clicked.connect(delete)

        self.t3 = Supply()
        self.click_counter03 = ClickCounter()  # 创建一个点击计数器实例

        def update():
            self.click_counter03.increment()  # 点击计数器加1
            if self.click_counter03.get_count() > 0:  # 如果点击次数大于0
                self.t3.myupdate(self.cursor, self.conn,self.edit2.text(),
                                 self.edit1.text())
                self.click_counter03.decrement()  # 计数器置0
                # 显示数据
                self.item0 = QTableWidgetItem(self.edit2.text())
                self.table_widget.setItem(0, 0, self.item0)
                self.item1 = QTableWidgetItem(self.edit1.text())
                self.table_widget.setItem(0, 1, self.item1)
                self.table_widget.setGeometry(0, 0, 1000, 400)
                self.table_widget.setParent(self.edit_result)
                self.table_widget.show()

        self.btn3.clicked.connect(update)

        self.t4 = Supply()
        # 创建一个点击计数器实例
        self.click_counter04 = ClickCounter()

        def addsup():
            self.click_counter04.increment()  # 点击计数器加1
            if self.click_counter04.get_count() > 0:  # 如果点击次数大于0
                self.t4.addSupermarket(self.cursor, self.conn,self.edit2.text(),
                                 self.edit1.text())
                self.click_counter04.decrement()  # 计数器置0
                # 显示数据
                self.item1 = QTableWidgetItem(self.edit2.text())
                self.table_widget.setItem(0, 1, self.item1)
                self.item2 = QTableWidgetItem(self.edit1.text())
                self.table_widget.setItem(0, 2, self.item2)
                self.table_widget.setGeometry(0, 0, 1000, 400)
                self.table_widget.setParent(self.edit_result)
                self.table_widget.show()

        self.btn4.clicked.connect(addsup)


        # 显示查询结果文本框
        self.edit_result = QLineEdit(self)
        self.edit_result.setPlaceholderText("查询结果")
        self.edit_result.setGeometry(600, 500, 1000, 600)
        self.edit_result.show()
        self.widgets_to_delete.append(self.edit_result)  # 将新按钮添加到删除列表中
        # 创建表格
        self.table_widget = QTableWidget(20, 2)
        # 设置数据标题
        self.table_widget.setHorizontalHeaderLabels(['供应商号',  '商品号'])
        # 显示表格
        self.table_widget.setGeometry(0, 0, 1000, 400)
        self.table_widget.setParent(self.edit_result)
        self.table_widget.show()
        self.widgets_to_delete.append(self.table_widget)

    def delete_widgets_in_range(self, x1, y1, x2, y2):
        for widget in self.widgets_to_delete:
            widget_rect = widget.geometry()
            widget_x = widget_rect.x()
            widget_y = widget_rect.y()
            if x1 <= widget_x <= x2 and y1 <= widget_y <= y2:
                widget.setParent(None)
        self.widgets_to_delete.clear()  # 删除后清空列表