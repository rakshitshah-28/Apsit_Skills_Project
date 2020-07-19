def Sort():
    print('Input Numbers spearted by \'<space>\'')
    a = list(map(int, input('Enter - ').split(' ')))
    while True:        
        print("1.Ascending order")
        print("2.Descending order")
        print("3.BACK")
        print("select : 1/2/3")
        choice = int(input("Enter choice(1/2/3): "))
        if choice > 3:
            continue
        if choice == 1:
            print("Ascending order is ",sorted(a, reverse=False))
        elif choice == 2:
            print("Descending order is ",sorted(a, reverse=True))
        elif choice == 3:
            print("Thank you for using List SORTER !!")
            break
