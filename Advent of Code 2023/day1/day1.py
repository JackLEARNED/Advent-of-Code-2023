def main():
    with open('input.txt') as f:
        Part1 = f.read().split()

    with open('input.txt') as t:
        Part2 = t.read()
    
    Part2 = word2num(Part2).split()
    
    
    countForPart1 = 0
    countForPart2 = 0

    for words in Part1:
        countForPart1 = countForPart1 + part1(words)

    for words in Part2:
        countForPart2 = countForPart2 + part1(words)
    print(countForPart1)
    print(countForPart2)

    

    
def part1(value : str) -> int:
    #Indexes over the string from front to back and records the first instance of an int
    x = 0
    y = 0
    for char in value:
        if char.isdigit():
            x = char
            break
    #Same thing but reversed 
    for char in reversed(value):
        if char.isdigit():
            y = char
            break
    
    thingy = str(x) + str(y)
    return int(thingy)

def word2num(str : str):
    str2num = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e",
    }
    for k, v in str2num.items():
        str = str.replace(k,v)
    
    return str



main()