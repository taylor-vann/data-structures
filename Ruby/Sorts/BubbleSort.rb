# Brian Taylor Vann
# https://github.com/taylor-vann

def bubble_sort(arr)
  return arr if arr.length < 2

  swpd = true

  while swpd
    swpd = false

    for j in 0..(arr.length - 2)
      if arr[j] > arr[j + 1]
        arr[j], arr[j + 1] = ar[j + 1], arr[j];
        swpd = true
      end
    end
  end

  return arr
end
