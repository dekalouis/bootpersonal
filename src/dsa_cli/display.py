from loader import Question

def show_question(question: Question) -> None:
    print(question.title)

    steps = question.steps

    # for step in steps:
    #     print(step)
    #     input('Next?')
    for i, step in enumerate(steps):
        print(f'{i+1}. {step}')
        input('->')
    print('Summary')
    print(f'Time Complexity: {question.time_complexity}')
    print(f'Space Complexity: {question.space_complexity}')


# show_question(Question(id='0', title='Contains Duplicates', category='Arrays & Hashing', difficulty='easy', steps=['Create an empty set/hashmap to store seen numbers', 'Loop the entire list of numbers', 'If the number exists in the hashmap, return True', 'Otherwise, add it to the hashmap'], time_complexity='O(n)', space_complexity='O(n)'),)
