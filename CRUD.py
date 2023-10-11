import mysql.connector
from tkinter import messagebox

db = mysql.connector.connect(
  host="localhost",
  user="skijer",
  password="admin",
  database="tallerdb"
)

mycursor = db.cursor()


##USER CRUD## 
def InsertUser (username, password, tier, name, lastname, phone, address):
    try:
      tier=int(tier)
      sql = "INSERT INTO users (username, password, tier, name, lastname, phone, address) VALUES (%s, %s, %s, %s, %s, %s, %s)"
      val = (username, password, tier, name, lastname, phone, address,)
      mycursor.execute(sql, val)
      db.commit()
      print("Ingresado correctamente")
    except:
        print("ERROR VUELVA A INTENTAR")

def SelectUser(id):
    try:
      id=int(id)
      sql = "SELECT * FROM users WHERE id = %s"
      val = (id,)
      mycursor.execute(sql, val)
      result = mycursor.fetchone()
      return result
    except:
        print("ERROR VUELVA A INTENTAR")

def LoginUser(username, password):
    try:
      sql = "SELECT * FROM users WHERE username = %s"
      val = (username,)
      mycursor.execute(sql, val)
      result = mycursor.fetchone()
      if str(result[2]) == str(password):
         return result[3]
      else:
        return 8
    except:
        print("ERROR VUELVA A INTENTAR")

def PseudoDropUser(id):
    try:
      id=int(id)
      if not id==1:
        sql = "UPDATE users  SET tier = 8 WHERE id = %s"
        val = (id,)
        mycursor.execute(sql, val)
        db.commit()
      else:
          messagebox.showerror("ATENCIÓN","No puedes dar de baja al admin")
    except:
        print("ERROR VUELVA A INTENTAR")

def ListUsers(tier):
    try:
      tier=int(tier)
      sql = "SELECT name FROM users WHERE tier >= %s"
      val = (tier,)
      mycursor.execute(sql,val)
      search=mycursor.fetchall()
      result=[]
      for res in search:
         result.append(str(res[0]))
      print(result)
      return result
    except:
        print("ERROR VUELVA A INTENTAR")

def UpdateUser(id, username, password, tier, name, lastname, phone, address):
    try:
      id=int(id)
      tier=int(tier)
      if id==1 and tier>0:
         messagebox.showerror("ATENCIÓN","NO PUEDES MODIFICAR EL PERFIL DEL ADMIN")
         return
      sql = "UPDATE users SET username=%s, password=%s, tier=%s, name=%s, lastname=%s, phone=%s, address=%s WHERE id = %s"
      val = (username, password, tier, name, lastname, phone, address, id,)
      mycursor.execute(sql, val)
      db.commit()
      print("ACTUALIZADO correctamente")
    except:
        print("ERROR VUELVA A INTENTAR")



#CLIENTS CRUD#
def InsertClient (name, lastname, user):
    try:
      user=int(user)
      sql = "INSERT INTO clients (name, lastname, creatorId, status) VALUES (%s, %s, %s, TRUE)"
      val = (name, lastname, user,)
      mycursor.execute(sql, val)
      db.commit()
      print("Ingresado correctamente")
    except:
        print("ERROR VUELVA A INTENTAR")

def SelectClient(id):
    try:
      id=int(id)
      sql = "SELECT * FROM clients WHERE id = %s"
      val = (id,)
      mycursor.execute(sql, val)
      result = mycursor.fetchone()
      return result
    except:
        print("ERROR VUELVA A INTENTAR")

def PseudoDropClient(id):
    try:
      id=int(id)
      sql = "UPDATE clients SET status = FALSE WHERE id = %s"
      val = (id,)
      mycursor.execute(sql, val)
      db.commit()
      print("Baja")
    except:
      print("ERROR VUELVA A INTENTAR")

def ListClient():
    try:
      sql = "SELECT name FROM clients WHERE status = TRUE"
      mycursor.execute(sql)
      search=mycursor.fetchall()
      result=[]
      for res in search:
         result.append(str(res[0]))
      print(result)
      return result
    except:
      print("ERROR VUELVA A INTENTAR")

def UpdateClient(id, name, lastname, user):
    try:
      id=int(id)
      sql = "UPDATE clients SET name=%s, lastname=%s, creatorID=%s WHERE id = %s"
      val = (name, lastname, user, id,)
      mycursor.execute(sql, val)
      db.commit()
      print("ACTUALIZADO correctamente")
    except:
        print("ERROR VUELVA A INTENTAR")




#VEHICLES CRUD#

def InsertVehicle(plate, brand, model, RecordDate, client):
    try:
      client=int(client)
      sql = "INSERT INTO vehicles (plate, brand, model, RecordDate, ownerId,  status) VALUES (%s, %s, %s, %s, %s, TRUE)"
      val = (plate, brand, model, RecordDate, client,)
      mycursor.execute(sql, val)
      db.commit()
      print("Ingresado correctamente")
    except:
        print("ERROR VUELVA A INTENTAR")

def SelectVehicle(id):
    try:
      id=int(id)
      sql = "SELECT * FROM vehicles WHERE id = %s"
      val = (id,)
      mycursor.execute(sql, val)
      result = mycursor.fetchone()
      print(result)
      return result
    except:
        print("ERROR VUELVA A INTENTAR")

def PseudoDropVehicle(id):
    try:
      id=int(id)
      sql = "UPDATE vehicles SET status = FALSE WHERE id = %s"
      val = (id,)
      mycursor.execute(sql, val)
      db.commit()
    except:
      print("ERROR VUELVA A INTENTAR")

