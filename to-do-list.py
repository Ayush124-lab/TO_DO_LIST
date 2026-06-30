def display_task(m):
    n=1
    for i in m:
        print(f'{n}) {i}')
        n+=1

def remove_task(m):
    
    while True:
        
        
        if len(m)!=0:
            a=int(input('Enter serial no. of tasks are completed:'))
            m.pop(a-1)
            display_task(m)
        else:
            print('No task is remaining')
            break    
        # for i in m:
        #     if a in i:
        #         m.pop(m.index(i))
        #     else:
        #         pass    
        if len(m)!=0:     
            print('Press 1 for YES\nPress any key for NO')
            ch=input('Do you want to remove more task:')g
            if ch=='1':
            # remove_task(m)
                continue
            else:
                print('remaining tasks:')
                display_task(m)
                break
        if len(m)==0:
                print('All tasks are completed')
                break    
                    
                    
n=1
print('Enter your tasks:')  
tasks=[]
while True:
    
    print(n,')',end='')
    a=input()
    
    tasks.append(a)
    if a[-1]=='':
        pass
    elif a[-1]==' ':
        break
    n+=1
print('\n')
print('Your tasks are:')
display_task(tasks)
print('\n')

remove_task(tasks)















