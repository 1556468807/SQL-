from PyQt5.QtWidgets import *
class Supplier(QWidget):
    def __init__(self):
        super().__init__()
    def myselect(self, result,cursor,conn,Sno='',Sname=''):
        Sno  = Sno
        Sname  = Sname
        self.cursor = cursor
        self.conn = conn
        if Sno == '':
            QMessageBox.warning(self, '警告', '请填写查询内容!')
            return
        try:
            # 执行查询操作
            conditions = []
            if Sno:
                conditions.append(f"Sno = '{Sno}'")
            if Sname :
                conditions.append(f"Sname  = '{Sname }'")
            query = "SELECT * FROM Supplier WHERE " + " AND ".join(conditions)
            self.cursor.execute(query)
            result.append(self.cursor.fetchall())
            if len(result)!=0:
                QMessageBox.information(self, '查询结果', '查询供应商信息成功!')
            else:
                QMessageBox.information(self, '查询结果', '未找到匹配记录!')
        except Exception as e:
            QMessageBox.warning(self, '错误', f'查询供应商信息失败: {str(e)}')

    def mydelete(self, cursor, conn,Sno='',Sname=''):
        Sno = Sno
        Sname = Sname
        self.cursor = cursor
        self.conn = conn
        try:
            conditions = []
            if Sno:
                conditions.append(f"Sno = '{Sno}'")
            if Sname:
                conditions.append(f"Sname  = '{Sname}'")
            query = "DELETE FROM Supplier WHERE " + " AND ".join(conditions)
            cursor.execute(query)
            conn.commit()
            QMessageBox.information(self, '成功', '供应商信息删除成功')
        except Exception as e:
            QMessageBox.warning(self, '错误', f'供应商信息删除失败: {str(e)}')

    def myupdate(self, cursor, conn,Sno='',Sname=''):
        Sno = Sno
        Sname = Sname
        self.cursor = cursor
        self.conn = conn
        if Sno == '':
            QMessageBox.warning(self, '警告', '请正确填写供应商号!')
            return
        try:
            # 执行修改操作
            sql = "UPDATE Supplier SET Sname = %s WHERE Sno = %s"
            val = (Sname,Sno)
            self.cursor.execute(sql, val)
            self.conn.commit()
            QMessageBox.information(self, "成功", "供应商信息已成功修改！")
        except Exception as e:
            QMessageBox.critical(self, "错误", f"供应商信息修改失败：{str(e)}")

    def addSupermarket(self,cursor,conn,Sno='',Sname=''):
        Sno = Sno
        Sname = Sname
        self.cursor=cursor
        self.conn=conn
        if Sno=='' or Sname=='':
            QMessageBox.warning(self, '警告', '请填写所有字段!')
            return
        try:
            # 执行插入操作
            sql = "INSERT INTO Supplier (Sno, Sname) VALUES (%s, %s)"
            val = (Sno, Sname)
            self.cursor.execute(sql, val)
            self.conn.commit()
            QMessageBox.information(self, '成功', '供应商信息添加成功!')
        except Exception as e:
            QMessageBox.warning(self, '错误', f'供应商信息添加失败: {str(e)}')