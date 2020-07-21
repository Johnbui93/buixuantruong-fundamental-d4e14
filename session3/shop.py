# stuff1 = 'ao tam'
# stuff2 = 'ao mua'
# stuff3 = 'ao phao'

stuffs = ['ao tam','ao mua','ao phao','quan boi']
# print(stuffs) #read 

#print(len(stuffs))

# print(stuffs[0]) #read one
#read all
# for i in range(len(stuffs)):
#     print(stuffs[i])

#creat
# new_item = input(' your new item:')
# stuffs.append(new_item) #them vao vi tri cuoi cung vi neu o vi tri khac thi list se loan

#update
# index = int(input('vi tri muon sua'))
# new_item = input('ten item moi')
#stuffs[0] = ''

# stuffs[index] = new_item
# print(len(stuffs))
# for item in stuffs:
#     print(item)

# stuffs.pop(0) #delete by index
# stuffs.delete('ao phao') #delete by value

stuffs = ['ao tam','ao mua','ao phao','quan boi']
    letter = input('welcome to our shop, what do you want? (C R U D)')
    if letter == 'C':
        new_item = input(' your new item:')
        stuffs.append(new_item)
        for i in range(len(stuffs)):
            print(stuffs[i])
    elif letter == 'R':

        for i in range(len(stuffs)):
            print(stuffs[i])
    elif letter == 'U':
        index = int(input('vi tri muon sua'))
        new_item = input('ten item moi')
        stuffs[index] = new_item
        for i in range(len(stuffs)):
            print(stuffs[i])
    else:
        delete_index = int(input('position you want to delete'))
        stuffs.pop(delete_index)
        print(stuffs)

