class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data):
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def sorted_merge(self, other):
        dummy = Node()
        tail = dummy

        p1 = self.head
        p2 = other.head

        while p1 and p2:
            if p1.data <= p2.data:
                tail.next = p1
                p1 = p1.next
            else:
                tail.next = p2
                p2 = p2.next
            tail = tail.next

        if p1:
            tail.next = p1
        elif p2:
            tail.next = p2

        self.head = dummy.next

    def merge_sort(self):
        if self.head is None or self.head.next is None:
            return self.head

        middle = self.get_middle(self.head)
        next_to_middle = middle.next

        middle.next = None

        left = LinkedList()
        right = LinkedList()

        left.head = self.head
        right.head = next_to_middle

        left.merge_sort()
        right.merge_sort()

        self.head = self.sorted_merge_lists(left.head, right.head)

    def get_middle(self, head):
        if head is None:
            return head

        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def sorted_merge_lists(self, left, right):
        if left is None:
            return right
        if right is None:
            return left

        if left.data <= right.data:
            result = left
            result.next = self.sorted_merge_lists(left.next, right)
        else:
            result = right
            result.next = self.sorted_merge_lists(left, right.next)

        return result


# Тестування функцій
llist = LinkedList()

# Вставляємо вузли в початок
llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)

# Вставляємо вузли в кінець
llist.insert_at_end(20)
llist.insert_at_end(25)

print("Зв'язний список:")
llist.print_list()

# Реверсування списку
llist.reverse()
print("\nРеверсований зв'язний список:")
llist.print_list()

# Сортування списку
llist.merge_sort()
print("\nВідсортований зв'язний список:")
llist.print_list()

# Створення другого списку та його сортування
llist2 = LinkedList()
llist2.insert_at_end(8)
llist2.insert_at_end(18)
llist2.insert_at_end(3)
llist2.merge_sort()

# Об'єднання двох відсортованих списків
llist.sorted_merge(llist2)
print("\nОб'єднаний відсортований зв'язний список:")
llist.print_list()