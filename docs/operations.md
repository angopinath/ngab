Operations
===
```shell script
python3 audio_book.py \
--pdf {filename} \
--page_range {staring page and ending page} \
--title {title of the story} \
--author {author of the story} \
--genre {genre about the story} \
--language {lanuage of pdf file} \
--speed {audio speed 0-1} \
--output {output location} \
--verbose
```

**Example:**

```shell script
python3 /mnt/c/Users/gopn/gerrit/ngab/src/main/python/audio_book.py \
--pdf /mnt/c/Users/gopn/Downloads/Aysha.pdf \
--page_range 9 44 \
--title "Aysha" \
--author "R. Natarajan" \
--genre "short" "moral" \
--language TA \
--speed 0.7 \
--output /mnt/c/Users/gopn/gerrit/ngab/audiobooks \
--verbose
```

**Davgiyen kadhalan**

```shell script
python3 /mnt/c/Users/gopn/gerrit/ngab/src/main/python/audio_book.py \
--pdf /mnt/c/Users/gopn/Downloads/Devagiyin_Kanavan.pdf \
--title "Devagiyin Kanavan" \
--author "kalki" \
--genre "short" "fantacy" \
--language TA \
--speed 0.7 \
--output /mnt/c/Users/gopn/gerrit/ngab/audiobooks \
--verbose
```

**ெபா􀂢􀂞􀁴􀂢 ெச􀂄வ􀂢**
```shell script
python3 /mnt/c/Users/gopn/gerrit/ngab/src/main/python/audio_book.py \
--pdf /mnt/c/Users/gopn/Downloads/ponniyin-selvan.pdf \
--page_range 49 54 \
--title "அத்தியாயம் 6: நடுநிசிக் கூட்டம்" \
--album "பொன்னியின் செல்வன்" \
--author "கல்கி ரா. கிருஷ்ணமூர்த்தி" \
--genre "Novel" "Fantacy" \
--language TA \
--speed 0.7 \
--output /mnt/c/Users/gopn/gerrit/ngab/audiobooks/ponniyin_selvan \
--verbose
```