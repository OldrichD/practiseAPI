import requests


def get_books_info(book_title, language="en"):
    """
    Retrieves information about books from Google Books API.

    Args:
        book_title (str): The title of the book to search for.
        language (str, optional): The language for searching the book. Defaults to "en" (English).

    Returns:
        list: List of dictionaries containing book information.
    """
    url = "https://www.googleapis.com/books/v1/volumes"
    params = {"q": book_title, "langRestrict": language}

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        if data["totalItems"] == 0:
            print("No book found with this title.")
            return []
        else:
            return [item["volumeInfo"] for item in data["items"]]
    else:
        print(f"Error: {response.status_code}. Failed to retrieve book information.")
        return []


def display_books_info(books_info):
    """
    Displays information about books.

    Args:
        books_info (list): List of dictionaries containing book information.

    Returns:
        None
    """
    if not books_info:
        return

    for index, book_info in enumerate(books_info, start=1):
        title = book_info.get("title", "N/A")
        authors = ", ".join(book_info.get("authors", ["N/A"]))
        published_date = book_info.get("publishedDate", "N/A")
        description = book_info.get("description", "N/A")

        print(f"Book {index}:")
        print(f"  Title: {title}")
        print(f"  Author(s): {authors}")
        print(f"  Published Date: {published_date}")
        print(f"  Description: {description}")
        print()


if __name__ == "__main__":
    book_title = input("Enter the book title: ")
    language = input("Enter the language (leave empty for English): ") or "en"
    books_info = get_books_info(book_title, language)
    if books_info:
        display_books_info(books_info)
