from PyQt5.QtWidgets import *
class Market(QWidget):
    def __init__(self):
        super().__init__()
    def myselect(self, result,cursor,conn,Pno='',Mno='',Sno='',Cno=''):
        Pno,Mno,Sno,Cno = Pno,Mno,Sno,Cno
        self.cursor = cursor
        self.conn = conn
        if Pno== '' and Mno== '' and Sno== '' and Cno=='':
            QMessageBox.warning(self, '警告', '请填写查询内容!')
            return
        try:
            # 执行查询操作
            conditions = []
            if Pno :
                conditions.append(f"Pno  = '{Pno }'")
            if Mno:
                conditions.append(f"Mno = '{Mno}'")
            if Sno:
                conditions.append(f"Sno = '{Sno}'")
            if Cno :
                conditions.append(f"Cno  = '{Cno }'")
            query = "SELECT * FROM Market WHERE " + " AND ".join(conditions)
            self.cursor.execute(query)
            result.append(self.cursor.fetchall())
            if len(result)!=0:
                QMessageBox.information(self, '查询结果', '查询销售信息成功!')
            else:
                QMessageBox.information(self, '查询结果', '未找到匹配记录!')
        except Exception as e:
            QMessageBox.warning(self, '错误', f'查询销售信息失败: {str(e)}')

    def mydelete(self, cursor, conn,Pno='',Mno='',Sno='',Cno=''):
        Pno,Mno,Sno,Cno = Pno,Mno,Sno,Cno
        self.cursor = cursor
        self.conn = conn
        try:
            conditions = []
            if Pno :
                conditions.append(f"Pno  = '{Pno }'")
            if Mno:
                conditions.append(f"Mno = '{Mno}'")
            if Sno:
                conditions.append(f"Sno = '{Sno}'")
            if Cno :
                conditions.append(f"Cno  = '{Cno }'")
            query = "DELETE FROM Market WHERE " + " AND ".join(conditions)
            cursor.execute(query)
            conn.commit()
            QMessageBox.information(self, '成功', '销售信息删除成功')
        except Exception as e:
            QMessageBox.warning(self, '错误', f'销售信息删除失败: {str(e)}')

    def myupdate(self, cursor, conn,Pno='',Mno='',Sno='',Cno=''):
        Pno,Mno,Sno,Cno = Pno,Mno,Sno,Cno
        self.cursor = cursor
        self.conn = conn
        if Pno == '' and Mno == '' and Sno == '' and Cno == '':
            QMessageBox.warning(self, '警告', '请填写查询内容!')
            return
        try:
            # 执行修改操作
            sql = "UPDATE Market SET Mno = %s,Sno = %s,Cno = %s WHERE Pno = %s"
            val = (Mno,Sno,Cno,Pno)
            self.cursor.execute(sql, val)
            self.conn.commit()
            QMessageBox.information(self, "成功", "销售信息已成功修改！")
        except Exception as e:
            QMessageBox.critical(self, "错误", f"销售信息修改失败：{str(e)}")

    def addSupermarket(self,cursor,conn,Pno='',Mno='',Sno='',Cno=''):
        Pno,Mno,Sno,Cno = Pno,Mno,Sno,Cno
        self.cursor=cursor
        self.conn=conn
        if Pno == '' and Mno == '' and Sno == '' and Cno == '':
            QMessageBox.warning(self, '警告', '请填写查询内容!')
            return
        try:
            # 执行插入操作
            sql = "INSERT INTO Market (Pno,Mno,Sno,Cno) VALUES (%s, %s,%s, %s)"
            val = (Pno,Mno,Sno,Cno)
            self.cursor.execute(sql, val)
            self.conn.commit()
            QMessageBox.information(self, '成功', '销售信息添加成功!')
        except Exception as e:
            QMessageBox.warning(self, '错误', f'销售信息添加失败: {str(e)}')