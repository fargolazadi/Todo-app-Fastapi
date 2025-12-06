from app.database import SessionLocal
from app.models import User, Task
from app.auth import get_password_hash

def run_seed():
    db = SessionLocal()


    user = db.query(User).filter(User.username == "testuser").first()
    if not user:
        user = User(username="testuser", hashed_password=get_password_hash("testpass"))
        db.add(user)
        db.commit()
        db.refresh(user)


    if not db.query(Task).filter(Task.owner_id == user.id).first():
        tasks = [
            Task(title="تسک اول", description="توضیح اول", completed=False, owner_id=user.id),
            Task(title="تسک دوم", description="توضیح دوم", completed=True, owner_id=user.id),
            Task(title="تسک سوم", description="توضیح سوم", completed=False, owner_id=user.id),
        ]
        db.add_all(tasks)
        db.commit()

    print(" داده‌های اولیه وارد شدند.")
    db.close()

if __name__ == "__main__":
    run_seed()
