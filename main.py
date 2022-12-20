from models import db,Deputat
from parsing import Parser


def check_connection(func):
    def wrapper(*args, **kwargs):
        try:
            db.connect()
            func(*args,**kwargs)
        finally:
            db.close()
    return wrapper

class DeputatCRUD:
    @check_connection
    def create_table(self):
        db.create_tables([cls])
        
        
    @check_connection
    def insert_data(self):
        objs = Parser().data
        with db.atomic():
            Deputat.insert_many(objs).execute()
        # for dep in objs:
        #     deputat = Deputat.create(**dep)
            

if __name__ == "__main__":
    crud = DeputatCRUD()
    crud.insert_data()