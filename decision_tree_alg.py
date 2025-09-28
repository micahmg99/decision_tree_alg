#micah gentry

#decision tree

from restaurant_data import examples, attributes

num_of_examples = len(examples)

def plurality_value(examples):

    yes = 0
    no = 0

    for i in examples:

        if i["Alt"] == True:
            yes += 1
        else:
            no +=1

        if i["Bar"] == True:
            yes += 1
        else:
            no += 1

        if i["Fri"] == True:
            yes += 1
        else:
            no += 1

        if i["Hun"] == True:
            yes += 1
        else:
            no += 1

        if i["Rain"] == True:
            yes += 1
        else:
            no += 1

        if i["Res"] == True:
            yes += 1
        else:
            no += 1
        
        if i["WillWait"] == True:
            yes += 1
        else:
            no += 1
        
    if yes >= no:
        return "yes"
    else:
        return "no"


if __name__ == "__main__":
    from restaurant_data import examples
    print(plurality_value(examples))

# def entropy(examples):

# def importance(attribute, examples):

# def partition(examples, attribute):
    

# def Learn_Decision_Tree(examples, attributes, parent_examples):
    