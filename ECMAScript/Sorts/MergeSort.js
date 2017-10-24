/*
Brian Taylor Vann
github.com/taylor-vann

Description:
- Function to merge sort a list

Requirements:
- None

Methods:
- mergeSort
- merge
*/


function mergeSort(a) {
  if (a.length < 2) {
    return a
  }

  var p = Math.floor(a.length / 2);

  var l1 = mergeSort(a.slice(0, p));
  var l2 = mergeSort(a.slice(p));

  return merge(l1, l2);
}


function merge(a, b) {
  var n = [];

  while(a.length > 0 && b.length > 0) {
    if(a[0] < b[0]) {
      n.push(a.shift());
    }else{
      n.push(b.shift());
    }
  }

  return n.concat(a, b);
}
