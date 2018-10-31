#ifndef STACK_H
#define STACK_H

template <class type> class Stack {
    typedef struct node {
      type value;
      node *next;
    } Node;

    Node *header;

  public:
    Stack();
    bool push(type);
    type pop();
    type peek();
    bool is_empty();
};

#endif
