'''## 3. <span title="A bit spicy" style="color: darkgreen ">🌶️</span>

Suppose we wanted to create a new type to represent hands in blackjack. One thing we might want to do with this type \
is overload the comparison operators like `>` and `<=` so that we could use them to check whether one hand beats another
. e.g. it'd be cool if we could do this:

```python
>>> hand1 = BlackjackHand(['K', 'A'])
>>> hand2 = BlackjackHand(['7', '10', 'A'])
>>> hand1 > hand2
True
```

Well, we're not going to do all that in this question (defining custom classes is a bit beyond the scope of these
lessons), but the code we're asking you to write in the function below is very similar to what we'd have to write
if we were defining our own `BlackjackHand` class. (We'd put it in the `__gt__` magic method to define our custom
behaviour for `>`.)

Fill in the body of the `blackjack_hand_greater_than` function according to the docstring.'''

def cal_num(hand):
    crads_dict = {
        'A': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'J': 10,
        'Q': 10,
        'K': 10
    }

    score = 0
    having_ace =False
    for h1 in hand:
        score += crads_dict[h1]

    for i in hand:
        if i == 'A':
            having_ace = True
            break
        else:
            continue

    if having_ace == True:
        if score + 10 <= 21:
            score = score+10
    return score


def blackjack_hand_greater_than(hand_1, hand_2):
    """
    Return True if hand_1 beats hand_2, and False otherwise.

    In order for hand_1 to beat hand_2 the following must be true:
    - The total of hand_1 must not exceed 21
    - The total of hand_1 must exceed the total of hand_2 OR hand_2's total must exceed 21

    Hands are represented as a list of cards. Each card is represented by a string.

    When adding up a hand's total, cards with numbers count for that many points. Face
    cards ('J', 'Q', and 'K') are worth 10 points. 'A' can count for 1 or 11.

    When determining a hand's total, you should try to count aces in the way that
    maximizes the hand's total without going over 21. e.g. the total of ['A', 'A', '9'] is 21,
    the total of ['A', 'A', '9', '3'] is 14.

    Examples:
    >>> blackjack_hand_greater_than(['K'], ['3', '4'])
    True
    >>> blackjack_hand_greater_than(['K'], ['10'])
    False
    >>> blackjack_hand_greater_than(['K', 'K', '2'], ['3'])
    False
    """

    h1_num = cal_num(hand_1)
    h2_num = cal_num(hand_2)
    if h1_num <= 21 and (h1_num > h2_num or h2_num > 21):
        return True
    else:
        return False

print(blackjack_hand_greater_than(['K','2','5'],['2','Q','K']))






