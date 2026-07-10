import pytest

# Replace with name of your own implementation here
from key import Trie


@pytest.fixture
def trie() -> Trie:
    return Trie()


def test_new_trie_has_no_prefixes(trie: Trie) -> None:
    assert trie.check_prefix("a") is False
    assert trie.check_prefix("apple") is False


def test_insert_word(trie: Trie) -> None:
    trie.insert("apple")

    assert trie.check_prefix("a") is True
    assert trie.check_prefix("app") is True
    assert trie.check_prefix("apple") is True


def test_insert_multiple_words(trie: Trie) -> None:
    trie.insert("apple")
    trie.insert("application")
    trie.insert("banana")

    assert trie.check_prefix("app") is True
    assert trie.check_prefix("ban") is True
    assert trie.check_prefix("cat") is False


def test_prefix_must_start_at_beginning(trie: Trie) -> None:
    trie.insert("apple")

    assert trie.check_prefix("app") is True
    assert trie.check_prefix("ppl") is False


def test_delete_existing_word(trie: Trie) -> None:
    trie.insert("apple")

    assert trie.delete("apple") is True
    assert trie.check_prefix("apple") is False


def test_delete_missing_word(trie: Trie) -> None:
    trie.insert("apple")

    assert trie.delete("banana") is False
    assert trie.check_prefix("apple") is True


def test_delete_preserves_shared_prefix(trie: Trie) -> None:
    trie.insert("apple")
    trie.insert("application")

    assert trie.delete("apple") is True

    # "app" must still exist because "application" remains.
    assert trie.check_prefix("app") is True
    assert trie.check_prefix("application") is True


def test_delete_longer_word_preserves_shorter_word(trie: Trie) -> None:
    trie.insert("app")
    trie.insert("apple")

    assert trie.delete("apple") is True

    assert trie.check_prefix("app") is True
    assert trie.check_prefix("apple") is False


def test_delete_only_word_removes_unused_nodes(trie: Trie) -> None:
    trie.insert("banana")

    assert trie.delete("banana") is True

    assert trie.check_prefix("b") is False
    assert trie.check_prefix("ban") is False
    assert trie.check_prefix("banana") is False


def test_delete_same_word_twice(trie: Trie) -> None:
    trie.insert("apple")

    assert trie.delete("apple") is True
    assert trie.delete("apple") is False


def test_insert_duplicate_word(trie: Trie) -> None:
    trie.insert("apple")
    trie.insert("apple")

    assert trie.check_prefix("apple") is True
    assert trie.delete("apple") is True
    assert trie.check_prefix("apple") is False


@pytest.mark.parametrize(
    ("word", "prefix"),
    [
        ("apple", "a"),
        ("apple", "ap"),
        ("apple", "app"),
        ("banana", "ban"),
        ("computer", "comp"),
    ],
)
def test_valid_prefixes(trie: Trie, word: str, prefix: str) -> None:
    trie.insert(word)

    assert trie.check_prefix(prefix) is True