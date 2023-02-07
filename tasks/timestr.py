__all__ = (
    'seconds_to_str',
)


def seconds_to_str(seconds: int) -> str:
    """
    Функция должна вернуть текстовое представление времени
    20 -> 20s
    60 -> 01m00s
    65 -> 01m05s
    3700 -> 01h01m40s
    93600 -> 01d02h00m00s
    """
    times_format = [
        (86400, '{}d'),
        (3600, '{}h'),
        (60, '{}m'),
        (1, '{}s')
    ]
    time_matching_check = False
    result_str = ''
    if seconds == 0:
        return '00s'
    for value, text in times_format:
        if seconds >= value or time_matching_check:
            time_matching_check = True
            result_str += text.format(str(int(seconds / value)).zfill(2))
            seconds %= value
    return result_str




