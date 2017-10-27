/*
Brian Taylor Vann
github.com/taylor-vann

Description:
- Function to quick sort a list
- untraditional, copies list, more "functional"

Requirements:
- None

Methods:
- quickSort
- partition
*/


function quickSort(a) {
  if(a.length < 2) {
    return a;
  }

  var p = partition(a.slice());

  var l1 = quickSort(p[0]);
  var l2 = quickSort(p[1]);

  return l1.concat(l2);
}


function partition(a) {
  var lo = 0;
  var hi = a.length - 1;

  while(true) {
    while(a[lo] <= a[hi]) {
      lo += 1;
    }

    while(a[hi] > a[lo]) {
      hi -= 1;
    }

    if(lo >= hi) {
      return [a.slice(0, lo), a.slice(lo)];
    }

    var tmp = a[lo];
    a[lo] = a[hi];
    a[hi] = tmp;
  }
}

console.log(quickSort([]));
console.log(quickSort([1]));
console.log(quickSort([1, 9, 3, 8, 4, 5, 1]));
console.log(quickSort([6, 2, 6, 7, 3, 3, 4, 5]));
console.log(quickSort([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]));
console.log(quickSort([9, 2, 1]));
