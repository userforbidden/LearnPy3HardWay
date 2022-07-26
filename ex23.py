import sys
script, input_encoding, error = sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt",encoding="utf-8")

main(languages, input_encoding, error)

'''

1. How modern computers store human languages for display and processing and how Python3 calls this strings.
2. How you must ”encode” and ”decode” Python’s strings into a type called bytes.
3. How to handle errors in your string and byte handling.
4. How to read code and find out what it means even if you’ve never seen it before.
'''
