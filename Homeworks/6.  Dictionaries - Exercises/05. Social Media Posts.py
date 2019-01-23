data = input()
social_media_dict = {}

while not data == 'drop the media':
    command = data.split()[0]
    post_name = data.split()[1]

    if command == 'post':
        social_media_dict[post_name] = {
            'likes': 0,
            'dislikes': 0,
            'comments': []
        }

    elif command == 'like':
        if post_name in social_media_dict.keys():
            social_media_dict[post_name]['likes'] += 1

    elif command == 'dislike':
        if post_name in social_media_dict.keys():
            social_media_dict[post_name]['dislikes'] += 1

    elif command == 'comment':
        if post_name in social_media_dict.keys():
            author = data.split()[2]
            comment = data.split()[3:]

            if post_name in social_media_dict.keys():
                social_media_dict[post_name]['comments'].append({
                    'author': author,
                    'content': " ".join(comment)
                })

    data = input()


for (post_name, post_data) in social_media_dict.items():
    print(f'Post: {post_name} | Likes: {post_data["likes"]} | Dislikes: {post_data["dislikes"]}')
    print('Comments:')
    if len(post_data['comments']):
        for comment in post_data['comments']:
            print(f"*  {comment['author']}: {comment['content']}")
    else:
        print('None')
