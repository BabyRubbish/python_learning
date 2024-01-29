from pathlib import Path

path = Path("alice.txt")
contents = path.read_text(encoding="Utf-8")
times = contents.lower().count("the")
print(times)
times = contents.lower().count("the ")
print(times)
times = contents.lower().count(" the ")
print(times)
