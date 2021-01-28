import os
import psycopg2
#databse_url=os.environ['postgres://tcykfsyhowqcje:1bc7dcbd9c0e7c7f74d3d3d1ed6045c9832048c53bb726e5b9fb26aaf676989c@ec2-3-220-193-133.compute-1.amazonaws.com:5432/d1c1c2jkicje']
try:
    conn=psycopg2.connect(host="ec2-3-220-193-133.compute-1.amazonaws.com",database="d1c1c2jkicje",user="tcykfsyhowqcje",password="1bc7dcbd9c0e7c7f74d3d3d1ed6045c9832048c53bb726e5b9fb26aaf676989c",port="5432")
except:
    print("not connected")
cur=conn.cursor()
cur.execute("""create table Location(username varchar(30),longitude varchar (30),latitude varchar (30),decription varchar (60))""")
conn.commit()
cur.close()
conn.close()