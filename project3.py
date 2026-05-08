import sys

def main():	
    if len(sys.argv) < 2:
        print("Usage: project3.py <command> [args}", file=sys.stderr)
        sys.exit(1)

    cmd = sys.argv[1]

    try:
        match cmd:
            case "create":
                if len(sys.argv) != 3:
                    raise RuntimeError("Usage: project3.py create <indexfile>")
                print("case create")
            case "insert":
                if len(sys.argv) != 5:
                    raise RuntimeError("Usage: project3.py insert <indexfile> <key> <value>")
                print("case insert")
            case "search":
                if len(sys.argv) != 4:
                    raise RuntimeError("Usage: project3.py search <indexfile> <key>")
                print("case search")
            case "load":
                if len(sys.argv) != 4:
                    raise RuntimeError("Usage: project3.py load <indexfile> <csvfile>")
                print("case load")
            case "print":
                if len(sys.argv) != 3:
                    raise RuntimeError("Usage: project3.py print <indexfile>")
                print("case print")
            case "extract":
                if len(sys.argv) != 4:
                    raise RuntimeError("Usage: project3.py extract <indexfile> <csvfile>")
                print("case create")
            case _:
                raise RuntimeError(f"Unknown command: {cmd}")
    except (RuntimeError, FileNotFoundError, FileExistsError, ValueError, IOError) as e:
        print(e, file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
	main()
