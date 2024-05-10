#Querying data from the tables (with different filters)
import psycopg2

conn = psycopg2.connect(
	database="Kydyrali",
	user='postgres',
	password='777777',
	host='localhost'
)
cursor = conn.cursor()
conn.autocommit = True

#select all
#sql = f"select * from phonebook";

#select filter 
sql = f"select * from phonebook where first_name = \'Mark\' ";


#select with sort filter decrease by first
#sql = f"select * from phonebook by order by first_name desc";


#select with sort filter increase by first
#sql = f"select * from phonebook by order by first_name asc";


cursor.execute(sql)
info = cursor.fetchall()
print(info)