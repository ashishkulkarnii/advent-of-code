from collections import Counter

hands = []

with open("input.txt") as f:
    for line in f.readlines():
        nh, bid = line.strip(" \n").split()
        hands.append((nh, int(bid)))

fiveofkind = []
fourofkind = []
fullhouse = []
threeofkind = []
twopair = []
pair = []
highcard = []

for hand, bid in hands:
    hand = hand.replace("J", "1").replace("Q", "C").replace("K", "D").replace("A", "E").replace("T", "A")
    sorted_hand = "".join(sorted(list(hand), reverse=True))
    if "1" in hand:
        highest = 1
        for j in ["2", "3", "4", "5", "6", "7", "8", "9", "A", "C", "D", "E"]:
            nh = sorted_hand.replace("1", j)
            nh = "".join(sorted(list(nh), reverse=True))
            if nh[0] == nh[1] == nh[2] == nh[3] == nh[4]:
                highest = max(highest, 7)
                break
            elif nh[0] == nh[1] == nh[2] == nh[3] or nh[1] == nh[2] == nh[3] == nh[4]:
                highest = max(highest, 6)
            elif nh[0] == nh[1] == nh[2] and nh[3] == nh[4] or nh[0] == nh[1] and nh[2] == nh[3] == nh[4]:
                highest = max(highest, 5)
            elif nh[0] == nh[1] == nh[2] or nh[1] == nh[2] == nh[3] or nh[2] == nh[3] == nh[4]:
                highest = max(highest, 4)
            elif nh[0] == nh[1] and nh[2] == nh[3] or nh[0] == nh[1] and nh[3] == nh[4] or nh[1] == nh[2] and nh[3] == nh[4]:
                highest = max(highest, 3)
            elif nh[0] == nh[1] or nh[1] == nh[2] or nh[2] == nh[3] or nh[3] == nh[4]:
                highest = max(highest, 2)
            else:
                pass
        match highest:
            case 7:
                fiveofkind.append((hand, bid))
            case 6:
                fourofkind.append((hand, bid))
            case 5:
                fullhouse.append((hand, bid))
            case 4:
                threeofkind.append((hand, bid))
            case 3:
                twopair.append((hand, bid))
            case 2:
                pair.append((hand, bid))
            case _:
                highcard.append((hand, bid))
    else:
        if sorted_hand[0] == sorted_hand[1] == sorted_hand[2] == sorted_hand[3] == sorted_hand[4]:
            fiveofkind.append((hand, bid))
        elif sorted_hand[0] == sorted_hand[1] == sorted_hand[2] == sorted_hand[3] or sorted_hand[1] == sorted_hand[2] == sorted_hand[3] == sorted_hand[4]:
            fourofkind.append((hand, bid))
        elif sorted_hand[0] == sorted_hand[1] == sorted_hand[2] and sorted_hand[3] == sorted_hand[4] or sorted_hand[0] == sorted_hand[1] and sorted_hand[2] == sorted_hand[3] == sorted_hand[4]:
            fullhouse.append((hand, bid))
        elif sorted_hand[0] == sorted_hand[1] == sorted_hand[2] or sorted_hand[1] == sorted_hand[2] == sorted_hand[3] or sorted_hand[2] == sorted_hand[3] == sorted_hand[4]:
            threeofkind.append((hand, bid))
        elif sorted_hand[0] == sorted_hand[1] and sorted_hand[2] == sorted_hand[3] or sorted_hand[0] == sorted_hand[1] and sorted_hand[3] == sorted_hand[4] or sorted_hand[1] == sorted_hand[2] and sorted_hand[3] == sorted_hand[4]:
            twopair.append((hand, bid))
        elif sorted_hand[0] == sorted_hand[1] or sorted_hand[1] == sorted_hand[2] or sorted_hand[2] == sorted_hand[3] or sorted_hand[3] == sorted_hand[4]:
            pair.append((hand, bid))
        else:
            highcard.append((hand, bid))

fiveofkind.sort(key=lambda x: x[0], reverse=True)
fourofkind.sort(key=lambda x: x[0], reverse=True)
fullhouse.sort(key=lambda x: x[0], reverse=True)
threeofkind.sort(key=lambda x: x[0], reverse=True)
twopair.sort(key=lambda x: x[0], reverse=True)
pair.sort(key=lambda x: x[0], reverse=True)
highcard.sort(key=lambda x: x[0], reverse=True)

hands = fiveofkind + fourofkind + fullhouse + threeofkind + twopair + pair + highcard

rank = 0
res = 0

while hands:
    rank += 1
    res += hands.pop(-1)[1] * rank

print(res)
