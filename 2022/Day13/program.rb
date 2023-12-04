require 'json'

input = File.open("input.txt").readlines

slice_size = 3

def save(thing)
  Marshal.dump(thing)
end

def load(thing)
  Marshal.load(thing)
end

def compare(left, right)

  left = load(left)
  right = load(right)

  if left.is_a?(Integer) && right.is_a?(Integer)
    return left < right if left != right    
  elsif left.is_a?(Array) && right.is_a?(Array)

    left.each.with_index do |l, i|
      
      return false if right[i].nil?
      res = compare(save(l), save(right[i]))

      return res unless res.nil?

    end

    return true if left.size < right.size

  elsif left.is_a?(Integer) && right.is_a?(Array)
    return compare(save([left]), save(right))
  elsif right.is_a?(Integer) && left.is_a?(Array)
    return compare(save(left), save([right]))
  end

end

sum = 0

input.each_slice(slice_size).with_index do |batch, i|
  first, second = batch.map(&:strip).reject(&:empty?).map { |el| JSON.parse(el) }
  correct = compare(Marshal.dump(first), Marshal.dump(second))
  sum += 1 + i if correct
end

puts sum