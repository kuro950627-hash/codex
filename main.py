"""A minimal executable example for this repository."""


def greet(name: str = "Codex") -> str:
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greet())
