#include <iostream>
#include <cstdlib>

#include "stack.h"
#include "stack.cpp"

int main (int argc, char *argv[]) {
  std::cout << "hey there world!\n";

  Stack<std::string> *stack = new Stack<std::string>();
  stack->push("hello");
  stack->push("world");

  std::cout << "Peek: " << stack->peek() << std::endl;
  std::cout << "Pop: " << stack->pop() << std::endl;
  std::cout << "Push: " << stack->push("ewe") << std::endl;
  std::cout << "Peek: " << stack->peek() << std::endl;

  while(!stack->is_empty()) {
    std::cout << "Pop: " << stack->pop() << std::endl;
  }

  return 0;
}
