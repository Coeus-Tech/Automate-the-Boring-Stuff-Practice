def spam():
    wings = 'spam local'
    print(wings) # prints 'spam local'
def bacon():
    pizza = 'bacon local'
    print (pizza) # prints 'bacon local'
    spam()
    print(eggs) # prints 'bacon local'
eggs = 'global'
bacon()
print(eggs) #prints 'global'
