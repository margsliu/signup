import webapp2
import cgi

# html boilerplate for header and footer
page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>Sign Up</title>
    <style type="text/css">
        .error {
            color: red;
        }
    </style>
</head>
<body>
"""

page_footer = """
</body>
</html>
"""

def validatepass(pw1,pw2):
    """compares and verifies that user input passwords are same"""
    if pw1 != pw2:
        return False
    else:
        return True

class Index(webapp2.RequestHandler):
    def get(self):
        edit_header = "<h1>Sign up <u>now</u> to have onions delivered to you <em>daily!</em></h1>"

        error = self.request.get('error')
        form = """
        <form action="/welcome" method="post">
            <label>Username</label>
                <input type="text" name="username" required/>
            <br>
            <label>Password</label>
                <input type="password" name="password1" required/>
            <br>
            <label>Verify Password</label>
                <input type="password" name="password2" required/> <font style="color:red">{0}</font>
            <br>
            <label>Email (optional)</label>
                <input type="email" name="useremail"/>
            <br>
            <input type="submit" value="Submit"/>
        </form>
        """.format(error)

        main_content = edit_header + form
        response = page_header + main_content + page_footer
        self.response.write(response)

class Welcome(webapp2.RequestHandler):




    def post(self):

        if validatepass(self.request.get("password1"),self.request.get("password2")) == False:
            error = "Passwords don't match."
            self.redirect('/?error={}'.format(cgi.escape(error, quote=True)))

        username = self.request.get("username")

        welcome_message = "<h1>Welcome, {0}! You're gonna have SO many onions now.</h1>".format(username)

        main_content = welcome_message

        response = page_header + main_content + page_footer
        self.response.write(response)

app = webapp2.WSGIApplication([
    ('/', Index),
    ('/welcome', Welcome)
], debug=True)
