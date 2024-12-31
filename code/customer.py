from PyQt5.QtWidgets import *
class customer(QWidget):
    def __init__(self):
        super().__init__()
    def myselect(self, result,cursor,conn,Cno='',Cname='',Chy=''):
        Cno  = Cno
        Cname  = Cname
        Chy = Chy
        self.cursor = cursor
        self.conn = conn
        if Cno == '':
            QMessageBox.warning(self, '警告', '请填写查询内容!')
            return
        try:
            # 执行查询操作
            conditions = []
            if Chy:
                conditions.append(f"Chy = '{Chy}'")
            if Cno :
                conditions.append(f"Cno  = '{Cno }'")
            if Cname:
                conditions.append(f"Maddress = '{Cname}'")
            query = "SELECT * FROM Customer WHERE " + " AND ".join(conditions)
            self.cursor.execute(query)
            result.append(self.cursor.fetchall())
            if len(result)!=0:
                QMessageBox.information(self, '查询结果', '查询顾客信息成功!')
            else:
                QMessageBox.information(self, '查询结果', '未找到匹配记录!')
        except Exception as e:
            QMessageBox.warning(self, '错误', f'查询顾客信息失败: {str(e)}')

    def mydelete(self, cursor, conn,Cno='',Cname='',Chy=''):
        Cno  = Cno
        Cname  = Cname
        Chy = Chy
        self.cursor = cursor
        self.conn = conn
        try:
            conditions = []
            if Chy:
                conditions.append(f"Chy = '{Chy}'")
            if Cno:
                conditions.append(f"Cno  = '{Cno}'")
            if Cname:
                conditions.append(f"Maddress = '{Cname}'")
            query = "DELETE FROM Customer WHERE " + " AND ".join(conditions)
            cursor.execute(query)
            conn.commit()
            QMessageBox.information(self, '成功', '顾客信息删除成功')
        except Exception as e:
            QMessageBox.warning(self, '错误', f'顾客信息删除失败: {str(e)}')

    def myupdate(self, cursor, conn,Cno='',Cname='',Chy=''):
        Cno  = Cno
        Cname  = Cname
        Chy = Chy
        self.cursor = cursor
        self.conn = conn
        if Cno == '':
            QMessageBox.warning(self, '警告', '请正确填写顾客号!')
            return
        try:
            # 执行修改操作
            sql = "UPDATE Customer SET Cname = %s, Chy = %s WHERE Cno = %s"
            val = (Cname,Chy,Cno)
            self.cursor.execute(sql, val)
            self.conn.commit()
            QMessageBox.information(self, "成功", "顾客信息已成功修改！")
        except Exception as e:
            QMessageBox.critical(self, "错误", f"顾客信息修改失败：{str(e)}")

    def addSupermarket(self,cursor,conn,Cno='',Cname='',Chy=''):
        Cno  = Cno
        Cname  = Cname
        Chy = Chy
        self.cursor=cursor
        self.conn=conn
        if Cno=='' or Cname=='' or Chy=='':
            QMessageBox.warning(self, '警告', '请填写所有字段!')
            return
        try:
            # 执行插入操作
            sql = "INSERT INTO Customer (Cno, Cname, Chy) VALUES (%s, %s, %s)"
            val = (Cno, Cname, Chy)
            self.cursor.execute(sql, val)
            self.conn.commit()
            QMessageBox.information(self, '成功', '顾客信息添加成功!')
        except Exception as e:
            QMessageBox.warning(self, '错误', f'顾客信息添加失败: {str(e)}')