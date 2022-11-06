def menu(title: str, *options: str, length: int = 40) -> int:
    print(title)
    print("="*length)

    for i, v in enumerate(options):
        print(f"{i + 1} - {v}")

    print("="*length)

    while True:
        response = int(input("Your Option: "))

        if 0 < response < len(options):
            return response
