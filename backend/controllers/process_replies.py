def process_replies(comment):
    replies = []
    for reply_item in comment.get("replies", {}).get("comments", []):
        reply = reply_item["snippet"]
        replies.append(
            [
                reply.get("authorDisplayName"),
                reply.get("publishedAt"),
                reply.get("likeCount"),
                reply.get("textOriginal"),
            ]
        )
    return replies
