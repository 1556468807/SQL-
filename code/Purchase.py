from PyQt5.QtWidgets import *
class Purchase(QWidget):
    def __init__(self):
        super().__init__()
    def myselect(self, result,cursor,conn,Eno='',Pno='',Ono='',Sno='',Pnum='',Price=''):
        Eno  = Eno
        Pno  = Pno
        Ono  = Ono
        Sno = Sno
        Pnum  = Pnum
        Price = Price
        self.cursor = cursor
        self.conn = conn
        if Eno == '' and Pno == '' and Ono == '' and Sno == '' and Pnum == '' and Price == '':
            QMessageBox.warning(self, '警告', '请填写查询内容!')
            return
        try:
            # 执行查询操作
            conditions = []
            if Eno:
                conditions.append(f"Eno = '{Eno}'")
            if Pno :
                conditions.append(f"Pno  = '{Pno }'")
            if Ono:
                conditions.append(f"Ono = '{Ono}'")
            if Sno:
                conditions.append(f"Sno = '{Sno}'")
            if Pnum:
                conditions.append(f"Pnum = '{Pnum}'")
            if Price:
                conditions.append(f"Price = '{Price}'")
            query = "SELECT * FROM Purchase WHERE " + " AND ".join(conditions)
            self.cursor.execute(query)
            result.append(self.cursor.fetchall())
            if len(result)!=0:
                QMessageBox.information(self, '查询结果', '查询采购信息成功!')
            else:
                QMessageBox.information(self, '查询结果', '未找到匹配记录!')
        except Exception as e:
            QMessageBox.warning(self, '错误', f'查询采购信息失败: {str(e)}')

    def mydelete(self, cursor, conn,Eno='',Pno='',Ono='',Sno='',Pnum='',Price=''):
        Eno  = Eno
        Pno  = Pno
        Ono  = Ono
        Sno = Sno
        Pnum  = Pnum
        Price = Price
        self.cursor = cursor
        self.conn = conn
        try:
            conditions = []
            if Eno:
                conditions.append(f"Eno = '{Eno}'")
            if Pno:
                conditions.append(f"Pno  = '{Pno}'")
            if Ono:
                conditions.append(f"Ono = '{Ono}'")
            if Sno:
                conditions.append(f"Sno = '{Sno}'")
            if Pnum:
                conditions.append(f"Pnum = '{Pnum}'")
            if Price:
                conditions.append(f"Price = '{Price}'")
            query = "DELETE FROM Purchase WHERE " + " AND ".join(conditions)
            cursor.execute(query)
            conn.commit()
            QMessageBox.information(self, '成功', '采购信息删除成功')
        except Exception as e:
            QMessageBox.warning(self, '错误', f'采购信息删除失败: {str(e)}')

    def myupdate(self, cursor, conn,Eno='',Pno='',Ono='',Sno='',Pnum='',Price=''):
        Eno  = Eno
        Pno  = Pno
        Ono  = Ono
        Sno = Sno
        Pnum  = Pnum
        Price = Price
        self.cursor = cursor
        self.conn = conn
        if Eno == '' and Pno == '' and Ono == '' and Sno == '' and Pnum == '' and Price == '':
            QMessageBox.warning(self, '警告', '请填写查询内容!')
            return
        try:
            # 执行修改操作
            sql = "UPDATE Purchase SET Pno = %s, Ono = %s, Sno = %s, Pnum = %s, Price = %s WHERE Eno = %s"
            val = (Pno,Ono,Sno,Pnum,Price,Eno)
            self.cursor.execute(sql, val)
            self.conn.commit()
            QMessageBox.information(self, "成功", "采购信息已成功修改！")
        except Exception as e:
            QMessageBox.critical(self, "错误", f"采购信息修改失败：{str(e)}")

    def addSupermarket(self,cursor,conn,Eno='',Pno='',Ono='',Sno='',Pnum='',Price=''):
        Eno  = Eno
        Pno  = Pno
        Ono  = Ono
        Sno = Sno
        Pnum  = Pnum
        Price = Price
        self.cursor=cursor
        self.conn=conn
        if Eno == '' and Pno == '' and Ono == '' and Sno == '' and Pnum == '' and Price == '':
            QMessageBox.warning(self, '警告', '请填写查询内容!')
            return
        try:
            # 执行插入操作
            sql = "INSERT INTO Purchase (Eno,Pno,Ono,Sno,Pnum,Price) VALUES (%s, %s, %s, %s, %s, %s)"
            val = (Eno,Pno,Ono,Sno,Pnum,Price)
            self.cursor.execute(sql, val)
            self.conn.commit()
            QMessageBox.information(self, '成功', '采购信息添加成功!')
        except Exception as e:
            QMessageBox.warning(self, '错误', f'采购信息添加失败: {str(e)}')