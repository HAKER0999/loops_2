# TASK_1
def Izogramma(items, lst):
    for i in items:
        lst.append(i)
    for x in lst:
        if lst.count(x) > 1:
            return False
        elif lst.count(x) == 1:
            return True

print(Izogramma('algorism', []))
print(Izogramma('consecutive', []))



# TASK_2
def society_name(names, result):
    for x in names:
        result = result + x[0]
    print(result)
society_name(["Adam", "Sarah", "Malcolm"], '')
society_name(["Harry", "Newt", "Luna", "Cho"], '')
society_name(["Phoebe", "Chandler", "Rachel", "Ross", "Monica", "Joey"], '')



# TASK_3
def alphabet_soup(item):
    sort_item = sorted(item)
    rer = ''
    for x in sort_item:
        rer += x
    return rer

print(alphabet_soup("hello"))
print(alphabet_soup("edabit"))
print(alphabet_soup("hacker"))
print(alphabet_soup("geek"))
print(alphabet_soup("javascript"))



# TASK_4
def filter_list(lst, lst2):
    for c in lst:
        if type(c) == int:
            lst2.append(c)
    return lst2

print(filter_list([1, 2, 3, "a", "b", 4], []))
print(filter_list(["A", 0, "Edabit", 1729, "Python", "1729"], []))
print(filter_list(["Nothing", "here"], []))



# TAsk_5
def index(item, lst):
    for x in item:
        if x == x.upper():
            lst.append(item.find(x))
    return lst

print(index("eDaBiT", []))
print(index("eQuINoX", []))
print(index("determine", []))
print(index("STRIKE", []))
print(index("sUn", []))


# TASK_6
def David(devid_dict):
    for x in devid_dict:

# CHIQMADI!!!

print(David({"David_age": 25, 'David_height': 175, 'David_weight': 75})