def find_ticket(ticket):
    num = str(ticket)
    lst1 = int(num[:1]) + int(num[1:2])
    lst2 = int(num[-1]) + int(num[-2])
    if lst1 == lst2:
        return True
    else:
        return False

ticket = int(input("введите номер билета:"))
print("повезло?", find_ticket(ticket))
