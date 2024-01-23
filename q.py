def enqueue(lst,value):
    lst.append(value)
    print("Value inserted")
    
def deque(lst):
    if len(lst)<1:
        print("Queue empty")
    else:
        a=lst.pop(0)
        print("Poped element is "+ str(a))
        
def display(lst):
    if len(lst)<1:
        print("Queue empty")
        
    else:
        print("Queue elements are: ")
        for i in lst:
            print(i)

def main():
    queue=[]
    loop='Y'
    while(loop=='Y'):
        choice=input("Enter 1 for enqueue, 2 for deque and 3 for display::")
        if choice=='1':
            val=int(input("Enter the value ::"))
            enqueue(queue,val)
        elif choice=='2':
            deque(queue)
        elif choice=='3':
            display(queue)
        else:
            print("Bad choice")

        loop=str(input("Do you want to continue Y/N?"))
        if(loop!='Y'):
            print("Ok ! Exited from this program")
            
main()