function depthFirstTraversal(graph, source) {
    const stack = [source];
    while (stack.length > 0) {
        const current = stack.pop();
        console.log(current);
        for (let neighbor of graph[current]) {
            stack.push(neighbor)
        }
    }
}

const graph = {
   "a": ["b", "c"],
   "b": ["d"],
   "c": ["e"],
   "d": [],
   "e": ["b"],
   "f": ["d"]
}
