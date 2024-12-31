from PyQt5.QtWidgets import *
class employee(QWidget):
    def __init__(self):
        super().__init__()
    def select_search(self, result,cursor, conn, Eno='', Ename='', Eage='0', Esalary='', Ezc='', Epyrq='', Mno=''):
        Eno , Ename , Eage , Esalary , Ezc , Epyrq , Mno = Eno , Ename , Eage , Esalary , Ezc , Epyrq , Mno
        self.cursor = cursor
        self.conn = conn
        if Eno=='' and Ename=='' and Eage=='' and Esalary=='' and Ezc=='' and Epyrq=='' and Mno=='':
            QMessageBox.warning(self, '警告', '请填写员工信息!')
            return
        try:
            # 执行查询操作
            conditions = []
            if Eno:
                conditions.append(f"Eno = '{Eno}'")
            if Ename:
                conditions.append(f"Ename = '{Ename}'")
            if Eage:
                conditions.append(f"Eage = '{Eage}'")
            if Esalary:
                conditions.append(f"Esalary = '{Esalary}'")
            if Ezc:
                conditions.append(f"Ezc = '{Ezc}'")
            if Epyrq:
                conditions.append(f"Epyrq = '{Epyrq}'")
            if Mno:
                conditions.append(f"Mno = '{Mno}'")
            query = "SELECT * FROM employee WHERE " + " AND ".join(conditions)
            self.cursor.execute(query)
            result.append(self.cursor.fetchall())
            if len(result)!=0:
                QMessageBox.information(self, '查询结果', '查询员工信息成功!')
            else:
                QMessageBox.information(self, '查询结果', '未找到匹配记录!')
        except Exception as e:
            QMessageBox.warning(self, '错误', f'查询员工信息失败: {str(e)}')

    def delete_employee(self, cursor, conn, Eno='', Ename='', Eage='0', Esalary='', Ezc='', Epyrq='', Mno=''):
        self.cursor = cursor
        self.conn = conn
        try:
            conditions = []
            if Eno:
                conditions.append(f"Eno = '{Eno}'")
            if Ename:
                conditions.append(f"Ename = '{Ename}'")
            if Eage:
                conditions.append(f"Eage = '{Eage}'")
            if Esalary:
                conditions.append(f"Esalary = '{Esalary}'")
            if Ezc:
                conditions.append(f"Ezc = '{Ezc}'")
            if Epyrq:
                conditions.append(f"Epyrq = '{Epyrq}'")
            if Mno:
                conditions.append(f"Mno = '{Mno}'")
            query = "DELETE FROM employee WHERE " + " AND ".join(conditions)
            cursor.execute(query)
            conn.commit()
            QMessageBox.information(self, '成功', '员工信息删除成功')
        except Exception as e:
            QMessageBox.warning(self, '错误', f'删除员工信息失败: {str(e)}')

    def update_employee(self, cursor, conn, Eno='', Ename='', Eage='', Esalary='', Ezc='', Epyrq='', Mno=''):
        self.cursor = cursor
        self.conn = conn
        if Eage == '' : Eage = int('')
        if Eno == '' or Eage=='' or Epyrq=='' or Mno=='':
            QMessageBox.warning(self, '警告', '请正确填写员工编号、年龄、入职时间及店号!')
            return
        try:
            # 执行修改操作
            sql = "UPDATE employee SET Ename = %s, Eage = %s, Esalary = %s, Ezc = %s, Epyrq = %s, Mno = %s WHERE Eno = %s"
            val = (Ename, Eage, Esalary, Ezc, Epyrq, Mno, Eno)
            self.cursor.execute(sql, val)
            self.conn.commit()
            QMessageBox.information(self, "成功", "员工信息已成功修改！")
        except Exception as e:
            QMessageBox.critical(self, "错误", f"修改失败：{str(e)}")

    def addemployee(self,cursor,conn, Eno='', Ename='', Eage='', Esalary='', Ezc='', Epyrq='', Mno=''):
        self.cursor=cursor
        self.conn=conn
        if Eno=='' and Ename=='' and Eage=='' and Esalary=='' and Ezc=='' and Epyrq=='' and Mno=='':
            QMessageBox.warning(self, '警告', '请填写所有字段!')
            return
        try:
            # 执行插入操作
            sql = "INSERT INTO employee (Eno , Ename , Eage , Esalary , Ezc , Epyrq , Mno) VALUES (%s,%s,%s,%s, %s, %s, %s)"
            val = (Eno , Ename , Eage , Esalary , Ezc , Epyrq , Mno)
            self.cursor.execute(sql, val)
            self.conn.commit()
            QMessageBox.information(self, '成功', '员工信息添加成功!')
        except Exception as e:
            QMessageBox.warning(self, '错误', f'员工信息添加失败: {str(e)}')
