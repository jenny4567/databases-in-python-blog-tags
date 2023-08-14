from lib.posts import Post

"""
Post constructs with an id, title and content
"""
def test_post_constructs():
    post = Post(1, "Test Title")
    assert post.id == 1
    assert post.title == "Test Title"

"""
We can format post to strings nicely
"""
def test_posts_format_nicely():
    post = Post(1, "Test Title")
    assert str(post) == "Post(1, Test Title)"

"""
We can compare two identical posts
And have them be equal
"""
def test_posts_are_equal():
    post1 = Post(1, "Test Title")
    post2 = Post(1, "Test Title")
    assert post1 == post2