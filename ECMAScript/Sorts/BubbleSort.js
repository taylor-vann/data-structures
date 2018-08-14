// Brian Taylor Vann
// github.com/taylor-vann

const bubbleSort = (arr) => {
  if(arr.length < 2) {
    return arr;
  }

  swpd = true;

  while(swpd) {
    swpd = false;

    for(var j = 0; j < arr.length - 2; j++) {
      if(arr[j] > arr[j + 1]) {
        [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
        swpd = true;
      }
    }
  }

  return list;
};


export {
  bubbleSort
};
