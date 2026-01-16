#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    new_dict = sorted(hidden_4.__dict__.keys())
    for words in new_dict:
        if not words.startswith("__"):
            print(words)
