from lib.posts_repository import PostRepository
from lib.posts import Post
from lib.tags import Tag

"""
When we call PostRepository#all
We get a list of post objects reflecting the seed data.
"""
def test_get_all_posts(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/blog_posts_tags.sql") # Seed our database with some test data
    repository = PostRepository(db_connection) # Create a new PostRepository
    posts = repository.all() # Get all Posts
    # Assert on the results
    assert posts == [
        Post(1, 'How to use Git'),
        Post(2, 'Fun classes'),
        Post(3, 'Using a REPL'),
        Post(4, 'My weekend in Edinburgh'),
        Post(5, 'The best chocolate cake EVER'),
        Post(6, 'A foodie week in Spain'),
        Post(7, 'SQL basics')
    ]

"""
When we call PostRepository#find
We get a single post object reflecting the seed data.
"""
def test_get_single_post(db_connection):
    db_connection.seed("seeds/blog_posts_tags.sql")
    repository = PostRepository(db_connection)
    post = repository.find(3)
    assert post == Post(3, 'Using a REPL')

"""
When we call PostRepository#create
We get a new post in the database.
"""
def test_create_post(db_connection):
    db_connection.seed("seeds/blog_posts_tags.sql")
    repository = PostRepository(db_connection)

    repository.create(Post(None, 'My divorce'))

    result = repository.all()
    assert result == [
        Post(1, 'How to use Git'),
        Post(2, 'Fun classes'),
        Post(3, 'Using a REPL'),
        Post(4, 'My weekend in Edinburgh'),
        Post(5, 'The best chocolate cake EVER'),
        Post(6, 'A foodie week in Spain'),
        Post(7, 'SQL basics'),
        Post(8, 'My divorce')
    ]

"""
When we call PostRepository#delete
We remove a post from the database.
"""
# def test_delete_post(db_connection):
#     db_connection.seed("seeds/blog_posts_tags.sql")
#     repository = PostRepository(db_connection)
#     repository.delete(1) 
#     result = repository.all()
#     assert result == [
#         Post(2, 'Fun classes'),
#         Post(3, 'Using a REPL'),
#         Post(4, 'My weekend in Edinburgh'),
#         Post(5, 'The best chocolate cake EVER'),
#         Post(6, 'A foodie week in Spain'),
#         Post(7, 'SQL basics')
#     ]

'''
Method	        Job	                                Arguments	        SQL query	        Returns
find_by_tag	    Find all posts for the given tag	A tag (string)	    SELECT ... JOIN 	Array of Post
'''
def test_find_by_tag(db_connection):
    db_connection.seed("seeds/blog_posts_tags.sql")
    repository = PostRepository(db_connection)
    assert repository.find_by_tag(1) == [
        Post(1, 'How to use Git'),
        Post(2, 'Fun classes'),
        Post(3, 'Using a REPL'),
        Post(7, 'SQL basics')
    ]

def test_find_by_post(db_connection):
    db_connection.seed("seeds/blog_posts_tags.sql")
    repository = PostRepository(db_connection)
    assert repository.find_by_post(1) == [
        Tag(1, 'coding')
    ]

