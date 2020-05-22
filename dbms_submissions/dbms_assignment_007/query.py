Q1='''SELECT COUNT(id)
      FROM Movie
      WHERE year<2000'''
      
Q2='''SELECT AVG(rank)
      FROM Movie
      WHERE year=1991'''
      
Q3='''SELECT min(rank)
      FROM Movie
      WHERE year=1991'''
      
Q4='''SELECT fname,lname
      FROM Actor INNER JOIN Cast
      ON id=pid
      WHERE mid=27'''
      
Q5='''SELECT COUNT(mid)
      FROM Actor INNER JOIN Cast
      On id=pid
      WHERE fname='Jon' AND lname='Dough';'''
      
Q6='''SELECT name 
      FROM Movie
      WHERE name LIKE 'Young Latin Girls%' AND year BETWEEN 2003 AND 2006'''
      
Q7='''SELECT DISTINCT fname,lname
      FROM ((Director INNER JOIN MovieDirector ON `Director`.id=did) INNER JOIN Movie ON `Movie`.id=mid)
      WHERE `Movie`.name LIKE "Star Trek%"'''


Q8='''SELECT name
      FROM ((((Movie INNER JOIN Cast ON `Movie`.id=`Cast`.mid) JOIN MovieDirector ON `Movie`.id=`MovieDirector`.mid) JOIN Director ON `Director`.id=`MovieDirector`.did) JOIN Actor ON `Actor`.id=`Cast`.pid) 
      WHERE (`Director`.fname='Jackie (I)' AND `Director`.lname='Chan') AND (`Actor`.fname='Jackie (I)' AND `Actor`.lname='Chan')  ORDER BY name ASC''' 
      
Q9='''SELECT fname,lname
      FROM ((Director INNER JOIN MovieDirector ON `Director`.id=did) INNER JOIN Movie ON `Movie`.id=mid)
      WHERE Year=2001 GROUP BY `Director`.id HAVING COUNT(did)>=4 ORDER BY fname ASC,lname DESC''' 
      
Q10='''SELECT gender,COUNT(gender)
      FROM Actor
      GROUP BY gender'''
      
Q11='''SELECT DISTINCT m1.name,m2.name,m1.rank,m1.year
       FROM Movie m1 JOIN Movie m2 ON (m1.name != m2.name AND m1.year=m2.year AND m1.rank=m2.rank)
       ORDER BY m1.name LIMIT 100'''
       
Q12=''' SELECT fname,year,AVG(rank)
        FROM (Actor INNER JOIN Cast ON `Actor`.id=`Cast`.pid) INNER JOIN Movie ON `Movie`.id=mid
        GROUP BY `Actor`.id,year
        ORDER BY fname ASC,year DESC LIMIT 100'''
        
Q13='''SELECT a.fname,d.fname,AVG(rank) AS score
       FROM (((Movie m JOIN MovieDirector md ON m.id=md.mid) JOIN Director d ON d.id=md.did)
       JOIN Cast c ON c.mid=md.mid) JOIN Actor a ON a.id=c.pid
       GROUP BY a.id,d.id HAVING COUNT(c.pid)>=5
       ORDER BY score DESC,d.fname ASC,a.fname DESC LIMIT 100'''