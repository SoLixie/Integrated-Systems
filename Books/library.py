import xml.etree.ElementTree as ET
import os

FILENAME = "library.xml"

def load_or_create_xml(filename=FILENAME):
    if not os.path.exists(filename):
        root = ET.Element("library")
        tree = ET.ElementTree(root)
        tree.write(filename, encoding='utf-8', xml_declaration=True)
        print("[INFO] New XML file created.")
    else:
        print("[INFO] XML file loaded.")
    return ET.parse(filename)

def view_books(tree):
    root = tree.getroot()
    books = root.findall("book")
    if not books:
        print("[INFO] No books in the library.")
        return
    print("\nLibrary Books:")
    for book in books:
        print(f"  ID: {book.get('id')}")
        print(f"   Title : {book.find('title').text}")
        print(f"   Author: {book.find('author').text}")
        print(f"   Rating  : {book.find('rating').text}\n")

def add_book(tree):
    root = tree.getroot()
    book_id = input("Enter Book ID: ").strip()
    
    # Check for duplicate ID
    for book in root.findall("book"):
        if book.get("id") == book_id:
            print("[ERROR] Book ID already exists.")
            return

    title = input("Enter Book Title: ").strip()
    author = input("Enter Book Author: ").strip()
    rating = input("Enter Book Rating: ").strip()

    book = ET.SubElement(root, "book", id=book_id)
    ET.SubElement(book, "title").text = title
    ET.SubElement(book, "author").text = author
    ET.SubElement(book, "rating").text = rating

    tree.write(FILENAME, encoding='utf-8', xml_declaration=True)
    print("[SUCCESS] Book added.")

def delete_book(tree):
    root = tree.getroot()
    book_id = input("Enter Book ID to delete: ").strip()
    for book in root.findall("book"):
        if book.get("id") == book_id:
            root.remove(book)
            tree.write(FILENAME, encoding='utf-8', xml_declaration=True)
            print(f"[SUCCESS] Book ID {book_id} deleted.")
            return
    print(f"[ERROR] Book ID {book_id} not found.")

def main():
    tree = load_or_create_xml()
    
    while True:
        print("\nLibrary Manager")
        print("1. View all books")
        print("2. Add a new book")
        print("3. Delete a book")
        print("4. Exit")
        choice = input("Select an option (1-4): ").strip()

        if choice == '1':
            view_books(tree)
        elif choice == '2':
            add_book(tree)
        elif choice == '3':
            delete_book(tree)
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
        else:
            print("[ERROR] Invalid choice. Please enter 1-4.")

if __name__ == "__main__":
    main()
