from sqlalchemy import create_engine
eng = create_engine('mysql+pymysql://user:pass@vit-demo-instance.czyykm7bj4cx.us-east-1.rds.amazonaws.com:3306')

with eng.begin() as conn:
    result = conn.execute('select * from dual')
    print(result)