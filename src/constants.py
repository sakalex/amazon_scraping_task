
START_URL = "https://www.amazon.co.uk/AMD-Ryzen-3900X-Processor-Cache/dp/B07SXMZLP9/"  # 4 offer-list pages
# START_URL = 'https://www.amazon.co.uk/Sony-MDRZX310-Foldable-Headphones/dp/B00I3LUWQA/'  # 2 offer-list pages


START_URL_REGEX = r"^(?P<domain>.+?\/\/.+?|.+?)\/(?P<product_name>.+?)\/dp\/(?P<asin>[A-Z0-9]{10})"  # domain, product_name, asin
SELLER_URL_REGEX = r"seller\=(?P<seller_id>[A-Z0-9]+)"  # seller_id

# template use OFFER_LISTING_URL_TEMPLATE.format(domain, asin, page_num, offset)
# offset = (1 - page_num) * ITEM_PER_PAGE
OFFER_LISTING_URL_TEMPLATE = "{}/gp/offer-listing/{}/ref=olp_page_{}?ie=UTF8&startIndex={}"

# template use PRODUCT_URL_TEMPLATE.format(domain, asin, seller)
PRODUCT_URL_TEMPLATE = "{}/dp/{}?m={}\n"

DEFAULT_AMAZON_SELLER_ID = "A3P5ROKL5A1OLE"

ITEM_PER_PAGE = 10

MAX_REQUEST_RETRY = 3
