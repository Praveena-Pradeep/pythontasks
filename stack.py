stack=[]
stack.append(15)
stack.append(25)
stack.append(35)
stack.append(45)
print("stack after pushes:",stack)
last_item=stack.pop()
print("popped item:",last_item)
print("stack after pop:",stack)
last_item=stack[-1]
print("last_item:",last_item)
is_empty=len(stack)==0
print("is the stack empty?",is_empty)
stack_size = len(stack)
print("stack size:",stack_size)
