def challenge_02(path: str) -> int:
    with open(path) as file:
        contents = file.read()
        contents = contents.split("\n")

    all_elf_calories = []
    current_elf_calories = []
    for val in contents:
        if len(val) > 0:
            current_elf_calories.append(int(val))
        else:
            all_elf_calories.append(sum(current_elf_calories))
            current_elf_calories = []

    return max(all_elf_calories)


if __name__ == "__main__":
    print(challenge_02("random_coding_challenge/data/002_actual.txt"))
