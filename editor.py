def format_bold(text: str):
    return f"**{text}**"


def format_italic(text: str):
    return f"*{text}*"


def format_header(text: str, level: int = 1):
    return f"{'#' * level} {format_new_line(text)}"


def format_link(url: str, label: str = ""):
    return f"[{label}]({url})"


def format_inline_code(text: str):
    return f"`{text}`"


def format_list(text: str, counter: str):
    return f"{counter} {format_new_line(text)}"


def format_new_line(text: str = ""):
    return f"{text}\n"


formatters = {
    "plain": lambda text: text,
    "bold": format_bold,
    "italic": format_italic,
    "header": format_header,
    "link": format_link,
    "inline-code": format_inline_code,
    "ordered-list": format_list,
    "unordered-list": format_list,
    "new-line": format_new_line,
}

user_command = input("Choose a formatter: ")
final_text = ""

while user_command != "!done":
    if user_command == "!help":
        print("Available formatters: " + " ".join(formatters))
        print("Special commands: !help !done")
    else:
        try:
            if user_command == "":
                raise ValueError("Unknown formatting type or command")

            if user_command not in formatters:
                raise ValueError("Unknown formatting type or command")

            if user_command == "header":
                user_level = int(input("Level: "))

                while user_level < 1 or user_level > 6:
                    print("The level should be within the range of 1 to 6")
                    user_level = int(input("Level: "))

                user_text = input("Text: ")
                final_text += formatters[user_command](user_text, user_level)
            elif user_command == "ordered-list" or user_command == "unordered-list":
                user_rows = int(input("Number of rows: "))

                while user_rows < 1:
                    print("The number of rows should be greater than zero")
                    user_rows = int(input("Number of rows: "))

                for i in range(user_rows):
                    counter = f"{i + 1}." if user_command == "ordered-list" else "-"
                    final_text += formatters[user_command](input(f"Row #{i + 1}: "), counter)

            elif user_command == "link":
                user_label = input("Label: ")
                user_url = input("URL: ")
                final_text += formatters[user_command](user_url, user_label)
            elif user_command == "new-line":
                final_text += formatters[user_command]()
            else:
                user_text = input("Text: ")
                final_text += formatters[user_command](user_text)

            print(final_text)

        except ValueError:
            print("Unknown formatting type or command")

    user_command = input("Choose a formatter: ")

with open("output.md", "w") as file:
    file.write(final_text)
