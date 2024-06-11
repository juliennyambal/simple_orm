from tkinter import *
from models import User, Comment, Profile
from sqla_engine import session

def calculate_sum():
  # Get values from entry fields
  try:

    # Create Comment, Profile, and User objects
    comment = Comment(comment=comment_entry.get())
    profile = Profile(profile=job_title_entry.get())
    age = int(age_entry.get())
    name = name_entry.get()
    user = User(name=name, age=age, profile=profile, comment=comment)
    
    session.add(user)
    session.commit()
  except:
      session.rollback()
      raise
  else:
      session.commit()

# Create the main window
window = Tk()
window.title("Addition Calculator")

# Create labels for input fields
label1 = Label(window, text="Name:")
label1.grid(row=0, column=0)

label2 = Label(window, text="Age:")
label2.grid(row=1, column=0)

label2 = Label(window, text="Job Title:")
label2.grid(row=2, column=0)

label2 = Label(window, text="LinkOut Comment:")
label2.grid(row=3, column=0)

# Create entry fields for user input
name_entry = Entry(window)
name_entry.grid(row=0, column=1)

age_entry = Entry(window)
age_entry.grid(row=1, column=1)

job_title_entry = Entry(window)
job_title_entry.grid(row=2, column=1)

comment_entry = Entry(window)
comment_entry.grid(row=3, column=1)

# Create a button to trigger calculation
button = Button(window, text="Save", command=calculate_sum)
button.grid(row=4, columnspan=2)

# Run the main loop
window.mainloop()