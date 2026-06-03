topics = [
    {
        "id": 1,
        "name": "Arrays",
        "description": "Learn how data is stored in order",
        "lessons": [
            {
                "id": 1,
                "title": "What is an Array?",
                "content": "An array is a collection of items stored in a specific order. Think of it like a row of mailboxes - each one has a number (index) and holds something inside. In Python, we use lists which work like arrays.",
                "example": "fruits = ['apple', 'banana', 'cherry']\nprint(fruits[0])  # prints 'apple'"
            },
            {
                "id": 2,
                "title": "Accessing Array Elements",
                "content": "You access items by their index, which starts at 0. So the first item is index 0, the second is index 1, and so on.",
                "example": "numbers = [10, 20, 30]\nprint(numbers[1])  # prints 20"
            }
        ]
    },
    {
        "id": 2,
        "name": "Linked Lists",
        "description": "Learn how data points to other data",
        "lessons": [
            {
                "id": 1,
                "title": "What is a Linked List?",
                "content": "A linked list is like a treasure hunt. Each item (node) holds some data AND a clue (pointer) to where the next item is. Unlike arrays, the items don't have to be next to each other in memory.",
                "example": "class Node:\n    def __init__(self, data):\n        self.data = data\n        self.next = None"
            }
        ]
    },
]



quizzes = {
    1: [
        {
            "id": 1,
            "question": "What index does an array start at?",
            "options": ["0", "1", "2", "10"],
            "answer": "0"
        },
        {
            "id": 2,
            "question": "How do you access the second item in this list: fruits = ['a', 'b', 'c']?",
            "options": ["fruits[0]", "fruits[1]", "fruits[2]", "fruits.second"],
            "answer": "fruits[1]"
        }
    ],
     2: [
        {
            "id": 1,
            "question": "What does each node in a linked list contain?",
            "options": ["Just data", "Data and a pointer to the next node", "Only a pointer", "An index number"],
            "answer": "Data and a pointer to the next node"
        }
    ]
}