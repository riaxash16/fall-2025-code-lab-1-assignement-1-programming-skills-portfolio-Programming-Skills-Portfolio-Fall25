names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"] #list of names

search_name = input("Enter search name: ").capitalize() #ask user to enter a name

if search_name in names: #check if name is in the list
    print(f"{search_name} was found in the list.") #print if name is found
else: #check if name is not in the list
    print(f"{search_name} was not found in the list.") #print if name is not found
