import sqlite3 
class Database():
    def __init__(self, DB):
        self.con = sqlite3.connect(DB)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS bom(
            id Integer Primary Key,
            Product_Name text,
            Quantity text,
            Serial_No text,
            Procurement_Spec text,
            Part_phase text,
            Level text,
            Comments text
        )
        """
        self.cur.execute(sql)
        self.con.commit()
    # Insert Function
    def insert(self, Product_Name, Quantity, Serial_No, Procurement_Spec, Part_phase, Level, Comments):
        self.cur.execute("insert into bom values (NULL,?,?,?,?,?,?,?)",
                     (Product_Name, Quantity, Serial_No, Procurement_Spec, Part_phase, Level, Comments))
        self.con.commit()

    # Fetch All Data from DB
    def fetch(self):
        self.cur.execute("SELECT * from bom")
        rows = self.cur.fetchall()
    # print(rows)
        return rows

    # Delete a Record in DB
    def remove(self, id):
        self.cur.execute("delete from bom where id=?", (id,))
        self.con.commit()

    # Update a Record in DB

    def update(self, id, Product_Name, Quantity, Serial_No, Procurement_Spec, Part_phase, Level, Comments):
        self.cur.execute( "update bom set Product_Name=?, Quantity=?, Serial_No=?, Procurement_Spec=?,  Part_phase=?,"
                          " Level=?, Comments=? where id=?",
         (Product_Name, Quantity, Serial_No, Procurement_Spec, Part_phase, Level, Comments, id))
        self.con.commit()