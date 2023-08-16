def have_common_element(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False


list1 = (item for item in input("Enter the list items : ").split())
list2 = (item for item in input("Enter the list items : ").split())
#list1 = [1, 2, 3, 4, 5]
#1list2 = [5, 6, 7, 8, 9]

if have_common_element(list1, list2):
    print("The lists have at least one common element.")
else:
    print("The lists do not have any common element.")
