

def left_justify(words, width):
    """Given an iterable of words, return a string consisting of the words
    left-justified in a line of the given width.

    >>> left_justify(["hello", "world"], 16)
    'hello world     '

    """
    return ' '.join(words).ljust(width)


def justify(text, width):

    words = text.split() # List of total words.
    line = []  # List of words in current line.
    col = 0  # Starting column of next word added to line.
    for word in words:
        if line and col + len(word) > width:
            # caso en que hay una sola palabra en la linea.
            if len(line) == 1:
                yield left_justify(line, width)
            else:
                # After n + 1 spaces are placed between each pair of
                # words, there are r spaces left over; these result in
                # wider spaces at the left.
                n, r = divmod(width - col + 1, len(line) - 1)
                narrow = ' ' * (n + 1)
                if r == 0:
                    yield narrow.join(line)
                else:
                    wide = ' ' * (n + 2)
                    yield wide.join(line[:r] + [narrow.join(line[r:])])
            line, col = [], 0
        line.append(word)
        col += len(word) + 1
    if line:
        yield left_justify(line, width)


def main():
    text = input("ingrese el texto a justificar\n")
    width = int(input("ingrese el tamaño de fila\n"))
    output = list(justify(text, width))
    print("\n".join(output))


if __name__ == '__main__':
    main()