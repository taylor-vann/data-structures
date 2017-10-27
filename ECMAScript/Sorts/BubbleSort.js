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
  if(a.length < 2) {
    return a;
  }

  notSwpd = true

  // until list is traversed without swapping ...
  while(notSwpd) {
    // compare one element to the next for the list ...
    for(var j = 0; j < a.length - 1; j++) {
      // if prev is less than next then swap ...
      if(a[j] > a[j + 1]) {
        tmp = a[j];
        a[j] = a[j + 1];
        a[j + 1] = tmp;

        notSwpd = false;
      }
    }

    // if there was no swap then break ...
    if(notSwpd === true) {
      break;
    }

    // reset for next round
    notSwpd = true;
  }

  return a;
}


console.log(bubbleSort([1, 6, 3, 8, 9, 4]))
