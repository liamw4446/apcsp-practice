def clamp(value, minimum, maximum):
    if value < minimum:
        return minimum
    if value > maximum:
        return maximum
    return value


def make_bar(current, maximum, width):
    filled = current * width // maximum
    bar = "["
    for position in range(width):
        if position < filled:
            bar = bar + "#"
        else:
            bar = bar + "-"
    return bar + "]"


def format_time(seconds):
    minutes = seconds // 60
    remainder = seconds % 60
    text = str(minutes) + ":"
    if remainder < 10:
        text = text + "0"
    return text + str(remainder)


def total_score(scores):
    total = 0
    for score in scores:
        total = total + score
    return total


def highest_score(scores):
    highest = scores[0]
    for score in scores:
        if score > highest:
            highest = score
    return highest


def count_at_least(scores, threshold):
    count = 0
    for score in scores:
        if score >= threshold:
            count = count + 1
    return count


def choose_level(total):
    if total < 100:
        return "Rookie"
    if total < 250:
        return "Skilled"
    return "Expert"


def meter_line(label, value, maximum):
    shown = clamp(value, 0, maximum)
    return label + make_bar(shown, maximum, 10) + " " + str(shown) + "/" + str(maximum)


def render_status(name, health, energy, elapsed_seconds, best_seconds, scores):
    # Keep this function's name, parameters, and returned report.
    total = total_score(scores)

    # Return one report. \n separates its lines; there is no final \n.
    report = "PLAYER: " + name
    report = report + "\n" + meter_line("Health  ", health, 100)
    report = report + "\n" + meter_line("Energy  ", energy, 60)
    report = report + "\nLevel:  " + choose_level(total)
    report = report + "\nTime:   " + format_time(elapsed_seconds)
    report = report + "\nBest:   " + format_time(best_seconds)
    report = report + "\nRecent: total=" + str(total)
    report = report + ", best=" + str(highest_score(scores))
    report = report + ", 80+=" + str(count_at_least(scores, 80))
    return report


if __name__ == "__main__":
    print(render_status("Nova", 75, 18, 125, 119, [40, 50, 90]))
    print()
    print(render_status("Orion", 110, -4, 61, 60, [80, 80, 90]))