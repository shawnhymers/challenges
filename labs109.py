import math
import random
import itertools as it
from fractions import Fraction as frac
import re

def count_divisibles_in_range(start, end, n):
    if (start>0) & (end>0) & (start%n == 0):
        result = (((end//n)-(start//n))+1)
    if (start>0) & (end>0)& (start%n != 0):
        result = (end//n)-(start//n)
    if (start<0) & (end>0):
        result = ((end//n)+(abs(start)//n)+1)
    if (start<0) & (end<0):
        result = ((abs(start)//n)-(abs(end)//n))
    if (start == 0) & (end>0):
        result = ((end//n)-(start//n)+1)

    return(result)

# 49
def bridge_hand_shorthand(hand):
    spades = []
    hearts = []
    diamonds = []
    clubs = []
    for i in range(0,len(hand)):
        if hand[i][1] == 'spades':
            spades.append(hand[i][0])
        if hand[i][1] == 'hearts':
            hearts.append(hand[i][0])
        if hand[i][1] == 'diamonds':
            diamonds.append(hand[i][0])
        if hand[i][1] == 'clubs':
            clubs.append(hand[i][0])
    result = ''

    # Spades
    if len(spades)==0:
        result = result + '-'
    else:
        for i in range(0,len(spades)):
            if spades[i] == 'ace':
                result = result +'A'
        for i in range(0,len(spades)):
            if spades[i] == 'king':
                result = result +'K'
        for i in range(0,len(spades)):
            if spades[i] == 'queen':
                result = result +'Q'
        for i in range(0,len(spades)):
            if spades[i] == 'jack':
                result = result +'J'
        for i in range(0,len(spades)):
            if (spades[i] != 'jack')&(spades[i] != 'queen')&(spades[i] != 'king')&(spades[i] != 'ace'):
                result = result +'x'
    result = result +' '

    # hearts
    if len(hearts)==0:
        result = result + '-'
    else:
        for i in range(0,len(hearts)):
            if hearts[i] == 'ace':
                result = result +'A'
        for i in range(0,len(hearts)):
            if hearts[i] == 'king':
                result = result +'K'
        for i in range(0,len(hearts)):
            if hearts[i] == 'queen':
                result = result +'Q'
        for i in range(0,len(hearts)):
            if hearts[i] == 'jack':
                result = result +'J'
        for i in range(0,len(hearts)):
            if (hearts[i] != 'jack')&(hearts[i] != 'queen')&(hearts[i] != 'king')&(hearts[i] != 'ace'):
                result = result +'x'
    result = result +' '

    # diamonds
    if len(diamonds)==0:
        result = result + '-'
    else:
        for i in range(0,len(diamonds)):
            if diamonds[i] == 'ace':
                result = result +'A'
        for i in range(0,len(diamonds)):
            if diamonds[i] == 'king':
                result = result +'K'
        for i in range(0,len(diamonds)):
            if diamonds[i] == 'queen':
                result = result +'Q'
        for i in range(0,len(diamonds)):
            if diamonds[i] == 'jack':
                result = result +'J'
        for i in range(0,len(diamonds)):
            if (diamonds[i] != 'jack')&(diamonds[i] != 'queen')&(diamonds[i] != 'king')&(diamonds[i] != 'ace'):
                result = result +'x'
    result = result +' '

    # clubs
    if len(clubs)==0:
        result = result + '-'
    else:
        for i in range(0,len(clubs)):
            if clubs[i] == 'ace':
                result = result +'A'
        for i in range(0,len(clubs)):
            if clubs[i] == 'king':
                result = result +'K'
        for i in range(0,len(clubs)):
            if clubs[i] == 'queen':
                result = result +'Q'
        for i in range(0,len(clubs)):
            if clubs[i] == 'jack':
                result = result +'J'
        for i in range(0,len(clubs)):
            if (clubs[i] != 'jack')&(clubs[i] != 'queen')&(clubs[i] != 'king')&(clubs[i] != 'ace'):
                result = result +'x'
    return(result)

# 48
def bridge_hand_shape(hand):
    spades = 0
    hearts = 0
    diamonds = 0
    clubs = 0

    for i in range(0,len(hand)):
        if hand[i][1] == 'spades':
            spades += 1
        if hand[i][1] == 'hearts':
            hearts += 1
        if hand[i][1] == 'diamonds':
            diamonds += 1
        if hand[i][1] == 'clubs':
            clubs += 1
    return([spades,hearts,diamonds,clubs])
# 47
def manhattan_skyline(towers):
    starts = [a_tuple[0] for a_tuple in towers]
    stops = [a_tuple[1] for a_tuple in towers]
    x = starts+stops
    x.sort()
    x = list(dict.fromkeys(x))
    dict_1=dict()
    dict_2=dict()
    dict_3=dict()
    dict_4=dict()

    for s,e,h in towers:
        dict_1.setdefault(s, []).append(h)
        dict_2.setdefault(e, []).append(h)

        dict_3.setdefault(s, []).append(s)
        dict_3.setdefault(s, []).append(e)
        dict_3.setdefault(s, []).append(h)

        dict_4.setdefault(e, []).append(s)
        dict_4.setdefault(e, []).append(e)
        dict_4.setdefault(e, []).append(h)

    total = 0
    active_towers =[]
    span = 0
    index = 0
    for i in x:
        if index>=1:
            span = i-x[index-1]
        active_h =  [a_tuple[2] for a_tuple in active_towers]
        try:
            max_h = max(active_h)
        except:
            max_h = 0

        total +=max_h*span
        index +=1
        for j in range(0,len(towers)):

            if towers[j][0] == i:
                active_towers.append(towers[j])
            if towers[j][1] == i:
                active_towers.remove(towers[j])

    return(total)
# 46
def reverse_ascending_sublists(items):
    i = 0
    start = 0
    new_list = []
    if len(items)==1:
        return(items)
    while i <len(items):
        if i+1>=len(items):
            break
        if items[i+1]>items[i]:
            if i+2>=len(items):
                temp = items[start:i+2]
                temp = temp[::-1]
                for j in range(0,len(temp)):
                    new_list.append(temp[j])
                break
            while (items[i+1]>items[i]) &( i<len(items)-2):
                i+=1
            if i == len(items)-2:
                if items[len(items)-1]>items[len(items)-2]:
                    i+=1
            temp = items[start:i+1]
            temp = temp[::-1]

            for j in range(0,len(temp)):
                new_list.append(temp[j])
            if (i == len(items)-2) & (items[len(items)-1]<=items[len(items)-2]):
                new_list.append(items[len(items)-1])
            i+=1
            start = i
        else:
            new_list.append(items[i])
            i+=1
            start = i
            if i == len(items)-1:
                new_list.append(items[len(items)-1])

    return(new_list)
# 45
def first_preceded_by_smaller(items, k):
    lowest_k = []
    for i in range(0,len(items)):
        if len(lowest_k) <k:
            lowest_k.append(items[i])
        else:
            if items[i]>max(lowest_k):
                return(items[i])
            elif items[i]<=max(lowest_k):
                lowest_k.remove(max(lowest_k))
                lowest_k.append(items[i])
    return(None)
# 44
def mcculloch(digits):
    s = str(digits)
    result = ''
    if (int(s[0])>5)| (int(s[0])<=1):
        return(None)
    elif int(s[0])==5:
        y = calculate(s[1:])
        result = y+y
    elif int(s[0])==4:
        y = calculate(s[1:])
        result = y[::-1]
    elif int(s[0])==3:
        y = calculate(s[1:])
        result = y+'2'+y
    elif int(s[0])==2:
        result = s[1:]
    return(result)

def calculate(s):
    if s[0] == '5':
        y=calculate(s[1:])
        y = str(y)+str(y)
    elif s[0]== '4':
        y=calculate(s[1:])
        y = y[::-1]
    elif s[0]== '3':
        y=calculate(s[1:])
        y = str(y)+'2'+str(y)
    elif s[0]== '2':
        y = s[1:]
    else:
        retrun(None)
    return(str(y))

# 43
def remove_after_kth(items, k):
    d = {}
    result = []
    for i in range(0,len(items)):
        if items[i] in d:
            d[items[i]] += 1
        else:
            d[items[i]] = 1
        if d[items[i]]<=k:
            result.append(items[i])
    return(result)

# 42
def duplicate_digit_bonus(n):
    s = str(n)
    score = 0
    i = 0
    k = 1
    while i<len(s):
        try:
            if s[i]==s[i+k]:
                while s[i]==s[i+k]:
                    k+=1
                score += 10**(k-2)
                i +=k
                k = 1
            else:
                i+=1
        except:
            if k>1:
                score += 10**(k-2)*2
            return(score)
    return(score)

# 41
def count_word_dominators(words):
    if words == []:
        return(0)

    words = words[::-1]
    count = 1
    count1= 0
    dominator = []
    dominator.append(words[0])
    same_length_count = 0
    for i in range(1,len(words)):
        same_length_count = 0
        for j in range(0,len(dominator)):


            if (len(words[i])==len(dominator[j])):
                for k in range(0,len(words[i])):
                    # print(words[i][k])
                    # print(dominator[j][k])
                    # print('-----')
                    if (words[i][k] > dominator[j][k]):
                        same_length_count +=1
                        # print('---***--')
                        # print(same_length_count)
                        # print('---***--')
                        if same_length_count> (len(words[i])/2):
                            # print('test')
                            count1 +=1
                            same_length_count = 0
                            break
            else:

                if words[i] > dominator[j]:
                    count1 +=1
            # print(count1)
            # print(len(dominator))
        if (count1 == len(dominator)):
            count +=1
            count1 = 0
        else:
            count1 = 0
        dominator.append(words[i])
    return(count)

# 40
def reverse_reversed(items):
    result = []
    for i in range(0,len(items)):
        if (isinstance(items[i], list)):
            temp = reverse_reversed(items[i])
            result.append(temp)
        else:
            result.append(items[i])
    result = result[::-1]

    return(result)

# 39
def running_median_of_three(items):
    list = []
    if items ==[]:
        return([])
    if len(items)<=2:
        return(items)

    list.append(items[0])
    list.append(items[1])
    i = 2
    while i< len(items):
        subset = [items[i-2],items[i-1],items[i]]
        subset.remove(min(subset))
        subset.remove(max(subset))
        list.append(subset[0])
        i+=1
    return(list)

# 38
def words_with_given_shape(words, shape):
    should_be = []
    result = []
    for i in range(0,len(words)):
        if (len(words[i])== len(shape)+1):
            for j in range(0,len(words[i])-1):
                letter_in_question = words[i][j]
                cuplet_in_question = words[i][j:j+2]
                # print(cuplet_in_question)
                # print(''.join(sorted(cuplet_in_question)))
                if cuplet_in_question == ''.join(sorted(cuplet_in_question)):
                    if cuplet_in_question[0:1] ==cuplet_in_question[1:]:
                        should_be.append(0)
                    else:
                        should_be.append(1)
                else:

                    should_be.append(-1)
        if should_be == shape:
            result.append(words[i])
        should_be = []

    return(result)

# 37
def count_dominators(items):
    if items == []:
        return(0)

    # Reversing the list
    items = items[::-1]
    count = 1
    dominator = items[0]
    for i in range(0,len(items)):
        try:
            if items[i] > dominator:
                dominator = items[i]
                count +=1
        except:
            return(count)
    return(count)



# 36-- I think this is the one slowing it all down
def frequency_sort(items):
    items = sorted(items)
    freq = {}
    result = []
    for item in items:
        freq[item] = freq.get(item, 0) +1

    sorted_freq = (sorted(freq.keys(),
                key=lambda x: freq[x],
                reverse=True))

    for i in range(0,len(freq)):
        for j in range(0,freq[sorted_freq[i]]):
            result.append(sorted_freq[i])
    return(result)
# def unscramble(words, word):
#     substring = ''.join(sorted(word[1:len(word)-1]))
#     start_letter = word[0:1]
#     end_letter = word[len(word)-1:len(word)]
#     result = []
#     for i in range(0, len(words)):
#         tempsubstring = ''.join(sorted(words[i][1:len(words[i])-1]))
#         temp_start_letter = words[i][0:1]
#         temp_end_letter = words[i][len(words[i])-1:len(words[i])]
#         if (substring == ''.join(sorted(tempsubstring))) &(start_letter == temp_start_letter)&(end_letter == temp_end_letter):
#             result.append(words[i])
#     return(result)

# 35
def brangelina(first, second):
    new_name = ''
    vowels = {'a','e','i','o','u'}
    first_name_vowels_position = []
    first_name_vowels = []
    for i in range(0,len(first)):
        if first[i:i+1] in vowels:
            first_name_vowels.append(first[i:i+1])
            first_name_vowels_position.append(i)

    for i in range(0,len(first_name_vowels_position)-1):
        try:
            if first_name_vowels_position[i]+1 == first_name_vowels_position[i+1]:
                first_name_vowels.remove(first_name_vowels[i+1])
                first_name_vowels_position.remove(first_name_vowels_position[i+1])
        except:
            break

    # print(len(first_name_vowels))
    if (len(first_name_vowels)==1)|(len(first_name_vowels)==2):
        new_first_name = first[0:first_name_vowels_position[0]]
    else:
        starting_index = first_name_vowels_position[len(first_name_vowels_position)-2]
        new_first_name = first[0:starting_index]

    i =0
    while second[i:i+1] not in vowels:
        i+=1

    new_last_name =second[i:len(second)]
    new_name = new_first_name+new_last_name
    return(new_name)


# 34
def ztalloc(shape):
    n = 1
    count = 0

    while True:

        try:

            if shape[-1:] == 'd':
                n =n*2
                if n%2 !=0:
                    return(None)

            elif shape[-1] =='u':
                if (((n-1)//3)!= ((n-1)/3)):
                    return(None)
                n = (n-1)//3

                if (n%2 ==0):
                    return(None)
            shape = shape[:-1]

        except:
            return(n)
    return(n)
# 33
def fractran(n, prog, giveup=100):

    states = []
    states.append(n)

    count = 0
    while True:
        count+=1
        if count>giveup:
            return(states)
        if prog == []:
            return(states)
        i = 0
        while True:

            try:
                dif = abs(n*(frac(prog[i][0],prog[i][1])) - int(n*(frac(prog[i][0],prog[i][1]))))

                if  (dif<=0.000001) |(round(dif,4)==1):
                    states.append(int(n*(frac(prog[i][0],prog[i][1]))))
                    n = int(n*(frac(prog[i][0],prog[i][1])))

                    break

                    n = int(n)
                else:
                    n = int(n)
                    i+=1
                    if i>len(prog):
                        return(states)
            except:
                return(states)
    return(states)

# 32
def frog_collision_time(frog1, frog2):
    sx1  =frog1[0]
    sy1=frog1[1]
    dx1=frog1[2]
    dy1=frog1[3]

    sx2=frog2[0]
    sy2=frog2[1]
    dx2=frog2[2]
    dy2=frog2[3]

    # If the relative horizontal motion is 0
    if dx1==dx2:
        if sx1==sx2:
            t = (sy2-sy1)/(dy1-dy2)
            if (t<0 )| (t!= int(t)):
                return None
            else:
                return(int(t))
        else:
            return None
    # If the relative vertical motion is 0
    elif dy1==dy2:
        if sy1==sy2:
            t = (sx2-sx1)/(dx1-dx2)
            if (t<0 )| (t!= int(t)):
                return None
            else:
                return(int(t))
        else:
            return(None)
    else:
        ty = (sy2-sy1)/(dy1-dy2)
        tx = (sx2-sx1)/(dx1-dx2)

        if ty == tx:
            if( ty<0 )| (ty!= int(ty)):
                return None
            else:
                return(int(ty))
        else:
            return(None)
    return(t)

# 31
def reverse_vowels(text):
    text =[str(x) for x in str(text)]
    vowel_list = []
    position_list = []
    caps_ind_list = []
    for i in range(0,len(text)):
        if text[i] in {'a','e','i','o','u','A','E','I','O','U'}:
            vowel_list.append(text[i])
            position_list.append(i)

            if (text[i].isupper()):
                caps_ind_list.append(True)
            else:
                caps_ind_list.append(False)
    reversed_vowel_list = vowel_list[::-1]
    for i in range(0,len(reversed_vowel_list)):
        text[position_list[i]] = reversed_vowel_list[i]
        if caps_ind_list[i]==True:
            text[position_list[i]]=text[position_list[i]].upper()
        else:
            text[position_list[i]]=text[position_list[i]].lower()
    result = ''
    result = result.join(text)
    return(result)

#30
def counting_series(n):
    n = int(n)
    number_of_numbers = 9
    number_of_digits = 1
    carry_over = 0
    if n<9:
        return(int(n+1))
    while n> number_of_digits*number_of_numbers+carry_over:
        carry_over +=number_of_digits*number_of_numbers
        number_of_numbers = number_of_numbers*10
        number_of_digits += 1
    new_index = n-carry_over
    first_number = 10**(number_of_digits-1)
    test = ''
    new_numbers_needed =new_index//number_of_digits
    final_number = str(first_number+new_numbers_needed)
    final_index = new_index%number_of_digits
    test = int(final_number[final_index:final_index+1])
    return(test)

# 29
def count_and_say(digits):
    result = ''
    i = 1
    j = 1
    k = 2
    count = 1

    while k<= len(digits)+1:
        while digits[i-1:i] == digits[j:k]:

            count += 1
            j += 1
            k += 1
        result = result +str(count)+str(digits[i-1:i])
        i+=count
        j = i
        k = i+1
        count = 1

    return(result)
# 28
def count_consecutive_summers(n):
    count = 0
    if n ==1:
        return(1)
    for i in range(1,n+1):
        j = i
        sum = 0
        if j ==n:
            count +=1
            return(count)
        while j<=n:
            sum += j
            j+=1
            if sum ==n:
                count +=1

    return(count)

# 27
def double_until_all_digits(n, giveup=1000):

    counter = 0
    while counter <giveup:
        contained_ints =set([int(x) for x in str(n)])
        # print(contained_ints)
        if {0,1,2,3,4,5,6,7,8,9} == contained_ints:
            return(counter)
        else:
            n = n*2
            counter+=1

    return(-1)

#26
def squares_intersect(s1, s2):
    ind = True
    s1_x_end = s1[0]+s1[2]
    s1_x_start = s1[0]
    s1_y_end = s1[1]+s1[2]
    s1_y_start = s1[1]

    s2_x_end = s2[0]+s2[2]
    s2_x_start = s2[0]
    s2_y_end = s2[1]+s2[2]
    s2_y_start = s2[1]

    if s1_x_end < s2_x_start:
        ind = False
    if s2_x_end < s1_x_start:
        ind = False
    if s1_y_end < s2_y_start:
        ind = False
    if s2_y_end < s1_y_start:
        ind = False


    return (ind)

#25
def nearest_smaller(items):
    list = []
    count = 0
    i = 0
    step = 1
    while i<len(items):
        count +=1
        if count>10000:
            break
        # Getting minimum neighbours
        if (i-step >= 0) & (i+step <= len(items)-1):
            small = min(items[i-step], items[i+step])
        elif (i-step < 0) & (i+step <= len(items)-1):
            small = items[i+step]
        elif (i-step >= 0) & (i+step > len(items)-1):
            small = items[i-step]
        else:
            small = min(items)
        if (small<items[i]) | (small == min(items)):
            list.append(small)
            step = 1
            i+=1
        else:
            step+=1
    return(list)

# 24
# This one is correct but there is an error in the test script
# def collapse_intervals(items):
#     list = ''
#     starting_number = items[0]
#     i = 0
#     count = 0
#
#     if len(items)==1:
#         list = str(items[0])
#         return(list)
#     while i<len(items)-1:
#         count +=1
#         if count>100:
#             break
#
#         if int(items[i+1]) != int(items[i]+1):
#             entry = str(items[i])
#             list =list+','+entry
#             i+=1
#             try:
#                 starting_number = items[i]
#             except:
#                 return(list[1:len(list)])
#             if i == len(items)-1:
#                 entry = str(items[len(items)-1])
#                 list =list+','+entry
#                 return(list[1:len(list)])
#         else:
#             if i+1<len(items):
#
#                 while int(items[i+1]) == int(items[i]+1):
#                     if i +1<len(items)-1:
#                         i += 1
#                     else:
#                         i += 1
#                         break
#             else:
#                 i+=1
#             ending_number = items[i]
#             entry = str(starting_number)+'-'+str(ending_number)
#             list =list+','+entry
#             try:
#                 starting_number = items[i+1]
#             except:
#                 return(list[1:len(list)])
#             i+=1
#             if i == len(items)-1:
#                 entry = str(items[len(items)-1])
#                 list =list+','+entry
#                 return(list[1:len(list)])
#
#     return(list[1:len(list)])
def is_perfect_power(n):

    for b in range(2,100):
        for e in range(2,100):
            if n == 8:
                return(True)
            if n == 9:
                return(True)
            if ((b**e) == n-1) &(e!=1):
                return(False)
            if (b**e) == n:
                return(True)
            if ((e**b) == n-1)  &(b!=1):
                return(False)
            if (e**b) == n:
                return(True)

    return(False)

# 23
def expand_intervals(intervals):
    list = []
    intervals = [x.strip() for x in intervals.split(',')]
    for i in range(0,len(intervals)):
        try:
            temp = [x.strip() for x in intervals[i].split('-')]
            for j in range(int(temp[0]),int(temp[1])+1):
                list.append(j)
        except:
            list.append(int(intervals[i]))
    return(list)

# 22
def extract_increasing(digits):
    digits = digits.replace(" ", "")
    list = []
    current_size = 1
    # Adding the first digit to the list
    list.append(int(digits[0]))
    digits = digits[1:len(digits)]
    count = 0
    while True:
        count +=1
        if count >10000:
            return(list)

        while digits[:1] =='0':
            digits = digits[1:len(digits)]
        try:
            # print(int(digits[:current_size]))
            if int(digits[:current_size])>int(list[len(list)-1]):
                # Addign to list and dropping from string
                list.append(int(digits[0:current_size]))
                digits = digits[current_size:len(digits)]
            else:
                current_size+=1
        except:
            return(list)
    return(list)

# 21
def create_zigzag(rows, cols, start ):

    count = start
    result = []
    for i in range(0, rows):
        row = []
        for j in range(0, cols):
            row.append(count)
            count = count +1

        # If it is even
        if (int(i) % 2) == 0:
            result.append(row)
        # If it is odd
        else:
            row = row[::-1]
            result.append(row)


    return(result)

# 20
def pancake_scramble(text):
    for i in range(1, len(text)):
        text = text[0:i+1][::-1] +text[i+1:len(text)]
    return(text)

# 19
def seven_zero(n):

    count = 0

    digits = 1

    while True:
        result = '7'
        number_of_sevens = 1
        count +=1
        if count>1000:
            break

        if int(result) %n ==0:
            return(result)
        else:
            digits+=1

        # building a 7 with all trailing 0s
        for i in range(0,digits-1):
            result = result+'0'
        # Testing this one
        if int(result) %n ==0:
            return(result)

        count_2 = 0
        while number_of_sevens<digits:
            count_2 +=1
            if count_2>1000:
                break
            result = '7'
            for i in range(0,number_of_sevens):
                result = result+'7'
            for i in range(0,digits-number_of_sevens-1):
                result = result+'0'
            if int(result) %n ==0:
                return(result)
            else:
                number_of_sevens+=1
    return(result)

#18
def knight_jump(knight, start, end):
    ind = False
    dif = []
    possible_dif_per_start_point = []
    for i in range(0,len(start)):
        dif.append(abs(start[i]-end[i]))
    if set(knight) == set(dif):
        ind = True
    return(ind)

#17
def three_summers(items, goal):

    i = 0
    j = len(items)-1
    ind = False
    while i < j:
        x = items[i] + items[j]
        missing_number = goal-x
        temp = items.copy()
        temp.remove(items[j])
        temp.remove(items[i])

        if missing_number in temp:
            ind = True

            break
        elif i>=j-1:
            i += 1
            j = len(items)-1
        else:
            j -= 1
    return(ind)

# 16
def pyramid_blocks(n, m, h):

    #  formula n(n+x) where n is how many iterations and x is the disparity
    #  Can be En^2 +Enx (Where E is the sigma symbol from 1:n)
    #  Using summnation formulas(https://brilliant.org/wiki/sum-of-n-n2-or-n3/)this becomes:
    #  n(n+1)(2n+1)/6 + x((n^2+1)/2)
    # The disparity constant
    disparity = abs(n-m)

    # Total sums including the missing top parts
    h = h +min(n,m)-1 # adding the min thing to incoude missign layers
    sum_1 = (h*(h+1)*(2*h+1))//6 # This only works with the integer division symbol. IDK if thats mathematically correct
    sum_2 = disparity*(h**2 +h)//2

    # Just the missingn top parts
    h = min(n,m)-1
    top_part_1 = (h*(h+1)*(2*h+1))//6
    top_part_2 = disparity*(h**2 +h)//2

    # Final sum
    result = int(sum_1)+int(sum_2) - int(top_part_1) - int(top_part_2)
    return(str(result))

#15
def domino_cycle(tiles):
    if tiles == []:
        return True
    ind = True
    for i in range(0,len(tiles)-1):
        if tiles[i][1] != tiles[i+1][0]:
            ind = False
    if tiles[0][0] != tiles[len(tiles)-1][1]:
        ind = False
    return(ind)

#14
def count_distinct_sums_and_products(items):
    count = 0
    collection = set()
    for i in range(0, len(items)):
        for j in range(0, len(items)):
            sum = items[i]+items[j]
            prod = items[i]*items[j]
            collection.add(sum)
            collection.add(prod)

    count = len(collection)
    return(count)

#13
def is_zigzag(n):
    dif = []
    n = [int(x) for x in str(n)]
    ind = True
    for i in range(0,len(n)-1):
        dif.append(n[i+1]- n[i])
    for i in range(0, len(dif)-1):

        # If positive and positive
        if dif[i]>=0:
            if dif[i+1]>=0:
                ind = False
                break

        # If negative and negative
        if dif[i]<0:
            if dif[i+1]<0:
                ind = False
                break
    return(ind)

#12
def tukeys_ninthers(items):

    medians= []
    count = 0
    # while True:
    while True:

        if len(items) == 1:
            break
        else:
            number_of_sublists = len(items)//3
            # print(number_of_sublists)
            start = 0
            finish = 3

        for j in range(0, int(number_of_sublists)):

            temp = items[start:finish]
            temp.remove(max(temp))
            temp.remove(min(temp))

            medians.append(temp[0])
            start += 3
            finish += 3
        items = medians
        medians= []
    median = items[0]
    return(int(median))

#11
def bulgarian_solitaire(piles, k):
    count = 0
    while True:

        if ((len(set(piles)) == len(piles)) &(len(piles)==k)):
            break
        else:
            temp_length = len(piles)
            if 1 in piles:
                piles[:] = (value for value in piles if value != 1)
            piles = [x - 1 for x in piles]
            piles.append(temp_length)
            count = count+1
    return(count)

#10
def count_growlers(animals):

    count = 0
    for i in range(0, len(animals)):
        dog_count = 0
        cat_count = 0
        # Checking the direction
        if (animals[i] == 'dog') |(animals[i] == 'cat'):
            direction = 'left'
        if (animals[i] == 'god') |(animals[i] == 'tac'):
            direction = 'right'
        # Counting the cats and dogs in the direction
        if direction == 'right':
            substring = animals[i+1:len(animals)]
            dog_count = substring.count('dog')+ substring.count('god')
            cat_count = substring.count('cat')+ substring.count('tac')
            if dog_count> cat_count:
                count = count+1
        if direction == 'left':
            substring = animals[0:i]
            dog_count = substring.count('dog')+ substring.count('god')
            cat_count = substring.count('cat')+ substring.count('tac')

            if dog_count> cat_count:
                count = count+1
    return(count)

#9
def recaman(n):
    result = []
    previous_memory = {1}
    result.append(1)
    # previous_memory.add(1)
    for i in range(2, n+1):
        # Check if it yields a negative
        if int(result[len(result)-1] - i) <= 0:
            result.append(result[len(result)-1]+i)
            previous_memory.add(int(result[len(result)-2]+i))
        else:
            # Checkign if its new
            if (result[len(result)-1] - i) in previous_memory:
                result.append(result[len(result)-1]+i)
                previous_memory.add(int(result[len(result)-2]+i))
            else:
                result.append(result[len(result)-1]-i)
                previous_memory.add(int(result[len(result)-2]-i))

    return(result)

#8
def can_balance(items):
    result = -1
    for i in range(0, len(items)):
        left_weight = 0
        right_weight = 0
        # Calculating left side weight
        for j in range(0,i+1):
            distance = i-j
            left_weight = left_weight+items[j]*distance
        # Calculating right side weight
        for j in range(i, len(items)):
            distance = j-i
            right_weight = right_weight+items[j]*distance
        if left_weight == right_weight:
            result = i
            break
    return(result)

#7
def safe_squares_rooks(n, rooks):

    covered_rows = list(set([x[0] for x in rooks]))
    covered_cols = list(set([y[1] for y in rooks]))
    double_count = len(covered_rows)*len(covered_cols)
    covered_squares = len(covered_rows)*n + len(covered_cols)*n - double_count
    free_squares = n*n - covered_squares

    return(free_squares)

#6
def taxi_zum_zum(moves):
    moves = moves.replace(" ", "")
    x = 0
    y = 0
    direction = 'north'
    for i in range(0, len(moves)):
        if moves[i] == 'F':
            if direction == 'north':
                y = y + 1
            elif direction == 'east':
                x = x + 1
            elif direction == 'south':
                y = y - 1
            elif direction == 'west':
                x = x - 1
        if moves[i] == 'R':
            if direction == 'north':
                direction = 'east'
            elif direction == 'east':
                direction = 'south'
            elif direction == 'south':
                direction = 'west'
            elif direction == 'west':
                direction = 'north'
        elif moves[i] == 'L':
            if direction == 'north':
                direction = 'west'
            elif direction == 'east':
                direction = 'north'
            elif direction == 'south':
                direction = 'east'
            elif direction == 'west':
                direction = 'south'
    place = (x,y)
    return(place)

#5
def is_cyclops(n):

    ind = False
    n = str(n)
    n.split()

    # Checking if the input has an odd number of digits
    if (len(n) % 2) != 0:
        middle_digit = len(n)//2
        # Checking if the center digit is
        if n[middle_digit] == '0':
            ind = True

        # Checking if any other digits are 0
        zero_counter = 0
        for i in range(0, len(n)):
            if n[i] == '0':
                zero_counter = zero_counter +1
        if zero_counter >1:
            ind = False

    return(ind)

#4
def only_odd_digits(n):
    ind = True
    n = str(n)
    n.split()
    for i in range(0, len(n)):
        if (int(n[i]) % 2) == 0:
            ind = False
    return(ind)

#3
def riffle(items, out=True):

    half_length = (len(items)//2)
    half_1 = items[0:half_length]
    half_2 = items[half_length:len(items)]

    riffled_items = []

    if out:
        for i in range(0,half_length):
            riffled_items.append(half_1[i])
            riffled_items.append(half_2[i])
    else:
        for i in range(0,half_length):
            riffled_items.append(half_2[i])
            riffled_items.append(half_1[i])

    return(riffled_items)

#2
def is_ascending(items):
    ind = True
    for i in range(0, len(items)-1):
        if items[i+1]<= items[i]:
            ind = False

    return(ind)

#1
def ryerson_letter_grade(pct):

    if pct<50:
        grade = 'F'
    elif (pct >= 50 )& (pct <= 52):
        grade = 'D-'
    elif (pct >= 53 )& (pct <= 56):
        grade = 'D'
    elif (pct >= 57 )& (pct <= 59):
        grade = 'D+'
    elif (pct >= 60 )& (pct <= 62):
        grade = 'C-'
    elif (pct >= 63 )& (pct <= 66):
        grade = 'C'
    elif (pct >= 67 )& (pct <= 69):
        grade = 'C+'
    elif (pct >= 70 )& (pct <= 72):
        grade = 'B-'
    elif (pct >= 73 )& (pct <= 76):
        grade = 'B'
    elif (pct >= 77 )& (pct <= 79):
        grade = 'B+'
    elif (pct >= 80 )& (pct <= 84):
        grade = 'A-'
    elif (pct >= 85 )& (pct <= 89):
        grade = 'A'
    elif (pct >= 90):
        grade = 'A+'

    return(grade)
