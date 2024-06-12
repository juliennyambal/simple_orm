# Start with this  

from sqlalchemy.orm import declarative_base, mapped_column, Mapped, relationship
from sqlalchemy import Integer, String, ForeignKey, select, delete, update, insert
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from models import Base

engine = create_engine(f"sqlite:///linkedout.sqlite3", echo=True)
session = Session(engine)

Base = declarative_base()

class User(Base):
    __tablename__ = "user_table"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]  = mapped_column(String(30))
    age: Mapped[int] = mapped_column(Integer)
    comment: Mapped["Comment"] = relationship(back_populates="user")
    profile: Mapped["Profile"] = relationship(back_populates="user")

    def __repr__(self):
        return f"{self.name}"
    
class Profile(Base):
    __tablename__ = "profile_table"
    id: Mapped[int] = mapped_column(primary_key=True)
    profile: Mapped[str]  = mapped_column(String(30))
    user_id: Mapped[int] = mapped_column(ForeignKey("user_table.id"))
    user: Mapped['User'] = relationship("User", back_populates="profile")

    def __repr__(self):
        return f"{self.profile}"
    

class Comment(Base):
    __tablename__ = "comment_table"
    id: Mapped[int] = mapped_column(primary_key=True)
    comment: Mapped[str]  = mapped_column(String(30))
    user_id: Mapped[int] = mapped_column(ForeignKey("user_table.id"))
    user: Mapped['User'] = relationship(back_populates="comment")

    def __repr__(self):
        return f"{self.comment}"
    
Base.metadata.create_all(engine)

# Think about making modules from here

# 2 - Extend the above to this 
while True:
    # Get user information
    user_name = input("Enter your name (or 'q' to quit): ")
    comment_text = input("Enter your linkedout comment (or 'q' to quit): ")
    profile_text = input("What's your current job ? (or 'q' to quit): ")
    age = int(input("How old are you ? (or '0' to quit): "))

    # Check for quit option
    if user_name.lower() == 'q':
        break

    try:
        # Create Comment, Profile, and User objects
        comment = Comment(comment=comment_text)
        profile = Profile(profile=profile_text)
        user = User(name=user_name, age=age, profile=profile, comment=comment)

        # Print the created user data (replace with actual database interaction)
        print(f"\nCreated User:")
        print(f"  Name: {user.name}")
        print(f"  Age: {user.age}")
        print(f"  Profile: {user.profile.profile}")
        print(f"  Comment: {user.comment.comment}")

        print("\n---\n")  # Separator between users
        session.add(user)
        session.commit()
    except:
        session.rollback()
        raise
    else:
        session.commit()

# # Print data
# statment_select = select(User)
# statement = session.scalars(statment_select).all()
# for user in statement:
#     print(f"Name: {user.name} - Age: {user.age} - Comment: {user.comment} - Profile: {user.profile}")
# session.commit()

# # Update row
# statement_update = update(User).values({"age": "70"}).where(User.name=="Nick")
# session.execute(statement_update)
# session.commit()

# # delete row
# statement_delete = (delete(User).where(User.name == 'Anri'))
# session.execute(statement_delete)
# session.commit()
