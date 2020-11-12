---
title: Web Application Security with secure.py
layout: post
categories: [python, flask, security]
description: "A post on web application security and how to avoid common pitfalls with `secure.py`"
customexcerpt: "A common pitfall when developing web applications is not knowing how to design a safe application.`"
---

A common pitfall when developing web applications is not knowing how to design a safe application.
`secure.py` is a great Python module that helps deal with the basic foundations of web application security.


## Goal

In this post, I go through web application security, and how to use `secure.py` to address
common pitfalls. Note that by web application security, I am not addressing authentication or database security.
I mean secure web headers, predominantly, as defined by the [OWASP Secure Headers Project.](https://owasp.org/www-project-secure-headers/)


## OWASP

The [Open Web Application Security Project®](https://owasp.org/) (OWASP) is a nonprofit foundation that works to improve the security of software.
It provides resources and guidelines about web application security, and holds educational and training conferences.

If you're concerning yourself with writing a web application, I highly recommend going through the OWASP guidelines
on various topics related to web application security.

This particular post will be centered around the OWASP guidelines on HTTP Headers. Reference links are at the bottom of the post.

## A Little Bit About HTTP Headers

HTTP Headers are the sort of things that don't *often* concern developers. We don't think about them, until we encounter
some issue with Cross-Site Requests or something similar. However, knowledge of headers gives you a lot to think about.

How do you even *see* the headers, anyway?

Let's try `curl`.

```bash

curl google.com
<HTML><HEAD><meta http-equiv="content-type" content="text/html;charset=utf-8">
<TITLE>301 Moved</TITLE></HEAD><BODY>
<H1>301 Moved</H1>
The document has moved
<A HREF="http://www.google.com/">here</A>.
</BODY></HTML>
```

Besides the HTML content, this tells us *nothing*. From the `title` tag, you can guess that the request
returned a [301 Moved HTTP status code](https://devhints.io/http-status). However, remember, developers are *human*.

It is only too easy to do this:

```python
import flask

app = flask.Flask(__name__)

@app.route("/")
def index():
    import textwrap
    html = textwrap.dedent("""
    <HTML><HEAD><meta http-equiv="content-type" content="text/html;charset=utf-8">
    <TITLE>301 Moved</TITLE></HEAD><BODY>
    <H1>301 Moved</H1>
    The document has moved
    <A HREF="http://localhost/">here</A>.
    </BODY></HTML>
    """)
    return html, 200

```

If you save that snippet to a file named `app.py`, and run it with the Flask command line using `FLASK_APP=app.py flask run`,
you can access this with `curl` again.


Note that you need to have a Python environment with `flask` installed for this to work.

PS: If you've noticed the `textwrap.dedent` trick, it's a neat way of telling python to ignore the indentation within a triple-quoted string.
I can get a bit pedantic about being exact.

```bash
$ curl localhost:5000/

<HTML><HEAD><meta http-equiv="content-type" content="text/html;charset=utf-8">
<TITLE>301 Moved</TITLE></HEAD><BODY>
<H1>301 Moved</H1>
The document has moved
<A HREF="http://localhost/">here</A>.
</BODY></HTML>
```

There's no difference here. Does that mean both are the same?

*No*.

Instead, let's try to see if `curl` can help.

`curl -s -D - <url>` Will give us the entire response, including the HTTP headers.

Let's try it on `google.com`

```bash

$ curl -s -D - google.com

HTTP/1.1 301 Moved Permanently
Location: http://www.google.com/
Content-Type: text/html; charset=UTF-8
Date: Wed, 11 Nov 2020 17:52:37 GMT
Expires: Fri, 11 Dec 2020 17:52:37 GMT
Cache-Control: public, max-age=2592000
Server: gws
Content-Length: 219
X-XSS-Protection: 0
X-Frame-Options: SAMEORIGIN

<HTML><HEAD><meta http-equiv="content-type" content="text/html;charset=utf-8">
<TITLE>301 Moved</TITLE></HEAD><BODY>
<H1>301 Moved</H1>
The document has moved
<A HREF="http://www.google.com/">here</A>.
</BODY></HTML>
```

The first line is the most important one. It tells us that the website we are trying to access has *moved permanently*.
In fact, the code there is the standard code for the 301 response.

Let's look at what we have.

```bash

$ curl -s -D - localhost:5000/

HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 213
Server: Werkzeug/1.0.1 Python/3.8.5
Date: Wed, 11 Nov 2020 17:52:41 GMT


<HTML><HEAD><meta http-equiv="content-type" content="text/html;charset=utf-8">
<TITLE>301 Moved</TITLE></HEAD><BODY>
<H1>301 Moved</H1>
The document has moved
<A HREF="http://localhost/">here</A>.
</BODY></HTML>
```

Not only does this say `HTTP/1.0 200 OK` when the *body* of the response says `301 Moved`, but it also has fewer items in the header.

This exercise served three purposes:

1. The actual response code of a HTTP request *does not have to match the response body*.
2. `curl -s -D - <url>` can be used to expose all the headers.
3. Despite the body being the same, the default headers of our flask app are not the same as those returned by `google.com`.

Look at point 3 again. **Despite the body being the same, the default headers of our flask app are not the same as those returned by `google.com`.**.

In the response you get from flask, the first *red flag* should be `Server: Werkzeug/1.0.1 Python/3.8.5`. Why?

This is telling any potential users of your API that your server is running on Werkzeug 1.0.1, using Python 3.8.5. Any malevolent user will just need to search for "vulnerabilities to exploit in Python 3.8.5" to get a list of ideas on how to bring down your app.

This is where we segui into the OWASP guidelines.

## OWASP Guidelines on Secure Headers

Open the [OWASP Secure Headers Project](https://owasp.org/www-project-secure-headers/#) and click on the `Response Headers` Tab. This displays the following list:

* HTTP Strict Transport Security (HSTS)
* X-Frame-Options
* X-Content-Type-Options
* Content-Security-Policy
* X-Permitted-Cross-Domain-Policies
* Referrer-Policy
* Feature-Policy
* Public Key Pinning Extension for HTTP (HPKP)
* Expect-CT
* X-XSS-Protection

This a list of the top ten best ways to ensure secure headers in an application. The link above provides detailed explanations of what these are and why you should be aware of them.
Explaining that is out of the scope of this post.

However, it is important that you add these headers into your own application. While you could theoretically learn how to do that with the flask
`app.after_request` hook and manually baking in the rules into that, there's an easier way: use `secure.py`.

## `secure.py`

`secure.py` is a minimal Python library that offers a way to add secure headers by default. It is designed with the OWASP guidelines in tow, and it is constantly updated
with the best practices baked in. The best part of it is that it is a uniform library that is agnostic of your framework, so Django devs, rejoice!

First, install `secure.py`:

```
pip install secure

```

Then, use this in a flask app.

```python
import flask
from secure import SecureHeaders

secure_headers = SecureHeaders()

app = flask.Flask(__name__)

@app.route("/")
def index():
    import textwrap
    html = textwrap.dedent("""
    <HTML><HEAD><meta http-equiv="content-type" content="text/html;charset=utf-8">
    <TITLE>Hello, World</TITLE></HEAD><BODY>
    <H1>Hello, World</H1>
    <P>Lorem ipsum dolor sit amet consectetur adipisicing elit. Perferendis quam, nisi ratione voluptatibus possimus eveniet odio iste id aperiam odit nihil provident ea a repellat consectetur repudiandae voluptas omnis placeat!</P>
    </BODY></HTML>
    """)
    return html, 200

@app.after_request
def set_secure_headers(response):
    secure_headers.flask(response)
    return response

```

`@app,after_request` allows you to add additional information to the response, or remove information from it. These lines of code ensure that your application
follows the OWASP Secure Headers guidelines to a T.

Let's try this out.

```bash
$curl -s -D - localhost:5000

HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 387
Strict-Transport-Security: max-age=63072000; includeSubdomains
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
Referrer-Policy: no-referrer, strict-origin-when-cross-origin
Pragma: no-cache
Expires: 0
Cache-control: no-cache, no-store, must-revalidate, max-age=0
Server: Werkzeug/1.0.1 Python/3.8.5
Date: Wed, 11 Nov 2020 18:18:38 GMT


<HTML><HEAD><meta http-equiv="content-type" content="text/html;charset=utf-8">
<TITLE>Hello, World</TITLE></HEAD><BODY>
<H1>Hello, World</H1>
<P>Lorem ipsum dolor sit amet consectetur adipisicing elit. Perferendis quam, nisi ratione voluptatibus possimus eveniet odio iste id aperiam odit nihil provident ea a repellat consectetur repudiandae voluptas omnis placeat!</P>
</BODY></HTML>
```

Now, you can see that a lot of additional headers have been added. These are the headers defined by the OWASP guidelines. However, `Server` is still present in the response. This is because
while it is *unsafe* to expose this information, it should be altered explicitly instead of
through a library since it may be necessary in some cases.

To address this, we can just add `response.headers.set("Server", "Secure")` in the `@app.after_request` function.

If you are interested, you may also use `SecureCookie` to add a cookie to the response.

```python
import flask
from secure import SecureHeaders
from secure import SecureCookie

secure_headers = SecureHeaders()
secure_cookie = SecureCookie(expires=1, samesite=SecureCookie.SameSite.STRICT)

app = flask.Flask(__name__)

@app.route("/")
def index():
    import textwrap
    html = textwrap.dedent("""
    <HTML><HEAD><meta http-equiv="content-type" content="text/html;charset=utf-8">
    <TITLE>Hello, World</TITLE></HEAD><BODY>
    <H1>Hello, World</H1>
    <P>Lorem ipsum dolor sit amet consectetur adipisicing elit. Perferendis quam, nisi ratione voluptatibus possimus eveniet odio iste id aperiam odit nihil provident ea a repellat consectetur repudiandae voluptas omnis placeat!</P>
    </BODY></HTML>
    """)
    return html, 200


@app.after_request
def set_secure_headers(response):
    secure_headers.flask(response)
    response.headers.set("Server", "Secure")
    secure_cookie.flask(response, name="spam", value="eggs")
    return response
```

Finally, let's take a look at that.

```bash
$ curl -s -D - localhost:5000

HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 387
Strict-Transport-Security: max-age=63072000; includeSubdomains
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
Referrer-Policy: no-referrer, strict-origin-when-cross-origin
Pragma: no-cache
Expires: 0
Cache-control: no-cache, no-store, must-revalidate, max-age=0
Server: Secure
Set-Cookie: spam=eggs; Expires=Wed, 11 Nov 2020 19:23:57 GMT; Secure; HttpOnly; Path=/; SameSite=Strict
Date: Wed, 11 Nov 2020 18:23:57 GMT


<HTML><HEAD><meta http-equiv="content-type" content="text/html;charset=utf-8">
<TITLE>Hello, World</TITLE></HEAD><BODY>
<H1>Hello, World</H1>
<P>Lorem ipsum dolor sit amet consectetur adipisicing elit. Perferendis quam, nisi ratione voluptatibus possimus eveniet odio iste id aperiam odit nihil provident ea a repellat consectetur repudiandae voluptas omnis placeat!</P>
</BODY></HTML>
```

As you can see, the `Server` has been set to `Secure`, and there is now a `Set-Cookie` header.

Each header added by `secure` can be customized. I recommend [reading the documentation](https://secure.readthedocs.io/en/latest/index.html) and deciding which to omit, if you feel that's absolutely necessary.

## X-Powered-By

There are some flask plugins that enable this particular header. While I am glad Flask (unlike electron) does not do this out of the box, I will say this.

*Do not, under any circumstances, advertise to your users what your API runs on.*

**Do not, under any circumstances, give potential hackers ideas on where to look for application vulnerabilities in your API**.

Both of these are *stupid ideas*. The only reason why you would like to advertise the stack of your API within the header would be if your API
is only accessed internally, by people you absolutely trust. Even then, developer documentation and access to the code base are better ideas.
Using `X-Powered-By` should never be a good idea.


## `httpie`

While `curl -s -D - <url>` solves the header visibility problem, I also recommend using `httpie` if you're looking for a more beginner-friendly tool.

`httpie` is installed by `pip`.

`pip install httpie`

```bash
$ http localhost:5000/

HTTP/1.0 200 OK
Cache-control: no-cache, no-store, must-revalidate, max-age=0
Content-Length: 387
Content-Type: text/html; charset=utf-8
Date: Wed, 11 Nov 2020 18:29:15 GMT
Expires: 0
Pragma: no-cache
Referrer-Policy: no-referrer, strict-origin-when-cross-origin
Server: Secure
Set-Cookie: spam=eggs; Expires=Wed, 11 Nov 2020 19:29:15 GMT; Secure; HttpOnly; Path=/; SameSite=Strict
Strict-Transport-Security: max-age=63072000; includeSubdomains
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block

<HTML><HEAD><meta http-equiv="content-type" content="text/html;charset=utf-8">
<TITLE>Hello, World</TITLE></HEAD><BODY>
<H1>Hello, World</H1>
<P>Lorem ipsum dolor sit amet consectetur adipisicing elit. Perferendis quam, nisi ratione voluptatibus possimus eveniet odio iste id aperiam odit nihil provident ea a repellat consectetur repudiandae voluptas omnis placeat!</P>
</BODY></HTML>
```

While this offers the same output, it also does this by default, and adds some nice colors to the output. Refer the documentation for more.


## References and Additional Tools

1. [OWASP Secure Headers Project](https://owasp.org/www-project-secure-headers/#)
2. [`secure.py`](https://secure.readthedocs.io/en/latest/index.html)
3. [Secure by Design - Book on Security best practices by Manning Publications](https://www.manning.com/books/secure-by-design)
4. [`hsecscan` - Python Tool to Check Headers of an API](https://github.com/riramar/hsecscan)
5. [`httpie` - Python Alternative for CURL](https://httpie.io/)
6. [OWASP Cheat Sheets](https://github.com/OWASP/CheatSheetSeries)
7. [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/v41/)
8. [OWASP Top 10 Web Application Security Risks](https://owasp.org/www-project-top-ten/)
