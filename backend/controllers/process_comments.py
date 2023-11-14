from . import process_replies


def process_comments(response):
    comments = []
    for item in response.get("items", []):
        comment = item["snippet"]["topLevelComment"]["snippet"]
        comments.extend(process_replies.process_replies(item))
        comments.append(
            [
                comment.get("authorDisplayName"),
                comment.get("publishedAt"),
                comment.get("likeCount"),
                comment.get("textOriginal"),
            ]
        )
    return comments
