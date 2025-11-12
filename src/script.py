"""
Reddit Publisher
A simple Python script to publish posts (text and images) on Reddit using PRAW.
"""

import os
import praw


def get_flair_template(flairs, key):
    """
    Get flair template ID by index or text.
    
    Args:
        flairs (list): List of available flair templates
        key (int|str): Flair index (int) or flair text (str)
    
    Returns:
        str|None: Flair template ID if found, None otherwise
    """
    if isinstance(key, int):
        if 0 <= key < len(flairs):
            return flairs[key]['flair_template_id']
    elif isinstance(key, str):
        for flair in flairs:
            if flair['flair_text'].lower() == key.lower():
                return flair['flair_template_id']
    return None


def publish_to_reddit(subreddit_name, title, config, flair=None, content=None, image_path=None):
    """
    Publish a post on Reddit (text or image).
    
    Args:
        subreddit_name (str): Target subreddit name
        title (str): Post title
        config (module): Configuration module with Reddit credentials
        flair (str|int, optional): Flair text or index
        content (str, optional): Text content for text posts
        image_path (str, optional): Path to image file for image posts
    
    Returns:
        praw.models.Submission|None: Submission object if successful, None otherwise
    """
    # Validate configuration
    required_vars = ['REDDIT_CLIENT_ID', 'REDDIT_CLIENT_SECRET',
                     'REDDIT_USERNAME', 'REDDIT_PASSWORD']
    
    missing_vars = [var for var in required_vars if not hasattr(config, var)]
    if missing_vars:
        print("❌ Missing configuration variables:")
        for var in missing_vars:
            print(f"   - {var}")
        print("\nPlease create a config.py file with these variables.")
        return None

    reddit = praw.Reddit(
        client_id=config.REDDIT_CLIENT_ID,
        client_secret=config.REDDIT_CLIENT_SECRET,
        username=config.REDDIT_USERNAME,
        password=config.REDDIT_PASSWORD,
        user_agent=getattr(config, 'REDDIT_USER_AGENT', 'RedditPublisher/1.0')
    )

    print(f"Connected as: {config.REDDIT_USERNAME}")

    try:
        subreddit = reddit.subreddit(subreddit_name)

        # Handle flair selection
        flair_id = None
        if flair is not None:
            try:
                flairs = list(subreddit.flair.link_templates.user_selectable())
                flair_id = get_flair_template(flairs, flair)
                if flair_id:
                    print(f"✓ Flair selected: {flair}")
                else:
                    print(f"⚠ Flair '{flair}' not found")
            except Exception as e:
                print(f"⚠ Unable to fetch flairs: {e}")

        # Image post
        if image_path:
            print(f"\n📸 Publishing image post...")

            if not os.path.exists(image_path):
                raise FileNotFoundError(f"Image not found: {image_path}")

            submission = subreddit.submit_image(
                title=title,
                image_path=image_path,
                flair_id=flair_id
            )

        # Text post
        else:
            print(f"\n📝 Publishing text post...")
            submission = subreddit.submit(
                title=title,
                selftext=content or "",
                flair_id=flair_id
            )

        print(f"\n✅ Post published successfully!")
        print(f"   URL: {submission.url}")
        print(f"   ID: {submission.id}")

        return submission

    except FileNotFoundError as e:
        print(f"\n❌ {str(e)}")
        return None
    except praw.exceptions.APIException as e:
        print(f"\n❌ Reddit API Error: {e.error_type}")
        print(f"   Message: {e.message}")
        return None
    except Exception as e:
        print(f"\n❌ Error during publication: {str(e)}")
        import traceback
        traceback.print_exc()
        return None