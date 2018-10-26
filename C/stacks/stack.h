#ifndef STACK_H
#define STACK_H

#include "node.h"

typedef struct stack stack;
struct stack {
  node *header;
};

typedef struct stack_interface stack_interface;
struct stack_interface {
  stack (*create_stack)();
  stack (*push)(stack *s, int value);
  int (*pop)(stack *s);
  int (*peek)(stack *s);
};

stack_interface create_stack_interface(stack_interface *s);

#endif
