# daily-dsa

A daily practice log of LeetCode-style DSA problems, each one reframed as a
scenario from a **real system** it's actually a building block of (or,
when no real match exists, a clearly-labeled illustrative example).
Every problem is solved in its own pull request, one per day.

## Why reframed?

Solving problems in the abstract is easy to forget. Reframing each one as
a scenario, ideally a real system the underlying data structure or
algorithm is an actual building block of, and otherwise a clearly-labeled
illustrative example, makes the pattern stick and builds intuition for
recognizing it later instead of just memorizing a solution.

## Repo structure

```
<topic-folder>/<problem-folder>/
├── README.md          # reframed problem statement (scenario, examples, constraints, follow-up)
├── solution.py         # function skeleton only — no solution logic, just `# your code here`
└── test_solution.py    # my own tests, written after I solve it (not pre-provided)
```

Example: [arrays-and-hashing/two-sum/](arrays-and-hashing/two-sum/)

Topic folders are grouped the way most DSA curricula group them
(`arrays-and-hashing`, `two-pointers`, `sliding-window`, `stack`, `trees`,
`heap`, `graphs`, `dynamic-programming`, etc.), created as needed.
Problem folders are named after the actual DSA problem (e.g. `two-sum`),
not the reframed scenario — the scenario name lives inside that problem's
`README.md`.

## Daily workflow

1. Pick the next problem, reframe it, and generate its `README.md` +
   `solution.py` skeleton under `<topic>/<problem>/`.
2. Create a branch, solve it in `solution.py`, and write my own
   `test_solution.py` against it.
3. Open a pull request for that single problem, merge it, done for the day.

No solutions or algorithm hints are pre-written — the skeleton only
defines the reframed function signature so the approach is derived from
scratch each time.
