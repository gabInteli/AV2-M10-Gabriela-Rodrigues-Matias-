from flask import Flask, request, jsonify

app = Flask(__name__)

blog_posts = []

class BlogPost:
    def __init__(self, id, title, content):
        self.id = id
        self.title = title
        self.content = content
    def __str__(self) -> str:
        return f'{self.id} - {self.title} - {self.content}'
    
    def toJson(self):
        return {'id': self.id, 'title': self.title, 'content': self.content}

@app.route('/blog', methods=['POST'])
def create_blog_post():
    try:
        data = request.get_json()
        blog_posts.append(BlogPost(data['id'], data['title'], data['content']))
        return jsonify({'status':'sucess'}), 201
    except KeyError:
        return jsonify({'error': 'Invalid request'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/blog', methods=['GET'])
def get_blog_posts():
    return jsonify({'posts': [blog.toJson() for blog in blog_posts]}), 200


@app.route('/blog/<int:id>', methods=['GET'])
def get_blog_post(id):
    for post in blog_posts:
        if post.id == id:
            return jsonify({'post': post.__dict__}), 200
    return jsonify({'error': 'Post not found'}), 404

@app.route('/blog/<int:id>', methods=['DELETE'])
def delete_blog_post(id):
    for post in blog_posts:
        if post.id == id:
            blog_posts.remove(post)
            return jsonify({'status':'sucess'}), 200
    return jsonify({'error': 'Post not found'}), 404

@app.route('/blog/<int:id>', methods=['PUT'])
def update_blog_post(id):
    try:
        data = request.get_json()
        for post in blog_posts:
            if post.id == id:
                post.title = data['title']
                post.content = data['content']
                return jsonify({'status':'sucess'}), 200
        return jsonify({'error': 'Post not found'}), 404
    except KeyError:
        return jsonify({'error': 'Invalid request'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)