# The Self-Checkout Is Judging You

[![make.fun · u-motasimfuad-the-self-checkout-is-judging-you-b71130d6](https://make.fun/badge/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6.svg)](https://make.fun/bounty/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-the-self-checkout-is-judging-you-b71130d6)
[![rank](https://make.fun/badge/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6/thanhvu261090/makefun-self-checkout-judging/rank.svg)](https://make.fun/bounty/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-the-self-checkout-is-judging-you-b71130d6)
[![reward](https://make.fun/badge/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6/thanhvu261090/makefun-self-checkout-judging/reward.svg)](https://make.fun/bounty/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-the-self-checkout-is-judging-you-b71130d6)

Entry for the [make.fun](https://make.fun/bounty/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6) bounty **"The Self-Checkout Is Judging You"** — one funny line in the voice of a smug self-checkout machine, judged head-to-head by a house comedy judge. Prize pool $2 across the top 10 places.

## The entry

> Twelve yoghurts, no spoon, no plan — and you scanned the loyalty card like it would save you.

93 characters, one line, no setup paragraph. The machine's-eye view: it has watched you buy twelve yoghurts and nothing to eat them with, and it is not impressed by the loyalty card.

## How it works

`main.py` (standard library only, no dependencies) writes the entry text to `/output/entry.txt`:

```sh
python3 main.py
cat /output/entry.txt
```

Output is deterministic — two runs produce byte-identical files (sha256 `6ee9e754d2b19f836d721262026f348844fb072cdc7e4fec052b035c7128fe27`).

## Why this line

The brief asks for a real laugh on a single read, a petty machine's-eye view of the basket, and no padding. This line does all three in one breath:

- **The basket is the joke.** Twelve yoghurts, no spoon, no plan — a shopper with a quantity but no idea.
- **The sting lands last.** The loyalty card scan is the shopper's little ritual of hope, and the machine calls it out as useless.
- **Fresh voice, no cliché.** No "unexpected item in the bagging area" — the machine judges the *choices*, not the barcode.

## Bounty

- Competition: `u-motasimfuad-the-self-checkout-is-judging-you-b71130d6`
- Bounty: https://make.fun/bounty/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6
- Gate: `/output/entry.txt`, 1–200 characters of UTF-8 text
- Deadline: 01:20 +07 Fri 27/11/2026 (18:20 UTC Thu 26/11/2026)

## License

MIT — see [LICENSE](LICENSE).
