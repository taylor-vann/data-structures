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

function bubbleSort(a) {
  l = a.length

  if(l < 2) {
    return lst;
  }

  b = true

  // until list is traversed without swapping ...
  while(b) {
    // compare one element to the next for the list ...
    for(var j = 0; j < l - 1; j++) {
      // if prev is less than next then swap ...
      if(a[j] > a[j + 1]) {
        tmp = a[j];
        a[j] = a[j + 1];
        a[j + 1] = tmp;

        b = false;
      }
    }

    // if there was no swap then break ...
    if(b === true) {
      break;
    }

    // reset for next round
    b = true;
  }

  return lst;
}
