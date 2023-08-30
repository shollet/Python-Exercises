# You are given a list of projects and a list of dependencies (which is a list of pairs of projects, where the second project is dependent on the first project). All of a project's dependencies must be built before the project is. Find a build order that will allow the projects to be built. If there is no valid build order, return an error.

def createGraph(projects, dependencies):
    projectGraph = {}
    for project in projects:
        projectGraph[project] = []
    for pairs in dependencies:
        projectGraph[pairs[0]].extend(pairs[1])
    return projectGraph

project = ['a', 'b', 'c', 'd', 'e', 'f']
dependencies = [('a','d'), ('f','b'), ('b','d'), ('f','a'), ('d','c')]


def findBuildOrder(projects, dependencies):
    def getDependencies(graph):
        projects = set()
        for project in graph:
            projects = projects.union(set(graph[project]))
        return projects
    
    def getIndependencies(projectsWD, graph):
        projectsWOD = set()
        for project in graph:
            if not project in projectsWD:
                projectsWOD.add(project)
        return projectsWOD
    
    buildOrder = []
    projectGraph = createGraph(projects, dependencies)
    while projectGraph:
        projectsWD = getDependencies(projectGraph)
        projectsWOD = getIndependencies(projectsWD, projectGraph)
        if len(projectsWOD) == 0 and projectGraph:
            raise ValueError("There is a cycle in the build order")
        for independentProject in projectsWOD:
            buildOrder.append(independentProject)
            del projectGraph[independentProject]
    return buildOrder