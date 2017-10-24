/*
Brian Taylor Vann
github.com/taylor-vann

Description:
- Function to insertion sort a list

Requirements:
- None

Methods:
- insetionSort
*/

function insertionSort(a) {
  l = a.length

  if(l < 2) {
    return a;
  }

  // walk through the list
  for(var j = 1; j < l; j++) {
    cur = j;
    prv = j - 1;

    // descend the list and swap elements if prev larger than next
    while(a[prv] > a[cur] && prv > -1) {
      tmp = a[prv]
      a[prv] = a[cur];
      a[cur] = tmp;

      cur -= 1;
      prv = cur - 1;
    }
  }

  return a;
}
