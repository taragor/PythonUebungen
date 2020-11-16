#!/bin/usr/python3

#Write a Python program to sort a list of dictionaries using Lambda.

def main():
    models = [{'make':'Nokia', 'model':216, 'color':'Black'}, {'make':'Mi Max', 'model':'2', 'color':'Gold'}, {'make':'Samsung', 'model': 7, 'color':'Blue'}]

    sortedModels = sorted(models,key= lambda x: x['color'])
    
    print(sortedModels)

    pass

if __name__ == "__main__":
    main()