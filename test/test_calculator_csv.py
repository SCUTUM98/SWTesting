import csv

def load_csv(path):
    # Load CSV
    cases = []
    with open(path, newline='', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        
        print('========== CSV ==========')
        for row in reader:
            print(row)
            
            a = row['a']
            b = row['b']
            expected = row['expected_result']
            
            cases.append((a, b, expected))
        print('========== Tuple ==========\n',cases)
        
        return cases
    
    # 별도의 close 과정 없이 with 가 파일 로드 후 close
    # windows에서 생성한 csv에서 헤더가 읽히는 경우 encoding을 utf-8 에서 utf-8-sig 로 변경
    
def trans(s):
    if s == '':
        return None
    try:
        return int(s)
    # int 형 변환
    except ValueError:
        return s
    # int 변환 실패시 char 그대로 사용