from models.modules.dbconfig import db, ma, hash_password, verify_password
from sqlalchemy import exc

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(500))
    content = db.Column(db.String(900))
    author = db.Column(db.String(100))
    category = db.Column(db.String(20))
    image = db.Column(db.String(500))
    date = db.Column(db.String(50))

    def __init__(self, title, content, author, category, image, date):
        self.title = title
        self.content = content
        self.author = author
        self.category = category
        self.image = image
        self.date = date

class BlogSchema(ma.Schema):
    class Meta:
        fields = ('title', 'content', 'author', 'category', 'image', 'date')

blog_scheme = BlogSchema()
blogs_scheme = BlogSchema(many = True)

db.create_all()