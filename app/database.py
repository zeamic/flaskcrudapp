from app import app 

class Database(object):
	def __init__(self, id = None, idnum = None, name =None, email = None, yrlvl = None, course = None):
		id = self.id
		idnum = self.idnum
		name = self.name
		email = self.email
		yrlvl = self.yrlvl
		course = self.course

	@classmethod
	def all(cls):
		cur = mysql.connection.cursor()
		cur.execute("SELECT * FROM students")
		data = cur.fetchall()
		cur.close()
		return data

	def create(self):
		cur = mysql.connection.cursor()
		cur.execute("INSERT INTO students(idnum, name, course, yrlvl, email) VALUES(%s, %s, %s, %s, %s)",(self.idnum, self.name, self.course, self.yrlvl, self.email))
		mysql.connection.commit()

	def update_info(self, id = None):
		cur = mysql.connection.cursor()
		cur.execute("UPDATE students SET idnum = %s, name = %s, course = %s, yrlvl = %s, email = %s WHERE id = %s",(self.idno, self.name, self.course, self.yrlvl, self.email, self.id))
		mysql.connection.commit()

	def delete_info(self, id = None):
		cur = mysql.connection.cursor()
		cur.execute("DELETE FROM students WHERE id = %s",[self.id])
		mysql.connection.commit()