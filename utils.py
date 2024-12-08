import re
from typing import Callable


class Matrix(list):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return (
            "[\n"
            + "\n".join(
                [
                    "[\t" + ",\t".join(['"{}"'.format(col) for col in row]) + "]"
                    for row in self
                ]
            )
            + " ]"
        )


def read_lines_as_matrix(lines: list[str]) -> list[list[str]]:
    return Matrix([[c for c in line.strip()] for line in lines if line.strip()])


def format_lines_as_numbers(lines):
    # group lines into lists
    number_lines = [line.strip() for line in lines if line.strip()]
    return [[int(num) for num in line.split()] for line in number_lines]


def split_and_cast[T](
    seq: list[str], sep: str | None = None, cast: Callable[[str], T] = int
) -> list[T]:
    return [cast(item) for item in seq.split(sep=sep)]


def middle_of_list[T](seq: list[T]) -> T:
    middle = round((len(seq) - 1) / 2)

    return seq[middle]


class Scanner(object):
    def __init__(self, src):
        self.src = src
        self.offset = 0
        self._match_history = None

    def eos(self):
        return self.offset >= len(self.src)

    def eol(self):
        if self.eos():
            return True
        p = self.peek(2)
        if p == "\r\n" or p.startswith("\r"):
            return True

        if p.startswith("\n"):
            if self.offset == 0 or self.src[self.offset - 1] != "\r":
                return True
        return False

    def peek(self, length=1):
        return self.src[self.offset : self.offset + length]

    def get(self, length=1):
        s = self.peek(length)
        self.offset += len(s)
        return s

    def _check(
        self,
        pattern,
        flags,
        consume=False,
        search_func="match",
        consume_match=True,
    ):
        if self.src is None:
            raise Exception("Scanner called with no string set")

        # if the pattern is a string we need to compile it
        # if it's not a string we assume it's a compiled regular expression
        if isinstance(pattern, str):
            regex = re.compile(pattern, flags)
        else:
            regex = pattern

        try:
            func = getattr(regex, search_func)
        except AttributeError:
            raise ValueError(
                "Object passed as 'pattern' to scan/check/skip does not implement a {0} method".format(
                    search_func
                )
            )

        m = func(self.src, self.offset)

        substr = None
        substr_len = None
        match_pos = None

        if m:
            match_pos = self.offset
            substr = (
                "" if m.start(0) == match_pos else self.src[self.offset : m.start(0)]
            )
            if consume_match:
                substr += m.group(0)
            substr_len = len(substr)

        if consume and m:
            self.offset = match_pos + substr_len

        return substr

    def check(self, pattern, flags=0):
        return self._check(pattern, flags)

    def exists(self, pattern, flags=0):
        return (
            self._check(pattern, flags, consume=False, search_func="search") is not None
        )

    def scan_to(self, pattern, flags=0):
        return self._check(
            pattern, flags, consume=True, consume_match=False, search_func="search"
        )

    def scan_until(self, pattern, flags=0):
        return self._check(pattern, flags, consume=True, search_func="search")

    def scan(self, pattern, flags=0):
        return self._check(pattern, flags, consume=True)

    def _match(self, strict=True):
        if self._match_history:
            return self._match_history[-1]
        else:
            if strict:
                raise Exception("No matches recorded")
        return None

    def matched(self):
        return self._match()["matchinfo"] is not None

    def _matched_exception(self):
        if not self.matched():
            raise Exception("Cannot access match information: most recent match failed")

    def match(self):
        self._matched_exception()
        return self._match()["text"]

    def match_len(self):
        self._matched_exception()

        return self._match()["len"]

    def match_pos(self):
        self._matched_exception()
        return self._match()["index"]

    def _match_info(self, strict=True):
        m = self._match()["matchinfo"]
        if m is None and strict:
            self._matched_exception()
        return m

    def match_info(self):
        return self._match_info(True)

    def skip(self, pattern, flags=0):
        m = self._check(pattern, flags, consume=True)
        return None if m is None else len(m)

    def skip_whitespace(self, n=None, multiline=True):
        chars = r"\s" if multiline else "[\b\f\t ]"
        chars += "+" if n is None else "{{,{0}}}".format(n)
        skipped = self.skip(chars)
        return 0 if skipped is None else skipped

    def rest(self):
        return self.src[self.offset :]


def bundles(inp):
    """
    Generator to turn input array from file with multi-line sequences divided by
    blank lines into something you can loop over.
    e.g.
    ```
    input = [i.strip() for i in open("input.txt","r").readlines()]

    max([sum(map(int, line)) for line in bundles(inp)])
    ```
    """
    r = []
    for line in inp:
        if line == "":
            yield r
            r = []
        else:
            r.append(line)
    yield (r)
