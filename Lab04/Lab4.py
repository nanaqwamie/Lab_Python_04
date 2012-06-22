#archibold_acheampong

print('(1a)')
print('')
groceries = ['bananas','strawberries','apples','bread']
groceries.append('champagne')
print groceries


print('')
print('(1b)')
print('')
groceries.remove('bread')
print groceries


print('')
print('(1c)')
print('')
grocery={'apple':'a','banana':'b','bread':'b','champagne':'c','strawberry':'s'}
grocery_type=raw_input('Please enter the grocery type :')
print 'The aisle to look into is aisle',grocery[grocery_type]
#print grocery['apple']



print('')
print'(2a)'
print('')
print 'dictionaries would be uesd for the catalogue'

print('')
print'(2b)'
print('')
catalogue={'apples':7.3,'bananas':5.5,'bread':1.0,'carrots':10.0,'champagne':20.90,'strawberries':32.6}
print catalogue


print('')
print'(2c)'
print('')
catalogue['bananas']=63.43
print catalogue

print('')
print'(2d)'
print('')
catalogue['chicken']=6.5
print catalogue


print('')
print'(3a)'
print('')
print"the 'dictionaries' data structure would best fit the data."

print('')
print'(3b)'
print('')
in_stock={'apples':7.3,'bananas':5.5,'bread':1.0,'carrots':10.0,'champagne':20.90,'strawberries':32.6}
print in_stock


print('')
print'(3c)'
print('')
print 'tuples do not change'

print('')
print'(3c)'
print('')
always_in_stock=('apples:7.3','bananas:5.5','bread:1.0','carrots:10.0','champagne:20.90','strawberries:32.6');
#print always_in_stock
for i in range(1,len(always_in_stock)):
    print always_in_stock[i]

print('')
print'(3d)'
print('')
print 'Come to shoprite! We always sell :'
for i in range(1,len(always_in_stock)):
    print always_in_stock[i]
