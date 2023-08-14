from lib.posts import Post

class PostRepository():
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute('SELECT * from posts')
        posts = []
        for row in rows:
            item = Post(row["id"], row["title"])
            posts.append(item)
        return posts

    def find(self, post_id):
        rows = self._connection.execute(
            'SELECT * from posts WHERE id = %s', [post_id])
        row = rows[0]
        return Post(row["id"], row["title"])


    def create(self, post):
        self._connection.execute('INSERT INTO posts (title) VALUES (%s)', [
                                post.title])
        return None
    
    # def delete(self, post_id):
    #     self._connection.execute(
    #         'DELETE FROM posts WHERE id = %s', [post_id])
    #     return None

    def find_by_tag(self, tag):
        rows = self._connection.execute('SELECT posts.id, posts.title FROM tags JOIN posts_tags ON posts_tags.tag_id = tags.id JOIN posts ON posts_tags.post_id = posts.id WHERE tags.id = (%s)', [tag])
        posts = []
        for row in rows:
            item = Post(row["id"], row["title"])
            posts.append(item)
        return posts
    
    def find_by_post(self, post):
        rows = self._connection.execute('SELECT tags.id, tags.name FROM tags JOIN posts_tags ON posts_tags.tag_id = tags.id JOIN posts ON posts_tags.post_id = posts.id WHERE posts.id = (%s)', [post])
        tags = []
        for row in rows:
            item = Post(row["id"], row["name"])
            tags.append(item)
        return tags
    
