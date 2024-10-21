from sqlalchemy import create_engine, insert, delete, update, select, text
import sqlalchemy
from sqlalchemy.orm import sessionmaker
import json
import pandas as pd

from db_control.mymodels import Base #, User, Comment

from db_control.connect import engine
from db_control.mymodels import Customers


# 1. 新しいテーブルを作成する関数
def create_new_customers_table():
    with engine.connect() as connection:
        connection.execute(text("""
            CREATE TABLE new_customers3 (
                customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_name TEXT,
                age INTEGER,
                gender TEXT
            );
        """))

# 2. 既存のデータを新しいテーブルに移行する関数
def migrate_data_to_new_table(session):
    customers = session.query(Customers).all()
    
    for customer in customers:
        # 新しいIDは自動で採番されるので指定しない
        session.execute(text("""
            INSERT INTO new_customers3 (customer_name, age, gender) 
            VALUES (:customer_name, :age, :gender);
        """), {
            'customer_name': customer.customer_name,
            'age': customer.age,
            'gender': customer.gender
        })
    
    session.commit()

# 3. 古いテーブルを削除し、新しいテーブルを元の名前に変更する関数
def finalize_schema():
    with engine.connect() as connection:
        # 古いテーブルを削除
        connection.execute(text("DROP TABLE customers1;"))
        
        # 新しいテーブルの名前を変更
        connection.execute(text("ALTER TABLE new_customers1 RENAME TO customers;"))
    

if __name__ == "__main__":
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # 1. 新しいテーブルを作成
        create_new_customers_table()

        # 2. データを新しいテーブルに移行
        migrate_data_to_new_table(session)

        # 3. 古いテーブルを削除し、新しいテーブルを元の名前に変更
        finalize_schema()
    finally:
        session.close()