class node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
n1=node('ele1')
print(n1)
head=n1
print(head)
n2=node('ele2')
n3=node('ele3')
n4=node('ele4')
n1.next=n2
n2.next=n3
n3.next=n4
pointer=head
while(pointer!=None):
    print(pointer.value)
    pointer=pointer.next
    
    
