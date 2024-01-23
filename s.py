def push(lst,value):
    lst.append(value)
    print("Value inserted")
    
def pop(lst):
    if len(lst)<1:
        print("Stack empty")
    else:
        a=lst.pop()
        print("Poped element is "+ str(a))
        
def display(lst):
    if len(lst)<1:
        print("Stack empty")
        
    else:
        print("Queue elements are: ")
        for i in lst:
            print(i)

def main():
    stack=[]
    loop='Y'
    while(loop=='Y'):
        choice=input("Enter 1 for push, 2 for pop and 3 for display::")
        if choice=='1':
            val=int(input("Enter the value ::"))
            push(stack,val)
        elif choice=='2':
            pop(stack)
        elif choice=='3':
            display(stack)
        else:
            print("Bad choice")

        loop=str(input("Do you want to continue Y/N?"))
        if(loop!='Y'):
            print("Ok ! Exited from this program")
            
main()