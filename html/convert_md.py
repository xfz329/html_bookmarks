#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   converter.py    
@Contact :   Jiang Feng(silencejiang@zju.edu.cn)
@License :   (C)Copyright 2004-2020, Zhejiang University
"""

import re
import os
from bs4 import BeautifulSoup

def parse_bookmarks(html_file_path, output_file_path):
    with open(html_file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    soup = BeautifulSoup(content, 'html.parser')

    groups = {}
    for bookmark in soup.find_all('a'):
        url = bookmark.get('href')
        title = bookmark.get_text()
        group = bookmark.find_parent('h3').get_text() if bookmark.find_parent('h3') else '未分组'
        if group not in groups:
            groups[group] = []
        groups[group].append(f'[{title}]({url})')

    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        for group, bookmarks in groups.items():
            output_file.write(f'## {group}\n')
            for bookmark in bookmarks:
                output_file.write(f'- {bookmark}\n')

html_file_path = 'favorites_2024_8_8.html'  # 请将这里替换为您的书签 HTML 文件的实际路径
output_file_path = 'bookmarks.md'
parse_bookmarks(html_file_path, output_file_path)