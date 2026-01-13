#!/usr/bin/env python3
import hidden_4

if __name__ == "__main__":
    new_dict = sorted(hidden_4.__dict__.keys())
    for el in new_dict:
        if not el.startswith("__"):
            print(el)
