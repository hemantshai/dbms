Q1="CREATE TABLE User(user_id INT PRIMARY KEY NOT NULL, first_name VARCHAR(200) NOT NULL, last_name VARCHAR(200) NOT NULL, address VARCHAR(300) NOT NULL, phone_number INT NOT NULL);"

Q2="CREATE TABLE post(user_id INT, post_id INTEGER PRIMARY KEY AUTOINCREMENT, post_content VARCHAR(500));"

Q3="INSERT INTO User values(1, 'tony', 'stark', 'new york', 1234567890);"

Q4="INSERT INTO User values(2, 'john', 'wick', 'la', 987654321);"

Q5="INSERT INTO post(user_id, post_content) values(1, 'my first post');"

Q6="SELECT * FROM User;"

Q7="SELECT first_name,last_name FROM User;"

Q8="UPDATE User SET first_name='thor',last_name='ragnarok' WHERE user_id=1;"

Q9="INSERT INTO post(user_id, post_content) values(2, 'My Second Post');"

Q10="DELETE FROM User where first_name='john';"

Q11="DROP TABLE post;"