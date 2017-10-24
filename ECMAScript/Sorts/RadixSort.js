/*
Brian Taylor Vann
github.com/taylor-vann

Description:
- Module to Radix sort a list

Requirements:
- Assumes whole numbers
- Least Significant Digit (LSD) Radix Sort

Methods:
- radix_sort
- bucketish_sort
*/

function radixSort(a, base = 10) {
  // var base = (typeof base === "undefined") ? 10 : base;

  if(a.length < 2) {
    return a;
  }

  var srtd = a.slice();
  var pos = base;
  var mod = 1;
  var maxNum = Math.max(...a);

  while(Math.floor(maxNum / mod) > 0) {
    srtd = digitSort(srtd, pos, mod, base);
    pos *= base;
    mod *= base;
  }

  return srtd;
}


function digitSort(a, pos, mod, base) {
  var bckt = [];

  for(j = 0; j < base; j++) {
    bckt.push([]);
  }

  for(k = 0; k < a.length; k++) {
    var indx = Math.floor((a[k] % pos) / mod);
    bckt[indx].push(a[k])
  }

  var coll = [];

  return coll.concat(...bckt);
}


console.log(radixSort([]));
console.log(radixSort([1]));
console.log(radixSort([9, 4, 12]));
console.log(radixSort([1, 8, 4, 7, 13, 67, 45]));
console.log(radixSort([5, 102, 56, 8]));
console.log(radixSort([90, 45, 67, 87, 22, 1, 5]));
console.log(radixSort([3456, 5, 64, 21, 10]));
