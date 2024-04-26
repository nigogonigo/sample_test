import csv
#機能概要
#list_fileに入れたCSVファイルを対象に、target_fileに入れた文言が含まれるのか検索する。
#検索にはorder_idを用いる。
#target_listが含まれていた場合、含まれた件数とuser_idを出力・ログ保存を行う。

#TODO：listに対して、ターゲットの内容を検索する処理を追加

def compare_csv(list,target):
    num = 0
    with open(list) as lf1:
        list_rows = csv.reader(lf1)
        csv_header = next(list_rows)
        for list_row in list_rows:
            # print('この時点のlistには{}が入っている'.format(list_row))
            with open(target) as tf1:
                target_rows = csv.reader(tf1)
                csv_header = next(target_rows)
                for target_row in target_rows:
                    # print('このシーケンスではtargetに{}が入っている'.format(target_row))
                    # print('このシーケンスではlist_row[0]に{}が入っている'.format(list_row[0]))
                    # print(type(target_row[0]))
                    # print(type(list_row[0]))
                    if list_row[0] == target_row[0]:
                        print('targetと同じorder_idを持つlistのuser_idは{}である'.format(list_row[1]))
                        num += 1
    print('target_listと同じorder_idを持つlistは{}である'.format(num))

list_file = "./csv/list.csv"
target_file = "./csv/target.csv"
compare_csv(list_file,target_file)