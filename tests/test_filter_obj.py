from filter_obj import __version__, filter_obj


def test_filters_by_value():
    result = filter_obj({"a": 1, "b": 2, "c": 3}, lambda k, v: v > 1)
    assert result == {"b": 2, "c": 3}


def test_filters_by_key():
    result = filter_obj({"keep": 1, "drop": 2}, lambda k, v: k == "keep")
    assert result == {"keep": 1}


def test_returns_new_dict():
    source = {"a": 1}
    result = filter_obj(source, lambda k, v: True)
    assert result == source
    assert result is not source


def test_version_is_exposed():
    assert __version__ == "0.1.0"
