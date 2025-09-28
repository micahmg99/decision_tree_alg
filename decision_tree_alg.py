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
   
    if num_of_examples == 0:
        return 0
    
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


def importance(attribute, examples):

    if num_of_examples == 0:
        return 0
    
    init_entropy = entropy(examples)
    
    groups = {}

    for i in examples:

        label = i[attribute]
        if label not in groups:

            groups[label] = []

        groups[label].append(i)

    after = 0

    for label, subset in groups.items():
        weight = len(subset) / num_of_examples
        after += weight * entropy(subset)

    gain = init_entropy - after
    return gain


# def partition(examples, attribute):
    

# def Learn_Decision_Tree(examples, attributes, parent_examples):
    
if __name__ == "__main__":
    from restaurant_data import examples
    print(plurality_value(examples))
    print(entropy(examples))
    print(importance("Rain", examples))