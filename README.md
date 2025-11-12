# Reddit Publisher 🚀

A simple and efficient Python script to publish posts (text and images) on Reddit using PRAW (Python Reddit API Wrapper).

## Features ✨

- 📝 Publish text posts
- 📸 Publish image posts
- 🏷️ Support for post flairs
- ✅ Configuration validation
- 🛡️ Comprehensive error handling
- 🎯 Easy-to-use interface

## Prerequisites 📋

- Python 3.7+
- A Reddit account
- Reddit API credentials (see setup below)

## Installation 🔧

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/reddit-publisher.git
cd reddit-publisher
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Create your configuration file
```bash
cp config.example.py config.py
```

## Reddit API Setup 🔑

### Step 1: Create a Reddit App

1. Go to https://www.reddit.com/prefs/apps
2. Click "Create App" or "Create Another App"
3. Fill in the form:
   - **Name**: Your app name (e.g., "My Reddit Publisher")
   - **App type**: Select "script"
   - **Description**: Optional
   - **About URL**: Optional
   - **Redirect URI**: http://localhost:8080 (required but not used)
4. Click "Create app"

### Step 2: Get your credentials

5. Note your credentials:
   - **client_id**: The string under your app name (e.g., "abc123def456")
   - **client_secret**: The string next to "secret"

## Configuration ⚙️

Edit `config.py` with your Reddit credentials:

```python
# Reddit API Credentials
REDDIT_CLIENT_ID = "your_client_id"
REDDIT_CLIENT_SECRET = "your_client_secret"
REDDIT_USERNAME = "your_reddit_username"
REDDIT_PASSWORD = "your_reddit_password"

# Optional: Custom user agent
REDDIT_USER_AGENT = "RedditPublisher/1.0 by /u/your_username"
```

⚠️ **Important**: 
- Never commit `config.py` to version control (it's in `.gitignore`)
- If you have 2FA enabled, you need to generate an app password in Reddit settings

## Usage 💻

### Test your configuration

```bash
python test_config.py
```

### Basic Examples

#### Text Post
```python
from src.script import publish_to_reddit
import config

publish_to_reddit(
    subreddit_name="test",
    title="My first post",
    config=config,
    content="This is the content of my post"
)
```

#### Image Post
```python
publish_to_reddit(
    subreddit_name="test",
    title="Check out this image",
    config=config,
    image_path="path/to/image.png"
)
```

#### Post with Flair
```python
publish_to_reddit(
    subreddit_name="test",
    title="Discussion topic",
    config=config,
    flair="Discussion",  # Flair name or index
    content="Let's discuss this topic"
)
```

### Run Examples

```bash
python example.py
```

Edit `example.py` and uncomment the examples you want to test.

## Function Reference 📚

### `publish_to_reddit()`

```python
publish_to_reddit(
    subreddit_name: str,
    title: str,
    config: module,
    flair: str|int = None,
    content: str = None,
    image_path: str = None
) -> praw.models.Submission|None
```

**Parameters:**
- `subreddit_name` (str): Target subreddit name (without "r/")
- `title` (str): Post title
- `config` (module): Configuration module with Reddit credentials
- `flair` (str|int, optional): Flair text or index number
- `content` (str, optional): Text content for text posts
- `image_path` (str, optional): Path to image file for image posts

**Returns:**
- `Submission` object if successful
- `None` if an error occurred

## Troubleshooting 🔍

### Error 401: Authentication Failed

- ✅ Verify your `client_id` and `client_secret`
- ✅ Check your username and password
- ✅ If 2FA is enabled, use an app password
- ✅ Run `python test_config.py` to diagnose

### Error 403: Forbidden

- The subreddit may have restrictions
- Your account might be too new
- Check if you're banned from the subreddit

### Image Not Found

- Verify the image path is correct
- Use absolute paths or relative paths from script location
- Supported formats: PNG, JPG, JPEG, GIF

### Flair Not Found

- Check available flairs in the subreddit
- Use exact flair name (case-insensitive)
- Or use flair index (0, 1, 2, etc.)

## Project Structure 📁

```
reddit-publisher/
├── src/
│   └── script.py        # Core publishing functions
├── example.py           # Usage examples
├── test_config.py       # Configuration testing
├── config.py            # Your credentials (not in git)
├── config.example.py    # Configuration template
├── requirements.txt     # Python dependencies
├── .gitignore          # Git ignore file
└── README.md           # This file
```

## License 📄

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer ⚠️

This tool is for educational purposes. Please follow Reddit's:
- [API Terms of Use](https://www.reddit.com/wiki/api-terms)
- [Content Policy](https://www.redditinc.com/policies/content-policy)
- Subreddit-specific rules

Excessive posting or spam may result in account suspension.

## Author ✍️

Created by CodinghubStudio

## Acknowledgments 🙏

- [PRAW](https://praw.readthedocs.io/) - Python Reddit API Wrapper
- Reddit API Documentation

---

**Star ⭐ this repository if you find it helpful!**
