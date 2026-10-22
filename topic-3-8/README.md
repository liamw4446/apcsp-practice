# Python files

Open the [program](game_status.py) and [test file](test_game_status.py).

Save `game_status.py` and `test_game_status.py` directly in `topic-3-8` in your course practice repository. Open the program and use Run, then open the test file and use Run.

**Keep the game reports working while replacing repeated code with reusable functions or static methods.**

## Start

Use your existing practice repository. Save these files beside Battery Check:

| Course | Folder | Program | Run the tests |
|---|---|---|---|
| AP CSP | `topic-3-8` | `game_status.py` | `test_game_status.py` |
| AP CSA | `topic-2-8` | `GameStatus.java` | `GameStatusTests.java` |

Open the program and use **Run** to see two player reports. Then open the test file and use **Run**. The original program should report **15/15 cases passed**.

If the files will not run, raise your hand and tell me what happened.

## Your work

1. Identify blocks of code that do the same kind of work. Mark what changes between them.
2. Choose a useful function name, its inputs, and its returned result.
3. Extract one block, then replace every matching block with a call.
4. Save and rerun the test file. Resolve the first failure before the next extraction.
5. Continue until the program is as clean as possible!

Choose your helper functions and how they fit together intentionally! Python helpers go above `render_status`. Java helpers are `static` methods inside `GameStatus`, outside all other methods.

Keep the supplied report function's name, parameter order, and returned text unchanged. Keep the tests unchanged. Pass the data helpers need as arguments, return their results, and use those results in the report. Do not replace the supplied algorithms with library shortcuts!

## Finished

- Shared helper functions replace both meter-bound blocks, both bar-building blocks, and both time-formatting blocks.
- Rank selection, total score, highest score, and counting scores at least 80 have been extracted into useful helpers.
- The helpers use their parameters, return results, and are actually called by the report.
- All 15 tests pass. The supplied score collection is unchanged, and the report function prints nothing.
- There is no duplicated or unused code.
- Save, commit, and push your program and its unchanged test file.

Passing tests establish the checked behavior. Your source must also show the refactoring.

## Report rules

The starter already implements these rules. Preserve them.

| Part | Rule |
|---|---|
| Health | Restrict the displayed value to 0 through 100. |
| Energy | Restrict the displayed value to 0 through 60. |
| Each bar | Ten cells inside brackets. Filled cells = whole-number part of `displayed value * 10 / maximum`. Use `#` for filled and `-` for empty. |
| Time and Best | Convert seconds to `minutes:seconds`; always show two digits for the seconds part. Minutes may exceed 59. |
| Recent scores | Calculate the total, highest score, and number of scores greater than or equal to 80. |
| Level | Total below 100: `Rookie`; 100 through 249: `Skilled`; 250 or more: `Expert`. |

The supplied inputs have these limits: names contain 1-20 printable ASCII characters with no line breaks; health and energy are whole numbers from -100 through 200; times are whole numbers from 0 through 86,400; scores contain 1-20 whole numbers from 0 through 100. You do not need to add input validation.

The report function returns exactly seven lines separated by `\n`, without a final newline. Preserve labels and spacing. The supplied demo prints the returned report.

For Nova, health 75, energy 18, elapsed 125 seconds, best 119 seconds, and scores `[40, 50, 90]`:

```text
PLAYER: Nova
Health  [#######---] 75/100
Energy  [###-------] 18/60
Level:  Skilled
Time:   2:05
Best:   1:59
Recent: total=180, best=90, 80+=1
```

## Support

Start with the two meter-bound blocks. The operation is the same; the value and maximum change. Trace one input below zero, one in range, and one above the maximum.

Possible signatures, if you need a starting point:

| Work | Python | Java |
|---|---|---|
| Bound a value | `clamp(value, minimum, maximum)` | `static int clamp(int value, int minimum, int maximum)` |
| Build a bar | `make_bar(current, maximum, width)` | `static String makeBar(int current, int maximum, int width)` |
| Format a duration | `format_time(seconds)` | `static String formatTime(int seconds)` |

For the bar helper, pass an already bounded current value and a positive maximum/width. A text-producing helper returns a string. It does not print it.

## Advance

In a separate demo file, reuse an unchanged bar helper function to add a third resource, such as a shield with maximum 40. Check empty, partial, and full values. Keep the tested report unchanged.

If ready, make a meter-line helper that calls your bounds and bar helpers, then use it for both Health and Energy. Rerun the original suite and make sure your tests work.

## Exit Ticket

**Save, commit, and push your code and unchanged test file.**

In your notebook or on paper:

1. Pick a helper used twice. What changes between its calls, and which parameters receive those changes?
2. Where exactly are you stopping? What is your first next extraction or repair?

Retain this with your notes.
