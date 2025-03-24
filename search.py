from collections import deque
import string
from node import Node
from dictionary import Dictionary



class Search:
    """
        Implements search algorithms for word transformations.
    """

    

    def __init__(self, start_word="", end_word=""):
        """
        Initializes the Search object with start and end words.

        Args:
            start_word (str): The word to start the transformation from.
            end_word (str): The target word to transform into.
        """    
        self.start_word = start_word
        self.end_word = end_word

    #self always come first in parameter and do not specify type in parameter
    def bfs(self, dict_obj):
        """
        use qt or tk to draw the algorithm, install pydot
        Performs Breadth-First Search (BFS).

        Returns:
            Node or None: The final Node representing the end_word if a path is found, otherwise None.
        """
        # TODO: Implement BFS logic
        endNode = Node( self.end_word)
        if not dict_obj.search_word(endNode.value):
            return None  # No solution if the end word isn't in the dictionary
        
        startNode = Node(self.start_word)
        startNode.set_parent(None)
        queue = deque([(startNode, [startNode])]) # pass an iterable to the queue
        visited = set()
        visited.add(startNode.value)

        while queue:
            newNode, path = queue.popleft()
          
            if newNode.value == endNode.value:
               # endNode.set_parent(newNode)
                return newNode # returns last node so you can backtrack to parent, can also return path
            
            for i in range(len(newNode.value)):
                 for letter in 'abcdefghijklmnopqrstuvwxyz':
                      next_word = newNode.value[:i] + letter + newNode.value[i+1:]  # letter is the new letter we're inserting at position i.

                      if dict_obj.search_word( next_word) and  next_word not in visited:
                          nd = Node(next_word)
                          nd.set_parent(newNode)
                          queue.append((nd, path + [nd]))
                          visited.add(nd.value)
                          
        return None

    def dfs(self, dict_obj):
        """
        Performs Depth-First Search (DFS).

        Returns:
            Node or None: The final Node representing the end_word if a path is found, otherwise None.
        """
        # TODO: Implement DFS logic
        endNode = Node( self.end_word)
        if not dict_obj.search_word(endNode.value):
            return None  # No solution if the end word isn't in the dictionary
        
        startNode = Node(self.start_word)
        startNode.set_parent(None)
        stack = [(startNode, [startNode.value])] # pass an iterable to the queue
        visited = set()
        visited.add(startNode.value)

        while stack:
            newNode, path = stack.pop()
          
            if newNode.value == endNode.value:
                return path # returns last node so you can backtrack to parent, can also return path
            
            for i in range(len(newNode.value)):
                 for letter in 'abcdefghijklmnopqrstuvwxyz':
                      next_word = newNode.value[:i] + letter + newNode.value[i+1:]  # letter is the new letter we're inserting at position i.

                      if dict_obj.search_word( next_word) and  next_word not in visited:
                          nd = Node(next_word)
                          nd.set_parent(newNode)
                          stack.append((nd, path + [nd.value]))
                          visited.add(nd.value)
                          
        return None
        

    def print_transformations(self, word_list):
        """
        Helper method to print the sequence of words
        Args:
            world_list(list) Sequence of words 
        """
        print(" --> ".join(word_list))  #turns word_list to a string and puts --> in between each word
