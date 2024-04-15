
import re

from bs4 import BeautifulSoup
from tqdm import tqdm


def cut_html():
    file_path = 'data/user_support.html'
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()[-1000:]
    html_content = '\n'.join(lines)
    with open('data/user_support_short.html', 'w', encoding='utf-8') as output_file:
        output_file.write(html_content)


def read_in_chunks(file_path, chunk_size=1024):
    """
    Generator to read a file chunk by chunk
    :param file_path: Path to the file
    :param chunk_size: Size of each chunk to be read (in bytes)
    :return: Generator object yielding chunks of data
    """
    with open(file_path, 'rb') as file:
        while True:
            data = file.read(chunk_size)
            if not data:
                break
            yield data


def parse_questions(soup):
    new_lines = []
    # find all class=chatlog__message-primary div
    message_primary = soup.find_all('div', class_='chatlog__message-primary')
    # itrate all message-primary div
    for message in message_primary:
        reply = message.find('div', class_='chatlog__reply-content')
        content = message.find('div', class_='chatlog__content')
        if reply and content:
            content_str = content.text.strip()
            content_fixed = re.sub(r'\n+', '\n', content_str)

            reply_str = reply.text.replace('\n\n', ' ').strip()
            if 'deleted' in content_fixed or 'deleted' in reply_str:
                continue
            if 'scam' in content_fixed or 'scam' in reply_str:
                continue
            new_lines.append('Q:' + reply_str)
            new_lines.append('A:' + content_fixed)
            new_lines.append('\n')
    return new_lines


def parse_questions_v2(soup):
    new_lines = []
    message_primary = soup.find_all('div', class_='chatlog__message-primary')
    for message in message_primary:
        author = message.find('span', class_='chatlog__author')
        content = message.find('div', class_='chatlog__content')
        if content:
            content_str = content.text.strip()
            content_fixed = re.sub(r'\n+', '\n', content_str)
            if author:
                author_str = author.text.strip()[0:10]
                msg = f'{author_str} said: {content_fixed}'
            else:
                msg = f'{content_fixed}'
            new_lines.append(msg)
    return new_lines


def convert_html_to_txt():
    file_path = 'data/user_support.html'
    chunk_size = 1024 * 100

    # Reading the file in chunks
    all_lines = []
    chunks = read_in_chunks(file_path, chunk_size)
    for html in tqdm(chunks):
        # Process each html here
        # print(len(html))
        soup = BeautifulSoup(html, 'html.parser')
        lines = parse_questions(soup)
        all_lines += lines
        # break

    with open('data/user_support.txt', 'w', encoding='utf-8') as output_file:
        output_file.write('\n'.join(all_lines))


if __name__ == '__main__':
    # cut_html()
    convert_html_to_txt()
