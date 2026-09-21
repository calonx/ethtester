"""Utilities for formatting elapsed durations."""

from math import isfinite


def format_elapsed_time(seconds: float) -> str:
    """Return a concise, human-readable representation of an elapsed duration.

    Args:
        seconds: A non-negative duration in seconds.

    Examples:
        >>> format_elapsed_time(0.25)
        '0.25 seconds'
        >>> format_elapsed_time(3661.5)
        '1 hour, 1 minute, 1.5 seconds'
    """
    if not isinstance(seconds, (int, float)) or isinstance(seconds, bool):
        raise TypeError("seconds must be a number")
    if not isfinite(seconds) or seconds < 0:
        raise ValueError("seconds must be a finite, non-negative number")

    seconds = float(seconds)
    days, remainder = divmod(seconds, 86_400)
    hours, remainder = divmod(remainder, 3_600)
    minutes, remaining_seconds = divmod(remainder, 60)

    parts = []
    for value, singular, plural in (
        (int(days), "day", "days"),
        (int(hours), "hour", "hours"),
        (int(minutes), "minute", "minutes"),
    ):
        if value:
            parts.append(f"{value} {singular if value == 1 else plural}")

    # Always include seconds so zero and sub-minute durations remain meaningful.
    if remaining_seconds or not parts:
        value = f"{remaining_seconds:.9f}".rstrip("0").rstrip(".")
        parts.append(
            f"{value} {'second' if remaining_seconds == 1 else 'seconds'}"
        )

    return ", ".join(parts)


def format_time_ago(seconds: float) -> str:
    """Return an approximate elapsed duration using its largest whole unit.

    Args:
        seconds: A non-negative duration in seconds.

    Examples:
        >>> format_time_ago(30)
        '30 seconds ago'
        >>> format_time_ago(90)
        '1 minute ago'
    """
    if not isinstance(seconds, (int, float)) or isinstance(seconds, bool):
        raise TypeError("seconds must be a number")
    if not isfinite(seconds) or seconds < 0:
        raise ValueError("seconds must be a finite, non-negative number")

    for unit_seconds, singular in (
        (86_400, "day"),
        (3_600, "hour"),
        (60, "minute"),
        (1, "second"),
    ):
        count = int(seconds // unit_seconds)
        if count or unit_seconds == 1:
            unit = singular if count == 1 else f"{singular}s"
            return f"{count} {unit} ago"
