
from listOfObj import ListOfObj

test_list = ListOfObj([2,3,4])

print(test_list)
print(type(test_list))

for n in test_list:
    print(n)

print(len(test_list))
print(test_list[1])

print(test_list[1:2])
print(type(test_list[1:2]))

print(test_list[::-1])

print(test_list > 2)

print(test_list == [2,3,4])

print(test_list[test_list > 2])

class Box:
    name = 'Baox'
    def test(self):
        print('I''m a Box')

test_list = ListOfObj([Box() for n in range(1,5)])
print(test_list[1])

print(test_list.name)
print(test_list[2].name)


test_list.surnemae = 'ciccio'
print(test_list[2].surnemae)

print(test_list.test)
test_list[1].test()
test_list.test()
