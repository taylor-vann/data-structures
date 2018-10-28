#ifndef STACK_H
#define STACK_H

class Stack {
  public:
    void push(int);
    int pop();
    int peek();
  private:
    node *header;
};

#endif
