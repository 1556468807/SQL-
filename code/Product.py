from PyQt5.QtWidgets import *
class Product(QWidget):
    def __init__(self):
        super().__init__()
    def myselect(self, result,cursor,conn,Pno='',Pname='',Scno=''):
        Pno  = Pno
        Pname  = Pname
        Scno = Scno
        self.cursor = cursor
        self.conn = conn
        if Pno == '':
            QMessageBox.warning(self, '警告', '请填写查询内容!')
            return
        try:
            # 执行查询操作
            conditions = []
            if Pno:
                conditions.append(f"Pno = '{Pno}'")
            if Pname :
                conditions.append(f"Pname  = '{Pname }'")
            if Scno:
                conditions.append(f"Maddress = '{Scno}'")
            query = "SELECT * FROM Product WHERE " + " AND ".join(conditions)
            self.cursor.execute(query)
            result.append(self.cursor.fetchall())
            if len(result)!=0:
                QMessageBox.information(self, '查询结果', '查询商品信息成功!')
            else:
                QMessageBox.information(self, '查询结果', '未找到匹配记录!')
        except Exception as e:
            QMessageBox.warning(self, '错误', f'查询商品信息失败: {str(e)}')

    def mydelete(self, cursor, conn,Pno='',Pname='',Scno=''):
        Pno = Pno
        Pname = Pname
        Scno = Scno
        self.cursor = cursor
        self.conn = conn
        try:
            conditions = []
            if Pno:
                conditions.append(f"Pno = '{Pno}'")
            if Pname:
                conditions.append(f"Pname  = '{Pname}'")
            if Scno:
                conditions.append(f"Maddress = '{Scno}'")
            query = "DELETE FROM Product WHERE " + " AND ".join(conditions)
            cursor.execute(query)
            conn.commit()
            QMessageBox.information(self, '成功', '商品信息删除成功')
        except Exception as e:
            QMessageBox.warning(self, '错误', f'商品信息删除失败: {str(e)}')

    def myupdate(self, cursor, conn,Pno='',Pname='',Scno=''):
        Pno = Pno
        Pname = Pname
        Scno = Scno
        self.cursor = cursor
        self.conn = conn
        if Pno == '':
            QMessageBox.warning(self, '警告', '请正确填写商品号!')
            return
        try:
            # 执行修改操作
            sql = "UPDATE Product SET Pname = %s, Scno = %s WHERE Pno = %s"
            val = (Pname,Scno,Pno)
            self.cursor.execute(sql, val)
            self.conn.commit()
            QMessageBox.information(self, "成功", "商品信息已成功修改！")
        except Exception as e:
            QMessageBox.critical(self, "错误", f"商品信息修改失败：{str(e)}")

    def addSupermarket(self,cursor,conn,Pno='',Pname='',Scno=''):
        Pno = Pno
        Pname = Pname
        Scno = Scno
        self.cursor=cursor
        self.conn=conn
        if Pno=='' or Pname=='' or Scno=='':
            QMessageBox.warning(self, '警告', '请填写所有字段!')
            return
        try:
            # 执行插入操作
            sql = "INSERT INTO Product (Cno, Cname, Chy) VALUES (%s, %s, %s)"
            val = (Pno, Pname, Scno)
            self.cursor.execute(sql, val)
            self.conn.commit()
            QMessageBox.information(self, '成功', '商品信息添加成功!')
        except Exception as e:
            QMessageBox.warning(self, '错误', f'商品信息添加失败: {str(e)}')