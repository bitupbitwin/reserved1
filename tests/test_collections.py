import pytest
from utils.collections import flatten, chunk, unique_ordered, frequencies


class TestFlatten:
    def test_single_level(self):
        assert flatten([1, 2, 3]) == [1, 2, 3]

    def test_nested(self):
        assert flatten([1, [2, 3], [4, [5, 6]]]) == [1, 2, 3, 4, 5, 6]

    def test_empty(self):
        assert flatten([]) == []


class TestChunk:
    def test_even_split(self):
        assert chunk([1, 2, 3, 4], 2) == [[1, 2], [3, 4]]

    def test_remainder(self):
        assert chunk([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]

    def test_size_larger_than_list(self):
        assert chunk([1, 2], 5) == [[1, 2]]

    def test_invalid_size(self):
        with pytest.raises(ValueError):
            chunk([1, 2], 0)


class TestUniqueOrdered:
    def test_basic_dedup(self):
        assert unique_ordered([1, 2, 1, 3, 2]) == [1, 2, 3]

    def test_preserves_order(self):
        assert unique_ordered([3, 1, 2, 1, 3]) == [3, 1, 2]

    def test_no_duplicates(self):
        assert unique_ordered([1, 2, 3]) == [1, 2, 3]

    def test_empty(self):
        assert unique_ordered([]) == []

    def test_strings(self):
        assert unique_ordered(["b", "a", "b", "c", "a"]) == ["b", "a", "c"]


class TestFrequencies:
    def test_basic(self):
        assert frequencies([1, 2, 1, 3, 2, 2]) == {1: 2, 2: 3, 3: 1}

    def test_empty(self):
        assert frequencies([]) == {}

    def test_strings(self):
        assert frequencies(["a", "b", "a"]) == {"a": 2, "b": 1}
