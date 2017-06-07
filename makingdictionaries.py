'''Assignment: Making Dictionaries
Create a function that takes in two lists and creates a single dictionary
where the first list contains keys and the second values. Assume the lists will be of equal length.

Your first function will take in two lists containing some strings.
by: Troy Center, troycenter1@gmail.com, Coding Dojo Python fundamentals, June 2017
'''
#pylint: disable=C0103
def zipdictionaries(arr1, arr2):
    '''function will create a dictionary, practicing fundamentals with dictionaries
    '''
    new_dict = {}
    new_dict = zip(arr1, arr2)

    return new_dict


def createdictionaries():
    '''This function sends the arrays to the zipdictionary function and then prints the output.
    '''
    name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar", "Troy"]
    favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

    print zipdictionaries(name, favorite_animal)

createdictionaries()