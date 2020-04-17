import os
from time import sleep
from typing import List, Optional
from urllib.error import HTTPError
from urllib.request import urlopen

import regex
from bs4 import BeautifulSoup, Tag

from constants import (
    START_URL_REGEX,
    START_URL,
    PRODUCT_URL_TEMPLATE,
    DEFAULT_AMAZON_SELLER_ID,
    SELLER_URL_REGEX,
    OFFER_LISTING_URL_TEMPLATE,
    ITEM_PER_PAGE,
    MAX_REQUEST_RETRY
)


def get_soup(domain: str, asin: str, page_num: int = 1) -> BeautifulSoup:
    ol_page_url = OFFER_LISTING_URL_TEMPLATE.format(domain, asin, page_num, (page_num - 1) * ITEM_PER_PAGE)

    for _ in range(MAX_REQUEST_RETRY):
        try:
            page = urlopen(ol_page_url)
            break
        except HTTPError as e:
            if e.code == 503:
                sleep(10)
            else:
                raise e

    return BeautifulSoup(page, features="html.parser")


def get_seller_id(href: str) -> Optional[str]:
    match = regex.findall(SELLER_URL_REGEX, href)
    return match[0] if match else ''


def extract_href(tag: Tag) -> str:
    span = tag.find("div", class_="olpSellerColumn").h3.span

    return span.a["href"] if span else ""


def get_product_links(soup: BeautifulSoup) -> List[str]:
    rows = soup.find_all("div", attrs={"role": "row"})[1:]
    products_href = []

    for href in map(extract_href, rows):
        if href:
            seller_id = get_seller_id(href)
        else:
            seller_id = DEFAULT_AMAZON_SELLER_ID

        if seller_id:
            products_href.append(PRODUCT_URL_TEMPLATE.format(domain, asin, seller_id))

    return products_href


if __name__ == "__main__":
    print("Task starting...")

    match = regex.findall(START_URL_REGEX, START_URL)

    if match:
        domain, product_name, asin = match[0]
        file_name = f"{product_name[:15]}.txt" if product_name else "urls.txt"
    else:
        raise Exception("wrong START_URL structure")

    soup = get_soup(domain, asin)
    pagination_items = soup.find("ul", class_="a-pagination")

    if pagination_items:
        # list slicing for skip NavigableString in pagination_items
        page_count = len(list(pagination_items)[2:-1:2])
    else:
        page_count = 1

    os.chdir("files")

    with open(file_name, "w") as file:
        for page_num in range(page_count):

            if page_num:
                soup = get_soup(domain, asin, page_num + 1)

            links_list = get_product_links(soup)

            if links_list:
                file.writelines(links_list)

    os.chdir("..")

    print("Task ended.")
