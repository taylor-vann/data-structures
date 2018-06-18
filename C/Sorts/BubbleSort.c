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

void bubbleSort(int arr[], int length) {
  if(length < 2) {
    return arr;
  }

  bool swpd = true;

  // until list is traversed without swapping ...
  while(swpd) {
    swpd = false;
    
    // compare one element to the next for the list ...
    for(int j = 0; j < length - 2; j++) {
      if(arr[j] < arr[j + 1]) {
        // if prev is less than next then swap ...
        swap(&arr[j], &arr[j + 1]);

        swpd = true;
      }
    }
  }

}
