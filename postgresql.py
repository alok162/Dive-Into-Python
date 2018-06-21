import psycopg2


conn = psycopg2.connect(database = "practicedb", user = "alok", password = "", host = "127.0.0.1", port = "5432")
print 'datatabse connection successfully'

curr = conn.cursor()
curr.execute("select e.emp_name, d.dept_name from employee e inner join department d on e.dept_id=d.department_id")
obj = curr.fetchall()
print obj