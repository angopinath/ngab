Operations
===
```shell script
python3 audio_book.py \
--pdf {filename} \
--page_range {staring page and ending page} \
--title {title of the story} \
--author {author of the story} \
--tags {tags about the story} \
--language {lanuage of pdf file} \
--speed {audio speed 0-1} \
--output {output location} \
--verbose
```

**Example:**

```shell script
python3 /mnt/c/Users/gopn/gerrit/ngab/src/main/python/audio_book.py \
--pdf /mnt/c/Users/gopn/Downloads/Aysha.pdf \
--page_range 9 11 \
--title "Aysha" \
--author "R. Natarajan" \
--tags "short" "moral" \
--language TA \
--speed 0.7 \
--output /mnt/c/Users/gopn/gerrit/ngab/audiobooks \
--verbose

```