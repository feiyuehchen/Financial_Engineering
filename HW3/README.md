Homework 3
===

學習歷程
---

一開始想說，既然input都是確定的，那我就做一個彈性/擴充性很低的程式，雖然醜而且很難修改，但至少可以算出答案吧！要是寫一個彈性很好的程式，結果算不出答案來就好笑了。
順利算出答案之後，發現自己的code超醜ＸＤ所以去參考了一下其他同學的code，發現其他同學有做能夠自由改變input的code，覺得我這樣實在不太行，就做了三個function：
1.payoff()用來計算call和put的payoff，可以用"call"和"put"切換公式
2.probability()考慮不同n的情況，所以不只能帶入n = 3了，而能夠彈性的變化
3.PV()用來讓code更加簡潔，使用者之後只需要呼叫PV，就能得到value

最後因為不太確定自己的答案，所以我有使用put-call parity檢查答案是否正確。



流程圖
---
[連結](https://github.com/feiyuehchen/Financial_Engineering/blob/master/HW3/hw3_流程圖.pdf)

程式碼
---
[連結](https://github.com/feiyuehchen/Financial_Engineering/blob/master/HW3/HW3_code.ipynb)




