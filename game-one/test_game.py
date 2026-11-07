import game


def test_rock_beats_scissors():
    assert game.round_result(0, 2) == "win"

def test_scissors_loses_to_rock():
    assert game.round_result(2, 0) == "lose"

def test_paper_vs_paper_is_tie():
    assert game.round_result(1, 1) == "tie"

def test_paper_beats_rock():
    assert game.round_result(1, 0) == "win"


def test_win_gives_player_one_a_point():
    assert game.update_scores(0, 0, "win") == (1, 0)

def test_lose_gives_player_two_a_point():
    assert game.update_scores(2, 1, "lose") == (2, 2)

def test_tie_gives_no_points():
    assert game.update_scores(3, 3, "tie") == (3, 3)


def test_two_and_two_is_draw():
    assert game.match_winner(2, 2) == "Draw"

def test_player_one_wins():
    assert game.match_winner(3, 1) == "Player 1"

def test_player_two_wins():
    assert game.match_winner(0, 1) == "Player 2"

def test_zero_zero_is_draw():
    assert game.match_winner(0, 0) == "Draw"


def test_beat_last_starts_with_paper():
    assert game.beat_last_strategy(1, -1) == 1

def test_beat_last_after_rock_plays_paper():
    assert game.beat_last_strategy(2, 0) == 1

def test_beat_last_after_scissors_plays_rock():
    assert game.beat_last_strategy(3, 2) == 0


def test_rotate_round_one_is_rock():
    assert game.rotate_strategy(1, -1) == 0

def test_rotate_round_three_is_scissors():
    assert game.rotate_strategy(3, 0) == 2

def test_rotate_round_four_wraps_to_rock():
    assert game.rotate_strategy(4, 1) == 0


def test_computer_move_is_always_valid():
    for i in range(100):
        assert game.computer_move(1, -1) in [0, 1, 2]

def test_computer_move_can_make_all_three():
    moves = {game.computer_move(1, -1) for i in range(200)}
    assert moves == {0, 1, 2}

def test_computer_move_uses_randint(monkeypatch):
    monkeypatch.setattr(game.random, "randint", lambda a, b: 2)
    assert game.computer_move(1, -1) == 2


def test_human_move_reads_number(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda prompt: "1")
    assert game.human_move(1, -1) == 1

def test_human_move_asks_again_after_bad_input(monkeypatch):
    answers = iter(["hello", "5", "2"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(answers))
    assert game.human_move(1, -1) == 2

def test_human_move_rejects_negative(monkeypatch):
    answers = iter(["-1", "0"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(answers))
    assert game.human_move(1, -1) == 0


def test_choose_human():
    assert game.choose_player("1") == game.human_move

def test_choose_strategies():
    assert game.choose_player("2") == game.beat_last_strategy
    assert game.choose_player("3") == game.rotate_strategy

def test_choose_bad_option_is_none():
    assert game.choose_player("9") is None


def test_play_game_beat_last_vs_rotate():
    # By hand: P,P,S,R,P vs R,P,S,R,P -> win,tie,tie,tie,tie = 1-0
    assert game.play_game(game.beat_last_strategy, game.rotate_strategy) == (1, 0)

def test_play_game_all_ties_is_draw(capsys):
    always_rock = lambda round_number, previous: 0
    assert game.play_game(always_rock, always_rock) == (0, 0)
    assert "draw" in capsys.readouterr().out

def test_play_game_prints_five_rounds(capsys):
    game.play_game(game.rotate_strategy, game.computer_move)
    output = capsys.readouterr().out
    assert output.count("Round ") == 5


if __name__ == "__main__":
    import sys
    import pytest
    sys.exit(pytest.main([__file__]))