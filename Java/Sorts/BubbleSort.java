// Brian Taylor Vann
// github.com/taylor-vann

import java.util.Arrays;

class BubbleSort {
  void bubbleSort(int[] arr) {
    if(arr.length < 2) {
      return arr;
    }

    boolean swpd = true;

    // until list is traversed without swapping ...
    while(swpd) {
      swpd = false
      // compare one element to the next for the list ...
      for(int j = 0; j < arr.length - 2; j++) {
        // if prev is less than next then swap ...
        if(arr[j] > arr[j + 1]) {
          int tmp = arr[j];
          arr[j] = arr[j + 1];
          arr[j + 1] = tmp;

          swpd = true;
        }
      }
    }
  }


  public static void main(String[] args) {
    BubbleSort bub = new BubbleSort();

    int[] arr = {1, 67, 4, 8, 3, 7};
    bub.bubbleSort(arr);

    System.out.println(Arrays.toString(arr));
  }
}
