import sqlite3
conn = sqlite3.connect("details.db")
cur = conn.cursor()

cur.execute("""
             CREATE TABLE IF NOT EXISTS details(
                 studentname TEXT,
                 collegename TEXT ,
                 round1marks FLOAT[10],
                 round2marks FLOAT[10], 
                    round3marks FLOAT[10],
                 technicalmarks FLOAT[20],
                 totalmarks FLOAT[50],
                 result TEXT,
                   rank TEXT
                 )
                """)

studentname = input("Enter the student name: ")
print("entered name is:", studentname)
collegename = input("Enter the college name: ")
print("entered college name is:", collegename)
round1marks = float(input("Enter the round 1 marks: "))
print("entered round 1 marks is:", round1marks)
round2marks = float(input("Enter the round 2 marks: "))
print("entered round 2 marks is:", round2marks)
round3marks = float(input("Enter the round 3 marks: "))
print("entered round 3 marks is:", round3marks)
technicalmarks = float(input("Enter the technical marks: "))
print("entered technical marks is:", technicalmarks)
totalmarks = round1marks + round2marks + round3marks + technicalmarks
print("total marks is:", totalmarks)
if len(studentname) > 30:
    print("Student name should be less than 30 characters.")
    exit()
if len(collegename) > 50:
    print("College name should be less than 50 characters.")
    exit()          
if round1marks < 0 or round1marks > 10:
    print("Round 1 marks should be between 0 and 10.")
    exit()
if round2marks < 0 or round2marks > 10:
    print("Round 2 marks should be between 0 and 10.")
    exit()
if round3marks < 0 or round3marks > 10:
    print("Round 3 marks should be between 0 and 10.")
    exit()
if technicalmarks < 0 or technicalmarks > 20:
    print("Technical marks should be between 0 and 20.")
    exit()

if totalmarks<35:
    result = "rejected"
elif totalmarks>=35:
    result = "selected"


if totalmarks<=40:
    rank = "average"
elif totalmarks>40 and totalmarks<=45:
    rank= "good"
elif totalmarks>45 and totalmarks<=50:
    rank = "excellent"        

cur.execute("""
             INSERT INTO details(studentname, collegename,round1marks,round2marks,round3marks,technicalmarks,totalmarks,result,rank)
             VALUES(?,?,?,?,?,?,?,?,?)
             """,(studentname,collegename,round1marks,round2marks,round3marks,technicalmarks,totalmarks,result,rank))    
conn.commit()

print("\ndetails of all students:")

cur.execute("SELECT* FROM details ORDER BY result DESC, rank")
rows = cur.fetchall()
for row in rows:
    print(row)

conn.close()    
