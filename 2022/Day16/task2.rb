require 'set'
regex = /Valve (?<name>.*) has flow rate=(?<flow_rate>\d*); tunnels? leads? to valves? (?<nodes>.*)\n?/
# Valve AA has flow rate=0; tunnels lead to valves DD, II, BB

class Node
  attr_accessor :neighbours, :name, :flow_rate, :important_neighbours
  def initialize(name, flow_rate, valves)
    @name = name
    @flow_rate = flow_rate.to_i
    @neighbours = valves.split(", ")
    @important_neighbours = {}
  end
end

graph = {}
while (l = gets)
  m = l.match(regex)
  graph[m["name"]] = Node.new(m["name"], m["flow_rate"], m["nodes"])
end

$cache = {}

start = graph["AA"]
# important is just nodes which have flow
important = graph.reject { |_, e| e.flow_rate.zero?}
# important["AA"] = start # add first node as well because its where we start

def bfs(start, graph, important)
  queue = [[start.name, 0]]
  visited = Set.new
  visited.add(start.name)

  until queue.empty?
    name, weight = queue.shift

    if important[name] && name != start.name

      important[start.name].important_neighbours[name] = weight
    end

    neighbours = graph[name].neighbours

    neighbours.each do |neighbor|
      # If the neighbor has not been visited, add it to the queue and mark it as visited
      unless visited.include?(neighbor)
        queue << [neighbor, weight + 1]
        visited.add(neighbor)
      end
    end
  end
end

important_with_aa = important.clone
important_with_aa['AA'] = start

# create a graph with important nodes
important_with_aa.each do |_, v1|
  important.each do |_, v2|
    if v1 != v2
      bfs(v1, graph, important)
    end
  end
end

puts(graph)

def params_to_s(cur_valve, minutes, cur_released, opened_valves)
  "#{cur_valve.name}::#{minutes}::#{opened_valves.join(",")}"
end

def find_most_pressure(cur_node, remaining_minutes, cur_released, opened_valves, graph, go_sloncek)
  cache_id = params_to_s(cur_node, remaining_minutes, cur_released, opened_valves)
  return $cache[cache_id] if $cache[cache_id]

  binding.irb if remaining_minutes.negative? # just checking, never stops here
  return cur_released if remaining_minutes <= 0

  max = -Float::INFINITY

  cur_node.important_neighbours.each do |next_node|
    weight = next_node[1]
    next_node = graph[next_node[0]]
    # open cur valve path if enough time and not opened yet
    if !opened_valves.include?(next_node.name) && remaining_minutes - weight - 1 >= 0

      opened = find_most_pressure(next_node,
                                  remaining_minutes - weight - 1,
                                  cur_released + (remaining_minutes - weight - 1) * next_node.flow_rate,
                                  opened_valves.clone.append(next_node.name),
                                  graph,
                                  go_sloncek
                                 )

      if go_sloncek
        sth = cur_released + (remaining_minutes - weight - 1) * next_node.flow_rate
        slo = find_most_pressure(graph["AA"], 26, 0, opened_valves.clone.append(next_node.name), graph, false)
        opened = slo + sth if slo && slo > opened
      end
    end

    # leave closed cur valve path
    if remaining_minutes - weight >= 0
      closed = find_most_pressure(next_node, remaining_minutes - weight, cur_released, opened_valves, graph, go_sloncek)
    end

    max = opened if opened && opened > max
    max = closed if closed && closed > max
  end

  cache_id = params_to_s(cur_node, remaining_minutes, cur_released, opened_valves)
  $cache[cache_id] = max
  max
end

res = find_most_pressure(start, 26, 0, [], important, true)
puts res
# binding.irb