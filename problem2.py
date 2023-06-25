# 2. with文で動作するオリジナルクラスを作ろう
# csvを読み込んだら、各行のカラム数を表示することのできるwithで動作する独自クラスを作成しよう
#
# 例えば、data.csvを読み込んで以下のように表示されればOK
# __enter__
# 4
# 4
# 2
# __exit__

class MyCsvReader:
  def __init__(self, file_name):
    self.file_name = file_name

  def __enter__(self):
    print('__enter__')
    self.file_obj = open(self.file_name, 'r')
    col_number = []
    # ここに処理を追加して処理を実現させる
    return col_number

  def __exit__(self, type, value, traceback):
    print('__exit__')
    self.file_obj.close()

with MyCsvReader('data.csv') as f:
  for i in f[0:]:
    print(i)
