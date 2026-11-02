import webbrowser

html = """
<!DOCTYPE html>
<html>
<head>
    <title>My Web Blog</title>
</head>
<body style="font-family: Arial; background-color: lightyellow;">

    <h1>Welcome to My Web Blog</h1>

    <a href="#home" title="Go to Home">Home</a> |
    <a href="#about" title="About Us">About</a> |
    <a href="#contact" title="Contact Us">Contact</a>

    <hr>

    <h2 id="home">My First Blog Post</h2>
    <p>Welcome to my web blog.</p>

    <h2>Python Programming</h2>
    <p>Python is a simple and powerful programming language.</p>

    <a href="https://www.python.org/"
       title="Learn Python"
       target="_blank">
       Learn Python
    </a>

    <h2 id="about">About Us</h2>
    <p>This blog provides information about programming.</p>

    <h2 id="contact">Contact Us</h2>
    <p>Email: myblog@example.com</p>

    <hr>

    <p>Copyright 2026 My Web Blog</p>

</body>
</html>
"""

with open("webblog.html", "w", encoding="utf-8") as file:
    file.write(html)

webbrowser.open("webblog.html")

print("Web blog created successfully!")
