Q1='''SELECT AVG(age)
      FROM Player'''
      
Q2='''SELECT match_no,play_date
      FROM Match 
      WHERE audience>50000
      ORDER BY match_no ASC'''
      
Q3='''SELECT team_id,COUNT(win_lose) AS C 
      FROM MatchTeamDetails WHERE win_lose='W' 
      GROUP BY team_id 
      ORDER BY C DESC,team_id ASC'''
      
Q4='''SELECT match_no,play_date
      FROM Match  
      WHERE stop1_sec>(SELECT AVG(stop1_sec) FROM Match)
      ORDER BY match_no DESC'''
      
Q5='''SELECT c.match_no,t.name,p.name
      FROM MatchCaptain c JOIN Team t ON t.team_id=c.team_id JOIN Player p ON c.captain=p.player_id 
      ORDER BY c.match_no ASC,t.name ASC''' 

Q6='''SELECT m.match_no,p.name,p.jersey_no
      FROM Match m JOIN Player p ON m.player_of_match=p.player_id 
      ORDER BY m.match_no ASC''' 
      
Q7='''SELECT name,
      (SELECT AVG(age) FROM Player p WHERE t.team_id=p.team_id GROUP BY p.team_id) AS avrg
      FROM Team t WHERE avrg>26 ORDER BY t.name;'''
      
Q8='''SELECT p.name,p.jersey_no,p.age,
       (SELECT COUNT(goal_id)
       FROM goaldetails gd
       WHERE gd.player_id=p.player_id) AS goal
       FROM Player p
       WHERE age<=27 AND goal>=1
       ORDER BY goal DESC,name ASC'''
       
Q9='''SELECT team_id,COUNT(goal_id)*100.0/(SELECT COUNT(goal_id)
      FROM goaldetails) 
      FROM goaldetails GROUP BY team_id HAVING COUNT(goal_id)>0'''

Q10= '''SELECT AVG(C) 
        FROM
        (SELECT COUNT(gd.goal_id) AS C
        FROM goaldetails gd
        GROUP BY gd.team_id)'''

Q11='''SELECT player_id,name,date_of_birth
       FROM Player P
       WHERE P.player_id 
       NOT IN (SELECT player_id FROM goaldetails)
       ORDER BY P.player_id'''
       
Q12='''SELECT T.name,M.match_no,M.audience,
      
       M.audience-(SELECT AVG(audience)
       FROM match m JOIN matchteamdetails mtd
       ON m.match_no=mtd.match_no AND T.team_id=mtd.team_id) 
      
       FROM 
       (match M JOIN matchteamdetails MTD ON M.match_no=MTD.match_no)
       JOIN team T ON T.team_id=MTD.team_id
       ORDER BY M.match_no;'''

      