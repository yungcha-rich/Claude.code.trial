#!/usr/bin/env python3
import json
import sys
from pathlib import Path

TODO_FILE = Path(__file__).parent / "todos.json"


def load_todos():
    if TODO_FILE.exists():
        return json.loads(TODO_FILE.read_text())
    return []


def save_todos(todos):
    TODO_FILE.write_text(json.dumps(todos, ensure_ascii=False, indent=2))


def add(todos, text):
    todos.append({"text": text, "done": False})
    save_todos(todos)
    print(f"추가됨: {text}")


def done(todos, index):
    todos[index]["done"] = True
    save_todos(todos)
    print(f"완료 처리됨: {todos[index]['text']}")


def remove(todos, index):
    removed = todos.pop(index)
    save_todos(todos)
    print(f"삭제됨: {removed['text']}")


def list_todos(todos):
    if not todos:
        print("할 일이 없습니다.")
        return
    for i, todo in enumerate(todos):
        mark = "x" if todo["done"] else " "
        print(f"[{mark}] {i}: {todo['text']}")


def usage():
    print("사용법:")
    print("  python todo.py add <할 일>")
    print("  python todo.py done <번호>")
    print("  python todo.py remove <번호>")
    print("  python todo.py list")


def main():
    todos = load_todos()
    args = sys.argv[1:]

    if not args:
        usage()
        return

    command = args[0]

    if command == "add" and len(args) >= 2:
        add(todos, " ".join(args[1:]))
    elif command == "done" and len(args) == 2:
        done(todos, int(args[1]))
    elif command == "remove" and len(args) == 2:
        remove(todos, int(args[1]))
    elif command == "list":
        list_todos(todos)
    else:
        usage()


if __name__ == "__main__":
    main()
