# https://leetcode.com/problems/design-browser-history/
# memory usage: 16.8 MB, time usage: 279 ms
class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = []
        self.history.append(homepage)
        self.curr = 0
        self.size = 1

    def visit(self, url: str) -> None:
        if self.curr != self.size - 1:
            self.history = self.history[:self.curr + 1]
            self.history.append(url)
            self.size = len(self.history)
            self.curr = self.size - 1
        else:
            self.history.append(url)
            self.size += 1
            self.curr += 1

    def back(self, steps: int) -> str:
        self.curr = self.curr - steps
        if self.curr < 0:
            self.curr = 0

        return self.history[self.curr]

    def forward(self, steps: int) -> str:
        self.curr = self.curr + steps
        if self.curr >= self.size:
            self.curr = self.size - 1

        return self.history[self.curr]


if __name__ == "__main__":
    obj = BrowserHistory("leet")
    obj.visit("google")
    obj.visit("face")
    obj.visit("youtube")
    obj.back(1)
    obj.back(1)
    obj.forward(1)
    obj.visit("linkedin")
    obj.forward(2)
    obj.back(2)
    obj.back(7)
