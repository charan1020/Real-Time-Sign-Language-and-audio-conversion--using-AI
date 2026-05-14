# Netlify Deployment

This project deploys to Netlify as a static version of the Django templates.
Netlify does not run the Django `gunicorn` server or the local desktop
camera/audio Python scripts.

## Netlify settings

The repository root contains `netlify.toml`, so Netlify can auto-detect these
settings:

- Build command: `python build_netlify_static.py`
- Publish directory: `dist`

If you configure the site manually in the Netlify UI, use the same values.

## What works on Netlify

- Home page
- About page
- Contact page
- Login and registration demo pages
- User home page
- Static CSS, JavaScript, fonts, and images

## What does not run on Netlify

The following features need a separate Python backend, desktop app, or another
hosting provider that supports long-running Python processes and system access:

- Microphone capture
- Camera capture
- `detect_gesture.py`
- `blogs/main2.py`
- TensorFlow, PyTorch, MediaPipe, OpenCV inference
- SQLite writes at runtime

For the full Django app, deploy to a Python server platform instead, such as
Render, Railway, Fly.io, a VPS, or AWS. Netlify can still host the static
frontend and call that backend through HTTP APIs.
