#include <iostream>
#include <cstdlib>

#include "stack.h"


template <class type>
Stack<type>::Stack()
{
  header = new Node();
  header->next = NULL;
};


template <class type>
bool Stack<type>::push(type new_value)
{
  Node* new_node = new Node;
  new_node->value = new_value;
  new_node->next = header->next;
  header->next = new_node;

  return true;
};


template<class type>
type Stack<type>::pop()
{
  if(header->next == NULL) {
    throw "Stack is empty!";
  }

  type tmp_value = header->next->value;
  Node* tmp_node = header->next;
  header->next = header->next->next;
  delete tmp_node;

  return tmp_value;
};


template<class type>
type Stack<type>::peek()
{
  if(header->next == 0) {
    return type();
  }

  return header->next->value;
};


template<class type>
bool Stack<type>::is_empty()
{
  if(header->next == NULL) {
    return true;
  }

  return false;
}
