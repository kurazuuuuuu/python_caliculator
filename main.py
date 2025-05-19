import sys
import tkinter as tk
from tkinter import ttk

BUTTON = [
    ['', 'B', 'C', '/'],
    ['7', '8', '9', '*'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+'],
    ['00', '0', '.', '=']
]

SYMBOL = [
    '+', '-', '*', '/'
]

class CalculatorGUI(object):
    def __init__(self, app=None):

        self.calc_str = ''

        app.title("Python Calculator")
        app.geometry("400x600")

        calculator_frame = tk.Frame(app, width=300, height=100) #計算式・結果表示用フレーム
        calculator_frame.propagate(False) #サイズ固定
        calculator_frame.pack(side=tk.TOP, padx=10, pady=10) #padding

        button_frame = tk.Frame(app, width=300, height=300) #ボタン用フレーム
        button_frame.propagate(False) #サイズ固定
        button_frame.pack(side=tk.BOTTOM) #padding

        self.calculate_value = tk.StringVar() #計算式・結果表示用変数
        self.result_value = tk.StringVar() #計算結果表示用変数
        calculate_label = tk.Label(calculator_frame, textvariable=self.calculate_value, font=("", 20)) #計算式表示用ラベル
        result_label = tk.Label(calculator_frame, textvariable=self.result_value, font=("", 15)) #計算結果表示用ラベル
        calculate_label.pack(anchor = tk.E)
        result_label.pack(anchor = tk.E)

        for y, row in enumerate(BUTTON, 1): #enumerateでボタン配置
            for x, num in enumerate(row):
                button = tk.Button(button_frame, text=num, font=("", 15), width=6, height=3) #button_frame関数・引数からボタン作成
                button.grid(row=y, column=x) #gridでボタン配置
                button.bind("<Button-1>", self.click_button) #ボタンを押したときのイベント呼び出し用

    def click_button(self, event):
        check = event.widget['text'] # 押したボタンのCheck

        if check == '=': # イコールの場合
            if self.calc_str[-1:] in SYMBOL: # 記号の場合、記号よりも前で計算
                self.calc_str = self.calc_str[:-1]

            res = '= ' + str(eval(self.calc_str)) # eval関数の利用
            self.result_value.set(res)
        elif check == 'C': # クリアの場合
            self.calc_str = ''
            self.result_value.set('')
        elif check == 'B': # バックの場合
            self.calc_str = self.calc_str[:-1]
        elif check in SYMBOL: # 記号の場合
            if self.calc_str[-1:] not in SYMBOL and self.calc_str[-1:] != '':
                self.calc_str += check
            elif self.calc_str[-1:] in SYMBOL: # 記号の場合、入れ替える
                self.calc_str = self.calc_str[:-1] + check
        else: # 数字などの場合
            self.calc_str += check

        self.calculate_value.set(self.calc_str)

def main():
    app = tk.Tk()
    CalculatorGUI(app)

    app.mainloop()

if __name__ == "__main__":
    main()