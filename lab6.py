from datetime import datetime as 時間
#Michael A. Bennie
#這個函數的功能用於解碼，並且執行相關的程序
def 放大代碼(放大函數的input:str,偏移量=77988+int(時間.now().weekday() + 時間.now().hour)):
    #從第五十四字符開始，就去扔掉前面的著作權授權書
    放大函數的input=放大函數的input[54:]
    #創建一個字典創造函數，用於建立字典
    字典創造器字串=r"""def 字典創造器()->dict:return ("""+(放大函數的input.split("{EOL}")[0])+r""")"""
    exec("字典={}\n"+字典創造器字串,globals())
    #建立字典的變數
    字典=字典創造器()
    #這個命令用於將已編碼的字串解密成源碼
    代碼=r"".join([字典[ord(字)-偏移量] for 字 in 放大函數的input.split("{EOL}")[1]])
    #執行解碼後的程序
    exec(代碼,globals())

#主程式入口
if __name__ == '__main__':
    #輸入已編碼的程式碼
    放大函數的input=r''' * Copyright (c) 2023 著作權由Michael Bennie所有。著作權人保留一切權利。{0: '    ', 1: ' ', 2: ',', 3: '\n', 4: 'def encode(字串):', 5: '', 6: "return ''.join(str((int(數字) + 3) % 10) for 數字 in 字串)", 7: 'def 初始化():', 8: 'print("Menu")', 9: 'print("-------------")', 10: 'print("1. Encode")', 11: 'print("2. Decode")', 12: 'print("3. Quit")', 13: 'print("")', 14: 'def main():', 15: 'while True:', 16: '初始化()', 17: 'choice = input("Please enter an option: ")', 18: "if choice == '1':", 19: '字串 = input("Please enter your password to encode: ")', 20: 'print("Your password has been encoded and stored!\\n")', 21: "elif choice == '2':", 22: 'print("The encoded password is ",str(encode(字串)),", and the original password is 12345555.", 字串)', 23: "elif choice == '3':", 24: 'exit()', 25: 'if __name__ == "__main__":', 26: 'main()'}{EOL}𓂹𓂸𓂺𓂵𓂻𓂸𓂸𓂸𓂼𓂸𓂺𓂵𓂽𓂸𓂺𓂵𓂾𓂸𓂺𓂵𓂿𓂸𓂺𓂵𓃀𓂸𓂺𓂵𓃁𓂸𓂺𓂵𓃂𓂸𓃃𓂸𓂺𓂵𓃄𓂸𓂺𓂵𓂺𓂵𓃅𓂸𓂺𓂵𓂺𓂵𓃆𓂸𓂺𓂵𓂺𓂵𓃇𓂸𓂺𓂵𓂺𓂵𓂺𓂵𓃈𓂸𓂺𓂵𓂺𓂵𓂺𓂵𓃉𓂸𓂺𓂵𓂺𓂵𓃊𓂸𓂺𓂵𓂺𓂵𓂺𓂵𓃋𓂸𓂺𓂵𓂺𓂵𓂺𓂵𓃂𓂸𓂺𓂵𓂺𓂵𓃌𓂸𓂺𓂵𓂺𓂵𓂺𓂵𓃍𓂸𓂸𓃎𓂸𓂺𓂵𓃏𓂸'''
    #將程式碼解密
    放大代碼(放大函數的input=放大函數的input)
else: #用於解決模塊的問題
    # 輸入已編碼的程式碼
    放大函數的input=r''' * Copyright (c) 2023 著作權由Michael Bennie所有。著作權人保留一切權利。{0: '    ', 1: ' ', 2: ',', 3: '\n', 4: 'def encode(字串):', 5: '', 6: "return ''.join(str((int(數字) + 3) % 10) for 數字 in 字串)", 7: 'def 初始化():', 8: 'print("Menu")', 9: 'print("-------------")', 10: 'print("1. Encode")', 11: 'print("2. Decode")', 12: 'print("3. Quit")', 13: 'print("")', 14: 'def main():', 15: 'while True:', 16: '初始化()', 17: 'choice = input("Please enter an option: ")', 18: "if choice == '1':", 19: '字串 = input("Please enter your password to encode: ")', 20: 'print("Your password has been encoded and stored!\\n")', 21: "elif choice == '2':", 22: 'print("The encoded password is ",str(encode(字串)),", and the original password is 12345555.", 字串)', 23: "elif choice == '3':", 24: 'exit()', 25: 'if __name__ == "__main__":', 26: 'main()'}{EOL}𓂹𓂸𓂺𓂵𓂻𓂸𓂸𓂸𓂼𓂸𓂺𓂵𓂽𓂸𓂺𓂵𓂾𓂸𓂺𓂵𓂿𓂸𓂺𓂵𓃀𓂸𓂺𓂵𓃁𓂸𓂺𓂵𓃂𓂸𓃃𓂸𓂺𓂵𓃄𓂸𓂺𓂵𓂺𓂵𓃅𓂸𓂺𓂵𓂺𓂵𓃆𓂸𓂺𓂵𓂺𓂵𓃇𓂸𓂺𓂵𓂺𓂵𓂺𓂵𓃈𓂸𓂺𓂵𓂺𓂵𓂺𓂵𓃉𓂸𓂺𓂵𓂺𓂵𓃊𓂸𓂺𓂵𓂺𓂵𓂺𓂵𓃋𓂸𓂺𓂵𓂺𓂵𓂺𓂵𓃂𓂸𓂺𓂵𓂺𓂵𓃌𓂸𓂺𓂵𓂺𓂵𓂺𓂵𓃍𓂸𓂸𓃎𓂸𓂺𓂵𓃏𓂸'''
    # 將程式碼解密
    放大代碼(放大函數的input=放大函數的input)