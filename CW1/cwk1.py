"""
Introduction to Programming Coursework 1

@author: Thomas Carey - sc23t2c
"""


def valid_puzzle(puzzle: list) -> bool:
    if not isinstance(puzzle, list): # Check if puzzle is a list
        return False
    length = -1 # Length of each string in puzzle, init at -1
    for string in puzzle:
        if not isinstance(string, str):
            return False
        if length == -1: # If first string, set length to length of string
            length = len(string)
        elif len(string) != length: # If length of string not equal to length, return False
            return False
    return True


def similarity_grouping(data: list) -> list:
    if not isinstance(data, list): # Check if data is a list
        return []
    found = []
    out = []
    for i, item in enumerate(data):
        if isinstance(item, str) and item.isdigit(): # Convert strings to int if possible
            data[i] = int(item)
        if item not in found: # If item not found, add to found and create new list
            found.append(item)
            out.append([item])
        else: # If item found, add to list with same index as found to keep the order
            out[found.index(item)].append(item)
    return out


def highest_count_items(data: str) -> list:
    elements = {} # Dictionary to store items and their count
    for item in data.split(','): # Split data into list
        item = item.strip() # Remove whitespace
        if item not in elements: # If item not found, add to items
            elements[item] = 1
        else:
            elements[item] += 1
    max_count = max(elements.values()) # Get max count
    out = []
    for key, value in elements.items():
        if value == max_count:
            out.append([key, max_count]) # Add items with max count to out
    return out


def valid_char_in_string(popList: list, charSet: list) -> bool:
    if not (isinstance(popList, list)
        and isinstance(charSet, list)): # Check if popList and charSet are lists
        return False
    for string in popList:
        for char in string:
            if char not in charSet: # If char not in charSet, return False
                return False
    return True


def total_price(unit: int) -> float:
    sixes = unit // 6 # Get number of 6 packs
    singles = unit % 6 # Get number of units not in 6 packs
    price = sixes * 5 + singles * 1.25 # Calculate price
    if price >= 20:
        price *= 0.9 # Apply 10% discount if price over £20
    return price

if __name__ == "__main__":
    # sample test for task 1.1
    puzzle1 = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
               'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
               'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']

    puzzle2 = ['NAROUNDDL', 'EDCIT', 'UWSWEDZYA', 'OTCONVOYV',
               'BOSEVRUCI', 'BLLCGLPBD', 'TEENAGEDL', 'TREWZLCGY',
               'RAPLEBAYG', 'ATYTBIWRA', 'YEMROFINU']

    puzzle3 = ['RUNAROU', ['EDCITOA'], ('ZYUWSWE'), 'AKOTCYV',
               'LSBOSEI', 'BOBLLCG', 'LKTEENA', 'ISTREWY',
               'AURAPLE', 'RDATYTB', 'TEYEMRO']
    puzzle4 = 'roundandround'
    print(valid_puzzle(puzzle1))
    print(valid_puzzle(puzzle2))
    print(valid_puzzle(puzzle3))
    print(valid_puzzle(puzzle4))

    # sample test for task 1.2
    data1 = [2, 1, 2, 1]
    data2 = [5, 4, 5, 5, 4, 3]
    data3 = [1, 2, 1, 3, 'a', 'b', "a",  'c']
    print(similarity_grouping(data1))
    print(similarity_grouping(data2))
    print(similarity_grouping(data3))

    # sample test for task 1.3
    data4 = ("3, 13, 7, 9, 3, 3, 5, 7, 12, 13, 11, 13, 8, 7, 5, 14, 15, 3, 9,"
             "7, 5, 9, 14, 3, 8, 2, 5, 5, 8, 14, 11, 11, 12, 8, 5, 3, 3, 10,"
             "3, 10, 7, 7, 10, 10, 2, 7, 4, 8, 1, 5")
    data5 = ("British Gas, British Gas, Ovo, Igloo, Igloo, Octopus, Bulb,"
             "Shell, E.ON, Npower, British Gas, Octopus, Igloo, Npower, Igloo,"
             "Shell, Scottish Power, Bulb, EDF, Bulb, EDF, Bulb,"
             "Scottish Power, Octopus, Scottish Power, Octopus, Octopus, EDF,"
             "Ovo, Shell, Octopus, E.ON, British Gas, Bulb, Npower, Shell,"
             "Scottish Power, Npower, Scottish Power, Npower")
    data6 = ("aac, ctt, gat, ccc, gcc, ctg, gtc, tcg, ccg, cca, ata, cca,"
             "tat, ata, cac, gcg, cca, gta, gtg, gac, taa, ata, gtc, aat, gct,"
             "gta, ggc, tgc, tca, ctt, tgt, ata, acc, tgc, gac, cgc, atc, cgt,"
             "tac, agg, ctt, cgc, cgc, tgg, gcg, tgg, taa, cta, aaa, tgc, cgt,"
             "tgc, gac, tta, aag, taa, act, cca, tac, agg, cgc, gtg, cca, gcg,"
             "gtt, gag, tca, aca, tct, gta, ata, ctt, gat, tcg, tcg, cac, cgt,"
             "tac, caa, aac, ctg, tgt, aag, ttc, ccc, tcc, ctc, cct, aga, gtt,"
             "tga, gaa, cct, ctc, tct, ggt, gcc, tct, ccc, agt, caa, gac, ccc,"
             "cgc")
    print(highest_count_items(data4))
    print(highest_count_items(data5))
    print(highest_count_items(data6))

    # sample test for task 1.4
    popList1 = ['00000', '00001', '00010', '00011', '00100']
    popList2 = ['aac', 'ctt', 'gat', 'ccc', 'gcc', 'ctg', 'gtc', 'tcg',
                'ccg', 'cca', 'ata']
    popList3 = ['aac', 'ctt', 'gat', 'ccc', 'gcc', 'ctg', 'gtc']
    charSet1 = ['0', '1']
    charSet2 = ['a', 'c', 't', 'g']
    charSet3 = ['a', 'c']
    charSet4 = '01'
    print(valid_char_in_string(popList1, charSet1))
    print(valid_char_in_string(popList2, charSet2))
    print(valid_char_in_string(popList3, charSet3))
    print(valid_char_in_string(popList1, charSet4))

    # sample test for task 1.5
    print(total_price(3))
    print(total_price(12))
    print(total_price(15))
    print(total_price(26))
