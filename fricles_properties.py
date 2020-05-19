__author__ = 'supertramp'


db_info = {
    'db' : 'content',
    'coll' : 'articles13',
    "kw_review" : "kw_review",
    "search_inputs":"search_inputs",
    "stats_db" : "stats",
    "stats_coll" : "demo2"
}
news_properties = {
    "news_article_limit" : 100
}
fricles_basic_properties = {
    "fricles_rest_server" : "localhost",
    "fricles_logfile_name" : "fricles.log",
    "fricles_rest_port" : 8000,
    "fricles_logsize" : 200000000,
    "fricles_logger_level" : 10, #Numeric value { NOTSET : 0, DEBUG:10, INFO:20, WARNING:30,ERROR:40,CRITICAL:50 }
    "fricles_logger_disabled" : False,
    "fricles_version" : "0.1"
}

nltk_properties = {
    'use_custom_data_path': 1,
    'custom_path_list' : ['/home/ubuntu/nltk_data']
}


twitter_properties = {
    'CONSUMER_KEY' : "LmB8VsCKuSHghK8NLhJCfw",
    'CONSUMER_SECRET' : "sKEEeNxlm1CG8X0LT0wJzu0X1Nb2F7UiCz6Ra3Vcbk",
    'OAUTH_TOKEN' : "195801966-pCLl7NBI5NXlYpV7sBTJe6ZcAPSRhHmxRyfrkTa8",
    'OAUTH_TOKEN_SECRET' : "m4tvEMjXY1R42HZzR7V89lYkGSSaMwJOn5Vk3fisbQ",
    'default_tweet_count' : 10
}

default_cleanup_rules = {
    'remove_unicode' : True,
    'remove_url' : False,
    'expand_acronyms' : True,
    'shorten_word' : True,
    'shorten_punctuations' : True,
    'remove_spl_characters' : True
}

file_properties = {
    "import_file" : "src/data_sources/xls/simulated_portfolio.xlsx"
}
