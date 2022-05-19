import feedparser


def main():
    feed = feedparser.parse("https://hnrss.org/frontpage")

    with open("./feeds1.md", "w") as f1, open("./feeds2.md", "w") as f2:
        f1.write(f"# {feed['feed']['title']}\n\n")
        f2.write(f"# {feed['feed']['title']}\n\n")
        for item in feed["entries"]:
            title = item["title"]
            link = item["link"]
            f1.write(f"- [{title}]({link})\n")
            f2.write(f"- [{title}]({link})\n")
            print(f"::set-output name=title::{title}")

    body = "\n".join(map(lambda e: "- " + e["title"], feed["entries"]))
    print(f"::set-output name=body::{body}")
    print(f"::set-output name=files::'feeds1.md\nfeeds2.md'")


if __name__ == "__main__":
    main()
