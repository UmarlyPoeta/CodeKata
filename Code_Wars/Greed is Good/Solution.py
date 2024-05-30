from collections import Counter
def score(dice):
    score=0
    check_dictionary = {i:dice.count(i) for i in range(1,7)}
    print(check_dictionary)
    if check_dictionary[1]>=3:
        score+=1000
        check_dictionary[1]=check_dictionary[1]-3
        
    if check_dictionary[6]>=3:
        score+=600
        
    if check_dictionary[5]>=3:
        score+=500
        check_dictionary[5]=check_dictionary[5]-3
        
    if check_dictionary[4]>=3:
        score+=400
        
    if check_dictionary[3]>=3:
        score+=300
        
    if check_dictionary[2]>=3:
        score+=200
        
    score+=(100*check_dictionary[1])
    score+=(50*check_dictionary[5])
    return score


    """
    Greed is a dice game played with five six-sided dice. Your mission, should you choose to accept it, is to score a throw according to these rules. You will always be given an array with five six-sided dice values.

 Three 1's => 1000 points
 Three 6's =>  600 points
 Three 5's =>  500 points
 Three 4's =>  400 points
 Three 3's =>  300 points
 Three 2's =>  200 points
 One   1   =>  100 points
 One   5   =>   50 point

A single die can only be counted once in each roll. For example, a given "5" can only count as part of a triplet (contributing to the 500 points) or as a single 50 points, but not both in the same roll.

Example scoring

 Throw       Score
 ---------   ------------------
 5 1 3 4 1   250:  50 (for the 5) + 2 * 100 (for the 1s)
 1 1 1 3 1   1100: 1000 (for three 1s) + 100 (for the other 1)
 2 4 4 5 4   450:  400 (for three 4s) + 50 (for the 5)

Note: your solution must not modify the input list.

    """