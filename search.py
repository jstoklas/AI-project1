# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
import heapq
from game import Directions
from typing import List

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()




def tinyMazeSearch(problem: SearchProblem) -> List[Directions]:
    """
    Returns a sequence of moves that solves tinyMaze.  For any o444ther maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"

    stack = util.Stack()
    start = problem.getStartState()
    stack.push((start,[]))

    visited = set()

    while not stack.isEmpty():
        state, path = stack.pop()
        if problem.isGoalState(state):
            return path
        if state not in visited:
            visited.add(state)
        for successor, action, stepCost in problem.getSuccessors(state):
            if successor not in visited:
                stack.push((successor, path + [action]))
    return []

    util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    queue = util.Queue()
    start = problem.getStartState()
    queue.push((start,[]))
    visited = set()

    while not queue.isEmpty():
        state, path  = queue.pop()
        if problem.isGoalState(state):
            return path
        if state not in visited:
            visited.add(state)
        for successor, action, stepCost in problem.getSuccessors(state):
            if successor not in visited:
                queue.push((successor, path +[action]))
    return []
    util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem) -> List[Directions]:
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    
    util.raiseNotDefined()

def nullHeuristic(state, problem=None) -> float:
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic) -> List[Directions]:
    """Search the node that has the lowest combined cost and heuristic first."""

    # Gets inital state and sets the fringe to be empty
    initialState = problem.getStartState()
    fringe = []

    # uses the heuristic function and gets an f(n) = priority. Then it pushes that f(n) + initialState and empty set which represents the actions to the fringe. 
    priority = heuristic(initialState, problem)
    heapq.heappush(fringe, (priority, initialState, []))

    # Makes a dictionary of all the costs to keep in the memory for later
    bestG = {initialState : 0}

    #While fringe is not empty
    while (fringe):
        #Strips the first priority node into the f(n), state, and the actions
        priority, state, actions = heapq.heappop(fringe)
    
        if problem.isGoalState(state):
            return actions #DONE!
        
        # Calculates the current G(n)
        newG = problem.getCostOfActions(actions)

        #Gets all the children and calculates the new G() by adding the current g(n) and the cost to get to it.
        for successorState, action, cost in problem.getSuccessors(state):
            successorG = newG + cost

            #if the child's g(n) is less than the best g(n), then add it to the dictionary and add the action to the actions list so you know where you have went. 
            if successorG < bestG.get(successorState, float("inf")):
                bestG[successorState] = successorG
                newActions = actions + [action]

                # priority = f(n) and push everything to the fringe for later
                priority = successorG + heuristic(successorState, problem)
                heapq.heappush(fringe, (priority, successorState, newActions))
    return []

        




# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
