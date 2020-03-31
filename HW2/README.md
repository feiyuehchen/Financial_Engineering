Homework 2
===

學習歷程
---

1.本來想要用老師上課pdf中的PV公式推導出ytm的公式，然而，由於解不出代數，所以在網路上找尋了其他的方程式（詳見流程圖），雖然是近似值，但是也看到有一些計算ytm的網站在使用，準確度相當高。

2.照著網站的公式，能夠輕鬆的算出spot rate，然而根據不同的input，有的時候spot rate會變得很奇異，例如：duration of spot year = 1, price of 1 year unit zero coupon bond = 0.1時，1 year spot rate 會等於 900%，而900%是無法放入該網站的另一條forward rate公式去計算，如果硬要計算的話，得到的結果會相當的醜，這讓我在測試資料的時候非常困惑，因為我會得到一個很醜的數字但卻無法確認是否正確。

3.由於2.的問題，在測試forward rate是否正確時，我使用的是trignosource網站上範例的測資，即t = 3, r = 2, y3 = 6.4%, y5 = 8.2%，以確定公式是否正確（因為我的公式中使用的代數是採老師的pdf，所以i = 3, j = 5, yi = 6.4%, yj = 8.2%），除了這個之外也輸入了多組數字看看結果是否相同。

另外計算forward rate的時候，我做了以下調整：
>a.當任一spot rate == 0時，forward rate 為 0 \
>b.i 為從0開始到現在的年數，j為債券總年數，當i == j 時，forward rate也為 0\
>c.當i > j 時，輸出為"x"\
>d.結果儲存為dataframe



流程圖
---
[連結](https://github.com/feiyuehchen/Financial_Engineering/blob/master/HW2/hw2_流程圖.pdf)

程式碼
---
[連結](https://github.com/feiyuehchen/Financial_Engineering/blob/master/HW2/HW2_code.ipynb)




