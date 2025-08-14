# creating dict
contact_book= {
    "emma":"123-456-7890",
    "liam":"987-654-3210",
    "olivia":"222-478-9876",
    "noah":"328-345-4783"
}
contact_book["malachi"]="098-708-2665"
contact_book["tamiweh"]="882-945-286"
print(contact_book["tamiweh"])

#accessing values
print(contact_book.get("jill", "not found" ))

#updating dictionary
contact_book["liam"]="234-576-8976"
#removing item in dictionary
removed_number=contact_book.pop('olivia')
del contact_book["liam"]
contact_book.clear()
print(contact_book)



menu={"pizza":"12.99", "salad":"6.99","fish":"10.99",}
del menu["salad"]
print(menu)

#looping through a dictionary

#loop through keys
for item in menu.keys():
    print(item)

#loop through values
for price in menu.values():
    print(price)   

#loop through key-value pair
for item, price in menu.items():
    print(f"{item}:{price}")  