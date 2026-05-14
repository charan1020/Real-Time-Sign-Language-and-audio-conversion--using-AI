from pathlib import Path
import re
import shutil


ROOT = Path(__file__).resolve().parent
PROJECT_DIR = ROOT / "Audio_Sign_Conversion_Project new" / "Translator"
TEMPLATE_DIR = PROJECT_DIR / "blogs" / "templates"
STATIC_DIR = PROJECT_DIR / "blogs" / "static"
DIST_DIR = ROOT / "dist"

URLS = {
    "homepage": "/",
    "login": "/login/",
    "registration": "/registration/",
    "about": "/about/",
    "contact": "/contact/",
    "userhome": "/userhome/",
    "audio_sign": "/userhome/",
    "sign_audio": "/userhome/",
}

PAGES = {
    "index.html": "index.html",
    "about.html": "about/index.html",
    "contact.html": "contact/index.html",
    "login.html": "login/index.html",
    "registration.html": "registration/index.html",
    "userhome.html": "userhome/index.html",
}


def django_static(match):
    return f"/static/{match.group(1)}"


def django_url(match):
    return URLS.get(match.group(1), "/")


def render_template(template_name):
    html = (TEMPLATE_DIR / template_name).read_text(encoding="utf-8")
    html = re.sub(r"{%\s*load\s+static\s*%}", "", html)
    html = re.sub(r"{%\s*csrf_token\s*%}", "", html)
    html = re.sub(r"{%\s*static\s+'([^']+)'\s*%}", django_static, html)
    html = re.sub(r'{%\s*static\s+"([^"]+)"\s*%}', django_static, html)
    html = re.sub(r"{%\s*url\s+'([^']+)'\s*%}", django_url, html)
    html = re.sub(r'{%\s*url\s+"([^"]+)"\s*%}', django_url, html)
    html = re.sub(r"{%\s*if\s+msg\s*%}.*?{%\s*endif\s*%}", "", html, flags=re.S)
    html = html.replace("{{msg}}", "")
    html = html.replace('action="/login/" method="post"', 'action="/userhome/" method="get"')
    html = html.replace('action="/registration/" method="post"', 'action="/login/" method="get"')
    return html


def write_page(source, destination):
    target = DIST_DIR / destination
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(render_template(source), encoding="utf-8")


def main():
    if DIST_DIR.exists():
        shutil.rmtree(DIST_DIR)
    DIST_DIR.mkdir()

    shutil.copytree(STATIC_DIR, DIST_DIR / "static")
    for source, destination in PAGES.items():
        write_page(source, destination)

    (DIST_DIR / "_headers").write_text(
        "/*\n"
        "  X-Frame-Options: DENY\n"
        "  X-Content-Type-Options: nosniff\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
