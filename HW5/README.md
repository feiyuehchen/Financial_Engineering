Homework 5
===

學習歷程
---
這次是一次很有挑戰性的作業，除了hull white model和quantlib的中文資源很少之外，方法也較為複雜，如果沒有老師在pdf提供的外部連結供參考的話，不知道會熬夜多久XD  
在這次的作業中，很大一部份不能確認自己的答案是否正確的原因有三個：  
第一個是由於是隨機過程，所以沒有固定答案
第二個是，hw model的利率依賴一開始給的sigma, a, foward rate，如果沒有設定好的話，最後折現的call 和option price會很醜，例如我一開始給定sigma和a都是0.1，forword rate是0.05，算出來的r（每單位時間）的期望值大概在0.2~0.8之間，期數為360，年數為30，結果最後算出來的call價格好幾百萬....
後來改成sigma和a都是0.001，forward rate是0.01之後就好多了。
第三個是，由於無風險利率也是自行設定的，所以要跟上面的sigma和a配合，不然折現過後的call和put價格也會超級醜。


流程圖
---
[連結](https://github.com/feiyuehchen/Financial_Engineering/blob/master/HW5/hw5_流程圖.pdf)



程式碼
---
[連結](https://github.com/feiyuehchen/Financial_Engineering/blob/master/HW5/hw5_code.ipynb)




