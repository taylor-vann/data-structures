#Python Practice#

##Abstract##

Algortithms and data structures in python3.

##Details##

This is technical practice with common algorithms and data structures in python3. The point is to not use built-in functions and classes and create homebrew stacks, queues, heaps, sorts, trees, and graphs. Of course, all of these endeavours are composed using test driven development.

##Usage##

Here's a bunch of boring algorithms and data structures. Cool beans.

If you're studying for your comp-sci courses, you should really rely on the examples given by your professors. That's what'll give you the grade.

If your teaching yourself and just need help or a guide, this is just one more perspective. It's not intended to be a tutorial.

Unfortunately, considering yourself an artist creates a stigma that hinders your ability to get a technical interview let alone be taken seriously in said hypothetical interview (even if you have a solid foundation in computer science and media theory). This is one attempt to bridge that gap between creativity and professionalism. 

So, like I said, here's a bunch of boring-ass algorithms and unit tests.

###Sorts###

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

QuickSort - module to quick sort a list

```
quick_sort(<list>, 0, len(<list>))

partition(<list>, lo, hi)
```


###Stacks, Queues, & Lists###

SLNode - Singly Linked Node

```
slnode = SLNode()
slnode = SLNode(<data>, next)

slnode.set_data(<data>)
slnode.get_data()
slnode.set_next(<SLNode>)
slnode.get_next()
```

Stack - Stack class

```
stack = Stack()
stack = Stack(<data>, <data>, ...)

stack.push(<data>)
stack.pop()
stack.peek()
stack.search()
```

Queue - Queue class

```
que = Queue()
que = Queue(<data>, <data>, ...)

que.enqueue(<data>)
que.dequeue()
que.peek()
que.search(<data>)
```

SLList - Singly Linked List class

```
lst = SLList()
lst = SLList(<data>, <data>, ...)

lst.insert(<data>)
lst.insert_after(<new>, <data>)
lst.remove()
lst.remove_data(<data>)
lst.peek()
lst.search(<data>)
```

DLNode - Doubly Linked Node

```
dlnode = DLNode()
dlnode = DLNode(<data>, prev, next)

slnode.set_data(<data>)
slnode.get_data()
slnode.set_prev(<DLNode>)
slnode.get_prev()
slnode.set_next(<DLNode>)
slnode.get_next()
```

DLList - Doubly Linked List class

```
dlst = DLList()
dlst = DLList(<data>, <data>, ...)

lst.insert(<data>)
lst.remove()
lst.remove_data(<data>)
lst.unshift(<data>)
lst.shift()
lst.insert_after(<insert>, <after>)
lst.peek()
lst.peek_last()
lst.find(<data>)
```

##License##

Licensed under the GNU [GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html) license.
