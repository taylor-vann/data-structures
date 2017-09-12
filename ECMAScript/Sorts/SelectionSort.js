/*
Brian Taylor Vann
github.com/taylor-vann

Description:
- Module to selection sort a list

Requirements:
- None

Methods:
- selection_sort
*/

function selectionSort(a) {
  l = a.length;

  if(a.length < 2) {
    return a
  }

  // walk through list ...
  for(var i = 0; i < l - 1; i++) {
    // establish an index
    var indx = i;

    // walk through the rest of the list ...
    for(var j = i; j < l; j++) {
      // if current is less than index, make index equal to current ...
      if(a[indx] > a[j]) {
        indx = j;
      }

      // if index is different than start, swap values ...
      if(indx !== i) {
        tmp = a[i];
        a[i] = a[indx];
        a[indx] = tmp;
      }
    }
  }

  return a;
}

console.log(selectionSort([0,3,4,3,2,5]))
