movies = ['Sholay','Baghban','DDLJ',
          'Ironman','RRR','Inception','spiderman',
          'Kung fu panda','Suryavansham','Batman']

print(len(movies))
print(movies)

movies.sort()
print(movies)

movies.reverse()
print(movies)

print('first movie',movies[0])
print('last movie',movies[-1])
print('first 3 movies',movies[:3])
print('all movies except first 3',movies[3:])
print('movies with even indexes',movies[::2])
