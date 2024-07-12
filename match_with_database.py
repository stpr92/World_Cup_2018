def match(a,b) :
    result=input()                              #a and b are team names. you should write them(for getting output from function) exactly as they are in your database
    result=result.split('-')               # be aware that you should use your mysql user,password and host! just leave the database name unchanged because I already uploaded the SQL file.
    import mysql.connector
    cnx=mysql.connector.connect(user='root',password='',host='127.0.0.1',database='world_cup')
    cursor=cnx.cursor()
    query1=('UPDATE b_group SET scored_goal=scored_goal+\'%i\' where country=\'%s\'')
    cursor.execute(query1 % (int(result[0]),a))
    query1=('UPDATE b_group SET scored_goal=scored_goal+\'%i\' where country=\'%s\'')
    cursor.execute(query1 % (int(result[1]),b))
    query2=('UPDATE b_group SET received_goal=received_goal+\'%i\' where country=\'%s\'')
    cursor.execute(query2 % (int(result[1]),a))
    query2=('UPDATE b_group SET received_goal=received_goal+\'%i\' where country=\'%s\'')
    cursor.execute(query2 % (int(result[0]),b))
    cnx.commit()
    if int(result[0])>int(result[1]) :
        query=('UPDATE b_group SET wins=wins+1 where country=\'%s\'')
        cursor.execute(query % (a,))
        query=('UPDATE b_group SET loses=loses+1 where country=\'%s\'')
        cursor.execute(query % (b,))
        cnx.commit()
    elif int(result[0])==int(result[1]) :  
        query=('UPDATE b_group SET draws=draws+1 where country=\'%s\'')
        cursor.execute(query % (a,))
        query=('UPDATE b_group SET draws=draws+1 where country=\'%s\'')
        cursor.execute(query % (b,))
        cnx.commit()
    elif int(result[0])<int(result[1]) :
        query=('UPDATE b_group SET wins=wins+1 where country=\'%s\'')
        cursor.execute(query % (b,))
        query=('UPDATE b_group SET loses=loses+1 where country=\'%s\'')
        cursor.execute(query % (a,))
        cnx.commit()

     # For convenience, I also wrote a cleaning function that resets all field values in the table to zero after 6 or any number of games you have called and outputted using other functions.


def clean_table() :                            
    import mysql.connector
    cnx=mysql.connector.connect(user='root',password='',host='127.0.0.1',database='world_cup')
    cursor=cnx.cursor()
    cursor.execute('UPDATE b_group SET wins=0;')
    cursor.execute('UPDATE b_group SET loses=0;')
    cursor.execute('UPDATE b_group SET draws=0;')
    cursor.execute('UPDATE b_group SET scored_goal=0;')
    cursor.execute('UPDATE b_group SET received_goal=0;')
    cnx.commit()
    cnx.close()

def output() :                             
    import mysql.connector
    cnx=mysql.connector.connect(user='root',password='',host='127.0.0.1',database='world_cup')
    cursor=cnx.cursor()
    query=('SELECT country,wins,loses,draws,(scored_goal-received_goal) as \'goal_difference\',(wins*3+draws) as \'points\' FROM b_group ORDER BY points DESC,goal_difference DESC,country')
    cursor.execute(query)
    for (country,wins,loses,draws,goal_difference,points) in cursor:
        print(country,'wins:',wins,',','loses:',',',loses,',','drwas:',draws,',','goal_difference:',goal_difference,',','points:',points)
   

# You can use this code with sql file not only for group B of world cup but also for the other groups in every competition. ENJOY:)

      







