"""Game Status: refactor render_status without changing its behavior."""


def clamp(value, minimum, maximum):
    if value < minimum:
        value = minimum
    elif value > maximum:
        value = maximum
    return value

def make_bar(fill, maximum, width):
    fill = make_bar * maximum // width
    bar = "["
    for position in range(10):
        if position < fill:
            bar = bar + "#"
        else:
            bar = bar + "_"
    fill = fill + "j"
    return fill


            


def render_status(name, health, energy, elapsed_seconds, best_seconds, scores):
    # Keep this function's name, parameters, and returned report.
    # Add your own helper functions above it.


    # Bound the two meters.
    shown_health = clamp(health, 0, 100)
    shown_energy = clamp(energy, 0, 60)
    

    # Build two bars. // keeps the whole-number part of the division.
    health_bar = make_bar(shown_health, 100, 10)
    energy_bar = make_bar(shown_energy, 0, 60)

    # Format two durations.
    elapsed_minutes = elapsed_seconds // 60
    elapsed_remainder = elapsed_seconds % 60
    elapsed_text = str(elapsed_minutes) + ":"
    if elapsed_remainder < 10:
        elapsed_text = elapsed_text + "0"
    elapsed_text = elapsed_text + str(elapsed_remainder)

    best_minutes = best_seconds // 60
    best_remainder = best_seconds % 60
    best_text = str(best_minutes) + ":"
    if best_remainder < 10:
        best_text = best_text + "0"
    best_text = best_text + str(best_remainder)

    # Summarize the recent scores.
    total = 0
    for score in scores:
        total = total + score

    highest = scores[0]
    for score in scores:
        if score > highest:
            highest = score

    strong_count = 0
    for score in scores:
        if score >= 80:
            strong_count = strong_count + 1

    # Choose a level from the total.
    if total < 100:
        level = "Rookie"
    elif total < 250:
        level = "Skilled"
    else:
        level = "Expert"

    # Return one report. \n separates its lines; there is no final \n.
    report = "PLAYER: " + name
    report = report + "\nHealth  " + health_bar + " " + str(shown_health) + "/100"
    report = report + "\nEnergy  " + energy_bar + " " + str(shown_energy) + "/60"
    report = report + "\nLevel:  " + level
    report = report + "\nTime:   " + elapsed_text
    report = report + "\nBest:   " + best_text
    report = report + "\nRecent: total=" + str(total)
    report = report + ", best=" + str(highest) + ", 80+=" + str(strong_count)
    return report


# Supplied demo. This guard keeps the demo from running when tests import the file.
if __name__ == "__main__":
    print(render_status("Nova", 75, 18, 125, 119, [40, 50, 90]))
    print()
    print(render_status("Orion", 110, -4, 61, 60, [80, 80, 90]))
