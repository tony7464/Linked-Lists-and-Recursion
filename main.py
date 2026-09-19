from linked_list import LinkedList

if __name__ == "__main__":
    """
    Drive the linked list: insert sample IDs, then sum, search, and reverse.
    """

    roster = LinkedList()

    # Insert employee IDs. Front inserts prepend, so the final order
    # after these three front inserts plus one end insert is:
    # 103 -> 102 -> 101 -> 104 -> None
    roster.insert_at_front(101)
    roster.insert_at_front(102)
    roster.insert_at_front(103)
    roster.insert_at_end(104)

    print("Initial roster:")
    roster.display()

    total = roster.recursive_sum()
    print(f"Sum of all IDs: {total}")

    found_existing = roster.recursive_search(102)
    found_missing = roster.recursive_search(999)
    print(f"Search for 102: {found_existing}")
    print(f"Search for 999: {found_missing}")

    roster.recursive_reverse()
    print("Reversed roster:")
    roster.display()
