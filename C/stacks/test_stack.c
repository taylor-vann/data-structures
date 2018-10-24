#include <stdio.h>
#include <stdlib.h>

#include "node.h"
#include "stack.h"

int main(int argc, const char* argv[]) {
  printf("Run the tests for stack!\n");

  node *new_node = malloc(sizeof(node));

  printf("the node's value is: %d\n", new_node->value);

  stack *new_stack = malloc(sizeof(stack));
  push(&new_node, 5);
  
  stack_interface *stack_int = malloc(sizeof(stack_interface));
  create_stack_interface(&stack_int);

  return 0;
};
