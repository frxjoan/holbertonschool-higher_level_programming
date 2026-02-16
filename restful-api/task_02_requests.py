#!/usr/bin/python3
import requests
import csv


def fetch_and_print_posts():
    link = "https://jsonplaceholder.typicode.com/posts"
    answer = requests.get(link)

    print(f"Status Code: {answer.status_code}")

    if answer.status_code == 200:
        posts = answer.json()

        for post in posts:
            print(post["title"])


def fetch_and_save_posts():
    link = "https://jsonplaceholder.typicode.com/posts"
    answer = requests.get(link)

    if answer.status_code == 200:
        posts = answer.json()

        structured_posts = [
            {
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            }
            for post in posts
        ]

        with open("posts.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(structured_posts)
