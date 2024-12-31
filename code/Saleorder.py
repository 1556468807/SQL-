from PyQt5.QtWidgets import *
class Saleorder(QWidget):
    def __init__(self):
        super().__init__()
    def select_search(self, result,cursor, conn, Sno='', Sdiscount='', Esum='', Edate='', Pno=''):
        Sno , Sdiscount , Esum , Edate , Pno = Sno , Sdiscount , Esum , Edate , Pno
        self.cursor = cursor
        self.conn = conn
        if Sno=='' and Pno=='' :
            QMessageBox.warning(self, '警告', '请填写销售订单信息!')
            return
        try:
            # 执行查询操作
            conditions = []
            if Sno:
                conditions.append(f"Sno = '{Sno}'")
            if Sdiscount:
                conditions.append(f"Sdiscount = '{Sdiscount}'")
            if Esum:
                conditions.append(f"Esum = '{Esum}'")
            if Edate:
                conditions.append(f"Edate = '{Edate}'")
            if Pno:
                conditions.append(f"Pno = '{Pno}'")
            query = "SELECT * FROM Saleorder WHERE " + " AND ".join(conditions)
            self.cursor.execute(query)
            result.append(self.cursor.fetchall())
            if len(result)!=0:
                QMessageBox.information(self, '查询结果', '查询销售订单信息成功!')
            else:
                QMessageBox.information(self, '查询结果', '未找到匹配记录!')
        except Exception as e:
            QMessageBox.warning(self, '错误', f'查询销售订单信息失败: {str(e)}')

    def delete_employee(self, cursor, conn,  Sno='', Sdiscount='', Esum='', Edate='', Pno=''):
        self.cursor = cursor
        self.conn = conn
        try:
            conditions = []
            if Sno:
                conditions.append(f"Sno = '{Sno}'")
            if Sdiscount:
                conditions.append(f"Sdiscount = '{Sdiscount}'")
            if Esum:
                conditions.append(f"Esum = '{Esum}'")
            if Edate:
                conditions.append(f"Edate = '{Edate}'")
            if Pno:
                conditions.append(f"Pno = '{Pno}'")
            query = "DELETE FROM Saleorder WHERE " + " AND ".join(conditions)
            cursor.execute(query)
            conn.commit()
            QMessageBox.information(self, '成功', '销售订单信息删除成功')
        except Exception as e:
            QMessageBox.warning(self, '错误', f'删除销售订单信息失败: {str(e)}')

    def update_employee(self, cursor, conn,  Sno='', Sdiscount='', Esum='', Edate='', Pno=''):
        self.cursor = cursor
        self.conn = conn
        if Esum == '' : Esum = int('')
        if Sno == '' or Pno=='':
            QMessageBox.warning(self, '警告', '请正确填写销售订单号、商品号!')
            return
        try:
            # 执行修改操作
            sql = "UPDATE Saleorder SET Sdiscount = %s, Esum = %s, Edate = %s, Pno = %s WHERE Sno = %s"
            val = (Sdiscount , Esum , Edate , Pno , Sno)
            self.cursor.execute(sql, val)
            self.conn.commit()
            QMessageBox.information(self, "成功", "销售订单信息已成功修改！")
        except Exception as e:
            QMessageBox.critical(self, "错误", f"修改失败：{str(e)}")

    def addemployee(self,cursor,conn,  Sno='', Sdiscount='', Esum='', Edate='', Pno=''):
        self.cursor=cursor
        self.conn=conn
        if Sno=='' and Sdiscount=='' and Esum=='' and Edate=='' and Pno=='':
            QMessageBox.warning(self, '警告', '请填写所有字段!')
            return
        try:
            # 执行插入操作
            sql = "INSERT INTO Saleorder (Sno , Sdiscount , Esum , Edate , Pno) VALUES (%s,%s, %s, %s, %s)"
            val = (Sno , Sdiscount , Esum , Edate , Pno)
            self.cursor.execute(sql, val)
            self.conn.commit()
            QMessageBox.information(self, '成功', '销售订单信息添加成功!')
        except Exception as e:
            QMessageBox.warning(self, '错误', f'销售订单信息添加失败: {str(e)}')
