class DoesNotExist(Exception):
    pass

class MultipleObjectsReturned(Exception):
    pass

class InvalidField(Exception):
    pass

class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.student_id = None
        self.age = age
        self.score = score
        
    @classmethod
    def get(cls,**s):
        for x,y in s.items():
            cls.k=x
            cls.v=y
            
        if x not in ('name','age','score','student_id'):
            raise InvalidField
            
        
        query="select * from Student where {}='{}'".format(cls.k,cls.v)
        
        a=read_data(query)
        
        if len(a)>1:
            raise MultipleObjectsReturned
        if len(a)==0:
            raise DoesNotExist    
        elif len(a)==1:
            c= Student(a[0][1],a[0][2],a[0][3])
            c.student_id=a[0][0]
            return c
        
        
    		
    def delete(self):
    	sql_query='delete from student where student_id={}'.format(self.student_id)
    	write_data(sql_query)
    
    def save(self):
        if self.student_id is None:
            query="insert into student(name,age,score) values ('{}',{},{})".format(self.name,self.age,self.score)
            write_data(query)
            q1='select student_id from student where name="{}" and age={} and score={}'.format(self.name,self.age,self.score)
            a=read_data(q1)   
            self.student_id=a[0][0]
        else:    
            sql_query="update student set name='{}',age={},score={} where student_id={}".format(self.name,self.age,self.score,self.v)
            write_data(sql_query) 


def write_data(sql_query):
    import sqlite3
    connection = sqlite3.connect("students.sqlite3")
    crsr = connection.cursor() 
    crsr.execute("PRAGMA foreign_keys=on;") 
    crsr.execute(sql_query) 
    connection.commit() 
    connection.close()


def read_data(sql_query):
    import sqlite3
    connection = sqlite3.connect("students.sqlite3")
    crsr = connection.cursor() 
    crsr.execute(sql_query) 
    ans= crsr.fetchall()  
    connection.close()
    return ans
	

