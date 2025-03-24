from dictionary import Dictionary
from search import Search
# This game is called a "word ladder" and was invented by Lewis Carroll in 1877.
# Rules
# Weave your way from the start word to the end word.
# Each word you enter can only change 1 letter from the word above it.
def main():
    
    #  create an instance of the Dictionary class
  file_name = r"C:\Users\thiol\Downloads\P1_python\python\words.txt"
  dict_obj = Dictionary(file_name) 
  if dict_obj.search_word("test"):
    print("The tested word is in our dictionary")

    

  print("Example to test search implementation **************")
  # can also use dictionary get word methods to test bfs and dfs method
  # arr = dict_obj.get_words(4)
  # start_word = arr[0]
  # end_word = arr[1]

  start_word = 'hit' #"glass"
  end_word = 'cog'   #"clink"
  new_search = Search(start_word, end_word)
   
  print('\ncalling depth first search')
  goal_node = new_search.dfs(dict_obj)
  print(goal_node, end=' ')

  print('\n\ncalling breadth first search')
  goal_node = new_search.bfs(dict_obj)
  if goal_node is not None:
    while goal_node.get_parent() is not None:
      print(f"{goal_node.value} <-", end="")
      goal_node = goal_node.get_parent()
    print(goal_node.value)
  else:
    print("You are yet to implement the code, try after implementation")



if __name__ == "__main__":
    main()
# This allows you to differentiate between the script being run directly and being used as a module.