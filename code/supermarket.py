from PyQt5.QtWidgets import *
class supermarket(QWidget):
    def __init__(self):
        super().__init__()
    def myselect(self, result,cursor,conn,supermarket_id='',supermarket_name='',address='',business_hours=''):
        Mno  = supermarket_id
        Mname  = supermarket_name
        Maddress  = address
        Eyysj = business_hours
        self.cursor = cursor
        self.conn = conn
        if supermarket_id == '' and supermarket_name == '' and address == '' and business_hours == '':
            QMessageBox.warning(self, '警告', '请填写查询内容!')
            return
        try:
            # 执行查询操作
            conditions = []
            if Mno:
                conditions.append(f"Mno = '{Mno}'")
            if Mname :
                conditions.append(f"Mname  = '{Mname }'")
            if Maddress:
                conditions.append(f"Maddress = '{Maddress}'")
            if Eyysj:
                conditions.append(f"Esalary = '{Eyysj}'")
            query = "SELECT * FROM Multipleshop WHERE " + " AND ".join(conditions)
            self.cursor.execute(query)
            result.append(self.cursor.fetchall())
            if len(result)!=0:
                QMessageBox.information(self, '查询结果', '查询连锁店信息成功!')
            else:
                QMessageBox.information(self, '查询结果', '未找到匹配记录!')
        except Exception as e:
            QMessageBox.warning(self, '错误', f'查询连锁店信息失败: {str(e)}')

    def mydelete(self, cursor, conn,supermarket_id='',supermarket_name='',address='',business_hours=''):
        Mno = supermarket_id
        Mname = supermarket_name
        Maddress = address
        Eyysj = business_hours
        self.cursor = cursor
        self.conn = conn
        try:
            conditions = []
            if Mno:
                conditions.append(f"Mno = '{Mno}'")
            if Mname:
                conditions.append(f"Mname  = '{Mname}'")
            if Maddress:
                conditions.append(f"Maddress = '{Maddress}'")
            if Eyysj:
                conditions.append(f"Eyysj = '{Eyysj}'")
            query = "DELETE FROM Multipleshop WHERE " + " AND ".join(conditions)
            cursor.execute(query)
            conn.commit()
            QMessageBox.information(self, '成功', '连锁店信息删除成功')
        except Exception as e:
            QMessageBox.warning(self, '错误', f'连锁店信息删除失败: {str(e)}')

    def myupdate(self, cursor, conn,supermarket_id='',supermarket_name='',address='',business_hours=''):
        Mno = supermarket_id
        Mname = supermarket_name
        Maddress = address
        Eyysj = business_hours
        self.cursor = cursor
        self.conn = conn
        if Mno == '':
            QMessageBox.warning(self, '警告', '请正确填写店号!')
            return
        try:
            # 执行修改操作
            sql = "UPDATE multipleshop SET Mname = %s, Maddress = %s, Eyysj = %s WHERE Mno = %s"
            val = (Mname,Maddress,Eyysj,Mno)
            self.cursor.execute(sql, val)
            self.conn.commit()
            QMessageBox.information(self, "成功", "连锁店信息已成功修改！")
        except Exception as e:
            QMessageBox.critical(self, "错误", f"连锁店信息修改失败：{str(e)}")

    def addSupermarket(self,cursor,conn,supermarket_id='',supermarket_name='',address='',business_hours=''):
        supermarket_id = supermarket_id
        supermarket_name = supermarket_name
        address = address
        business_hours = business_hours
        self.cursor=cursor
        self.conn=conn
        if supermarket_id=='' or supermarket_name=='' or address=='' or business_hours=='':
            QMessageBox.warning(self, '警告', '请填写所有字段!')
            return
        try:
            # 执行插入操作
            sql = "INSERT INTO Multipleshop (Mno, Mname, Maddress, Eyysj) VALUES (%s, %s, %s, %s)"
            val = (supermarket_id, supermarket_name, address, business_hours)
            self.cursor.execute(sql, val)
            self.conn.commit()
            QMessageBox.information(self, '成功', '超市信息添加成功!')
        except Exception as e:
            QMessageBox.warning(self, '错误', f'超市信息添加失败: {str(e)}')