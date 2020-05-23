
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
        
    def __repr__(self):
        return "Student(student_id={0}, name={1}, age={2}, score={3})".format(
            self.student_id,
            self.name,
            self.age,
            self.score)    
        
    @classmethod
    def get(cls,**s):
        for x,y in s.items():
            cls.k=x
            cls.v=y
            
        if x not in ('name','age','score','student_id'):
            raise InvalidField
            
        
        query="select * from Student where {}='{}'".format(cls.k,cls.v)
        
        a=read_data(query)
        #print(a)
        if len(a)>1:
            raise MultipleObjectsReturned
        elif len(a)==0:
            raise DoesNotExist    
        elif len(a)==1:
            c= Student(a[0][1],a[0][2],a[0][3])
            c.student_id=a[0][0]
            return c
            
    @classmethod    
    def filter(cls,**kwargs):
        out=[]
        for key,value in kwargs.items():

            if(key=='age' or key =='score' or key=='student_id' or key=='name'):
                q='SELECT * FROM Student WHERE {}=\'{}\''.format(key,value)
                
            elif(key=='age__lt' or key=='score__lt' or key=='student_id__lt'):
                k=key.split("__")
                q='SELECT * FROM Student WHERE {} < {}'.format(k[0],value)
                
            elif(key=='age__lte' or key=='score__lte' or key=='student_id__lte'):
                k=key.split("__")
                q='SELECT * FROM Student WHERE {} <= {}'.format(k[0],value)
                
            elif(key=='age__gt' or key=='score__gt' or key=='student_id__gt'):
                k=key.split("__")
                q='SELECT * FROM Student WHERE {} > {}'.format(k[0],value)
                
            elif(key=='age__gte' or key=='score__gte' or key=='student_id__gte'):
                k=key.split("__")
                q='SELECT * FROM Student WHERE {} >= {}'.format(k[0],value)
                
            elif(key=='age__neq' or key=='score__neq' or key=='student_id__neq' or key=='name__neq'):
                k=key.split("__")
                q='SELECT * FROM Student WHERE {} <> \'{}\''.format(k[0],value)
                
            elif(key=='age__in' or key=='score__in' or key=='student_id__in' or key=='name__in'):
                value=tuple(value)
                k=key.split("__")
                q='SELECT * FROM Student WHERE {} in {}'.format(k[0],value)
            
            elif(key=='name__contains'):
                q='SELECT * FROM Student WHERE name like \'%{}\''.format(value)

            else:
                raise InvalidField
            
            results=read_data(q)
            #print (out)
            #print(results)
            for i in results:
                student_obj=Student(i[1],i[2],i[3])
                student_obj.student_id=i[0]
                out.append(student_obj)
        return out
        
            
    		
    def delete(self):
    	sql_query='delete from Student where student_id={}'.format(self.student_id)
    	write_data(sql_query)

    def save(self):
        if self.student_id is None:
            query="insert into Student(name,age,score) values ('{}',{},{})".format(self.name,self.age,self.score)
            write_data(query)
            q1='select student_id from Student where name="{}" and age={} and score={}'.format(self.name,self.age,self.score)
            a=read_data(q1)
            self.student_id=a[0][0]
        else:
            sql_query="update Student set student_id={},name='{}',age={},score={} where student_id={}".format(self.student_id,self.name,self.age,self.score,self.v)
            write_data(sql_query) 



def write_data(sql_query):
    import sqlite3
    connection = sqlite3.connect("selected_students.sqlite3")
    crsr = connection.cursor() 
    crsr.execute("PRAGMA foreign_keys=on;") 
    crsr.execute(sql_query) 
    connection.commit() 
    connection.close()


def read_data(sql_query):
    import sqlite3
    connection = sqlite3.connect("selected_students.sqlite3")
    crsr = connection.cursor() 
    crsr.execute(sql_query) 
    ans= crsr.fetchall()  
    connection.close()
    return ans
	
