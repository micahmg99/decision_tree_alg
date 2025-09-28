#micah gentry

#decision tree

from restaurant_data import examples, attributes
import math

num_of_examples = len(examples)

def plurality_value(examples):

    yes = 0
    no = 0

    for i in examples:
        if i["WillWait"] == True:
            yes += 1
        else:
            no += 1
        
    if yes >= no:
        return True
    else:
        return False


def entropy(examples):
    yes = 0
    no = 0

    for i in examples:
        if i["WillWait"] == True:
            yes += 1
        else:
            no += 1
    
    p_true = yes / len(examples)
    p_false = no / len(examples)

    a = p_true * math.log2(p_true)
    b = p_false * math.log2(p_false)

    awnser = -(a+b)

    return awnser


# def importance(attribute, examples):

# def partition(examples, attribute):
    

# def Learn_Decision_Tree(examples, attributes, parent_examples):
    
if __name__ == "__main__":
    from restaurant_data import examples
    print(plurality_value(examples))
    print(entropy(examples))