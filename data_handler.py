"""Data read/write and manipulation functions."""
import csv
from datetime import datetime, timedelta
from typing import Any
import string
import random

HEADERS_QUESTION: list[str] = ['id', 'submission_time', 'view_number',
                    'vote_number', 'title', 'message', 'image']
HEADERS_ANSWER: list[str] = ['id', 'submission_time', 'vote_number',
                            'question_id', 'message', 'image']

def get_data_from_file(filename: str) -> list[Any]:
    """Read data from file into list of dictionaries."""
    with open(filename, 'r', encoding='UTF-8') as data:
        data_list = []
        reader = csv.DictReader(data)
        for item in reader:
            data_list.append(item)
        return data_list


def write_data_to_file(headers, filename: str, data_dict: dict[str, str]):
    """Write dictionaries to file."""
    with open(filename, 'a+', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writerow(data_dict)
    print('end')


dict_1 = {'id': '1', 'submission_time': '2', 'view_number': '3', 'vote_number': '4', 'title': '5', 'message': '6', 'image': '7'}
print(dict_1)
write_data_to_file(HEADERS_QUESTION, 'question.csv', dict_1 )


def generate_id():
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    alphabet = list(string.ascii_lowercase)
    data = get_data_from_file('question.csv')
    ids = []
    for question in data:
        ids.append(question['id'])
    id = random.choice(numbers) + random.choice(numbers) +random.choice(alphabet)
    if id in ids:
        generate_id()
    else:
        return id

def count_comments() -> dict[str, int]:
    """Get comment count for each question."""
    comments_count = {}
    questions = get_data_from_file('sample_data/question.csv')
    answers = get_data_from_file('sample_data/answer.csv')
    for question in questions:
        for key, value in question.items():
            if key == 'id':
                comments_count.update({value: 0})
    for answer in answers:
        for key, value in answer.items():
            if key == 'question_id':
                comments_count[value] += 1
    return comments_count


def sorter(data_dict: list[dict[str, str]], sort_by='date',
           direction='descending') -> list[dict[str, str]]:
    """Sort given data by specific header."""
    order_translate: dict[str, str] = {'date': 'submission_time',
                    'title': 'title', 'message': 'message',
                    'views': 'view_number', 'votes': 'vote_number',
                    'comments': 'comments'}
    if sort_by in ['date', 'views', 'votes']:
        ordered = sorted(data_dict,
                        key=lambda k: int(k[order_translate[sort_by]]),
                        reverse=direction == 'descending')
        return ordered
    if sort_by != 'comments':
        ordered = sorted(data_dict,
                        key=lambda k: k[order_translate[sort_by]],
                        reverse=direction == 'descending')
        return ordered
    comments: dict[str, int] = count_comments()
    comments = sorted(comments.items(), key=lambda k: k[1],
                    reverse=direction == 'descending')
    ordered_set: set[dict[str, str]] = set()
    for key in comments.keys():
        for item in data_dict:
            if key == item['id']:
                ordered_set.add(item)
    for item in data_dict:
        if item not in ordered_set:
            ordered_set.add(item)
    return list(ordered_set)


def how_much_time_passed(unix_date: int) -> str:
    """Calculate how much time has passed since date."""
    time_now: datetime = datetime.now()
    time_then: datetime = datetime.fromtimestamp(int(unix_date))
    delta: timedelta = time_now - time_then
    delta: timedelta = delta - timedelta(microseconds=delta.microseconds)
    time_list: list[str] = str(delta).split(',')
    if len(time_list) == 1:
        hours, minutes, seconds = [int(time) for time in time_list[0].split(':')]
        if hours > 0:
            return f'{hours} hours ago'
        if minutes > 0:
            return f'{minutes} minutes ago'
        if seconds > 0:
            return f'{seconds} seconds ago'
    days = int(time_list[0].split(' ')[0])
    if (days // 365) > 0:
        return f'{days // 365} years ago'
    return f'{days} days ago'



def generate_id() -> str:
    """Generate new id."""
