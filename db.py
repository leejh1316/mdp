import pymysql
from pymysql import NULL, cursors

class snacksql():
    def __init__(self, ip, db):
        self.ip = ip
        self.db = db
    # db연결 함수
    def dbConnect(self):
        global cursor, db,cursor_sel
        db = pymysql.connect(host=self.ip, user='root',password='1234',db=self.db, charset='utf8')
        cursor = db.cursor()   
        cursor_sel = db.cursor(cursors.DictCursor)
    #과자를 db에 넣는 함수 각 컬럼들은 NULL값을 받지 않음
    def SnackInsert(self,snackTitle, stock, pay):
        sql_insert = "INSERT INTO snackdata(title, stock, pay) VALUES(%s,%s,%s)"
        cursor.execute(sql_insert,(snackTitle, stock, pay))
        db.commit()
    
    #과자세팅 stock, pay를 gui에따라 변경 또는 유지
    def SnackUpdate(self, snackTitle, stock):
        sql_update="UPDATE snackdata SET stock=%s WHERE title = %s"
        cursor.execute(sql_update,(str(stock),snackTitle))
        db.commit()

    #과자 개수
    def SnackStockCnt(self,title):
        cursor_sel.execute(f"select stock from snackdata where title='{title}'")
        rows = cursor_sel.fetchall()
        for row in rows:
            continue
        Snackstock = row['stock']
        return Snackstock


    #과자가 팔리면 stock 업데이트
    def SnackSell(self, snackTitle, stock):
        sql_update="UPDATE snackdata SET stock=%s WHERE title = %s"
        cursor.execute(sql_update,(str(stock), snackTitle))
        db.commit()

    def SnackSellUpdate(self,title, sell_stock, price):
        sql_sum = "select sell_stock, total_price from selldata"
        cursor_sel.execute(sql_sum)
        rows = cursor_sel.fetchall()
        for row in rows:
            continue
        Stock = row['sell_stock'] + sell_stock
        Price = row['total_price'] + price
        sql_update=f"UPDATE selldata SET sell_stock={int(Stock)}, total_price={int(Price)} where title='{str(title)}'"
        cursor.execute(sql_update)
        db.commit()

    
    #데이터 삭제 함수, snackTitle에 맞는 데이터 삭제됨
    def SnackDelete(slef, snackTitle):
        sql_delete="DELETE FROM snackdata WHERE title=%s"
        cursor.execute(sql_delete,(snackTitle))
        db.commit()
    
    #snacksell 테이블의 데이터를  읽어옴
    def SnackSellSerch(self):
        sql = "SELECT id,title,sell_stock,total_price FROM selldata"
        cursor_sel.execute(sql)
        rows = cursor_sel.fetchall()
        # for row in rows:
        #     print(row['sold'], row['title'], row['total'], row['time'])
        return rows

    def SnackSerch(self):
        sql = "SELECT * FROM snackdata"
        cursor_sel.execute(sql)
        rows = cursor_sel.fetchall()
        # for row in rows:
        #     print(row['id'], row['title'], row['stock'], row['pay'])
        return rows


    #id Auto_INCREMENT 재조정
    def SnackIdAdjustment(self, table, keyColumn):
        sql_alter = f"ALTER TABLE {table} AUTO_INCREMENT=1"
        cursor.execute(sql_alter)
        cursor.execute("SET @COUNT=0")
        sql_update = f"UPDATE {table} SET {keyColumn} = @COUNT:=@COUNT+1"
        cursor_sel.execute(sql_update)
        db.commit()

    def login(self):
        cursor_sel.execute("SELECT password FROM password")
        rows = cursor_sel.fetchall()
        for row in rows:
            print(end='')
            # print(row['password'])
            # print(type(row['password']))
        return row

    def close(self):
        db.close()

# c= snacksql('192.168.0.13','snack')
# c.dbConnect()
# print(c.SnackStockCnt('chip'))
# c.close()

# a= snacksql('localhost','snack_mdp')
# a.dbConnect()
# b = a.SnackStockCnt('ddd')
#
# print(b[0]['snack_stock'])
# a.close()


# b = snacksql("192.168.0.20", "snack_test")
# b.dbConnect()
# b.SnackInsert("dd",5,5)
# b.SnackIdAdjustment("snackdata","id")
#
# b.SnackSerch()
# b.close()

# sql = "SELECT * FROM snack_backup"
# cursor.execute(sql)
# rows=cursor.fetchall()
# for row in rows:
#     print(row)
#     print(row['pay'],row['id'],row['title'])