Q1='''SELECT d.id,d.fname FROM Director d
      WHERE
      NOT EXISTS(SELECT * FROM Movie m JOIN MovieDirector md ON m.id=md.mid 
      AND md.did=d.id WHERE m.year<2000)
      AND EXISTS(SELECT * FROM Movie m JOIN MovieDirector md ON m.id=md.mid 
      AND md.did=d.id WHERE m.year>2000)
      ORDER BY id'''
      
Q2='''SELECT d.fname,(SELECT m.name FROM Movie m JOIN MovieDirector md 
      ON m.id=md.mid 
      AND md.did=d.id ORDER BY m.rank DESC,m.name ASC LIMIT 1)   
      FROM Director d LIMIT 100'''
      
Q3=''' SELECT * FROM Actor a
       WHERE 
       NOT EXISTS
       (SELECT * FROM Movie m JOIN Cast c ON m.id=c.mid AND c.pid=a.id
       WHERE year BETWEEN 1990 AND 2000)
       ORDER BY a.id DESC LIMIT 100'''