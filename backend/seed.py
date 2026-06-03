from database import SessionLocal, engine
from models import Base, Topic, Lesson, QuizQuestion

Base.metadata.create_all(bind=engine)

db = SessionLocal()

# Clear out any old data
db.query(QuizQuestion).delete()
db.query(Lesson).delete()
db.query(Topic).delete()
db.commit()

# Create topics
arrays = Topic(name="Arrays", description="Learn how data is stored in order")
linked_lists = Topic(name="Linked Lists", description="Learn how data points to other data")
stacks = Topic(name="Stacks", description="Learn about last-in, first-out")
queues = Topic(name="Queues", description="Learn about first-in, first-out")
trees = Topic(name="Trees", description="Learn about hierarchical data")

db.add_all([arrays, linked_lists, stacks, queues, trees])
db.commit()

# Create lessons for Arrays
db.add(Lesson(
    title="What is an Array?",
    content="An array is a collection of items stored in a specific order. Think of it like a row of mailboxes - each one has a number (index) and holds something inside. In Python, we use lists which work like arrays.",
    example="fruits = ['apple', 'banana', 'cherry']\nprint(fruits[0])  # prints 'apple'",
    topic_id=arrays.id
))

db.add(Lesson(
    title="Accessing Array Elements",
    content="You access items by their index, which starts at 0. So the first item is index 0, the second is index 1, and so on.",
    example="numbers = [10, 20, 30]\nprint(numbers[1])  # prints 20",
    topic_id=arrays.id
))

# Create lessons for Linked Lists
db.add(Lesson(
    title="What is a Linked List?",
    content="A linked list is like a treasure hunt. Each item (node) holds some data AND a clue (pointer) to where the next item is. Unlike arrays, the items don't have to be next to each other in memory.",
    example="class Node:\n    def __init__(self, data):\n        self.data = data\n        self.next = None",
    topic_id=linked_lists.id
))

db.commit()

# Create quiz questions for Arrays
db.add(QuizQuestion(
    question="What index does an array start at?",
    options="0,1,2,10",
    answer="0",
    topic_id=arrays.id
))

db.add(QuizQuestion(
    question="How do you access the second item in this list: fruits = ['a', 'b', 'c']?",
    options="fruits[0],fruits[1],fruits[2],fruits.second",
    answer="fruits[1]",
    topic_id=arrays.id
))

# Create quiz questions for Linked Lists
db.add(QuizQuestion(
    question="What does each node in a linked list contain?",
    options="Just data,Data and a pointer to the next node,Only a pointer,An index number",
    answer="Data and a pointer to the next node",
    topic_id=linked_lists.id
))

db.commit()
db.close()

print("Database seeded successfully!")