# Python Practice #

## Abstract ##

Algortithms and data structures in python3.

## Details ##

This is just some fun technical practice with algorithms and data structures in python3. The point is to not use built-in libraries. They're homebrew stacks, queues, heaps, sorts, trees, traversals, and graphs that will run without library extensions.

Of course, like every good computer science student, all of these endeavours are composed using test driven development. You are using TDD, yes? Of course you are. \*Wink \*Wink.

## Usage ##

If you're studying for your comp-sci courses, you should rely on the examples provided by your professors. That's what'll give you the grade.

If you're in a coding bootcamp program like Udacity or Treehouse, go away. I don't like you. Nobody does. You're disenfranchising a union-less market. Go to college or university and support real educators and institutions.

If you're teaching yourself and just need an extra perspective, I hope these help.

### Sorts ###

Types of Sorts
* BubbleSort
* InsertionSort
* SelectionSort
* ShellSort
* QuickSort
* MergeSort
* HeapSort
* RadixSort

```Python
bubble_sort(<list>)
insertion_sort(<list>)
selection_sort(<list>)
shell_sort(<list>)
quick_sort(<list>, 0, len(<list>))
sorted = merge_sort(<list>)
heap_sort(<list>)
sorted = radix_sort(<list>)
```


### Traversals ###


* Level Order
* In Order
* Pre Order
* Post Order

```Python
level_order(<node>)

in_order(<node>)
rec_in_order(<node>)
itr_in_order(<node>)

pre_order(<node>)
rec_pre_order(<node>)
itr_pre_order(<node>)

post_order(<node>)
rec_post_order(<node>)
itr_post_order(<node>)
```

### Stacks, Queues, & Lists ###

```Python
stack = Stack()
stack = Stack(<data>, <data>, ...)

stack.peek()
stack.search()
stack.push(<data>)
stack.pop()
```

Queue

```Python
que = Queue()
que = Queue(<data>, <data>, ...)

que.peek()
que.search(<data>)
que.enqueue(<data>)
que.dequeue()
```

Singly Linked List

```Python
lst = SLList()
lst = SLList(<data>, <data>, ...)

lst.peek()
lst.search(<data>)
lst.insert(<data>)
lst.insert_after(<new>, <data>)
lst.remove()
lst.remove_data(<data>)
```

Doubly Linked List

```Python
dlst = DLList()
dlst = DLList(<data>, <data>, ...)

lst.peek()
lst.peek_last()
lst.find(<data>)
lst.insert(<data>)
lst.insert_after(<insert>, <after>)
lst.remove()
lst.remove_data(<data>)
lst.unshift(<data>)
lst.shift()
```

### Trees & Heaps ###

BSTree

```Python
bstree = BSTree()
tnode = BSTree(<data>, <data>, ...)

tnode.insert(<data>)
tnode.remove(<data>)
tnode.search(<data>)
```

MaxHeap

```Python
mx = MaxHeap()
mx = MaxHeap(<data>, <data>, ...)

mx.push(<data>)
mx.pop()
mx.remove(<data>)
mx.peek()
```

MinHeap

```Python
mn = MinHeap()
mn = MinHeap(<data>, <data>, ...)

mn.push(<data>)
mn.pop()
mn.remove(<data>)
mn.peek()
```

AVLTree

```Python
avl = AVLTree()
avl = BSTree(<data>, <data>, ...)

avl.insert(<data>)
avl.remove(<data>)
avl.search(<data>)
```

## License ##

Licensed under the GNU [GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html) license.
