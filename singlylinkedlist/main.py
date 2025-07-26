from singlylinkedlist.linked_list import LinkedList

ll = LinkedList()

ll.insert_node(3)
ll.insert_node(5)
ll.insert_node(7)
ll.insert_node(10)

print(ll)

ll.insert_node(4)
ll.insert_node(8)
ll.insert_node(2)

print(ll)
print(ll.count_node())

print(f"does node : 4 exists ? : {ll.find_node(4)}")

print(f"delete the node 3 from the list: {ll.delete_node(3)}")
print(ll)
