

def mustHaveLength(len):
    DFA = {}
    for i in range(len):
        DFA[i] = {}
        DFA[i]["*"] = i+1
    DFA["final"] = len
    return DFA


def mustMatch(regex):

    return


def generate(DFA, word = [], current_state = 0, colored = []):

    colored.append(current_state)

    if DFA["final"] == current_state:
        return word

    possible_states = DFA[current_state]


    for key in possible_states.keys():
        if not key in colored:
            new_word = word.copy()
            new_word.append(key)
            return generate(DFA, new_word, possible_states[key])


def linearize(regex):
    linear = []
    i = 0
    for letter in list(regex):
        if letter in ['+', '*', '(', ')', '?']:
            linear.append(letter)
        else:
            linear.append(letter + str(i))
            i+=1

    return linear


def P(linear):

    return

def D(linear):
    return

def F(linear):
    return

def emptyWord(linear):
    return


def glushkov(regex):
    linear = linearize(regex)
    print(linear)
    p = P(linear)
    d = D(linear)
    f = F(linear)


if __name__ == "__main__":
    #word = generate(mustHaveLength(4))
    regex = "aa*b"

    print(linearize(regex))