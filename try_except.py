print("We've got some buggy code, try running the code. The code will crash and give you a **KeyError**. \
This is because some of the posts in the `facebook_posts` don't have any `'Likes'`.This program will give you an \idea about  try and except in python")
facebook_posts = [
    {'Likes': 21, 'Comments': 2}, 
    {'Likes': 13, 'Comments': 2, 'Shares': 1}, 
    {'Likes': 33, 'Comments': 8, 'Shares': 3}, 
    {'Comments': 4, 'Shares': 2}, 
    {'Comments': 1, 'Shares': 1}, 
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
  try:
    total_likes = total_likes + post['Likes']

  except KeyError:
    print("likes are missing,no likes are got for it.ther is only comments and shares")
  
print(total_likes)
