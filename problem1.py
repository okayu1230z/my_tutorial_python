# 1. IndentationErrorをキャッチしよう

def main():
  try:
    print("")
    # ここにコードを記述してIdentationErrorをキャッチしてください。
  except IndentationError as ie:
    print("IndentationErrorの例外をキャッチしました。おめでとう！")
    raise IndentationError
  except Exception as e:
    print("その他の例外: " + e + " をキャッチしました。")

if __name__ == '__main__':
    main()