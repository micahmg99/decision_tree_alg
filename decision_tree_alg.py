#micah gentry

#decision tree

from restaurant_data import examples, attributes
import math


#returns which value of "WillStay" is more prevelent. 
def plurality_value(examples):

    n = len(examples)
    #dataset is empty
    if n == 0:
        return 0
    #initialize the counting variables
    yes = 0
    no = 0

    #iterate through the data
    for i in examples:
        if i["WillWait"] == True:
            yes += 1
        else:
            no += 1

    #return the finding   
    if yes >= no:
        return True
    else:
        return False

#calculates the entropy of "WillStay"
def entropy(examples):
   
    n = len(examples)
    #dataset is empty
    if n == 0:
        return 0
    
    #initialize counting variables
    yes = 0
    no = 0

    #iterate through data
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

#returns how mixed/pure the data is based on attributes
def importance(attribute, examples):

    n = len(examples)
    #dataset is empty
    if n == 0:
        return 0
    
    #entropy of entire dataset
    init_entropy = entropy(examples)
    
    #container to keep the different groups we have in the attribute
    groups = {}

    #iterate through examples
    for i in examples:
    
        label = i[attribute]
        #add label to groups
        if label not in groups:

            groups[label] = []

        groups[label].append(i)

    after = 0
    #iterate through groups
    for label, subset in groups.items():
        weight = len(subset) / n
        after += weight * entropy(subset)

    gain = init_entropy - after
    return gain


def partition(examples, attribute):
    
    values = {i[attribute] for i in examples}
    groups = {v: [] for v in values}

    for i in examples:
        groups[i[attribute]].append(i)

    return groups  

    

# def Learn_Decision_Tree(examples, attributes, parent_examples):
    
if __name__ == "__main__":
    from restaurant_data import examples
    print(plurality_value(examples))
    print(entropy(examples))
   # print(importance("Rain", examples))
    print(partition(examples, "Type"))