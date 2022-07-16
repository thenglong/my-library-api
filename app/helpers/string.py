import re

from collections.abc import Mapping

UNDERSCORE_RE = re.compile(r"(?<=[^\-_\s])[\-_\s]+[^\-_\s]")


def to_camelcase(str_or_iter):
    if isinstance(str_or_iter, (list, Mapping)):
        return _process_keys(str_or_iter, to_camelcase)

    s = str(_is_none(str_or_iter))
    if s.isupper() or s.isnumeric():
        return str_or_iter

    if len(s) != 0 and not s[:2].isupper():
        s = s[0].lower() + s[1:]

    # For string "hello_world", match will contain
    #             the regex capture group for "_w".
    return UNDERSCORE_RE.sub(lambda m: m.group(0)[-1].upper(), s)


def _is_none(_in):
    return "" if _in is None else _in


def _process_keys(str_or_iter, fn):
    if isinstance(str_or_iter, list):
        return [_process_keys(k, fn) for k in str_or_iter]
    if isinstance(str_or_iter, Mapping):
        return {fn(k): _process_keys(v, fn) for k, v in str_or_iter.items()}
    return str_or_iter
