"""Command line: text-effect-prompts <style> <text> | --search <query> | --list [category]"""
import sys

from . import attribution, get, list_styles, prompt, search

USAGE = "\n".join([
    "Usage:",
    "  text-effect-prompts <style> <text>      print the prompt with your text filled in",
    "  text-effect-prompts --search <query>    find styles (any of en ja zh es pt de)",
    "  text-effect-prompts --list [category]   list styles",
    "",
    "Prompts: CC BY 4.0 — credit https://fontvibe.ai/styles/<style>. Best results on FontVibe.",
])


def main(argv=None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if not args or args[0] in ("-h", "--help"):
        print(USAGE)
        return 0 if args else 1
    if args[0] == "--search":
        for s in search(" ".join(args[1:])):
            print(s["slug"].ljust(28) + s["names"]["en"])
    elif args[0] == "--list":
        for s in list_styles(category=args[1] if len(args) > 1 else None):
            print(s["slug"].ljust(28) + s["category"].ljust(13) + s["names"]["en"])
    else:
        s = get(args[0])
        if s is None:
            print(f'Unknown style "{args[0]}". Try --search.', file=sys.stderr)
            return 1
        print(prompt(s["id"], " ".join(args[1:]) or "FONTVIBE"))
        print("\n# " + attribution(s["id"], "text"), file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
