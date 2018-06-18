# Brian Taylor Vann
# github.com/taylor-vann

def bubble_sort(a)
  return a if a.length < 2

  swpd = true

  # until list is traversed without swapping ...
  while swpd
    swpd = false

    # compare one element to the next for the list ...
    for j in 0..(a.length - 2)
      # if prev is less than next then swap ...
      if a[j] > a[j + 1]
        a[j], a[j + 1] = a[j + 1], a[j]
        swpd = true
      end
    end
  end

  return a
end
