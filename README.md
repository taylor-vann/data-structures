# Python Practice #

## Abstract ##

Algortithms and data structures in python3.

## Details ##

This is technical practice with common algorithms and data structures in python3. The point is to not use built-in functions and classes and create homebrew stacks, queues, heaps, sorts, trees, and graphs. Of course, like every good computer science student, all of these endeavours are composed using test driven development (you are using TDD, yes? of course you are, \*wink \*wink).

## Usage ##

Here's a bunch of the algorithms and data structures.

If you're studying for your comp-sci courses, you should rely on the examples provided by your professors. That's what'll give you the grade.

If you're teaching yourself and just need help or a delineation, here's one more perspective. It's not intended to be a tutorial.

### Sorts ###

BubbleSort - module to bubble sort a list

```
bubble_sort(<list>)
```

InsertionSort - module to insertion sort a list

```
insertion_sort(<list>)
```

SelectionSort - module to selection sort a list

```
selection_sort(<list>)
```

ShellSort - module to selection sort a list

```
shell_sort(<list>)
```

QuickSort - module to quick sort a list

```
quick_sort(<list>, 0, len(<list>))
```

MergeSort - module to merge sort a list

```
sorted = merge_sort(<list>)
```

HeapSort - module to heap sort a list

```
heap_sort(<list>)
```

RadixSort - module to radix sort a list

```
sorted = radix_sort(<list>)
```


### Stacks, Queues, & Lists ###

Singly Linked Node

```Python
slnode = SLNode()
slnode = SLNode(<data>, next)

slnode.get_data()
slnode.set_data(<data>)
slnode.get_next()
slnode.set_next(<SLNode>)
```

Stack

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

Doubly Linked Node

```Python
dlnode = DLNode()
dlnode = DLNode(<data>, prev, next)

slnode.get_data()
slnode.set_data(<data>)
slnode.get_prev()
slnode.set_prev(<DLNode>)
slnode.get_next()
slnode.set_next(<DLNode>)
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

BSTNode

```Python
tnode = BSTNode()
tnode = BSTNode(<data>, left, right)

tnode.get_data()
tnode.set_data(<data>)
tnode.get_left()
tnode.set_left(<BSTNode>)
tnode.get_next()
tnode.set_next(<BSTNode>)
```

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
