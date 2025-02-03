def create_box(text: str, padding: int = 1) -> str:
    lines = text.split('\n')
    max_length = max(len(line) for line in lines)
    box_width = max_length + padding * 2 + 2

    top_border = '+' + '-' * (box_width - 2) + '+'
    empty_line = '|' + ' ' * (box_width - 2) + '|'

    box = [top_border]
    for _ in range(padding):
        box.append(empty_line)

    for line in lines:
        box.append('|' + ' ' * padding + line.center(max_length) + ' ' * padding + '|')

    for _ in range(padding):
        box.append(empty_line)
    box.append(top_border)

    return '\n'.join(box)

# Example usage
text = "Warren Ikin"
print(create_box(text, padding=2))
# Output: