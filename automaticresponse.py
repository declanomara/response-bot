import praw
import time

from load import *
from save import *


def print_subs(subreddits):
    print("Currently watching these subs:")
    for sub in subreddits:
        print(f"    {sub}")
    print("")

def print_phrases(phrases):
    print("Currently responding to these phrases:\n")
    for phrase, response in phrases.items():
        print(f"    Phrase:{phrase}")
        print(f"    Response:{response}")
        print("")


def analyze_comment(comment, phrases, reddit):
    for search, response in phrases.items():
        if(search in comment.body) and (comment.author.name != reddit.user.me().name):
            comment.reply(response)
            print(f"Replied to comment by {comment.author.name}")


def analyze_subreddit(reddit, subreddit, phrases, unsaved_processed_ids, saved_processed_ids):
    for comment in reddit.subreddit(subreddit).comments():
        if not ((comment.id in saved_processed_ids) or (comment.id in unsaved_processed_ids)):
            unsaved_processed_ids.append(comment.id)

            #Make use of untouched comment
            analyze_comment(comment, phrases, reddit)

        else:
            return("Complete")



def main():
    reddit = praw.Reddit('bot1', user_agent='autoresponsebot')
    print(f"Current user: {reddit.user.me().name}")

    print("Loading config...")
    config = load_config('config.cfg')
    print("Config loaded.\n")


    saved_processed_ids = load_processed_ids(config['save_file'])
    unsaved_processed_ids = []
    subreddits = load_subreddits(config['subreddits'])
    print_subs(subreddits)
    phrases = load_phrases(config['phrases'])
    print_phrases(phrases)

    watch = True
    while watch:
        for subreddit in subreddits:
            try:
                analyze_subreddit(reddit, subreddit, phrases, unsaved_processed_ids, saved_processed_ids)

            except:
                print("Error: Sleeping for 1 minute")
                time.sleep(60)

        save_processed_ids(config['save_file'], saved_processed_ids, unsaved_processed_ids)


main()
