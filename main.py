import datetime
import os

import feedparser


def main():
    feed = feedparser.parse("https://hnrss.org/frontpage")

    with open("./feeds1.md", "w") as f1, open("./feeds2.md", "w") as f2:
        time_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        title = f"# {feed['feed']['title']} {time_str}\n\n"
        f1.write(title)
        f2.write(title)
        for item in feed["entries"]:
            title = item["title"]
            link = item["link"]
            f1.write(f"- [{title}]({link})\n")
            f2.write(f"- [{title}]({link})\n")
            print(f"::set-output name=title::{title}")

    body = "\n".join(map(lambda e: "- " + e["title"], feed["entries"]))
    print(f"::set-output name=body::{body}")
    os.environ["RELEASE_FILES"] = "feeds1.md\nfeeds2.md"


if __name__ == "__main__":
    main()
