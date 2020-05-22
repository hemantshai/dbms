Q1='''SELECT p.player_id,mc.team_id,p.jersey_no,p.name,p.date_of_birth,p.age
      FROM
      Player p JOIN MatchCaptain mc 
      ON mc.captain=p.player_id
      LEFT JOIN GoalDetails gd ON gd.player_id=mc.captain
      WHERE
      goal_id IS NULL
    '''
    
Q2='''SELECT team_id,COUNT(match_no) 
      FROM MatchTeamDetails GROUP BY team_id''' 
    
Q3='''SELECT team_id,
      COUNT(goal_id)*1.0/(SELECT COUNT(player_id) FROM Player GROUP BY team_id)
      FROM GoalDetails GROUP BY team_id'''
      
Q4='''SELECT captain,COUNT(mc.match_no)
      FROM MatchCaptain mc JOIN Match m 
      ON mc.match_no=m.match_no GROUP BY captain'''

Q5='''SELECT COUNT(DISTINCT captain)
      FROM match m JOIN MatchCaptain mc
      ON mc.match_no=m.match_no 
      AND m.player_of_match=mc.captain'''
      
Q6='''SELECT player_id FROM Player p
      WHERE EXISTS
      (SELECT * FROM MatchCaptain mc WHERE p.player_id=mc.captain)
      AND NOT EXISTS
      (SELECT * FROM Match m WHERE p.player_id=m.player_of_match)'''
      
Q7='''SELECT strftime('%m',play_date) as month,
      COUNT(match_no) C FROM Match GROUP BY month 
      ORDER BY C DESC'''       
      
Q8='''SELECT jersey_no,COUNT(captain) C
      FROM Player p JOIN MatchCaptain mc
      ON mc.captain=p.player_id
      GROUP BY jersey_no
      ORDER BY C DESC,jersey_no DESC'''
      
Q9='''SELECT player_id,AVG(audience) avg_audience
       FROM Match m JOIN MatchTeamDetails mtd 
       ON m.match_no=mtd.match_no
       JOIN Player p
       ON p.team_id=mtd.team_id
       GROUP BY player_id
       ORDER BY avg_audience DESC,player_id DESC'''
       
Q10='''SELECT team_id,AVG(age)
       FROM Player
       GROUP BY team_id'''
       
Q11='''SELECT AVG(age)
       FROM Player p JOIN MatchCaptain mc
       ON p.player_id=mc.captain'''
       
Q12='''SELECT strftime('%m',date_of_birth) month,
       COUNT(player_id) C
       FROM Player
       GROUP BY month
       ORDER BY C DESC,month DESC'''
       
Q13='''SELECT captain,COUNT(win_lose) no_of_wins
       FROM MatchCaptain mc JOIN MatchTeamDetails mtd
       ON mc.team_id=mtd.team_id 
       AND mc.match_no=mtd.match_no
       WHERE mtd.win_lose='W'
       GROUP BY captain
       ORDER BY no_of_wins DESC'''