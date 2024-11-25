import csv
import pymysql

connection = pymysql.connect(
    user = 'root',
    password = '1234',
    host = 'localhost',
    database = 'my_db'
    
)


cursor = connection.cursor()

cursor.execute('''
     CREATE TABLE IF NOT EXISTS salary_data (
        idx INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        average DECIMAL(10, 2),
        minimum DECIMAL(10, 2),
        maximum DECIMAL(10, 2)
    )         
''')

with open('salary_list.csv', mode='r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)

    for row in csv_reader:
        name = row[0]
        average = float(row[1].replace(',', ''))
        minimum = float(row[2].replace(',', ''))
        maximum = float(row[3].replace(',', ''))


        sql = "INSERT INTO salary_data (name, average, maximum, minimum) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (name, average, maximum, minimum))

        
        
connection.commit()
cursor.close()
connection.close()

print('완료')

