Q1='''SELECT * FROM MOVIE
      ORDER BY rank DESC LIMIT 10;'''

Q2='''SELECT * FROM MOVIE
      ORDER BY rank DESC LIMIT 10 OFFSET 10;'''

Q3='''SELECT name FROM MOVIE
      WHERE year>2004;'''
      
Q4='''SELECT name FROM MOVIE
      WHERE rank<1.1;'''
      
Q5='''SELECT * FROM MOVIE
      WHERE year IN(2004,2005,2006);'''
      
Q6='''SELECT name,year FROM MOVIE
      WHERE name LIKE "Harry%";'''
      
Q7='''SELECT * FROM ACTOR
      WHERE fname="Christin" AND lname != "Watson";''' 
      
Q8='''SELECT * FROM ACTOR
      WHERE fname="Woody" AND lname="Watson";'''

Q9='''SELECT name FROM MOVIE
      WHERE year=1990 AND rank=5;'''
      
Q10='''SELECT * FROM ACTOR
       WHERE fname="Christin" AND lname="Watson";'''
       
Q11='''SELECT name FROM MOVIE
       WHERE year BETWEEN 2003 AND 2005;'''
       
Q12='''SELECT DISTINCT year FROM MOVIE 
       ORDER BY year ASC;'''
       
Q13='''SELECT * FROM ACTOR
       WHERE (fname="Christin" OR lname="Watson") 
       AND (gender="M") 
       ORDER BY fname ASC LIMIT 10;'''
       
