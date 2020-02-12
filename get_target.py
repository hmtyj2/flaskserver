import client


def get_target_page(input_words):
    db = client.ClientDb()
    max_page_n = int(db.select_all("max_page")[0]["contents"])
    target_page_idx = -1
    m=10000
    for i in range(1,max_page_n+1):
        page = db.select_all(str(i)+"_rank")  # list

        score=0
        for search_word in input_words:
            is_find = False
            for col in page:
                if search_word == col["title"]:
                    score += int(col["contents"])
                    is_find=True
            if not is_find:
                score += 200

        if score<m:
            m=score
            target_page_idx=i

    return target_page_idx