import csv
import numpy as np

def split_csv(csv_file):
    # Hot Temp [℃]를 기준으로 split합니다.

    rdr = list(csv_file)

    new_data = []
    split_num = []

    for a, line in enumerate(rdr):
        if len(line) > 0:
            if line[1] == 'Hot Temp [℃] ':
                split_num.append(a)

    split_num.append(len(rdr)-1)

    for i in range(len(split_num) - 1):
        new_data.append(rdr[split_num[i]:split_num[i + 1] - 1])

    print("split 결과")
    print(str(len(new_data))+"개")
    return new_data

def split_col(data, index):

    col_data = []
    for a, i in enumerate(data):
        if a != 0:
            col_data.append(float(i[index]))
    print(data[0][index])

    return np.array(col_data)


# csv 불러오기
f = open('Cu13_3-Raw.csv', 'r')
rdr = csv.reader(f)
split_data = split_csv(rdr)
f.close()


for i in split_data:
    for j in i:
        print(j)
    print("\n\n")


temp = split_col(split_data[0],10)
print(temp.mean())



# csv 저장
f = open('write.csv', 'w', newline='')

wr = csv.writer(f)
wr.writerow([1, '림코딩', '부산'])
wr.writerow([2, '김갑환', '서울'])

f.close()



# zero_crossing
# sum_x = np.where(sum_x > 3060, 1, 0)
# zero_crossings = np.where(np.diff(sum_x) != 0)[0]
