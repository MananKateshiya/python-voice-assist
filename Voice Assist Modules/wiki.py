
# importing the module
import wikipedia

# search = (wikipedia.search("john wick movie"))
# print("search is: ", search[0])
search = <Search term>
genre = f"{search} {search}"

# print(wikipedia.search("bill gates", results=5))
print(wikipedia.summary(search + " " +genre, sentences=5))