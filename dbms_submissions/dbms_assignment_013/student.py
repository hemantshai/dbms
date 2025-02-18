
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
    def filter(cls,**kid):
        cls.li=[]
        cls.operator={'lt':'<','lte':'<=','gt':'>','gte':'>=','neq':'!='}
        
        
        #if(len(kid))>=1:
        l=[]
        for x,y in kid.items():
            cls.a=x
            cls.b=y
                    
            #field=cls.a
            field=x.split('__')
            if field[0] not in ('name','age','score','student_id'):
                raise InvalidField 
            
            if(len(field))==1:
                query=" {}='{}'".format(cls.a,cls.b)
            elif field[1]=='contains':
                query=" {} like '%{}%'".format(field[0],cls.b)
            elif field[1]=='in':
                query=" {} {} {}".format(field[0],field[1],tuple(cls.b))
            else:    
                query="{} {} '{}'".format(field[0],cls.operator[field[1]],cls.b)
                
            l.append(query)
                    
            x = " and ".join(l)
            #print(l)
            #print(x)
            query= "select * from Student where "+x        
            
            
            
        #print(query)            
        obj=read_data(query)
        for i in range(len(obj)):
            c=Student(obj[i][1],obj[i][2],obj[i][3])
            c.student_id=obj[i][0] 
            cls.li.append(c)
        return cls.li    
            
    # @classmethod    
    # def filter(cls,**kwargs):
    #     out=[]
    #     for key,value in kwargs.items():
    #         k=key.split("__")
            
    #         if (k[0] not in ('age','score','student_id','name')):
    #             raise InvalidField        
            
    #         if len(k)==1: 
    #             if(k[0] in ('age','score','student_id','name')):
    #                 q=read_data('SELECT * FROM Student WHERE {}=\'{}\''.format(key,value))
    #             #results=read_data(q)
            
    #         elif len(k)>1:        
    #             if(k[1]=='lt'):
    #                 q=read_data('SELECT * FROM Student WHERE {} < {}'.format(k[0],value))
                
    #             elif(k[1]=='lte'):
    #                 q=read_data('SELECT * FROM Student WHERE {} <= {}'.format(k[0],value))
                
    #             elif(k[1]=='gt'):
    #                 q=read_data('SELECT * FROM Student WHERE {} > {}'.format(k[0],value))
                
    #             elif(k[1]=='gte'):
    #                 q=read_data('SELECT * FROM Student WHERE {} >= {}'.format(k[0],value))
                
    #             elif(k[1]=='neq'):
    #                 q=read_data('SELECT * FROM Student WHERE {} <> \'{}\''.format(k[0],value))
                
    #             elif(k[1]=='in'):
    #                 value=tuple(value)
    #                 q=read_data('SELECT * FROM Student WHERE {} in {}'.format(k[0],value))
            
    #             elif(k[1]=='contains'):
    #                 q=read_data('SELECT * FROM Student WHERE {} like \'%{}%\''.format(k[0],value))
            
    #             #results=read_data(q)
    #         #print (out)
    #         #print(q,sep='\n')
    #         #print()
            
    #         #if len(q)==0:
    #             #out=[]
    #         #else:
    #             #print()
    #             #print(q)
    #             #print()
    #             #out=[]
    #         for i in q:
    #             student_obj=Student(i[1],i[2],i[3])
    #             student_obj.student_id=i[0]
    #             out.append(student_obj)
    #             print(out)
    #             print()
                
                
    #     #return out
        
            
    		
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
	

# selected_students = Student.filter(age__in=[25,34],score__lt=50)
# print(selected_students)