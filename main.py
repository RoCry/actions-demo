import datetime
import os

import feedparser


def main():
    feed = feedparser.parse("https://hnrss.org/frontpage")

    with open("./feeds1.md", "w") as f1, open("./feeds2.md", "w") as f2:
        time_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        title = f"# {feed['feed']['title']} {time_str}\n\n"
        print(f"::set-output name=title::{title}")
        f1.write(title)
        f2.write(title)
        for item in feed["entries"]:
            title = item["title"]
            link = item["link"]
            f1.write(f"- [{title}]({link})\n")
            f2.write(f"- [{title}]({link})\n")

    body = "\n".join(map(lambda e: "- " + e["title"], feed["entries"]))
    print(f"::set-output name=body::{body}")
    put_github_action_env("E_BODY", body)
    put_github_action_env("RELEASE_FILES", "feeds1.md\nfeeds2.md")


def put_github_action_env(key: str, value: str):
    env_file = os.getenv('GITHUB_ENV')
    if env_file is None:
        raise Exception("GITHUB_ENV is not set")

    with open(env_file, "a") as f:
        f.write(f"{key}<<EOF\n{value}\nEOF\n")


if __name__ == "__main__":
    main()
