import json
import pandas as pd
import os
import shutil
import csv

DATA_DIR = "./data"
DATA_FILE = os.path.join(DATA_DIR, "NL_BO_SENSE_202012.csv")
DUMP_FILE = os.path.join(DATA_DIR, "dump.pkl")

base_titles = []
base_contents = []


def import_data(data_path=DATA_FILE):
    """
    Req. 1-1-1 음식점 데이터 파일을 읽어서 Pandas DataFrame 형태로 저장합니다
    """

    try:
        with open(data_path, 'rt', encoding="UTF8") as f:
            reader = csv.reader(f)

            stores = dict()  # {키워드 : [긍정, 부정], ... }
            print(reader)
            for d in reader:
                # 긍정 부정 점수
                rates = []
                rates.append(d[2])
                rates.append(d[3])
                # 저장소에 저장 딕셔너리로 추가
                stores[d[1]] = rates

            f.closed
            
            return stores

    except FileNotFoundError as e:
        print(f"`{data_path}` 가 존재하지 않습니다.")
        exit(1)


def check(content, scores):
    content_lst = content.split()
    positive_score = []
    negative_score = []
    for content_factor in content_lst:
        if len(content_factor) > 1 and content_factor[-1] in "은는이가의":
            # print("변경")
            content_factor = content_factor[:len(content_factor)-1]
        try:
            # print("점수측정")
            # print("스코어!!!!!!!!!! : ", scores[content_factor])
            positive_score.append(float(scores[content_factor][0]))
            negative_score.append(float(scores[content_factor][1]))
        except:
            # print("오류")
            continue
            
    total_positive_score = sum(positive_score)
    total_negative_score = sum(negative_score)
    
    score = max(total_positive_score, total_negative_score)
    if total_positive_score >= total_negative_score:
        state = 1
    else:
        state = 0

    return score, state


def get_title():
    # for _ in range(1):
    #     i = '02'
    for i in range(3, 13):
        if i == 9:
            continue
        if i < 10:
            i = '0' + str(i)
        else:
            i = str(i)
        
        FILE = os.path.join(DATA_DIR, f'NL_BO_BEST_BOOK_HISTORY_ARCHIVE_2021{i}.csv')
        try:
            with open(FILE, 'rt', encoding="UTF8") as f:
                reader = csv.reader(f)
                for r in reader:
                    base_titles.append(r[5])
                # title만 뽑자
                # f.closed


        except FileNotFoundError as e:
            print(f"`{FILE}` 가 존재하지 않습니다.")
            exit(1)


def get_detail():
    # for _ in range(1):
    #     i = '02'
    for i in range(3, 13):
        if i == 9:
            continue
        if i < 10:
            i = '0' + str(i)
        else:
            i = str(i)
        
        FILE = os.path.join(DATA_DIR, f'NL_BO_BEST_BOOK_HISTORY_ARCHIVE_2021{i}.csv')
        try:
            with open(FILE, 'rt', encoding="UTF8") as f:
                reader = csv.reader(f)
                for r in reader:
                    base_contents.append((r[5], r[7]))


        except FileNotFoundError as e:
            print(f"`{FILE}` 가 존재하지 않습니다.")
            exit(1)


def main():
    data = import_data()
    get_detail()

    results = list()
    for content in base_contents:
        score, state = check(content[1], data)
        if score == 0:
            continue
        results.append((content[0], content[1], score, state))

    results.sort(key=lambda x:(x[3], x[2]))
    # print(results)

    f = open('write.csv','w', newline='', encoding='UTF8')
    wr = csv.writer(f)
    i = 0
    for final_title, final_content, final_rate, final_state in results:
        i += 1
        if final_state == 1:
            final_state = "P"
        else:
            final_state = "N"
        wr.writerow([i, final_state, final_rate, final_title, final_content])
    
    f.close()


if __name__ == "__main__":
    main()
