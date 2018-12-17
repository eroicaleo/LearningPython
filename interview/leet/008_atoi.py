#!/usr/bin/env python

def myAtoi(str):

    STATE_WHITESPACE = 0
    STATE_SIGN = 1
    STATE_DIGIT = 2
    STATE_DONE = 3

    state = STATE_WHITESPACE
    ret = 0
    sign = 1
    for c in str:
        print(c)
        print('STATE: ', state)
        if state == STATE_WHITESPACE:
            if c == ' ':
                next_state = STATE_WHITESPACE
            elif c in '+-':
                if c == '+':
                    sign = 1
                else:
                    sign = -1
                next_state = STATE_SIGN
                print('Next state 1: ', next_state)
            elif c.isdigit():
                ret = ret * 10 + int(c)
                next_state = STATE_DIGIT
            else:                        
                next_state = STATE_DONE
        elif state == STATE_SIGN or state == STATE_DIGIT:
            if c.isdigit():
                ret = ret * 10 + int(c)
                next_state = STATE_DIGIT
            else:
                next_state = STATE_DONE

        print('Next state: ', next_state)
        if next_state == STATE_DONE:
            break
        else:
            state = next_state
        print('STATE end: ', state)

    ret = (ret if sign == 1 else -ret)
    if ret >= 2 ** 31:
        ret = 2 ** 31 - 1
    elif ret < -2 ** 31:
        ret = -2 ** 31

    return ret

# print(myAtoi('42'))
# print(myAtoi("   -42"))
# print(myAtoi("4193 with words"))
# print(myAtoi("words and 987"))
# print(myAtoi("-91283472332"))
print(myAtoi("+-2"))
