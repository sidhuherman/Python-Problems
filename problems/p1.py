# Say you have a list value like this: spam = ['apples', 'bananas, 'tofu', 'cats']
# Write a function that takes a list value as an argument and returns a string with all the
# items separated by a comma and a space, with and inserted before the last item. For
# example, passing the previous spam list to the function would return &#39;apples, bananas,
# tofu, and cats&#39;. But your function should be able to work with any list value passed to
# it


def result(list):
    string = ""
    for i in range(len(list)-1):
        string = string + list[i] + ", "
    string = string + "and " + list[-1]
    return string


spam = ['apples', 'bananas', 'tofu', 'cats']
print(result(spam))
