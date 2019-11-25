
from Models import User 
from SqlUtils2 import SqlUtils



s = SqlUtils()
admin = User(id=1312,email="email@",username="user3112name",password="passwo321rd",fname="fna321me",mname="mn321ame",lname="lna1312me")
s.Insert(admin)

def add_User(email,username,password,fname,mname,lname,registerdate):
    s = SqlUtils()
    admin = User(id=st_id,email=email,username=username,password=password,fname=fname,mname=mname,lname=lname,registerdate=registerdate)
    s.Insert(admin)

    """for i in range(5):
        st_id = random.randint(1,2**24)
        
        try:
            Session = sessionmaker(bind=engine)
            session = Session()
            admin = User(id=st_id,email=email,username=username,password=password,fname=fname,mname=mname,lname=lname,registerdate=registerdate)
            session.add(admin)
            session.commit()
            break
        except:
            continue    """