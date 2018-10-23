#include <stdio.h>
#include <stdlib.h>

#include "node.h"
#include "stack.h"


int push(node *n, int value)
{
  printf("node:%d, %d\n", n->value, value)

  return 1;
};


void create_stack_interface(stack_interface *s)
{
  s->push = push;

  return 0;
};
