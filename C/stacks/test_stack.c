#include <stdio.h>
#include <stdlib.h>

#include "stack.h"

int main(int argc, const char* argv[]) {
  printf("Run the tests for stack!\n");

  stack_interface *stck_interface = malloc(sizeof(stack_interface));
  *stck_interface = create_stack_interface(stck_interface);

  stack *new_stack = malloc(sizeof(stack));
  *new_stack = stck_interface->create_stack();

  stck_interface->push(new_stack, 2);
  stck_interface->push(new_stack, 5);
  stck_interface->push(new_stack, 10);

  printf("top of the stack: %d\n", stck_interface->peek(new_stack));
  stck_interface->pop(new_stack);
  printf("top of the stack: %d\n", stck_interface->peek(new_stack));
  stck_interface->pop(new_stack);
  printf("top of the stack: %d\n", stck_interface->peek(new_stack));
  stck_interface->pop(new_stack);
  printf("top of the stack: %d\n", stck_interface->peek(new_stack));
  stck_interface->pop(new_stack);
  printf("top of the stack: %d\n", stck_interface->peek(new_stack));


  return 0;
};
