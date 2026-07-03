from linked_list import LinkedList

if __name__ == "__main__":
    """
    Create a LinkedList instance and perform operations.
    """

    # Create a LinkedList
    linked_list = LinkedList()

    # Insert sample data
    linked_list.insert_at_end(10)
    linked_list.insert_at_end(20)
    linked_list.insert_at_end(30)
    linked_list.insert_at_end(40)
    linked_list.insert_at_end(50)

    # Display the list
    print("Original Linked List:")
    linked_list.display()

    # Recursive sum
    total = linked_list.recursive_sum()
    print(f"\nSum of all node values: {total}")

    # Recursive search
    target = 30
    found = linked_list.recursive_search(target)
    print(f"\nSearching for {target}: {'Found' if found else 'Not Found'}")

    # Reverse recursively
    linked_list.recursive_reverse()
    print("\nReversed Linked List:")
    linked_list.display()