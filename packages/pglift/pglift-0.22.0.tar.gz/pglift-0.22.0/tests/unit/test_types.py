import io

import yaml

from pglift.types import Manifest, StrEnum


class Point(Manifest):
    x: float
    y: float


def test_parse_yaml() -> None:
    stream = io.StringIO()
    yaml.dump({"x": 1.2, "y": 3.4}, stream)
    stream.seek(0)
    point = Point.parse_yaml(stream)
    assert point == Point(x=1.2, y=3.4)


def test_yaml() -> None:
    point = Point(x=0, y=1.2)
    s = point.yaml()
    assert s == "---\nx: 0.0\ny: 1.2\n"


def test_strenum() -> None:
    class Pets(StrEnum):
        cat = "cat"

    assert str(Pets.cat) == "cat"
