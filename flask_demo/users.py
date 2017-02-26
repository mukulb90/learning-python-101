# ORM or no ORM ?
from sqlalchemy import create_engine
connection_url = 'mysql+pymysql://user:pass@vit-demo-instance.czyykm7bj4cx.us-east-1.rds.amazonaws.com:3306/demo';
engine = create_engine(connection_url);

def getUsers():
    users = []
    with engine.begin() as conn:
        resultProxy = conn.execute('select * from Users')
        result = resultProxy.fetchall()
        for user in result:
            (userId, fname, lname) = user
            users.append({'userId':userId, 'fname':fname, 'lname':lname})
    return users

if __name__ == '__main__':
    print(getUsers())
