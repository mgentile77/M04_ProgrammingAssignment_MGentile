import csv, sqlite3
import sqlalchemy as sa



conn = sqlite3.connect('books.db')
curs = conn.cursor()
curs.execute("DROP TABLE books;")


curs.execute('''CREATE TABLE books
    (title VARCHAR(200) PRIMARY KEY,
     author VARCHAR(80),
     year INT);''')

with open('books2.csv', 'r') as books:
    seperate = csv.DictReader(books)
    to_db = [(i['title'], i['author'], i['year']) for i in seperate]
    
curs.executemany("INSERT INTO books(title, author, year) VALUES (?,?,?);", to_db)
curs.execute("SELECT * FROM books ORDER BY year DESC;")
mytable = curs.fetchall()
# print ()
# for row in (mytable):
#     print (row)
conn.commit()
conn.close()

eng = sa.create_engine('sqlite:///books.db')
conx = eng.connect()
meta = sa.MetaData()
books = sa.Table('books', meta, autoload_with=eng)

query = sa.select(books.columns.title).order_by(books.columns.title)
results = conx.execute(query)
mytable2 = results.fetchall()

print()
for row in (mytable2):
    print (row)
conx.close()


 