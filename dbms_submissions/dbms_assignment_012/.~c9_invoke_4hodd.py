class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.student_id = None
        self.age = age
        self.score = score
        
        
    def write_data(self,sql_query):
	    import sqlite3
	    connection = sqlite3.connect("db.sqlite3")
	    crsr = connection.cursor() 
	    crsr.execute("PRAGMA foreign_keys=on;") 
	    crsr.execute(sql_query) 
	    connection.commit() 
	    connection.close()

    def read_data(self,sql_query):
	    import sqlite3
	    connection = sqlite3.connect("db.sqlite3")
	    crsr = connection.cursor() 
	    crsr.execute(sql_query) 
	    ans= crsr.fetchall()  
	    connection.close() 
	    return ans
    
    
student_object = Student.get(student_id=1)
student_object.student_id   