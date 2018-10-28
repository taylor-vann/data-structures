#include <stdio.h>
#include <stdlib.h>

#include "stack.h"


static stack create_stack()
{
  stack *stck = malloc(sizeof(stack));
  stck->header = malloc(sizeof(node));
  stck->header->value = -1;
  stck->header->next = NULL;

  return *stck;
};


static stack push(stack *s, int value)
{
  node *n = malloc(sizeof(node));
  n->value = value;
  n->next = s->header->next;

  s->header->next = n;

  return *s;
};


static int pop(stack *s)
{
  if (s->header->next == NULL) {
    return -1;
  }

  int tmp_int = s->header->next->value;
  node *tmp_node = s->header->next;
  s->header->next = s->header->next->next;

  free(tmp_node);

  return tmp_int;
};


static int peek(stack *s)
{
  if (s->header->next == NULL) {
    return -1;
  }

  return s->header->next->value;
};


stack_interface create_stack_interface(stack_interface *s)
{
  s->create_stack = create_stack;
  s->push = push;
  s->pop = pop;
  s->peek = peek;

  return *s;
};
