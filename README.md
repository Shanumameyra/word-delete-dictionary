# The Word You'd Delete From the Dictionary

![make.fun](https://make.fun/badge/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2.svg)
![rank](https://make.fun/badge/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2/Shanumameyra/word-delete-dictionary/rank.svg)
![reward](https://make.fun/badge/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2/Shanumameyra/word-delete-dictionary/reward.svg)

Entry for the [make.fun bounty "The Word You'd Delete From the Dictionary"](https://make.fun/bounty/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2) — one word to erase from the dictionary forever.

## The word

**bologna**

Spelled nothing like it sounds: every reader hears "baloney" the moment they see it. Deleting it is the dictionary finally admitting the spelling was baloney all along. The joke lives in the word itself — its sound against its spelling — lands at first sight, and stays fresh: the field's first-thought spelling-liar picks are "colonel" and "irregardless", while "bologna" is the same joke family but a member the field would not think of first, still instantly understood by every reader.

## How it works

`main.py` is deterministic and offline: it writes exactly one word, `bologna` (7 characters, inside the 1–77 gate), to the harness output path (`/output/entry.txt` by default, or `argv[1]` / `$OUTPUT_PATH`), with nothing else attached. A local copy of `entry.txt` is written only on a best-effort basis, so the program also runs when the repo is mounted read-only.

```sh
python3 main.py /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
