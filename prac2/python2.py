import mysql.connector

connection=mysql.connector.connect(
    host='localhost',
    database='udp',
    user='root',
    password='root123'
)
if connection.is_connected():
    print('successfully connected to the database')

    cursor = connection.cursor()
    create_table_query = """
              CREATE TABLE IF NOT EXISTS students (
                  id int auto_increment primary key,
                  name varchar(225) not null,
                  age int,
                  gender varchar(10)
                  )
                  """
    cursor.execute(create_table_query)
    print("table students created successfully")
    

    insert_query="""
            INSERT INTO students(name,age,gender)
            VALUES(%s,%s,%s)
            """
    student_records=[
                ('Alice',22,'female'),
                ('Bob',24,'male'),
                ('Charlie',26,'male')
     ]
    cursor.executemany(insert_query,student_records)
    connection.commit()
    print(f"{cursor.rowcount}records inserted into 'students'table.")