DB_HOST = "127.0.0.1"
DB_NAME = "vectorstat_"
DB_USER = "postgres"
DB_PASS = "postgres"
import psycopg2
import psycopg2.extras

conn = psycopg2.connect(dbname = DB_NAME, user = DB_USER, password = DB_PASS, host = DB_HOST)
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
users = [
    'sysadmin@test.com',
    'useradmin@test.com',
    'fieldservice@test.com',
    'eoltech@test.com',
    'engineering@test.com',
    'customersupport@test.com'
]
i = 0
query = "SELECT id_role FROM \"authorization\".\"user\" WHERE email ='" + str(users[i])+"'"
cur.execute(query)
result = cur.fetchone()
key = result[0]

query = """SELECT pms.name AS permission FROM \"authorization\".\"role\" AS r
	INNER JOIN \"authorization\"."role_permission" AS rp ON r.id = rp.id_role
	INNER JOIN "authorization"."permission" AS pms ON pms.id = rp.id_permission
WHERE rp.id_role ='""" + str(key)+"'"
cur.execute(query)
permissions  = cur.fetchall()
flat_list = [item for sublist in permissions for item in sublist]
print(flat_list)
for i in flat_list:
    print(i)

conn.commit()
cur.close()
conn.close()


descriptions = ['AddUnit','UpdateUnit','AddUnitNotes','ViewUnit Notes','DeleteUnit']
flat_list = [x.lower() for x in flat_list]
if descriptions[1].lower() in flat_list:
    print("Yes")
else:
    print("No")
