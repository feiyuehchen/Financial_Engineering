Homework 5
===

學習歷程
---
這次是一次很有挑戰性的作業，除了hull white model和quantlib的中文資源很少之外，方法也較為複雜，如果沒有老師在pdf提供的外部連結供參考的話，不知道會熬夜多久XD
在這次的作業中，很大一部份不能確認自己的答案是否正確的原因有三個：
第一個是由於是隨機過程，所以沒有固定答案
第二個是，hw model的利率依賴一開始給的sigma和a，而無風險利率也是自行設定的，所以如果兩者之間沒有配合好的話，最後折現的call 和option price會很醜，例如在我的code中，給定sigma和a都是0.1，算出來的r（每單位時間）的期望值大概在0.2~0.8之間，如果無風險利率沒有配合好這個數子的話，很容易出現0.00000....的價格。
最後就是dt的大小會嚴重影響ST的價格，之前我dt不小心設太大，結果S0為100，ST變成上萬....（目前是讓dt = 年數/期數）


流程圖
---
[連結](https://github.com/feiyuehchen/Financial_Engineering/blob/master/HW5/hw5_流程圖.pdf)



程式碼
---
[連結](https://github.com/feiyuehchen/Financial_Engineering/blob/master/HW5/hw5_code.ipynb)




