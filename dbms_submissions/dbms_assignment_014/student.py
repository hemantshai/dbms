
'''class DoesNotExist(Exception):
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
    def avg(cls, field, **kwargs):
        if field not in ('name','age','score','student_id'):
            raise InvalidField
        if len(kwargs)>=1:
            k=Student.filter(**kwargs)
            q='select avg({}) from Student where {}'.format(field,k)
        else:
            q='select avg({}) from Student'.format(field)
            
        out=read_data(q)
        return out[0][0]

    @classmethod
    def min(cls, field, **kwargs):
        if field not in ('name','age','score','student_id'):
            raise InvalidField
        if len(kwargs)>=1:
            k=Student.filter(**kwargs)
            q='select min({}) from Student where {}'.format(field,k)
        else:
            q='select min({}) from Student'.format(field)
        out=read_data(q)
        return out[0][0]    
    
    @classmethod
    def max(cls, field, **kwargs):
        if field not in ('name','age','score','student_id'):
            raise InvalidField
        if len(kwargs)>=1:
            k=Student.filter(**kwargs)
            q='select max({}) from Student where {}'.format(field,k)
        else:
            q='select max({}) from Student'.format(field)
        out=read_data(q)
        return out[0][0]    

    @classmethod
    def sum(cls, field, **kwargs):
        if field not in ('name','age','score','student_id'):
            raise InvalidField
        if len(kwargs)>=1:
            k=Student.filter(**kwargs)
            q='select sum({}) from Student where {}'.format(field,k)
        else:
            q='select sum({}) from Student'.format(field)
        out=read_data(q)
        return out[0][0]    
         
    @classmethod
    def count(cls, field=None, **kwargs):
        if field==None:
            q='select count(*) from Student'
        elif field not in ('name','age','score','student_id'):
            raise InvalidField
        elif len(kwargs)>=1:
            k=Student.filter(**kwargs)
            q='select count({}) from Student where {}'.format(field,k)
        else:
            q='select count({}) from Student'.format(field)
            
        out=read_data(q)
        return out[0][0]        
            
    @classmethod
    def filter(cls,**kid):
        cls.operator={'lt':'<','lte':'<=','gt':'>','gte':'>=','neq':'!='}

        l=[]
        for x,y in kid.items():
            cls.a=x
            cls.b=y
            
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
            query= " "+x        
        return query

def read_data(sql_query):
    import sqlite3
    connection = sqlite3.connect("students.sqlite3")
    crsr = connection.cursor() 
    crsr.execute(sql_query) 
    ans= crsr.fetchall() 
    connection.close()
    return ans'''

class InvalidField(Exception):
    pass
class Student:
    def __init__(self,name,age,score):
        self.name=name
        self.student_id=None
        self.age=age
        self.score=score
    @staticmethod
    def filter(**kwargs):
        list=[]
        mem=["student_id","name","age","score"]
        operations={'lt':'<','lte':'<=','gt':'>','gte':'>=','eq':'=','neq':'!='}
        for key,value in kwargs.items():
            l=key.split("__")
            
            if l[0] not in mem:
                raise InvalidField
            if l[0] in mem and len(l)==1:
                if l[0]=='name':
                    query=f"{key}='{value}'"
                else:
                    query=f"{key}={value}"
            elif l[1]=='in':
                query=f"{l[0]} in {tuple(value)}"
            elif l[1]=='contains':
                query=f"{l[0]} Like '%{value}%'"
            else:
                query=f"{l[0]}{operations[l[1]]}{value}"
            list.append(query)
        return " and ".join(list)
    
    @staticmethod
    def aggregate(op,field,**kwargs):
        att=["student_id","name","age","score"]
        if field not in att:
            raise InvalidField
        if len(kwargs)==0:
            q=f"select {op}({field}) from Student"
        else:
            cond=Student.filter(**kwargs)
            q=f"select {op}({field}) from student where {cond}"
        res=read_data(q)
        return res[0][0]
        
    
    @classmethod
    def avg(cls,field,**kwargs):
        x=cls.aggregate("avg",field,**kwargs)
        return x
        
    @classmethod
    def min(cls,field,**kwargs):
        x=cls.aggregate("min",field,**kwargs)
        return x
    
    @classmethod
    def max(cls,field,**kwargs):
        x=cls.aggregate("max",field,**kwargs)
        return x
    
    @classmethod
    def sum(cls,field,**kwargs):
        x=cls.aggregate("sum",field,**kwargs)
        return x
        
    @classmethod
    def count(cls,field=None,**kwargs):
        x=cls.aggregate("count",field,**kwargs)
        return x
    
def read_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("students.sqlite3")
	crsr = connection.cursor() 
	crsr.execute(sql_query) 
	ans= crsr.fetchall()  
	connection.close() 
	return ans

https://ap-southeast-1.console.aws .amazon.com/cloud9/ide/5daabffa44814b6ea3fa7a2bdb34e811