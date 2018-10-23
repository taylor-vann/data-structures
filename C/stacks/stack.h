#ifndef STACK_H
#define STACK_H

typedef struct stack stack;
struct stack {
  node *header;
};

typedef struct stack_interface stack_interface;
struct stack_interface {
  void (*push)(node *n, int value);
};

int push(node *n, int value);
int pop(node *n);
void print(node *n);

void create_stack_interface(stack_interface *s);

#endif
