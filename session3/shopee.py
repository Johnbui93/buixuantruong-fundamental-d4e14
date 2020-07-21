stuffs = ['ao tam','ao mua','ao phao','quan boi']
def list_out_item():
    for i in range(len(stuffs)):
        print(f'{i+1},{stuffs[i]}')
while True:
    action = input('welcome to our shop, what do you want? (C R U D)')
    if action == 'C' or action == 'c':
        new_item = input('your new item:')
        stuffs.append(new_item)
        list_out_item()
    elif action == 'R':
        list_out_item()

        # for i in range(len(stuffs)):
        #     #print(i,stuffs[i])
        #     print(f'{i+1},{stuffs[i]}')
    elif action == 'U':
        index = int(input('position you want to update')) -1
        new_item = input('your new item')
        stuffs[index] = new_item
        list_out_item()
        # for i in range(len(stuffs)):
        #     print(f'{i+1},{stuffs[i]}')
    elif action == 'D':
        #remove_value = input('enter the name of item')
        index = int(input('position you want to delete'))
        stuffs.pop(index)
        for i in range(len(stuffs)):
            print(f'{i+1},{stuffs[i]}')
    
