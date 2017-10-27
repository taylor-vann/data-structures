/*
Brian Taylor Vann
github.com/taylor-vann

Description:
- Function to bubble sort a list

Requirements:
- None

Methods:
- bubbleSort()
*/

void swap(int *a, int *b) {
  int tmp = *a;
  *a = *b;
  *b = tmp;
}

void bubbleSort(int a[], int size) {
  if(size < 2) {
    return;
  }

  bool notSwpd = true;

  // until list is traversed without swapping ...
  while(notSwpd) {
    // compare one element to the next for the list ...
    for(int j = 0; j < size - 2; j++) {
      if(a[j] < a[j + 1]) {
        // if prev is less than next then swap ...
        swap(&a[j], &a[j + 1]);

        notSwpd = false;
      }
    }

    // if there was no swap then break ...
    if(notSwpd == true) {
      break;
    }

    // reset for next round
    notSwpd = true
  }

}
