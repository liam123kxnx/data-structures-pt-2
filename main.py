my_list = [1,2,3,4,5,6]
my_tuple = ("vegeta","kakarot","kale","caulifla","gohan","goten")
 
my_list.append(5)
print(my_list)
print(my_tuple[1:5])
set1 = {"minazuki","jokuho-raikoben","tesa-zangetsu","daiguren-hiorinmaru","hakka-no-togame"}
cool_powers = {"bankai","quirks","shikai","devil-fruits","haki"}
powers = {"minazuki","demon-blood","shikai"}
print(cool_powers.union(powers))
print(cool_powers.intersection(powers))
print(cool_powers.difference(powers))
print(cool_powers.symmetric_difference(powers))