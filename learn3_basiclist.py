stock_of_magazine = [100, 30, 40, 50, 60, 34, 90]

stock_of_magazine.remove(100)
stock_of_magazine.append(88)
# print (stock_of_magazine[:2])
# print (stock_of_magazine[-3:])
# print (len(stock_of_magazine))

test_ratings = [1, 2, 3, 4, 5]
test_liked = [i>=4 for i in test_ratings]
print(len(test_liked))
# print(len(test_ratings))

print(test_ratings[:-2]) #return: [1, 2, 3] (trim rest of list by -2 from the end)
print(test_ratings[:2]) #return: [1, 2] (stop at index = 2)
print(test_ratings[2:]) #return: [3, 4, 5] (start at index = 2 to the end of list)
print(test_ratings[-2:]) #return: [4, 5] (take 2 values from the end of the list)
print(test_ratings[2:-2]) #return: [3] (start at index = 2 AND trim rest of list by -2 from the end of the list)
print("\n")

print(test_ratings.index(5))
print(30 in stock_of_magazine)
print("\n")

#list is MUTABLE (can be modified when running) and use "{}"
#tuples: IMMUTABLE and use "()" (not: "{}")
#example: a = (1, 2, 3) or a = 1,2,3
a = 1,2,3
b = 0.33
print(a)
numerator, denominator = b.as_integer_ratio()
print(numerator / denominator)

a, b = b, a
print(a, b)