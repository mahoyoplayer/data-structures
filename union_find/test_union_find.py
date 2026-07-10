import pytest

# Replace with name of your own implementation here
import key as union_find


@pytest.fixture(autouse=True)
def reset_union_find():
    """
    Reset the global parent and rank arrays before every test.
    """
    union_find.parent = list(range(6))
    union_find.rank = [0] * 6


def test_find_parent_initially_returns_itself():
    assert union_find.find_parent(0) == 0
    assert union_find.find_parent(3) == 3
    assert union_find.find_parent(5) == 5


def test_union_connects_two_nodes():
    union_find.union(0, 1)

    assert union_find.find_parent(0) == union_find.find_parent(1)


def test_union_different_groups():
    union_find.union(0, 1)

    assert union_find.find_parent(0) != union_find.find_parent(2)


def test_union_is_transitive():
    union_find.union(0, 1)
    union_find.union(1, 2)

    assert union_find.find_parent(0) == union_find.find_parent(1)
    assert union_find.find_parent(1) == union_find.find_parent(2)


def test_union_equal_ranks_increases_root_rank():
    union_find.union(0, 1)

    root = union_find.find_parent(0)

    assert union_find.rank[root] == 1


def test_union_lower_rank_goes_under_higher_rank():
    # This makes node 0's group have rank 1.
    union_find.union(0, 1)

    root_before = union_find.find_parent(0)
    assert union_find.rank[root_before] == 1

    # Node 2 has rank 0, so it should be attached to root_before.
    union_find.union(0, 2)

    assert union_find.find_parent(2) == root_before
    assert union_find.rank[root_before] == 1


def test_union_same_group_does_nothing():
    union_find.union(0, 1)

    parent_before = union_find.parent.copy()
    rank_before = union_find.rank.copy()

    union_find.union(0, 1)

    assert union_find.parent == parent_before
    assert union_find.rank == rank_before


def test_path_compression():
    # Manually construct:
    # 3 -> 2 -> 1 -> 0
    union_find.parent = [0, 0, 1, 2, 4, 5]

    assert union_find.find_parent(3) == 0

    # Path compression should make 3 point directly to 0.
    assert union_find.parent[3] == 0
    assert union_find.parent[2] == 0
    assert union_find.parent[1] == 0


@pytest.mark.parametrize(
    "x, y",
    [
        (0, 1),
        (2, 3),
        (4, 5),
    ],
)
def test_multiple_union_pairs(x, y):
    union_find.union(x, y)

    assert union_find.find_parent(x) == union_find.find_parent(y)