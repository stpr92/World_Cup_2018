ir_win=0
sp_win=0                       
p_win=0
m_win=0
ir_lose=0
sp_lose=0
p_lose=0
m_lose=0
ir_draw=0
sp_draw=0
p_draw=0
m_draw=0
ir_gf=0
sp_gf=0
p_gf=0
m_gf=0
ir_point=0
sp_point=0
p_point=0
m_point=0
all=list()
for _ in range(1,7) :
    x=input()                   # here we receive input for all matches but in the order of countries and matches as stated in the problem.
    all.append(int(x[0]))
    all.append(int(x[2]))    
if all[0]>all[1] :
    ir_win+=1
    ir_gf+=all[0]-all[1]          # Up to line 127, we calculate all the necessary fields and send each one to its corresponding variable. 
    ir_point+=3
    sp_lose+=1
    sp_gf-=all[0]-all[1]
elif all[0]== all[1] :
    ir_draw+=1
    ir_point+=1
    sp_draw+=1
    sp_point+=1 
else :
    sp_win+=1
    sp_gf+=all[1]-all[0]
    sp_point+=3
    ir_lose+=1
    ir_gf-=all[1]-all[0]
if all[2]>all[3] :
    ir_win+=1
    ir_gf+=all[2]-all[3]
    ir_point+=3
    p_lose+=1
    p_gf-=all[2]-all[3]
elif all[2]== all[3] :
    ir_draw+=1
    ir_point+=1
    p_draw+=1
    p_point+=1 
else :
    p_win+=1
    p_gf+=all[3]-all[2]
    p_point+=3
    ir_lose+=1
    ir_gf-=all[3]-all[2] 
if all[4]>all[5] :
    ir_win+=1
    ir_gf+=all[4]-all[5]
    ir_point+=3
    m_lose+=1
    m_gf-=all[4]-all[5]
elif all[4]== all[5] :
    ir_draw+=1
    ir_point+=1
    m_draw+=1
    m_point+=1 
else :
    m_win+=1
    m_gf+=all[5]-all[4]
    m_point+=3
    ir_lose+=1
    ir_gf-=all[5]-all[4] 
if all[6]>all[7] :
    sp_win+=1
    sp_gf+=all[6]-all[7]
    sp_point+=3
    p_lose+=1
    p_gf-=all[6]-all[7]
elif all[6]== all[7] :
    sp_draw+=1
    sp_point+=1
    p_draw+=1
    p_point+=1 
else :
    p_win+=1
    p_gf+=all[7]-all[6]
    p_point+=3
    sp_lose+=1
    sp_gf-=all[7]-all[6] 
if all[8]>all[9] :
    sp_win+=1
    sp_gf+=all[8]-all[9]
    sp_point+=3
    m_lose+=1
    m_gf-=all[8]-all[9]
elif all[8]== all[9] :
    sp_draw+=1
    sp_point+=1
    m_draw+=1
    m_point+=1 
else :
    m_win+=1
    m_gf+=all[9]-all[8]
    m_point+=3
    sp_lose+=1
    sp_gf-=all[9]-all[8] 
if all[10]>all[11] :
    p_win+=1
    p_gf+=all[10]-all[11]
    p_point+=3
    m_lose+=1
    m_gf-=all[10]-all[11]
elif all[10]== all[11] :
    p_draw+=1
    p_point+=1
    m_draw+=1
    m_point+=1 
else :
    m_win+=1
    m_gf+=all[11]-all[10]
    m_point+=3
    p_lose+=1
    p_gf-=all[11]-all[10]                
points={'Spain':sp_point,'Iran':ir_point,'Morocco':m_point,'Portugal':p_point}   #Then we create dictionary for each country.
wins={'Spain':sp_win,'Iran':ir_win,'Morocco':m_win,'Portugal':p_win}
loses={'Spain':sp_lose,'Iran':ir_lose,'Morocco':m_lose,'Portugal':p_lose}
goal_diff={'Spain':sp_gf,'Iran':ir_gf,'Morocco':m_gf,'Portugal':p_gf}        
draws={'Spain':sp_draw,'Iran':ir_draw,'Morocco':m_draw,'Portugal':p_draw}
m=list()                   #Now, we need to make sure it prints line by line in the order specified in the problem statement. Therefore, we create a temporary list called 
x=list(points.values())    
x=set(x)
y=list(x)                    
y.sort(reverse=True)
for i in range(0,len(y)):             #Next, we extract the values of each dictionary key and put them into our temporary list, and then we proceed to generate the output.
    for key,value in points.items() :
        if value==y[i] :
            m.append(key)
            m.sort()
    if len(m)==1:          # One point to note is that I did not consider the number of wins for each team for ordering because any team with a higher score than another definitely has more or equal wins compared to the other team.
        print(m[0],'','wins:'+str(wins[m[0]]),',','loses:'+str(loses[m[0]]),',','draws:'+str(draws[m[0]]),',','goal difference:'+str(goal_diff[m[0]]),',','points:'+str(points[m[0]]))
    elif len(m)==2 :
        print(m[0],'','wins:'+str(wins[m[0]]),',','loses:'+str(loses[m[0]]),',','draws:'+str(draws[m[0]]),',','goal difference:'+str(goal_diff[m[0]]),',','points:'+str(points[m[0]]))
        print(m[1],'','wins:'+str(wins[m[1]]),',','loses:'+str(loses[m[1]]),',','draws:'+str(draws[m[1]]),',','goal difference:'+str(goal_diff[m[1]]),',','points:'+str(points[m[1]]))
    elif len(m)==3 :
        print(m[0],'','wins:'+str(wins[m[0]]),',','loses:'+str(loses[m[0]]),',','draws:'+str(draws[m[0]]),',','goal difference:'+str(goal_diff[m[0]]),',','points:'+str(points[m[0]]))
        print(m[1],'','wins:'+str(wins[m[1]]),',','loses:'+str(loses[m[1]]),',','draws:'+str(draws[m[1]]),',','goal difference:'+str(goal_diff[m[1]]),',','points:'+str(points[m[1]]))
        print(m[2],'','wins:'+str(wins[m[2]]),',','loses:'+str(loses[m[2]]),',','draws:'+str(draws[m[2]]),',','goal difference:'+str(goal_diff[m[2]]),',','points:'+str(points[m[2]]))
    elif len(m)==4 :
        print(m[0],'','wins:'+str(wins[m[0]]),',','loses:'+str(loses[m[0]]),',','draws:'+str(draws[m[0]]),',','goal difference:'+str(goal_diff[m[0]]),',','points:'+str(points[m[0]]))
        print(m[1],'','wins:'+str(wins[m[1]]),',','loses:'+str(loses[m[1]]),',','draws:'+str(draws[m[1]]),',','goal difference:'+str(goal_diff[m[1]]),',','points:'+str(points[m[1]]))
        print(m[2],'','wins:'+str(wins[m[2]]),',','loses:'+str(loses[m[2]]),',','draws:'+str(draws[m[2]]),',','goal difference:'+str(goal_diff[m[2]]),',','points:'+str(points[m[2]]))
        print(m[3],'','wins:'+str(wins[m[3]]),',','loses:'+str(loses[m[3]]),',','draws:'+str(draws[m[3]]),',','goal difference:'+str(goal_diff[m[3]]),',','points:'+str(points[m[3]]))  
    m=list()
