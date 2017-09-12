/*
 * Brian Taylor Vann
 * github.com/taylor-vann
 *
 * Description:
 * - Module to bubble sort a list
 *
 * Requirements:
 * - None

 * Methods:
 * - bubbleSort()
 */

function bubbleSort(lst) {
  l = lst.length

  if(l < 2) {
    return lst;
  }

  b = true

  while(b) {
    for(var j = 0; j < l - 1; j++) {
      if(lst[j] > lst[j + 1]) {
        tmp = lst[j];
        lst[j] = lst[j + 1];
        lst[j + 1] = tmp;

        b = false;
      }
    }

    if(b === true) {
      break;
    }

    b = true;
  }

  return lst;
}
