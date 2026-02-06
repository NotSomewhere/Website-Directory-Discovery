import argparse
import os
import sys
import time
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen

DEFAULT_TIMEOUT = 6.0
DEFAULT_STATUS = {200, 204, 301, 302, 307, 308}


def normalize_base(target: str) -> str:
    target = target.strip()
    if not target:
        raise ValueError("target is empty")
    parsed = urlparse(target)
    if not parsed.scheme:
        target = "https://" + target
    if not target.endswith("/"):
        target += "/"
    return target


def iter_words(wordlist: Path):
    with wordlist.open("r", encoding="utf-8", errors="ignore") as fh:
        for line in fh:
            word = line.strip()
            if not word or word.startswith("#"):
                continue
            yield word


def check_url(url: str, timeout: float, user_agent: str):
    req = Request(url, method="GET")
    req.add_header("User-Agent", user_agent)
    try:
        with urlopen(req, timeout=timeout) as resp:
            return resp.status
    except HTTPError as e:
        return e.code
    except URLError:
        return None


def main(argv=None):
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    parser = argparse.ArgumentParser(
        prog="wdd",
        description="Simple website directory discovery",
    )
    parser.add_argument("target", help="Base target (e.g. google.com or https://example.com)")
    parser.add_argument("wordlist", help="Wordlist file (one path per line)")
    parser.add_argument("-o", "--output", help="Write found URLs to this file")
    parser.add_argument(
        "--status",
        help="Comma-separated list of status codes treated as found (default: 200,204,301,302,307,308)",
    )
    parser.add_argument("--timeout", type=float, default=DEFAULT_TIMEOUT)
    parser.add_argument("--delay", type=float, default=0.0, help="Delay between requests (seconds)")
    parser.add_argument("--user-agent", default="WDD/0.1")

    args = parser.parse_args(argv)

    try:
        base = normalize_base(args.target)
    except ValueError as e:
        print(f"error: {e}", file=sys.stderr)
        return 2

    wordlist = Path(args.wordlist)
    if not wordlist.exists():
        print(f"error: wordlist not found: {wordlist}", file=sys.stderr)
        return 2

    status_set = DEFAULT_STATUS
    if args.status:
        try:
            status_set = {int(s.strip()) for s in args.status.split(",") if s.strip()}
        except ValueError:
            print("error: --status must be a comma-separated list of integers", file=sys.stderr)
            return 2

    out_fh = None
    if args.output:
        out_fh = Path(args.output).open("w", encoding="utf-8")

    found_count = 0
    try:
        for word in iter_words(wordlist):
            url = urljoin(base, word.lstrip("/"))
            status = check_url(url, args.timeout, args.user_agent)
            if status in status_set:
                found_count += 1
                line = f"found: {url} ({status})"
                print(line)
                if out_fh:
                    out_fh.write(url + "\n")
            if args.delay:
                time.sleep(args.delay)
    finally:
        if out_fh:
            out_fh.close()

    return 0 if found_count > 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
