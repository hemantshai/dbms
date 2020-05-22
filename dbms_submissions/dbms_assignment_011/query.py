Q1='''SELECT a.id,a.fname,a.lname,a.gender 
      FROM Actor a JOIN Cast c
      ON c.pid=a.id
      JOIN Movie m 
      ON m.id=c.mid
      WHERE m.name LIKE "Annie%"'''
            
      
Q2='''SELECT m.id,m.name,m.rank,m.year 
      FROM Director d JOIN MovieDirector md
      ON md.did=d.id
      JOIN Movie m 
      ON m.id=md.mid
      WHERE (d.fname="Biff" AND d.lname="Malibu") 
      AND m.year IN (1999,1994,2003)
      ORDER BY m.rank DESC,m.year ASC'''
      
Q3='''SELECT year,COUNT(id)
      FROM Movie GROUP BY year
      HAVING AVG(rank)>
      (SELECT AVG(rank) FROM Movie)
      ORDER BY year ASC'''
    
Q4='''SELECT * FROM Movie WHERE year=2001
      AND rank <
      (SELECT AVG(rank) FROM Movie 
      WHERE year=2001)
      ORDER BY rank DESC LIMIT 10'''
      
Q6='''SELECT DISTINCT a.id   
      FROM Actor a JOIN Cast c
      ON c.pid=a.id
      JOIN Movie m
      ON m.id=c.mid
      GROUP BY a.id,m.id
      HAVING COUNT(DISTINCT role)>1
      ORDER BY a.id ASC LIMIT 100'''
      
Q7='''SELECT fname,COUNT(id)
      FROM Director
      GROUP BY fname
      HAVING COUNT(fname)>1'''
      
Q8='''SELECT id,fname,lname
      FROM Director d
      WHERE EXISTS
      (SELECT * FROM MovieDirector md
      JOIN Cast c ON c.mid=md.mid
      AND d.id=md.did
      GROUP BY md.did,md.mid
      HAVING COUNT(c.role)>=100)
      
      AND NOT EXISTS
      (SELECT * FROM MovieDirector md
      JOIN Cast c ON c.mid=md.mid
      AND d.id=md.did
      GROUP BY md.did,md.mid
      HAVING COUNT(c.role)<100)'''
      
      
Q5='''      