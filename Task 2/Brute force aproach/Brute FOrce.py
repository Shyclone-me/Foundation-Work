# simple brute force approach 

Name = ["Ram", "Shyam", "Hari", "Sita", "Gita", "Laxman", "Rawan", "Nobita", "Sunio", "Gian", "Sizuka", 
        "degisugi", "Doreamon", "Doreme", "Sourav", "Puyush", "Sahil", "Avantiva"]

Name_to_search = "Doreamon"

for i in Name:
    if i == Name_to_search:
        print(f"{i} found in list")
    else:
        continue
