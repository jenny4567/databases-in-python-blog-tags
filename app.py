from lib.database_connection import DatabaseConnection
#from lib.artist_repository import ArtistRepository
from lib.posts_repository import PostRepository
from lib.comments_repository import CommentRepository


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/blogger.sql")

# Create our repositories
post_repository = PostRepository(connection)
comment_repository = CommentRepository(connection)

# Get a post
post = post_repository.find(1)


# Get all comments
comments = comment_repository.all()


# And then filter the comments array depending on the id of the post
comments_in_post = []
for comment in comments:
    if comment.post_id == post.id:
        comments_in_post.append(comment)

print(post)
for comment in comments_in_post:
    print(comment)

# List them out
#for artist in artists:
    #print(artist)
