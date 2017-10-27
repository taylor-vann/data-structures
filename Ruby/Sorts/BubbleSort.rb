=begin
Brian Taylor Vann
github.com/taylor-vann

Description:
- Function to bubble sort a list

Requirements:
- None

Methods:
- bubbleSort()
=end


def bubble_sort(a)
  if a.length < 2
    return a
  end

  not_swpd = true

  # until list is traversed without swapping ...
  while not_swpd
    # compare one element to the next for the list ...
    for j in 0..(a.length - 2)
      # if prev is less than next then swap ...
      if a[j] > a[j + 1]
        a[j], a[j + 1] = a[j + 1], a[j]
        not_swpd = false
      end
    end

    # if there was no swap then break ...
    if not_swpd == true
      break
    end

    # reset for next round
    not_swpd = true
  end

  return a
end
