#!/usr/bin/env python
import json, subprocess


def main():
    username = input("Enter Goodreads username : ")
    subprocess.run(['scrapy', 'crawl', 'shelves', '--nolog', '-a', f'username={username}'], capture_output=False)

    with open("shelves.json") as f:
        shelves = json.loads(f.read())

    if len(shelves) == 0:
        print(f"{username}'s profile not found or is private.")
        exit(0)

    print(f"You have {len(shelves)} shelves, Which shelf do you want to examine ?")

    for index, shelf in enumerate(shelves):
        print(f"[{index}] {shelf['name']} ({shelf['number']} books)")
    choice = input("Enter shelf number : ")

    if shelves[int(choice)]['number'] == 0:
        print(f"\"{shelves[int(choice)]['name']}\" shelf is empty!")
        exit(0)

    link = shelves[int(choice)]['link']
    subprocess.run(['scrapy', 'crawl', 'books', '--nolog', '-a', f'start_urls={link}'], capture_output=False)

    with open("books.json") as f:
        books = json.loads(f.read())

    for index, book in enumerate(books):
        print(f"{book['title']} ( By {book['author']} )  * * *  {book['link']}")

    subprocess.run(['rm', 'shelves.json', 'books.json'], capture_output=False)

if __name__ == "__main__":
    main()
