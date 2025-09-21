#import random module
import random

#2-create subjects,objects,actions
subjects=["SRK","Virat kohli","Modi ji","A central fox","State dog"]
Actions=["Launches fart","dance","Plays","orders","Celebrates"]
Objects=["At red fort","In mumbai train","in nursery school","At ganga ghat","At dummpyard"]

#Start the headline generation loop
while True:
    subjects=random.choice(subjects)
    Actions=random.choice(Actions)
    objects=random.choice(Objects)

    headline =print(f"Breaking news: {subjects} {Actions} {objects}")
    User=input("Do you want another headline(Yes/No):").strip().lower()
    if User=="no":
        break
print("Thanks for using the fake news headline generator")




