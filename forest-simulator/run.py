from forest_simulator import *



whitebark1 = WhitebarkTree()        
# print("whitebark1 = ",whitebark1)   # will print the object value
whitebark2 = WhitebarkTree(5)
# print("whitebark2 = ",whitebark2) 
foxtail1 = FoxtailPine()
foxtail2 = FoxtailPine(4)
jack = Lumberjack()
hundred_acre_wood = Forest([whitebark1, whitebark2, foxtail1, foxtail2])
print(hundred_acre_wood.is_empty())
print(whitebark1.get_height())  # Should print: 0
print(whitebark2.get_height())  # Should print: 5
print(hundred_acre_wood.get_status()) # Should print: ['There is a 0 tall FoxtailPine in the forest.', 'There is a 5 tall FoxtailPine in the forest.', 'There is a 0 tall FoxtailPine in the forest.', 'There is a 4 tall FoxtailPine in the forest.']
hundred_acre_wood.cut_trees(jack)
print(hundred_acre_wood.get_status()) # Should print: ['There is a 0 tall FoxtailPine in the forest.', 'There is a 0 tall FoxtailPine in the forest.', 'There is a 4 tall FoxtailPine in the forest.']
hundred_acre_wood.rain()
hundred_acre_wood.cut_trees(jack)
print(hundred_acre_wood.get_status()) # Should print: ['There is a 2 tall FoxtailPine in the forest.', 'There is a 1 tall FoxtailPine in the forest.']
print(hundred_acre_wood.is_empty()) #Should print: False


