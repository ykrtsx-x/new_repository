import pytest
from string_utils import StringUtils


class TestStringUtils:

    @pytest.fixture
    def utils(self):
        return StringUtils()

    @pytest.mark.parametrize("input_str, expected", [
        ("skypro", "Skypro"),
        ("SKYPRO", "Skypro"),
        ("sKyPrO", "Skypro"),
        ("123abc", "123abc"),
        ("   skypro", "   skypro"),
        ("skypro   ", "Skypro   "),
        ("04 апреля 2023", "04 апреля 2023"),
    ])
    def test_capitalize_positive(self, utils, input_str, expected):
        assert utils.capitalize(input_str) == expected

    @pytest.mark.parametrize("input_str, expected", [
        ("", ""),
        (" ", " "),
        (None, ""),
    ])
    def test_capitalize_negative(self, utils, input_str, expected):
        if input_str is None:
            with pytest.raises(AttributeError):
                utils.capitalize(input_str)
        else:
            assert utils.capitalize(input_str) == expected

    @pytest.mark.parametrize("input_str, expected", [
        ("   skypro", "skypro"),
        ("skypro", "skypro"),
        ("   skypro   ", "skypro   "),
        ("\tskypro", "skypro"),
        ("", ""),
    ])
    def test_trim_positive(self, utils, input_str, expected):
        assert utils.trim(input_str) == expected

    @pytest.mark.parametrize("input_str", [
        " ",
        None,
    ])
    def test_trim_negative(self, utils, input_str):
        if input_str is None:
            with pytest.raises(AttributeError):
                utils.trim(input_str)
        else:
            assert utils.trim(input_str) == ""

    @pytest.mark.parametrize("input_str, delimiter, expected", [
        ("a,b,c,d", ",", ["a", "b", "c", "d"]),
        ("1:2:3", ":", ["1", "2", "3"]),
        ("", ",", []),
        ("a,b,c,", ",", ["a", "b", "c", ""]),
        (",a,b,c", ",", ["", "a", "b", "c"]),
        ("a b c", " ", ["a", "b", "c"]),
    ])
    def test_to_list_positive(self, utils, input_str, delimiter, expected):
        assert utils.to_list(input_str, delimiter) == expected

    @pytest.mark.parametrize("input_str, delimiter, expected", [
        (None, ",", []),
        ("abc", "", ["a", "b", "c"]),
    ])
    def test_to_list_negative(self, utils, input_str, delimiter, expected):
        if input_str is None:
            with pytest.raises(AttributeError):
                utils.to_list(input_str, delimiter)
        else:
            assert utils.to_list(input_str, delimiter) == expected

    @pytest.mark.parametrize("input_str, symbol, expected", [
        ("SkyPro", "S", True),
        ("SkyPro", "o", True),
        ("SkyPro", "k", True),
        ("SkyPro", "U", False),
        ("", "a", False),
        ("abc", "", False),
    ])
    def test_contains_positive(self, utils, input_str, symbol, expected):
        assert utils.contains(input_str, symbol) == expected

    @pytest.mark.parametrize("input_str, symbol", [
        (None, "a"),
        ("abc", None),
    ])
    def test_contains_negative(self, utils, input_str, symbol):
        with pytest.raises(AttributeError):
            utils.contains(input_str, symbol)

    @pytest.mark.parametrize("input_str, symbol, expected", [
        ("SkyPro", "k", "SyPro"),
        ("SkyPro", "Pro", "Sky"),
        ("SkyPro", "xyz", "SkyPro"),
        ("", "a", ""),
        ("abc", "", "abc"),
        ("aaa", "a", ""),
    ])
    def test_delete_symbol_positive(self, utils, input_str, symbol, expected):
        assert utils.delete_symbol(input_str, symbol) == expected

    @pytest.mark.parametrize("input_str, symbol", [
        (None, "a"),
        ("abc", None),
    ])
    def test_delete_symbol_negative(self, utils, input_str, symbol):
        with pytest.raises(AttributeError):
            utils.delete_symbol(input_str, symbol)

    @pytest.mark.parametrize("input_str, symbol, expected", [
        ("SkyPro", "S", True),
        ("SkyPro", "P", False),
        ("", "a", False),
        ("abc", "", False),
        ("abc", "", False),
        ("   abc", " ", True),
    ])
    def test_starts_with_positive(self, utils, input_str, symbol, expected):
        assert utils.starts_with(input_str, symbol) == expected

    @pytest.mark.parametrize("input_str, symbol", [
        (None, "a"),
        ("abc", None),
    ])
    def test_starts_with_negative(self, utils, input_str, symbol):

        with pytest.raises(AttributeError):
            utils.starts_with(input_str, symbol)

    @pytest.mark.parametrize("input_str, symbol, expected", [
        ("SkyPro", "o", True),
        ("SkyPro", "y", False),
        ("", "a", False),
        ("abc", "", False),
        ("abc123", "3", True),
        ("abc   ", " ", True),
    ])
    def test_end_with_positive(self, utils, input_str, symbol, expected):
        assert utils.end_with(input_str, symbol) == expected

    @pytest.mark.parametrize("input_str, symbol", [
        (None, "a"),
        ("abc", None),
    ])
    def test_end_with_negative(self, utils, input_str, symbol):
        with pytest.raises(AttributeError):
            utils.end_with(input_str, symbol)

    @pytest.mark.parametrize("input_str, expected", [
        ("", True),
        (" ", True),
        ("   ", True),
        ("\t", True),
        ("\n", True),
        ("SkyPro", False),
        ("  SkyPro  ", False),
        ("0", False),
    ])
    def test_is_empty_positive(self, utils, input_str, expected):
        assert utils.is_empty(input_str) == expected

    @pytest.mark.parametrize("input_str", [
        None,
    ])
    def test_is_empty_negative(self, utils, input_str):
        assert utils.is_empty(input_str) is True

    @pytest.mark.parametrize("input_list, joiner, expected", [
        ([1, 2, 3, 4], ", ", "1, 2, 3, 4"),
        (["Sky", "Pro"], ", ", "Sky, Pro"),
        (["Sky", "Pro"], "-", "Sky-Pro"),
        ([], ", ", ""),
        (["a"], ", ", "a"),
        ([1, "two", 3.5], " | ", "1 | two | 3.5"),
    ])
    def test_list_to_string_positive(
        self, utils, input_list, joiner, expected
    ):
        assert utils.list_to_string(input_list, joiner) == expected

    @pytest.mark.parametrize("input_list, joiner", [
        (None, ", "),
        ([1, 2, 3], None),
    ])
    def test_list_to_string_negative(self, utils, input_list, joiner):

        if input_list is None:

            with pytest.raises(AttributeError):
                utils.list_to_string(input_list, joiner)
        else:

            result = utils.list_to_string(input_list, joiner)
            assert result == "1, 2, 3"
