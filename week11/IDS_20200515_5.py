def where_are_you_from(city, country):
    return city, country

print(where_are_you_from("Taipei", "Taiwan"))
print(type(where_are_you_from("Taipei", "Taiwan")))

my_city, my_country = where_are_you_from("Taipei", "Taiwan")
print(my_city)
print(my_country)