def ListVehicles():
    try:
      sql = "SELECT plate FROM vehicles WHERE status = TRUE"
      mycursor.execute(sql)
      search=mycursor.fetchall()
      result=[]
      for res in search:
         result.append(str(res[0]))
      print(result)
      return result
    except:
      print("ERROR VUELVA A INTENTAR")

def UpdateVehicle(id, plate, brand, model, RecordDate, client):
    try:
      id=int(id)
      sql = "UPDATE vehicles SET plate=%s, brand=%s, model=%s, RecordDate=%s, ownerId=%s WHERE id = %s"
      val = (plate, brand, model, RecordDate, client, id,)
      mycursor.execute(sql, val)
      db.commit()
      print("ACTUALIZADO correctamente")
    except:
        print("ERROR VUELVA A INTENTAR")









#SERVICES CRUD#

def InsertService(name, total, enterDate, deportDate, vehicleId, pieces):
    try:
      vehicleId=int(vehicleId+1)
      total=int(total)
      pieces=int(pieces+1)
      sql = "INSERT INTO services (name, total, enterDate, deportDate, vehicleId, pieces) VALUES (%s, %s, %s, %s, %s, %s)"
      val = (name, total, enterDate, deportDate, vehicleId, pieces,)
      mycursor.execute(sql, val)
      PieceQuantity(pieces,-total)
      db.commit()
      print("Ingresado correctamente")
    except:
        print("ERROR VUELVA A INTENTAR")

def SelectService(id):
    try:
      id=int(id)
      sql = "SELECT * FROM services WHERE id = %s"
      val = (id,)
      mycursor.execute(sql, val)
      result = mycursor.fetchone()
      print(result)
      return result
    except:
        print("ERROR VUELVA A INTENTAR")

def DropService(id,quantity):
    try:
      id=int(id)
      service = SelectService(id)
      pieces = service[-1]
      sql = "DELETE FROM services WHERE id = %s"
      val = (id,)
      mycursor.execute(sql, val)
      PieceQuantity(pieces,-quantity)
      db.commit()
      print("Baja")
    except:
      print("ERROR VUELVA A INTENTAR")

def ListService(vehicle):
    try:
      sql = "SELECT name FROM services WHERE vehicleId = %s"
      val = (vehicle,)
      mycursor.execute(sql, val)
      search=mycursor.fetchall()
      result=[]
      for res in search:
         result.append(str(res[0]))
      print(result)
      print(result)
      return result
    except:
      print("ERROR VUELVA A INTENTAR")

def UpdateService(id, name, total, enterDate, deportDate, vehicleId, pieces):
#    try:
      id=int(id)
      total=int(total)
      vehicleId=int(vehicleId+1)
      pieces=int(pieces+1)
      service = SelectService(id)
      lastpieces = int(service[2])
      if pieces == lastpieces:
        sql = "UPDATE services SET name=%s, total=%s, enterDate=%s, deportDate=%s, vehicleId=%s, pieces=%s WHERE id = %s"
        val = (name, total, enterDate, deportDate, vehicleId, pieces, id)
        mycursor.execute(sql, val)
        db.commit()
      else:
        lastpieces=lastpieces-total
        sql = "UPDATE services SET name=%s, total=%s, enterDate=%s, deportDate=%s, vehicleId=%s, pieces=%s WHERE id = %s"
        val = (name, total, enterDate, deportDate, vehicleId, pieces, id)
        mycursor.execute(sql, val)
        db.commit()
        PieceQuantity(pieces,lastpieces)
      print("ACTUALIZADO correctamente")
#    except:
      print("ERROR VUELVA A INTENTAR")










#PIECES CRUD#

def InsertPiece(name, quantity):
    try:
      quantity=int(quantity)
      sql = "INSERT INTO stock (name, quantity) VALUES (%s, %s)"
      val = (name, quantity,)
      mycursor.execute(sql, val)
      db.commit()
    except:
        print("ERROR VUELVA A INTENTAR")

def SelectPiece(id):
    try:
      id=int(id)
      sql = "SELECT * FROM stock WHERE id = %s"
      val = (id,)
      mycursor.execute(sql, val)
      result = mycursor.fetchone()
      return result
    except:
        print("ERROR VUELVA A INTENTAR")

def PseudoDropPiece(id):
    try:
      id=int(id)
      sql = "UPDATE stock SET quantity = -1 WHERE id = %s"
      val = (id,)
      mycursor.execute(sql, val)
      db.commit()
    except:
      print("ERROR VUELVA A INTENTAR")

def ListPieces():
    try:
      sql = "SELECT name FROM stock WHERE quantity > 0"
      mycursor.execute(sql)
      search=mycursor.fetchall()
      result=[]
      for res in search:
         result.append(str(res[0]))
      return result
    except:
      print("ERROR VUELVA A INTENTAR")

def UpdatePieces(name, quantity, id):
#    try:
      id=int(id)
      quantity=int(quantity)
      sql = "UPDATE stock SET name=%s, quantity=%s WHERE id = %s"
      val = (name, quantity, id,)
      mycursor.execute(sql, val)
      db.commit()
#    except:
      print("ERROR VUELVA A INTENTAR")

def PieceQuantity(piece, number):
#    try:
      sql = "SELECT * FROM stock WHERE name = %s"
      val = (piece,)
      mycursor.execute(sql, val)
      result = mycursor.fetchone()
      print(result)
      print(number)
      if result[3] > 0:
        UpdatePieces(result[0], result[1], result[2]+number, result[3], result[4], result[5])
        db.commit()
      else:
          messagebox.showwarning("ALERTA","NO HAR PIEZAS DISPONIBLES")
#    except:
      messagebox.showwarning("ALERTA","PIEZAS DEVUELTAS")
    

