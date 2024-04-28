import csv
####機能概要####
#list_fileに入れたCSVファイルを対象に、target_fileに入れた文言が含まれるのか検索する。
#検索にはorder_idを用いる。
#target_listが含まれていた場合、含まれた件数とuser_idを出力・ログ保存を行う。
#commit用(2024/4/28)

#TODO：listに対して、ターゲットの内容を検索する処理を追加

def compare_csv(list,target,output):
    num = 0
    sameid_list = []
    with open(list) as lf1:
        list_rows = csv.reader(lf1)
        csv_header = next(list_rows)
        for list_row in list_rows:
            #list_rowはorder_idが格納されており、10桁の数字となっている。そのため10桁以下をスキップする処理を加えて、処理負荷を下げる。
            if len(list_row[0]) > 9:
                with open(target) as tf1:
                    target_rows = csv.reader(tf1)
                    csv_header = next(target_rows)
                    for target_row in target_rows:
                        #target_rowの桁数チェック
                        if len(target_row[0]) > 9:
                            if list_row[0] == target_row[0]:
                                #print('targetと同じorder_idを持つlistのuser_idは{}である'.format(list_row[1]))
                                sameid_list.append(list_row[1])
                                num += 1
                        else:
                            print('target_row　{}は10桁に満たない。'.format(target_row[0]))
            else:
                print('list_row {}は10桁に満たない'.format(list_row[0]))
    with open(output, mode = 'w') as f:
        print('target_listと同じorder_idを持つlistは{}である'.format(num))
        #write logs
        f.write('target_listと同じorder_idを持つlistは{}である\n'.format(num))
        for word in sameid_list:
            print('targetと同じorder_idを持つlistのuser_idは「{}」である'.format(word))
            #write logs
            f.write('targetと同じorder_idを持つlistのuser_idは「{}」である\n'.format(word))

list_file = "./csv/list.csv"
target_file = "./csv/target.csv"
output_file = "./output/compare_output.txt"
#Initialize the output.txt
try:
    with open(output_file, mode = 'w') as fs:
        fs.truncate(0)
except OSError as e:
    print(e)
    
compare_csv(list_file,target_file,output_file)