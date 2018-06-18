// Brian Taylor Vann
// github.com/taylor-vann

let bubbleSort = (arr) => {
  if(arr.length < 2) {
    return arr;
  }

  swpd = true;

  // until list is traversed without swapping ...
  while(swpd) {
    swpd = false;

    // compare one element to the next for the list ...
    for(var j = 0; j < arr.length - 2; j++) {
      // if prev is less than next then swap ...
      if(arr[j] > arr[j + 1]) {
        [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]]
        swpd = true;
      }
    }
  }

  return arr;
}
