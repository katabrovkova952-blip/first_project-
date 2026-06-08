def delete_html_tags(html_file, result_file="cleaned.txt"):
    with open(html_file, "r", encoding="utf-8") as file:
        html = file.read()
        new_txt = []
        res = False
        for txt in html:
            for char in txt:
                if char == "<":
                    res = True
                elif char == ">":
                    res = False
                elif not res:
                    new_txt.append(char)
    with open(result_file, "w", encoding="utf-8") as new_file:
        new_file.write("".join(new_txt))

delete_html_tags("draft.html")