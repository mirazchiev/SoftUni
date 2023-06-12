def race(times: list):
    total_time_left = 0
    total_time_right = 0
    winner = ""
    total_time_winner = 0
    for time_index_left in range(len(times) // 2):
        time = int(times[time_index_left])
        if time == 0:
            total_time_left *= 0.8
        else:
            total_time_left += time
    for time_index_right in range(-1, -(len(times) // 2) -1, -1):
        time = int(times[time_index_right])
        if time == 0:
            total_time_right *= 0.8
        else:
            total_time_right += time
    if total_time_left <= total_time_right:
        winner = "left"
        total_time_winner = total_time_left
    else:
        winner = "right"
        total_time_winner = total_time_right

    return f"The winner is {winner} with total time: {total_time_winner:.1f}"


user_input = list(input().split())
result = race(user_input)
print(result)
