import argparse
import os
import glob
import re
import logging
from enum import Enum
from collections import namedtuple

from PIL import Image
import pytesseract
from pdf2image import convert_from_path
from tts.mytts import gTTS
import music_tag

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

SAVE_AS_TEXT = True
OUTPUT_BASE_PATH = '/mnt/c/Users/gopn/gerrit/ngab/audiobooks'
Lang = namedtuple('Lang', ['pdf', 'audio'])
AudioMeta = namedtuple('audioMeta', ['title', 'author', 'tags'])


class Language(Enum):
    TA = Lang('tam', 'ta')
    EN = Lang('eng', 'en')

    def __str__(self):
        return self.name

    @staticmethod
    def from_string(s):
        try:
            return Language[s]
        except KeyError:
            raise ValueError()


def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--pdf', help='Pdf file', required=True)
    parser.add_argument('--page_range', help='Page number range', required=False, nargs=2, type=int)
    parser.add_argument('--title', help='name of the audio file', required=True)
    parser.add_argument('--author', help='author', required=True)
    parser.add_argument('--tags', help='tags', required=True, nargs='+')
    parser.add_argument('--language', help='content language', required=True, type=Language.from_string, choices=list(Language))
    parser.add_argument('--speed', help='audio speed', required=False, default=0.7, type=float)
    parser.add_argument('--output', help='output location', required=False, default=OUTPUT_BASE_PATH)
    parser.add_argument('--verbose', help='log verbose', action='store_true')
    return parser.parse_args()


def create_images_from_page(pdf: str, page_range: list, path: str) -> list:
    logger.debug('creating images be reading pdf file: pdf file->{}, page range->{}, image path->{}'.format(pdf, page_range, path))
    if page_range:
        return convert_from_path(
            pdf_path=pdf,
            output_folder=path,
            first_page=page_range[0],
            last_page=page_range[1],
            paths_only=True,
            dpi=300
        )
    return convert_from_path(
        pdf_path=pdf,
        output_folder=path,
        paths_only=True,
        dpi=300
    )


def image_path(base_path: str, title: str) -> str:
    path = os.path.join(base_path, title)
    logger.debug("path: {}".format(path))
    os.makedirs(path, exist_ok=True)
    return path


def get_page_contents(pages: list, language: str) -> str:
    contents = []
    for page in pages:
        text = str(pytesseract.image_to_string(Image.open(page), lang=language))
        contents.append(text)
        logger.debug("page content: " + text)
    return " ".join(contents)


def pre_process_content(content: str) -> list:
    content = content.replace("-\n", "")
    content = re.sub(r'[\n]{2,}', '. ', content)
    content = re.sub(r'[\s]{2,}', ' ', content)
    content = " ".join(content.splitlines())
    content = re.sub(r'[\\.]{2,}', '.', content)
    content = content.replace('.,', ',')

    content_list = re.split(r'[.,?]', content)
    logger.debug("preprocessed content: {}".format(content_list))
    return [c.strip() + "." for c in content_list if c and c.strip()]


def form_audio_file(path: str, title: str) -> str:
    return os.path.join(path, title+".mp3")


def form_text_file(path: str, title: str) -> str:
    return os.path.join(path, title+".txt")


def create_audio(contents: list, language: str, audio_file: str, audio_speed: float) -> None:
    with open(audio_file, 'wb') as file:
        for content in contents:
            if content:
                logging.debug("converting audio for the text {}".format(content))
                engine = gTTS(content, lang=language, lang_check=False)
                engine.write_to_fp(file)


def log_handler(verbose):
    stream = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s: %(message)s')
    stream.setFormatter(formatter)
    if verbose:
        stream.setLevel(logging.DEBUG)
        logger.setLevel(logging.DEBUG)
    else:
        stream.setLevel(logging.INFO)
        logger.setLevel(logging.INFO)
    logger.addHandler(stream)


def post_cleanup(path: str):
    for f in glob.glob(os.path.join(path, "*.ppm")):
        os.remove(f)


def create_text_file(file, contents):
    with open(file, 'w+') as f:
        f.writelines("%s\n" % content for content in contents)
    logger.debug("text file as been created: {}".format(file))


def add_audio_meta(audio_file, audio_meta):
    meta = music_tag.load_file(audio_file)
    meta['title'] = audio_meta.title
    meta['artist'] = audio_meta.author
    meta['genre'] = ','.join(audio_meta.tags)
    meta.save()


def main():
    args = arg_parser()
    log_handler(args.verbose)
    logger.debug("input args: {}".format(args))

    language = args.language.value
    audio_meta = AudioMeta(args.title, args.author, args.tags)
    output_path = image_path(args.output, audio_meta.title)
    text_file = form_text_file(output_path, audio_meta.title)
    audio_file = form_audio_file(output_path, audio_meta.title)
    try:
        pages = create_images_from_page(args.pdf, args.page_range, output_path)
        contents = get_page_contents(pages, language.pdf)
        processed_contents = pre_process_content(contents)
        if SAVE_AS_TEXT:
            create_text_file(text_file, processed_contents)

        create_audio(processed_contents, language.audio, audio_file, args.speed)
        add_audio_meta(audio_file, audio_meta)
        logger.info('audio book {} has been created successfully'.format(audio_file))
    except Exception:
        logger.exception("Error while creating story audio")
    finally:
        post_cleanup(output_path)


if __name__ == '__main__':
    main()
    #add_audio_meta("/Users/gopn/Music/Villain Theme.mp3", AudioMeta(title='test', author='test1', tags=['tes'], ))

