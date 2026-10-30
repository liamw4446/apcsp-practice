import pytest
import game

# Replace this template with at least three tests per game function:
# def test_describe_the_case():
#     assert game.your_function(chosen_input) == expected_result

# should be integers
def test_integer():
#return only 0, 1 or 2
    def test_random_move_only_012():
        for i in range (0, 10000, 1):
            result = game.random_move()
        assert result == 0 or result == 1 or result == 2
# should be evenly distributed on 0,1,2
def test_random_move_evenly_distributed():
    counts = [0,0,0]
    for i in range(0, 10000, 1):
        result = game.random.move()
        counts[result] += 1
    assert counts == pytest.approx([3333, 3333, 3333], rel=0.05)


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-q"]))
