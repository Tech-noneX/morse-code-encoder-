# Morse Decoder

A small Python practice project that converts plain text into Morse code.

The current script reads text from the terminal, converts letters `A-Z` into Morse symbols, converts spaces into `/`, and prints the encoded message.

## Project Files

- `morse_decoder.py` - main text-to-Morse script
- `morse_test.py` - empty placeholder test file

## How To Run

From the project folder:

```bash
python morse_decoder.py
```

Example input:

```text
hello world
```

Example output:

```text
.... . .-.. .-.. --- / .-- --- .-. .-.. -.. /(hello world)
```

## Notes

- The script currently supports letters and spaces.
- Numbers, punctuation, and Morse-to-text decoding are not implemented yet.
