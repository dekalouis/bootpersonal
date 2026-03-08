from loader import Question
from rich import print
from rich.panel import Panel

def show_question(question: Question) -> None:
    print(Panel(question.title, title="Question"))

    steps = question.steps

    # for step in steps:
    #     print(step)
    #     input('Next?')
    for i, step in enumerate(steps):
        print(f'[bold green]{i+1}. {step}[/bold green]')
        print("[dim]-> Press Enter for next step...[/dim]", end="")
        input()
    
    summary = f"[bold cyan]Summary\nTime Complexity: {question.time_complexity}\nSpace Complexity: {question.space_complexity}[/bold cyan]"
    print(Panel(summary))


# show_question(Question(id='0', title='Contains Duplicates', category='Arrays & Hashing', difficulty='easy', steps=['Create an empty set/hashmap to store seen numbers', 'Loop the entire list of numbers', 'If the number exists in the hashmap, return True', 'Otherwise, add it to the hashmap'], time_complexity='O(n)', space_complexity='O(n)'),)
