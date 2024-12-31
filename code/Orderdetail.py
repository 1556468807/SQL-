from PyQt5.QtWidgets import *
class Orderdetail(QWidget):
    def __init__(self):
        super().__init__()
    def select_search(self, result,cursor, conn, Ono='', Osum='', Odate=''):
        Ono , Odate , Osum  = Ono , Odate , Osum
        self.cursor = cursor
        self.conn = conn
        if Ono=='':
            QMessageBox.warning(self, '警告', '请填写采购订单信息!')
            return
        try:
            # 执行查询操作
            conditions = []
            if Ono:
                conditions.append(f"Ono = '{Ono}'")
            if Odate:
                conditions.append(f"Odate = '{Odate}'")
            if Osum:
                conditions.append(f"Eage = '{Osum}'")
            query = "SELECT * FROM Orderdetail WHERE " + " AND ".join(conditions)
            self.cursor.execute(query)
            result.append(self.cursor.fetchall())
            if len(result)!=0:
                QMessageBox.information(self, '查询结果', '查询采购订单信息成功!')
            else:
                QMessageBox.information(self, '查询结果', '未找到匹配记录!')
        except Exception as e:
            QMessageBox.warning(self, '错误', f'查询采购订单信息失败: {str(e)}')

    def delete_employee(self, cursor, conn, Ono='', Osum='', Odate=''):
        self.cursor = cursor
        self.conn = conn
        try:
            conditions = []
            if Ono:
                conditions.append(f"Ono = '{Ono}'")
            if Odate:
                conditions.append(f"Odate = '{Odate}'")
            if Osum:
                conditions.append(f"Eage = '{Osum}'")
            query = "DELETE FROM Orderdetail WHERE " + " AND ".join(conditions)
            cursor.execute(query)
            conn.commit()
            QMessageBox.information(self, '成功', '采购订单信息删除成功')
        except Exception as e:
            QMessageBox.warning(self, '错误', f'删除采购订单信息失败: {str(e)}')

    def update_employee(self, cursor, conn,Ono='', Osum='', Odate=''):
        self.cursor = cursor
        self.conn = conn
        if Ono == '' or Odate=='' or Osum=='':
            QMessageBox.warning(self, '警告', '请正确填写采购订单号!')
            return
        try:
            # 执行修改操作
            sql = "UPDATE Orderdetail SET  Odate = %s, Osum = %s WHERE Ono = %s"
            val = (Odate, Osum, Ono)
            self.cursor.execute(sql, val)
            self.conn.commit()
            QMessageBox.information(self, "成功", "采购订单信息已成功修改！")
        except Exception as e:
            QMessageBox.critical(self, "错误", f"修改失败：{str(e)}")

    def addemployee(self,cursor,conn,Ono='', Osum='', Odate=''):
        self.cursor=cursor
        self.conn=conn
        if Ono=='' and Odate=='' and Osum=='' :
            QMessageBox.warning(self, '警告', '请填写所有字段!')
            return
        try:
            # 执行插入操作
            sql = "INSERT INTO Orderdetail (Ono , Odate , Osum ) VALUES (%s, %s, %s)"
            val = (Ono , Odate , Osum)
            self.cursor.execute(sql, val)
            self.conn.commit()
            QMessageBox.information(self, '成功', '采购订单信息添加成功!')
        except Exception as e:
            QMessageBox.warning(self, '错误', f'采购订单信息添加失败: {str(e)}')
