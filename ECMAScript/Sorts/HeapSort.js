/*
Brian Taylor Vann
github.com/taylor-vann

Description:
- Function for heap sort

Requirements:
- None
*/


function heapSort(a) {
  l = a.length;
  h = Math.floor(l / 2);

  if(l < 2) {
    return a;
  }

  // from last parent to first, sift down so largest value on top
  while(h > -1) {
    siftDown(a, h, l);
    h -= 1;
  }

  // walk back and swap first and index and sift new first down
  for(var j = l - 1; j > -1; j--) {
    var tmp = a[0];
    a[0] = a[j];
    a[j] = tmp;

    siftDown(a, 0, j);
  }

  return a;
}


function siftDown(a, i, l) {
  var c = i;
  var n = 2 * c + 1;

  while(n < l) {
    if(n < l - 1 && a[n] < a[n + 1]) {
      n += 1;
    }

    if(a[c] < a[n]) {
      var tmp = a[c];
      a[c] = a[n];
      a[n] = tmp;

      c = n;
      n = c * 2 + 1;
    }else{
      break
    }
  }
}

console.log(heapSort([]));
console.log(heapSort([1]));
console.log(heapSort([1, 3, 5]));
console.log(heapSort([4, 8, 6, 9, 0, 1, 10]));
console.log(heapSort([11, 7, 8, 7, 0]));
