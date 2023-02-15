from string import Template

VERSION = '0.1.0-alpha'
REPO_URL = 'https://github.com/TheShooter89/tgc-data-inspector/'

SPLASH_TEXT = Template("""+-------------------------------------+
|  tgc-data-inspector (v$version)  |
|                         by @tanque  |
+-------------------------------------+
(repo: $repo_url)""")

def render_splash_text():
    """docstring for render_splash_text"""
    text = SPLASH_TEXT.substitute(version=VERSION, repo_url=REPO_URL)

    return print(text)


if __name__ == "__main__":
    render_splash_text()
