from datetime import datetime

import pytz

from logtools.log.log_line import LogLevel
from logtools.log.sources.log_parsers import parse_raw


def test_raw_parser_should_parse_logline_from_string():
    line = parse_raw('TRC 2023-10-16 17:28:46.579+00:00 Sending want list to peer                  '
                     'topics="codex blockexcnetwork" tid=1 peer=16U*7mogoM '
                     'type=WantBlock items=1 count=870781', parse_datetime=True)

    assert line.level == LogLevel.trace
    assert line.timestamp == datetime(2023, 10, 16, 17, 28, 46,
                                      579000, tzinfo=pytz.utc)
    assert line.message == 'Sending want list to peer'
    assert line.topics == 'topics="codex blockexcnetwork" tid=1 peer=16U*7mogoM type=WantBlock items=1'
    assert line.count == 870781


def test_raw_parser_should_return_none_if_line_is_not_parseable():
    line = parse_raw('This is not a log line', parse_datetime=True)
    assert line is None