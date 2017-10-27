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

import java.util.Arrays;

class BubbleSort {
  void bubbleSort(int[] a) {
    if(a.length < 2) {
      return;
    }

    boolean notSwpd = true;

    // until list is traversed without swapping ...
    while(notSwpd) {
      // compare one element to the next for the list ...
      for(int j = 0; j < a.length - 1; j++) {
        // if prev is less than next then swap ...
        if(a[j] > a[j + 1]) {
          int tmp = a[j];
          a[j] = a[j + 1];
          a[j + 1] = tmp;

          notSwpd = false;
        }
      }

      // if there was no swap then break ...
      if(notSwpd == true) {
        break;
      }

      // reset for next round
      notSwpd = true;
    }
  }


  public static void main(String[] args) {
    BubbleSort bub = new BubbleSort();

    int[] arr = {1, 67, 4, 8, 3, 7};
    bub.bubbleSort(arr);

    System.out.println(Arrays.toString(arr));
  }
}
