class Book:
    def __init__(self,book_id,title,texts):
        self.book_id = book_id
        self.title = title
        self.texts = texts
    
    def __str__(self):
        return f"Book(ID: {self.book_id}, Title: '{self.title}')"

    def count_word(self,word):
        word = word.lower()
        words = []
        for w in self.texts.split():
            words.append(w.strip().lower()) 
        return words.count(word)

class Bookstore:
    def __init__(self):
        self.books = {}

    def add_book(self, book_id,title,texts):
        if book_id not in self.books:
            self.books[book_id] = Book(book_id,title,texts) 
            return f"{title} was Added to the bookstore"
        else:
            return "Already Book is present"
        
    def remove_book(self,book_id):
        if book_id not in self.books:
            return "Book not found"
        else:
            del self.books[book_id]
            return f"{book_id} deleted"
    
    def __str__(self):
        if not self.books:
            return "Store has no book"
        else:
            lines = []
            for book in self.books.values():
                lines.append(str(book))          # convert each Book to a string
            joined_lines = "\n".join(lines)      # combine with newline
            result = "Books in store:\n" + joined_lines
            return result

    def count_word_in_book(self,book_id,word,):
        if book_id not in self.books:
            return "book not found"
        else:
            return self.books[book_id].count_word(word)

long_text = """
Cracking the Coding Interview is a must-read book for anyone preparing for technical interviews. 
The book covers a wide range of topics including data structures, algorithms, system design, 
and behavioral questions. Coding interviews often test not only your problem-solving skills 
but also your ability to communicate effectively. Practicing coding problems regularly, 
especially on platforms like LeetCode and HackerRank, can improve your confidence.

System design interviews, on the other hand, assess your understanding of building scalable 
and reliable systems. Topics like load balancing, caching, database sharding, and 
CAP theorem are frequently discussed. System design is not just about technical knowledge, 
but also about trade-offs, constraints, and real-world application.

This book on coding is structured well with explanations, diagrams, and mock interviews. 
Interview preparation also involves good rest, understanding the company’s culture, 
and being ready to explain your thought process. Coding, system design, and communication 
are the pillars of interview success.

The word coding appears many times in this passage to test the word count. 
So does the word system. And of course, the word interview. Interview. INTERVIEW!
"""
store = Bookstore()
print(store.add_book(101,"'Cracking the coding interview'",long_text))
print(store.add_book(102,"'The Self thought book'","You can write whatever you like"))
print(store)

print("coding:", store.count_word_in_book(101, "coding"))         # Expect ~5
print("system:", store.count_word_in_book(101, "system"))         # Expect ~4
print("interview:", store.count_word_in_book(101, "interview"))   # Expect ~3
print("design:", store.count_word_in_book(101, "design"))         # Expect ~2
print("nonexistent:", store.count_word_in_book(101, "nonexistent"))  # Expect 0

store.remove_book(102)
print(store)