#Slicing = create a subsiring by extracing elements from another string
#           indexing[] or slice()
#           [start:stop:step]


name = "Csaszar Daniel"

first_name = name[0:7] 
last_name = name[8:14]
funky_name = name[0:14:2]
reversed_name = name[::-1]
website = "http://google.com"
website2 = "http://wikipedia.com"
website_slice = slice(7,-4)
print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)
print(website[website_slice])
print(website2[website_slice])
