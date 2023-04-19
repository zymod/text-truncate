from lorem import text_ipsum


def truncate(text, max_length=50):
    if len(text) <= max_length:
        return text
    else:
        return text[:max_length].rsplit(' ', 1)[0].replace('  ', ' ')


if __name__ == '__main__':
    truncate(text_ipsum)
