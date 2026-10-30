# Module 5 Laboratory: Stacks and Queues

## Files
- `lesson5_stacks_queues.py` — contains `ArrayStack`, `LinkedStack`, `ArrayQueue`, `LinkedQueue`, the menu-driven test driver, and both application exercises.
- `analysis.md` — answer to the analysis question.

## Requirements
Python 3. Run the program from a terminal:

```bash
python lesson5_stacks_queues.py
```

## Main menu
1. **Run stack/queue menu:** choose one of the four implementations, then push/pop/peek or enqueue/dequeue/peek-front. The structure state is shown after operations.
2. **Run application exercises:** checks whether parentheses, square brackets, and braces are balanced, then simulates a print queue with job IDs and page counts.
3. **Test underflow and overflow:** demonstrates empty removal and pushing/enqueuing into full fixed-capacity array structures.
4. **Exit:** closes the program.

Array implementations require a positive capacity. Linked-list implementations have no fixed capacity and are limited by available memory.
