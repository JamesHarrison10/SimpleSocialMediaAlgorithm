#Protoype By James Harrison
# Github: https://github.com/JamesHarrison10
#Purpose of this project: For fun and learning.
#What is this project?: This project is a VERY basic sorting algorythm. It takes post using a OOP Approach, takes its data and sorts them into order based on the engagment score. This sort of code can be seen in more complex social media softwares.

content_types = ["Video", "Image", "Text"]

#Object oriantated class for posts. 
class Post:
    def __init__(self, name, content, likes, comments, views, age):
        self.name = name
        self.content = content
        self.likes = likes
        self.comments = comments
        self.views = views
        self.age = age
    
    def engagement_score(self):
        return self.likes * 3 + self.comments * 2 + self.views * 0.1 / self.age
    
    def __repr__(self):
        return f"{self.name}: {self.content}: {self.engagement_score():.2f}: score at {self.age} days"
    
#Posts [Content, likes, comments, views]
post1 = Post("Post1","Video", 10, 2, 100, 1)
post2 = Post("post2","Image", 20, 5, 200, 0.5)
post3 = Post("Post3", "Text", 260, 50, 1000, 10)
post4 = Post("Post4", "Text", 10, 2, 100, 0.5)

def sortPosts(posts):
    return sorted(posts, key=lambda post: post.engagement_score(), reverse=True)

posts = [post1, post2, post3, post4]
sorted_posts = sortPosts(posts)

for post in sorted_posts:
    print(post)