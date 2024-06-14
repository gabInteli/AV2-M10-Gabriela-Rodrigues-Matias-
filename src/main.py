from fastapi import FastAPI
from pydantic import BaseModel
from logs import log_info, log_critical, log_error, log_warning
import uvicorn

blog_posts = []
app = FastAPI()

class BlogPost(BaseModel):
    id: int
    title: str
    content: str

@app.get('/')
def hello_world():
    log_info('Server is Working!')
    return {'message': 'Server is Working!'}

@app.post('/blog')
def create_blog_post(post: BlogPost):
    try:
        blog_posts.append(post)
        log_warning('Post created')
        return {'status': 'success'}
    except Exception as e:
        log_error(str(e))
        return {'error': str(e)}


@app.get('/blog')
def get_blog_posts():
    log_warning('Getting all posts')
    return {'posts': blog_posts}

@app.get('/blog/{id}')
def get_blog_post(id: int):
    for post in blog_posts:
        if post.id == id:
            log_info('Post found')
            return {'post': post}

    return {'error': 'Post not found'}

@app.delete('/blog/{id}')
def delete_blog_post(id: int):
    for post in blog_posts:
        if post.id == id:
            log_critical('Post deleted')
            blog_posts.remove(post)
            return {'status': 'success'}
    return {'error': 'Post not found'}

@app.put('/blog/{id}')
def update_blog_post(id: int, post: BlogPost):
    try:
        for existing_post in blog_posts:
            if existing_post.id == id:
                existing_post.title = post.title
                existing_post.content = post.content
                log_warning('Post updated')
                return {'status': 'success'}
        return {'error': 'Post not found'}
    except Exception as e:
        return {'error': str(e)}

        
    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
