class Solution:
    def capitalizeTitle(self, title: str) -> str:
        title = title.split(" ")
        ln_title = len(title)
        for i in range(ln_title):
            if len(title[i])<=2:
                title[i] = title[i].lower()
            else:
                title[i] = title[i].capitalize()
        return " ".join(title)     