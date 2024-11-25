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
     CREATE TABLE IF NOT EXISTS company_salary (
        idx INT AUTO_INCREMENT PRIMARY KEY,
        company VARCHAR(255),
        average DECIMAL(13, 2),
        minimum DECIMAL(13, 2),
        maximum DECIMAL(13, 2)
    )         
''')

with open('company_salary.csv', mode='r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)

    for row in csv_reader:
        company = row[0]
        average = float(row[1].replace(',', '')) * 1000
        minimum = float(row[2].replace(',', '')) * 1000
        maximum = float(row[3].replace(',', '')) * 1000


        sql = "INSERT INTO company_salary (company, average, maximum, minimum) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (company, average, maximum, minimum))

        
        
connection.commit()
cursor.close()
connection.close()

print('완료')

