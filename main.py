import feedparser


def main():
    feed = feedparser.parse("https://hnrss.org/frontpage")

    with open("./feeds.md", "w") as f:
        f.write(f"# {feed['feed']['title']}\n\n")
        for item in feed["entries"]:
            title = item["title"]
            link = item["link"]
            f.write(f"- [{title}]({link})\n")


if __name__ == "__main__":
    main()
