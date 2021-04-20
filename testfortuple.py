class State:
    VISITED = 2
    IS_VISITING = 1
    TO_VISIT = 0

def is_valid_course_schedule():
    n = 2
    prerequisites =[[0,1]]

    def build_graph(courses):
        graph = {}
        for i in range(n):
            graph[i] = []

        for course, dependency in prerequisites:
            graph[course].append(dependency)
        return graph

    def dfs(i, states):
        states[i] = State.IS_VISITING
        for prereq in graph[i]:
            if states[prereq] == State.VISITED:
                continue
            if states[prereq] == State.IS_VISITING:
                return False        
            if not dfs(prereq, states):
                return False
        states[i] = State.VISITED
        return True

    graph = build_graph(prerequisites)
    states = [State.TO_VISIT] * n

    for i in range(n):

        if not dfs(i, states):
            return False
        return True
        
print(is_valid_course_schedule())








