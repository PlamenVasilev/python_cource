data = input()
forum_dict = {}

while not data == 'filter':
    topic = data.split(' -> ')[0]
    tags = data.split(' -> ')[1].split(', ')
    if topic not in forum_dict:
        forum_dict[topic] = tags
    else:
        forum_dict[topic].extend(tags)

    data = input()

filter_list = input().split(', ')
for topic, tags in forum_dict.items():
    unique_tags_list = sorted(set(tags), key=tags.index)
    if set(filter_list).issubset(unique_tags_list):
        print(f'{topic} | {", ".join([f"#{t}" for t in unique_tags_list])}')
        #print(f'{topic} | {", ".join(map(lambda x: "#"+x, unique_tags_list))}')
