myph={"virat":[9066060,"virat@gmail.com","Chennai","TN"],
      "MSD":[99999999,"MSD@gmail.com","Vellore","TN"],
      "Rohit": [66665555,"Rohit@gmail.com","Chennai","TN"]

}

"""for k,v in myph.items():#list (myph.items()):
    print("Name", k)
    print("Ph num", v)
    print("********************")

"""
for k,v in list (myph.items()):
    print("Name", k)
    print("Ph num", v[0])
    print("Mail", v[1])
    print("city", v[2])
    print("state", v[3])
    print("********************")
