import time
import random

def create_christmas_tree():
    tree = [
        "       ^       ",
        "      ^^^      ",
        "     ^^^^^     ",
        "    ^^^^^^^    ",
        "   ^^^^^^^^^   ",
        "  ^^^^^^^^^^^  ",
        " ^^^^^^^^^^^^^ ",
        "^^^^^^^^^^^^^^^",
        "      |||      "
    ]
    return tree

def blink_lights(tree, iterations=10, blink_interval=1):
    for _ in range(iterations):
        for i in range(len(tree)):
            if i != len(tree) - 1:
                tree[i] = tree[i].replace("^", "*")
                tree[i + 1] = tree[i + 1].replace("^", "^")
                print("\n".join(tree))
                time.sleep(blink_interval)
        for i in range(len(tree)):
            tree[i] = tree[i].replace("*", "^")

if __name__ == "__main__":
    tree = create_christmas_tree()
    print("\n".join(tree))
    print("Blinking lights...\n")
    blink_lights(tree, iterations=10, blink_interval=0.5)
