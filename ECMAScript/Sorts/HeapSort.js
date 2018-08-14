/*
Brian Taylor Vann
github.com/taylor-vann

Description:
- Function for heap sort

Requirements:
- None
*/


const heapSort = (arr) => {
  l = arr.length;
  h = Math.floor(l / 2);

  if(l < 2) {
    return arr;
  }

  // from last parent to first, sift down so largest value on top
  while(h > -1) {
    siftDown(arr, h, l);
    h -= 1;
  }

  // walk back and swap first and index and sift new first down
  for(var j = l - 1; j > -1; j--) {
    var tmp = arr[0];
    arr[0] = arr[j];
    arr[j] = tmp;

    siftDown(arr, 0, j);
  }

  return arr;
}


function siftDown(arr, i, l) {
  var c = i;
  var n = 2 * c + 1;

  while(n < l) {
    if(n < l - 1 && arr[n] < arr[n + 1]) {
      n += 1;
    }

    if(arr[c] < arr[n]) {
      var tmp = arr[c];
      arr[c] = arr[n];
      arr[n] = tmp;

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
