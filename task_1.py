

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

  def insert_after(self, prev_node: Node, data):
    if prev_node is None:
      print("Попереднього вузла не існує.")
      return
    new_node = Node(data)
    new_node.next = prev_node.next
    prev_node.next = new_node

  def delete_node(self, key: int):
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

  def search_element(self, data: int) -> Node | None:
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

  def reverse_list(self):
      prev = None
      current = self.head
        
      while current is not None:
          next_node = current.next  
          current.next = prev       
          prev = current            
          current = next_node       
        
      self.head = prev
def merge_sort_linked_list(head):
    if head is None or head.next is None:
        return head
    
    middle = find_middle(head)
    next_to_middle = middle.next
    middle.next = None
    
    left_half = merge_sort_linked_list(head)
    right_half = merge_sort_linked_list(next_to_middle)
    
    sorted_list = merge_sorted_lists(left_half, right_half)
    
    return sorted_list

def find_middle(head):
    if head is None:
        return head
    
    slow = head
    fast = head
    
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
    
    return slow

def merge_sorted_lists(left, right):
    result = None
    
    if left is None:
        return right
    if right is None:
        return left
    
    if left.data <= right.data:
        result = left
        result.next = merge_sorted_lists(left.next, right)
    else:
        result = right
        result.next = merge_sorted_lists(left, right.next)
        
    return result

def merge_sorted_linked_lists(list1, list2):
    dummy = Node()
    current = dummy
    
    while list1 is not None and list2 is not None:
        if list1.data <= list2.data:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    if list1 is not None:
        current.next = list1
    elif list2 is not None:
        current.next = list2
    
    return dummy.next


llist = LinkedList()

# Вставляємо вузли в початок
llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)

# Вставляємо вузли в кінець
llist.insert_at_end(20)
llist.insert_at_end(25)

# Друк зв'язного списку
print("Зв'язний список:")
llist.print_list()

llist.reverse_list()
print('reverse list:')
llist.print_list()

# Створення та заповнення списків
list1 = LinkedList()
list1.insert_at_end(2)
list1.insert_at_end(5)
list1.insert_at_end(7)

list2 = LinkedList()
list2.insert_at_end(3)
list2.insert_at_end(6)
list2.insert_at_end(9)

# Сортування списків
sorted_list1 = merge_sort_linked_list(list1.head)
sorted_list2 = merge_sort_linked_list(list2.head)

# Об'єднання відсортованих списків
merged_list = merge_sorted_linked_lists(sorted_list1, sorted_list2)

# Друк результату
current = merged_list
while current:
    print(current.data, end=" ")
    current = current.next
