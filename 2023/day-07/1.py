hands = []

with open("input.txt") as f:
    for line in f.readlines():
        hand, bid = line.strip(" \n").split()
        hands.append((hand, int(bid)))

fiveofkind = []
fourofkind = []
fullhouse = []
threeofkind = []
twopair = []
pair = []
highcard = []

for hand, bid in hands:
    og_hand = hand.replace("J", "B").replace("Q", "C").replace("K", "D").replace("A", "E").replace("T", "A")
    hand = "".join(sorted(list(og_hand), reverse=True))
    if hand[0] == hand[1] == hand[2] == hand[3] == hand[4]:
        fiveofkind.append((og_hand, bid))
    elif hand[0] == hand[1] == hand[2] == hand[3] or hand[1] == hand[2] == hand[3] == hand[4]:
        fourofkind.append((og_hand, bid))
    elif hand[0] == hand[1] == hand[2] and hand[3] == hand[4] or hand[0] == hand[1] and hand[2] == hand[3] == hand[4]:
        fullhouse.append((og_hand, bid))
    elif hand[0] == hand[1] == hand[2] or hand[1] == hand[2] == hand[3] or hand[2] == hand[3] == hand[4]:
        threeofkind.append((og_hand, bid))
    elif hand[0] == hand[1] and hand[2] == hand[3] or hand[0] == hand[1] and hand[3] == hand[4] or hand[1] == hand[2] and hand[3] == hand[4]:
        twopair.append((og_hand, bid))
    elif hand[0] == hand[1] or hand[1] == hand[2] or hand[2] == hand[3] or hand[3] == hand[4]:
        pair.append((og_hand, bid))
    else:
        highcard.append((og_hand, bid))

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
