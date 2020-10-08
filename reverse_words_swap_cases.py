def reverse_words_order_and_swap_cases(sentence):
    # Write your code here
    phrase = []
    words = sentence.split(' ')
    words2 = words[::-1]
    print(words2)

    for n in words2:
        for mm in n:
            if mm.islower():
                mm1 = mm.upper()
            else:
                mm1 = mm.lower()
            phrase.append(mm1)
        phrase.append(' ')

    phrase2 = ('').join(phrase)
    return phrase2


if __name__ == '__main__':
    print(reverse_words_order_and_swap_cases('DoGs RuNs'))
    print(reverse_words_order_and_swap_cases(
        input('Enter with a sentence --> ')))
