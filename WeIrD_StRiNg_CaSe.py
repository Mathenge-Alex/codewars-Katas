# Write a function that accepts a string, and returns the same string with all even indexed characters in each word upper cased, and all odd indexed characters in each word lower cased. The indexing just explained is zero based, so the zero-ith index is even, therefore that character should be upper cased and you need to start over for each word.

# The passed in string will only consist of alphabetical characters and spaces(' '). Spaces will only be present if there are multiple words. Words will be separated by a single space(' ').

# Examples:
# "String" => "StRiNg"
# "Weird string case" => "WeIrD StRiNg CaSe"

# Solution

def to_weird_case(words):
    wds = [i.lower() for i in words[:]]
    weird = []
    for i in range(len(wds)):
        if i % 2 == 0:
            weird.append(wds[i].upper())
        else:
            weird.append(wds[i])
    weird = str("".join(weird))

    return weird

# Test  case




#  For Each word:

def to_weird_case(words):
    words = words.split()
    wds = [i.lower() for i in words[:]]
    weird = []
    for x in wds:
        cluster = []
        for i in range(len(x)):
            if i % 2 == 0:
                cluster.append(x[i].upper())
            else:
                cluster.append(x[i])
        weird.append(cluster[:])
    weird = ' '.join([''.join(wd) for wd in weird])

    return weird


print(to_weird_case("Hello World")) #HeLlO WoRlD
print(to_weird_case("This is a test")) # ThIs Is A TeSt
