from PyQt5.QtWidgets import *
class Supply(QWidget):
    def __init__(self):
        super().__init__()
    def myselect(self, result,cursor,conn,Pno='',Sno=''):
        Sno  = Sno
        Pno  = Pno
        self.cursor = cursor
        self.conn = conn
        if Sno == '' and Pno == '':
            QMessageBox.warning(self, '警告', '请填写查询内容!')
            return
        try:
            # 执行查询操作
            conditions = []
            if Sno:
                conditions.append(f"Sno = '{Sno}'")
            if Pno :
                conditions.append(f"Pno  = '{Pno }'")
            query = "SELECT * FROM Supply WHERE " + " AND ".join(conditions)
            self.cursor.execute(query)
            result.append(self.cursor.fetchall())
            if len(result)!=0:
                QMessageBox.information(self, '查询结果', '查询供应信息成功!')
            else:
                QMessageBox.information(self, '查询结果', '未找到匹配记录!')
        except Exception as e:
            QMessageBox.warning(self, '错误', f'查询供应信息失败: {str(e)}')

    def mydelete(self, cursor, conn,Pno='',Sno=''):
        Sno = Sno
        Pno = Pno
        self.cursor = cursor
        self.conn = conn
        try:
            conditions = []
            if Sno:
                conditions.append(f"Sno = '{Sno}'")
            if Pno:
                conditions.append(f"Pno  = '{Pno}'")
            query = "DELETE FROM Supply WHERE " + " AND ".join(conditions)
            cursor.execute(query)
            conn.commit()
            QMessageBox.information(self, '成功', '供应信息删除成功')
        except Exception as e:
            QMessageBox.warning(self, '错误', f'供应信息删除失败: {str(e)}')

    def myupdate(self, cursor, conn,Pno='',Sno=''):
        Sno = Sno
        Pno = Pno
        self.cursor = cursor
        self.conn = conn
        if Sno == '':
            QMessageBox.warning(self, '警告', '请正确填写供应商号!')
            return
        try:
            # 执行修改操作
            sql = "UPDATE Supply SET Sno = %s WHERE Pno = %s"
            val = (Sno,Pno)
            self.cursor.execute(sql, val)
            self.conn.commit()
            QMessageBox.information(self, "成功", "供应信息已成功修改！")
        except Exception as e:
            QMessageBox.critical(self, "错误", f"供应信息修改失败：{str(e)}")

    def addSupermarket(self,cursor,conn,Pno='',Sno=''):
        Sno = Sno
        Pno = Pno
        self.cursor=cursor
        self.conn=conn
        if Sno=='' or Pno=='':
            QMessageBox.warning(self, '警告', '请填写所有字段!')
            return
        try:
            # 执行插入操作
            sql = "INSERT INTO Supply (Pno, Sno) VALUES (%s, %s)"
            val = (Pno, Sno)
            self.cursor.execute(sql, val)
            self.conn.commit()
            QMessageBox.information(self, '成功', '供应信息添加成功!')
        except Exception as e:
            QMessageBox.warning(self, '错误', f'供应信息添加失败: {str(e)}')