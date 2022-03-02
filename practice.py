counties_dict = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
for county, voters in counties_dict:
     print(f"{county} county has {voters:.2f} registered voters")