from src.script import publish_to_reddit
import config


def main():
    """Main function with usage examples."""
    print("=== Reddit Publisher ===\n")

    # Example usage (uncomment to use):
    
    # Example 1: Text post
    #publish_to_reddit(
    #    subreddit_name="test",
    #    title="Test text post",
    #    config=config,
    #    content="This is a test text post"
    #)

    # Example 2: Image post
    # publish_to_reddit(
    #    subreddit_name="test",
    #    title="Test image post",
    #    config=config,
    #    image_path="path/to/your/image.png"
    # )

    # Example 3: Post with flair
    # publish_to_reddit(
    #    subreddit_name="LearnToReddit",
    #    title="post with flair",
    #    config=config,
    #    flair=1,
    #    content="Post content here"
    #)

    print("✓ Setup complete!")
    print("Uncomment example code above to test publishing.")


if __name__ == "__main__":
    main()