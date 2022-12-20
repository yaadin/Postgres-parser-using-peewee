import peewee as pw
from settings import settings

db = pw.PostgresqlDatabase(settings.db)


class Deputat(pw.Model):
    name = pw.CharField(max_length=100)
    fraction = pw.CharField(max_length=255)
    phone = pw.CharField(max_length=20, null=True)
    email = pw.CharField(max_length=100, null=True)
    
    class Meta:
        database = db
        

if __name__ == "__main__":
    db.create_tables([Deputat])