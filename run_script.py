from sqlalchemy import select
from models import User, Comment, Profile
from orm_engine import session

# # 1 - Uncomment this for the bulk insert, just to show how to insert many
# try:
#     for user_name in ["Sian", "Ron", "Anri", "Zara"]:
#         comment_text = f"This is a comment for {user_name}"  
#         profile_text = f"This is a profile for {user_name}" 
#         comment = Comment(comment=comment_text)
#         profile = Profile(profile=profile_text)
#         user = User(name=user_name, age=17+user_name.count("a"), profile=profile, comment=comment)
#         session.add(user)
#         session.commit()
# except:
#     session.rollback()
#     raise
# else:
#     session.commit()


# statement = session.execute(select(User)).all()
# for user in statement:
#     print(f"Name: {user[0].name} - Age: {user[0].age} - Comment: {user[0].comment} - Profile: {user[0].profile}")


while True:
    # Get user information
    user_name = input("Enter your name (or 'q' to quit): ")
    comment_text = input("Enter your linkedout comment (or 'q' to quit): ")
    profile_text = input("What's your current job ? (or 'q' to quit): ")
    age = int(input("How old are you ? (or 'q' to quit): "))

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