"""Run this file with the Run button. Keep these checks unchanged."""
from contextlib import redirect_stdout
from io import StringIO
import sys

# Importing the program should not print its demo.
import_output = StringIO()
with redirect_stdout(import_output):
    from game_status import render_status
if import_output.getvalue():
    print("FAIL: importing game_status printed output. Keep the supplied demo guard.")
    sys.exit(1)

CASES = [
    ('ordinary report', ('Nova', 75, 18, 125, 119, [40, 50, 90]),
     'PLAYER: Nova\nHealth  [#######---] 75/100\nEnergy  [###-------] 18/60\nLevel:  Skilled\nTime:   2:05\nBest:   1:59\nRecent: total=180, best=90, 80+=1'),
    ('zero meters and zero score', ('Zero', 0, 0, 0, 0, [0]),
     'PLAYER: Zero\nHealth  [----------] 0/100\nEnergy  [----------] 0/60\nLevel:  Rookie\nTime:   0:00\nBest:   0:00\nRecent: total=0, best=0, 80+=0'),
    ('full meters and rank 250', ('Full', 100, 60, 59, 60, [100, 100, 50]),
     'PLAYER: Full\nHealth  [##########] 100/100\nEnergy  [##########] 60/60\nLevel:  Expert\nTime:   0:59\nBest:   1:00\nRecent: total=250, best=100, 80+=2'),
    ('negative meters and score boundary', ('Below', -1, -5, 60, 9, [79, 80, 81]),
     'PLAYER: Below\nHealth  [----------] 0/100\nEnergy  [----------] 0/60\nLevel:  Skilled\nTime:   1:00\nBest:   0:09\nRecent: total=240, best=81, 80+=2'),
    ('meters above maximum and rank 99', ('Above', 150, 90, 3600, 3601, [99]),
     'PLAYER: Above\nHealth  [##########] 100/100\nEnergy  [##########] 60/60\nLevel:  Rookie\nTime:   60:00\nBest:   60:01\nRecent: total=99, best=99, 80+=1'),
    ('rank exactly 100', ('One Hundred', 101, 61, 61, 600, [100]),
     'PLAYER: One Hundred\nHealth  [##########] 100/100\nEnergy  [##########] 60/60\nLevel:  Skilled\nTime:   1:01\nBest:   10:00\nRecent: total=100, best=100, 80+=1'),
    ('rank 249 and first filled cell', ('Almost', 10, 6, 600, 599, [80, 80, 89]),
     'PLAYER: Almost\nHealth  [#---------] 10/100\nEnergy  [#---------] 6/60\nLevel:  Skilled\nTime:   10:00\nBest:   9:59\nRecent: total=249, best=89, 80+=3'),
    ('rank 251 and partial bars', ('Expert', 99, 59, 3599, 86400, [100, 100, 51]),
     'PLAYER: Expert\nHealth  [#########-] 99/100\nEnergy  [#########-] 59/60\nLevel:  Expert\nTime:   59:59\nBest:   1440:00\nRecent: total=251, best=100, 80+=2'),
    ('floor partial cells', ('Fraction', 9, 5, 1, 10, [1, 2, 3]),
     'PLAYER: Fraction\nHealth  [----------] 9/100\nEnergy  [----------] 5/60\nLevel:  Rookie\nTime:   0:01\nBest:   0:10\nRecent: total=6, best=3, 80+=0'),
    ('single score exactly 80', ('Boundary', 20, 12, 10, 59, [80]),
     'PLAYER: Boundary\nHealth  [##--------] 20/100\nEnergy  [##--------] 12/60\nLevel:  Rookie\nTime:   0:10\nBest:   0:59\nRecent: total=80, best=80, 80+=1'),
    ('highest score first', ('First', 50, 30, 120, 121, [100, 0, 10]),
     'PLAYER: First\nHealth  [#####-----] 50/100\nEnergy  [#####-----] 30/60\nLevel:  Skilled\nTime:   2:00\nBest:   2:01\nRecent: total=110, best=100, 80+=1'),
    ('highest score last', ('Last', 50, 30, 121, 120, [0, 10, 100]),
     'PLAYER: Last\nHealth  [#####-----] 50/100\nEnergy  [#####-----] 30/60\nLevel:  Skilled\nTime:   2:01\nBest:   2:00\nRecent: total=110, best=100, 80+=1'),
    ('maximum supported score collection', ('Twenty', 100, 60, 86400, 0, [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]),
     'PLAYER: Twenty\nHealth  [##########] 100/100\nEnergy  [##########] 60/60\nLevel:  Expert\nTime:   1440:00\nBest:   0:00\nRecent: total=2000, best=100, 80+=20'),
    ('same value different meter scales', ('Scales', 59, 59, 9, 10, [80, 1, 80, 0]),
     'PLAYER: Scales\nHealth  [#####-----] 59/100\nEnergy  [#########-] 59/60\nLevel:  Skilled\nTime:   0:09\nBest:   0:10\nRecent: total=161, best=80, 80+=2'),
    ('repeat original after other calls', ('Nova', 75, 18, 125, 119, [40, 50, 90]),
     'PLAYER: Nova\nHealth  [#######---] 75/100\nEnergy  [###-------] 18/60\nLevel:  Skilled\nTime:   2:05\nBest:   1:59\nRecent: total=180, best=90, 80+=1'),
]

def check(label, arguments, expected):
    scores = list(arguments[-1])
    before = scores[:]
    output = StringIO()
    actual = None
    error = None
    try:
        with redirect_stdout(output):
            actual = render_status(*arguments[:-1], scores)
    except Exception as caught:
        error = type(caught).__name__ + ": " + str(caught)
    if error is None and actual == expected and scores == before and output.getvalue() == "":
        print("PASS: " + label)
        return True
    print("FAIL: " + label)
    print("Inputs: " + repr(arguments))
    print("EXPECTED REPORT:\n" + expected)
    print("ACTUAL REPORT:\n" + (actual if isinstance(actual, str) else repr(actual)))
    if isinstance(actual, str):
        print("Expected repr: " + repr(expected))
        print("Actual repr:   " + repr(actual))
    if error:
        print("ERROR: " + error)
    if scores != before:
        print("The function changed scores: " + repr(scores))
    if output.getvalue():
        print("Unexpected printed output: " + repr(output.getvalue()))
    return False


def main():
    passed = 0
    for label, arguments, expected in CASES:
        if check(label, arguments, expected):
            passed = passed + 1
    print(str(passed) + "/" + str(len(CASES)) + " cases passed.")
    print("Passing cases check behavior. Also check that your code actually reuses helpers.")
    return 0 if passed == len(CASES) else 1


if __name__ == "__main__":
    sys.exit(main())
