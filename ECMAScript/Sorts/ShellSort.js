/*
Brian Taylor Vann
github.com/taylor-vann

Description:
- Function to shell sort a list

Requirements:
- None

Methods:
- shellSort()
*/

function shellSort(a) {
  l = a.length;

  if(l < 2) {
    return a;
  }

  // make space half of array length
  spc = Math.floor(l / 2);

  // while space is greater than 1
  while(spc > 0) {
    // run through everl element between space and array length
    for(var j = spc; j < l; j++) {
      // modified insertion sort using space
      while(j > -1 && a[j - spc] > a[j]) {
        var tmp = a[j - spc];
        a[j - spc] = a[j];
        a[j] = tmp;

        j -= spc;
      }
    }

    spc = Math.floor(spc / 2);
  }

  return a;
}

console.log(shellSort([]));
console.log(shellSort([1]));
console.log(shellSort([5, 2, 6, 8, 9, 2]));
console.log(shellSort([2, 4, 5]));
console.log(shellSort([7, 3, 6, 7]));
console.log(shellSort([2, 4, 1, 9, 3]));
