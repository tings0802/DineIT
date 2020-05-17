import os
import time
from datetime import datetime

def list_menu(path):
    print ("All stores:")
    with open(path, 'r') as file:
        lines = file.readlines()
        if lines == []:
            print ('The list is empty now.\n')
    with open(path, 'r') as file:
        for i in file:
            print(i, end = '')
    print("\n")


def reset_menu(path1, path2, path3):

    with open(path1, 'w') as file1:
        file1.write('')
        file1.close()
    with open(path2, 'w') as file2:
        file2.write('')
        file2.close()
    with open(path3, 'w') as file3:
        file3.write('')
        file3.close()
    os.system('clear')
    print ('Data is reset!\n')

def add_item(path):
    with open(path, "r") as store_list:
        lines = store_list.readlines()
        new_store = input('Add one new store ......')
        new_store += '\n'
        if lines == []:
            pass
        elif new_store not in lines:
            pass
        else:
            del_item(path, new_store)
    with open(path, "a") as store_list:
        store_list.write(new_store)
        store_list.close()
        add_business_hours("open_hours_lunch.txt", "close_hours_lunch.txt")
        os.system('clear')
        print ('Data is update!\n')

def del_item(path, item):
    item += '\n'
    count = 0
    with open(path, 'r') as file:
        lines = file.readlines()
        for i in lines:
            if i == item:
                break
            else:
                count += 1
        lines = [i for i in lines if i != item]
        with open(path, 'w') as file:
            file.writelines(lines)
    del_business_hours("open_hours_lunch.txt", count)
    del_business_hours("close_hours_lunch.txt", count)


def add_business_hours(path1, path2):
    with open(path1, "a") as add_open_hours:
        new_hours1 = input('Add open_hours ...... (ex: 7.25)')
        add_open_hours.write(new_hours1 + "\n")
        add_open_hours.close()
    with open(path2, "a") as add_close_hours:
        new_hours2 = input('Add close_hours ...... (ex: 16.30)')
        add_close_hours.write(new_hours2 + "\n")
        add_close_hours.close()

def del_business_hours(path, n):
    with open(path, 'r') as file:
        lines = file.readlines()
        item = lines[n]
        lines = [i for i in lines if i != item]
        with open(path, 'w') as file:
            file.writelines(lines)

def test(path, data = []):
    if not data:
        data = ['Store_A\n', 'Store_B\n', 'Store_C\n', 'Store_D\n', 'Store_E\n']
    with open(path, 'w') as file:
        file.writelines(data)

def random_meal(path, path1, path2, T):
    with open(path, 'r') as file:
        lines = file.readlines()
        if lines == []:
            os.system('clear')
            print ('The list is empty now.\n')
        else:
            while T > 0 or T == 0:
                m = time.time() ** 2
                with open(path, 'r') as file:
                    lines = file.readlines()
                with open(path1, 'r') as file1:
                    lines1 = file1.readlines()   
                with open(path2, 'r') as file2:
                    lines2 = file2.readlines()   
                m %= len(lines)
                m = int(m)
                t = str(T) + '\n'
                L1 = lines1[m]
                L2 = lines2[m]
                if (L1 < t and t < L2) or (L1 < t and L2 < L1) or (L1 == L2):
                    return lines[m]
                break
    
def now_list(path, path1, path2, T):
    t = str(T) + '\n'
    with open(path, 'r') as file:
        lines = file.readlines()
        l = len(lines)
        if lines == []:
            os.system('clear')
            print ('The list is empty now.\n')
        else:
            print ('The stores are opening now:')
            count = 0
            lists = ''
            for i in range(l):
                with open(path1, 'r') as file1:
                    lines1 = file1.readlines()
                    L1 = lines1[i]   
                with open(path2, 'r') as file2:
                    lines2 = file2.readlines()
                    L2 = lines2[i]
                if (L1 < t and t < L2) or (L1 < t and L2 < L1) or (L1 == L2):
                    lists += lines[i]
                    count += 1
            print (lists)
            if count == 0:
                    print ('None\n')

                    

def main():
    count = 1
    os.system('clear')
    while count == 1: 
        now = datetime.now()
        Time = now.hour + now.minute * 0.01
        now_list("store_list_lunch.txt", "open_hours_lunch.txt", "close_hours_lunch.txt", Time)       
        command = input('(E)xecute program\n(L)ist all stores\n(A)dd store\n(D)elete store\n(R)eset data\nLet\'s choose what to eat ......')
      
        if command == 'L':
            os.system('clear')
            list_menu("store_list_lunch.txt")
            
        
        elif command == 'A':
            add_item("store_list_lunch.txt")
        
        elif command == 'D':
            item = input('Delete one store ......')
            del_item("store_list_lunch.txt", item)
            os.system('clear')
            print ('Data is update!\n')

        elif command == 'E':
            os.system('clear')
            print ('How about......')
            now = datetime.now()
            Time = now.hour + now.minute * 0.01
            print (random_meal("store_list_lunch.txt", "open_hours_lunch.txt", "close_hours_lunch.txt", Time))
            
        elif command == 'R':
            Insurance = input('Are you sure to reset data? (y/n)')
            if Insurance == 'y':
                reset_menu("store_list_lunch.txt", "open_hours_lunch.txt", "close_hours_lunch.txt")
            else:
                os.system('clear')
                print ('Cancel reset ......\n')
        
        else:
            print ('Thanks for your visit!')
            count = 0
            end = 0
    return 0

if __name__ == '__main__':
    main()




