### NBER WORKING PAPER SERIES 

COMPETITION FOR ATTENTION IN THE ETF SPACE 

Itzhak Ben-David Francesco Franzoni Byungwook Kim Rabih Moussawi 

Working Paper 28369 http://www.nber.org/papers/w28369 

NATIONAL BUREAU OF ECONOMIC RESEARCH 1050 Massachusetts Avenue Cambridge, MA 02138 January 2021, Revised January 2022 

We thank Thummim Cho, Nicola Gennaioli, Wes Gray, Denis Gromb, Elisabeth Kempf, Steve Oh, Amin Shams, Matt Sheridan, Andrei Shleifer, Jim Simpson (ETP Resources), René Stulz, David Thesmar, Petra Vokata, Rodrigo Wagner, and the seminar audience at the University of Colorado at Boulder, Bank for International Settlements, The Ohio State University, AEA meetings, the Virtual Finance Seminar in Corporate Finance and Investments, Democratize Quant Conference, the Frankfurt School of Finance & Management, National University of Singapore, Santiago Finance Workshop, and CFA (Lugano chapter) seminars for helpful comments. We are especially grateful to Alp Simsek for detailed comments. Ben- David is with The Ohio State University and the National Bureau of Economic Research. Franzoni is with USI Lugano, the Swiss Finance Institute, and the Center for Economic and Policy Research. Kim is with The Ohio State University. Moussawi is with Villanova University and Wharton Research Data Services. Ben-David is a co-founder and a partner in an investment advisor.  The views expressed herein are those of the authors and do not necessarily reflect the views of the National Bureau of Economic Research. 

NBER working papers are circulated for discussion and comment purposes. They have not been peer-reviewed or been subject to the review by the NBER Board of Directors that accompanies official NBER publications. 

© 2021 by Itzhak Ben-David, Francesco Franzoni, Byungwook Kim, and Rabih Moussawi. All rights reserved. Short sections of text, not to exceed two paragraphs, may be quoted without explicit permission provided that full credit, including © notice, is given to the source. 

Competition for Attention in the ETF Space Itzhak Ben-David, Francesco Franzoni, Byungwook Kim, and Rabih Moussawi NBER Working Paper No. 28369 January 2021, Revised January 2022 JEL No. G12,G14,G15 

### **<u>ABSTRACT</u>** 

The interplay between investors' demand and providers' incentives has shaped the evolution of exchange-traded funds (ETFs). While early ETFs invest in broad-based indexes and therefore offered diversification at low cost, later products track niche port- folios and charge high fees. Strikingly, over their first five years, specialized ETFs lose about 30% in risk-adjusted terms. This underperformance cannot be explained by high fees or hedging demand. Rather, it is driven by the overvaluation of the underlying stocks at the time of the launch. Our results are consistent with providers catering to investors' extrapolative beliefs by issuing specialized ETFs that track attention- grabbing themes. 

Itzhak Ben-David The Ohio State University Fisher College of Business 606A Fisher Hall Columbus, OH 43210-1144 and NBER ben-david.1@osu.edu 

Byungwook Kim The Ohio State University Fisher College of Business 606 Fisher Hall Columbus, OH 43210-1144 kim.7336@osu.edu 

Rabih Moussawi Francesco Franzoni Villanova University Swiss Finance Institute 800 Lancaster Ave Via G. Buffi 13 Bartley 2051 6904, Lugano - Switzerland Villanova, PA 19085 and University of Lugano Rabih.Moussawi@villanova.edu francesco.franzoni@usi.ch 

# **1 Introduction** 

The wide adoption of exchange-traded funds is often celebrated as the democratization of investments (e.g., Novick, 2017).<sup>1</sup> According to this view, investors—no matter how small—can use ETFs to achieve portfolio diversification at a low cost as well as obtain long and short exposure to a wide variety of investment styles without the intermediation of expensive asset managers. However, this narrative may not accurately and completely describe investors’ experience with these products. In practice, the ETFs currently available in the market originate from the interplay of investor demand and the profit-maximizing incentives of ETF providers. Some investors may use ETFs as inexpensive buy-and-hold portfolios, while others may use them to speculate based on their beliefs—rational or not. Therefore, to assess the merits of the greatest financial innovation of the last decades, we need to investigate how providers respond to investor demand. 

The goal of this paper is to study the dynamics of financial innovation in the ETF industry and their potential implications for product performance. Our evidence helps explain the evolution of the ETF landscape and sheds new light on investors’ experience with these products. Overall, our findings suggest that the ETF industry has evolved along two separate paths. Broad-based ETFs offer investors an opportunity to achieve diversification at a low cost. Other, more expensive, specialized ETFs appear to cater to investor demand for popular, yet overvalued, investment themes. As a result, their performance is on average disappointing. 

Prior literature has already studied the dynamics of financial innovation, but the specific nature of ETFs motivates a fresh look at these issues. For example, the providers of active mutual funds, relying on the fact that managerial skill is not observable, tend to promote a positive track record as an implicit promise of good future performance (e.g., Jain and Wu, 

> 1An exchange-traded fund (ETF) is a pooled investment vehicle whose shares are traded on exchanges. In 2021, the assets managed by ETFs in the United States alone surpassed the $6 trillion mark, amounting to about 18% of the total assets in U.S. investment companies. To date, over 3,400 ETFs have been launched, covering a wide array of investments, from broad-based indexes like the S&P 500 to niche investment themes, such as a trade war, cannabis, vegan products, work from home, and COVID-19 vaccines. 

1 

2000). Also, the sponsors of structured products exploit the opaqueness of these vehicles to tout their high yields and shroud risks.<sup>2</sup> However, ETFs are different from other financial products (e.g., mutual funds) in that their portfolios are more transparent and the investment style is passive; hence, it does not involve managerial skill. Moreover, the short time-tomarket of ETFs (as short as 75 days) and their intraday liquidity make these products more suited to cater to investor demand for popular investment themes. Therefore, previously studied competitive strategies may not be relevant in this context. 

As a first approximation on the dynamics of innovation in the ETF market, Figure 1 provides a bird’s eye view of the evolution of the ETF “species” over time. The left axis shows the average annual fees that these products charge their investors, a proxy for their direct cost. The markers’ colors reflect the degree of differentiation with respect to the existing products in the market. The first breed of ETFs that came into existence in 1993 tracked broad-based indexes and charged low fees. Over time, tighter competition in this segment of the market has led to even lower fees. To preserve high margins, the response of the ETF industry has been to launch higher priced breeds of ETFs that diverge from existing products, focusing on more specialized indexes. The industry, therefore, appears to have progressed toward more differentiated products, and this evolution has allowed incumbents and new entrants to remain profitable despite the growing competition. 

Our analysis has two main parts. In the first part, we propose that the dynamics of competition in the ETF industry fit the framework of Bordalo, Gennaioli, and Shleifer (2016). The authors model the behavior of suppliers in a market in which consumers have limited attention. To attract consumers, firms can make different product attributes salient. As a result, competition can occur along the _price_ and _quality_ dimensions. While in their model 

> 2See Henderson and Pearson (2011), C´el´erier and Vall´ee (2017), Henderson, Pearson, and Wang (2020), Gao, Hu, Kelly, Peng, and Zhu (2020), and Vokata (2021). More generally, prior literature has studied the competitive strategies of the providers of financial products in the context of closed-end funds (Lee, Shleifer, and Thaler, 1991), fixed-income securities (Gennaioli, Shleifer, and Vishny, 2012; Greenwood and Hanson, 2013), mutual funds (Elton, Gruber, and Rentzler, 1989; Arteaga, Ciccotello, and Grant, 1998; Massa, 1998; Khorana and Servaes, 1999; Cooper, Gulen, and Rau, 2005; Evans, 2010; Kostovetsky and Warner, 2020, among others), and equity offerings (Baker and Wurgler, 2007). 

2 

### **Figure 1. The Evolution of the ETF Species** 

The figure shows the average annual fees and the degree of product differentiation per ETF category weighted by their assets under management (AUM): broad-index ETFs, smart-beta ETFs, sector/industry ETFs, and thematic ETFs. The sample period is from 1993 to 2019. The _y_ -axis shows average fees, and the colors of the markers represent the average degree of product differentiation, computed as one minus the cosine similarity between the ETF portfolio weights and the weights of the aggregate portfolio of all ETFs that exist in the market at that point in time. Section 3 provides information about the classification of ETFs. 



<!-- Start of picture text -->
70 Broad-index ETFs<br>0 . 9<br>Smart-beta ETFs<br>65 Sector/industry ETFs<br>60 Thematic ETFs 0 . 8<br>55 0 . 7<br>50<br>0 . 6<br>45<br>40 0 . 5<br>35<br>0 . 4<br>30<br>25 0 . 3<br>20<br>0 . 2<br>15<br>10 0 . 1<br>5<br>0<br>1995 2000 2005 2010 2015<br>(bps)Fees<br>Differentiation<br><!-- End of picture text -->

the market converges to either a price-salient or a quality-salient equilibrium, to describe the structure of the ETF industry, we extend the interpretation of this framework. We suggest that the two equilibria can coexist and characterize different segments of the ETF industry. Specifically, broad-based ETFs compete on price, while more specialized ETFs compete along the quality dimension. We interpret quality as other salient product attributes, different from price, that investors may find attractive. 

The empirical evidence is consistent with segmentation in the ETF industry corresponding to the price-salient and quality-salient equilibria. Our sample consists of nearly all equity ETFs that ever traded in the U.S. equity market. We classify as _broad-based_ all ETFs that track broad market indexes, i.e., the broad-index and smart-beta categories in Figure 1. These two groups differ only in that the latter adopts portfolio weights different from market capitalization. We classify as _specialized_ the ETFs that invest in a specific sector or in sectors that are tied by a theme, i.e., the sector/industry and thematic categories in Fig- 

3 

ure 1. As of December 2019, specialized ETFs managed 18% of the industry’s assets, yet they generated about 36% of the industry’s fee revenues. In the market for broad-based products, ETFs hold large portfolios and compete on price by offering similar portfolios at a low cost. In the specialized segment, ETFs hold small and differentiated portfolios and charge higher fees. 

Providing further support for the conjecture of a segmented market, we find a marked difference between the two groups of products in the sensitivity of investors’ demand to ETF fees and to past performance. Specifically, flows to broad-based ETFs display a significantly higher sensitivity to fees, whereas flows to specialized ETFs are unrelated to fees and respond more strongly to past performance. Moreover, high media exposure of the stocks in an ETF portfolio reduces the sensitivity of flows to fees, suggesting that investors neglect the fees charged by ETFs when their attention is drawn to other product attributes. 

In the second part of our analysis, we study what makes specialized ETFs attractive to investors, that is, we investigate the _quality_ aspect of specialized ETFs. The first obvious candidate is that ETF providers are able to identify sectors and themes that deliver positive risk-adjusted returns and issue products that track them. 

Our tests show that this is not the case. In fact, we find that the performance of specialized ETFs is disappointing in terms of both raw and risk-adjusted returns. A portfolio of all specialized ETFs achieves risk-adjusted returns of _−_ 3 _._ 1% per year, after fees. This underperformance is due mostly to recently launched specialized ETFs, which grossly underperform: about _−_ 6% annually in the first five years after inception. In comparison, the performance of broad-based ETFs is slightly negative, though statistically indistinguishable from zero. The underperformance of specialized ETFs is not explained by their higher fees or trading frictions, and has similar magnitude when considering the underlying indexes directly. The absolute size of the underperformance of specialized ETFs is non-negligible in dollar terms given their sizeable assets under management (AUM)—about $460 billion at the end of our sample period. Figure 2 illustrates this result. 

4 

### **Figure 2. Performance of ETFs Around Launch** 

The figure shows the performance of ETFs around launch, split by groups of broad-based and specialized ETFs. The sample period is from 2000 to 2019. For each ETF group, we form 60 calendar-time portfolios that include returns of ETFs in their month +1 _,_ +2 _, . . . ,_ +60 since the launch date (month 0). The portfolio returns are value-weighted using one-month-lagged market capitalization. We have 60 time series of portfolio returns per ETF category. To adjust returns for risk factors, we estimate the Fama-FrenchCarhart four-factor model (FFC-4) alphas of the portfolios (Fama and French, 1993; Carhart, 1997). We have 60 estimated FFC-4 alphas per ETF category. The lines represent cumulative FFC-4 alphas, and the shaded areas represent 95% confidence intervals. 



<!-- Start of picture text -->
0<br>− 5<br>− 10<br>− 15<br>− 20<br>− 25<br>− 30<br>Broad-based ETFs<br>Specialized ETFs<br>− 35<br>0 10 20 30 40 50 60<br>Months relative to ETF launch date<br>(%)CumulativeFFC-4alphas<br><!-- End of picture text -->

Given this evidence, we test an alternative hypothesis: that specialized ETFs serve as a hedging tool against risks to which investors are exposed. More broadly, this explanation relates to the view that financial innovation is a means to achieve market completion and enables risk sharing (Allen and Gale, 1994; Duffie and Rahi, 1995). While, in principle, investors could potentially replicate the portfolios of ETFs using the underlying assets, ETFs create value by reducing the costs associated with information acquisition, transactions, and search for a large swath of investors. 

We do not find evidence consistent with the hedging motive. The portfolio of stocks that are most negatively correlated with the portfolio of all specialized ETFs does not earn positive abnormal returns, which should be the case if it were a risk factor of hedging concern. Importantly, while an insurance motive predicts that investors are willing to sacrifice performance for hedging purposes, specialized ETFs are more likely to experience capital 

5 

outflows over their existence, which suggests instead that investors are disappointed by the poor performance. Similarly, specialized ETFs experience closures at a significantly higher rate, and not just early in their life, and the likelihood of closure is more sensitive to past performance. Also indicative of a souring mood around these investment themes after the launch, we document that stocks that are included in specialized ETFs have been favorably covered in the media. The sentiment of the media, however, drops sharply right after the time of launch. These findings make a related explanation unlikely, i.e., that investors accept the underperformance of specialized ETFs because they obtain non-pecuniary benefits—a “warm glow”—from exposure to themes complying with their values (e.g., environmental, social, and corporate governance (ESG) and faith-compliant ETFs). 

We develop a final hypothesis, that specialized ETFs cater to investor sentiment (akin to closed-end funds in Lee, Shleifer, and Thaler, 1991, and other literature discussed below).<sup>3</sup> We conjecture that issuers of specialized ETFs identify the popular trends in the market and respond to that demand by issuing products that track these investment themes. However, by the time new ETFs enter the market, the securities in which they invest have already reached their valuation peak. Thus, specialized ETFs underperform after launch. According to this hypothesis, specialized ETFs are chosen as a speculative vehicle by investors who extrapolate past performance into the future. 

Our empirical findings are consistent with the overvaluation hypothesis. newly-launched specialized ETFs hold portfolios of securities in attention-grabbing segments of the market: These are stocks that experienced recent price run-ups, had recent media exposure (especially positive exposure), had more positive earnings surprises, and displayed general traits that have been previously shown to indicate overvaluation (high market-to-book and high short interest). We also find evidence of catering to preferences for gambling (Brunnermeier and Parker, 2005; Brunnermeier, Gollier, and Parker, 2007; Mitton and Vorkink, 2007; Barberis and Huang, 2008; Kumar, 2009): Specialized ETFs contain securities with relatively more 

> 3In line with the literature, we interpret sentiment as the component of expectations about future asset returns not warranted by fundamentals (e.g., De Long, Shleifer, Summers, and Waldmann, 1990a). 

6 

positively skewed returns. Moreover, the investor clientele of specialized ETFs has a greater fraction of retail investors, who are typically considered less sophisticated and, therefore, more prone to holding incorrect beliefs and engaging in positive feedback trading (De Long, Shleifer, Summers, and Waldmann, 1990b). Relatedly, specialized ETFs are very popular among Robinhood investors, who have become famous in recent years for being prone to investment frenzies (Barber, Huang, Odean, and Schwarz, 2022). 

We find additional evidence indicating that specialized ETFs target investors’ extrapolative beliefs, i.e., the tendency to expect recent performance of an asset to continue into the future, or to their diagnostic expectations, which lead to overweighting of the best-case scenario.<sup>4</sup> Specifically, after the launch of specialized ETFs, analysts’ long-term growth expectations for the underlying securities prove to be too optimistic, and analysts constantly revise downward their earlier bullish forecasts. 

Overall, our results suggest a new narrative for the evolution of the most transformative financial innovation of the last three decades. The early ETFs, which are broad-based products, are beneficial investment platforms, as they reduce transaction costs and provide diversification.<sup>5</sup> Specialized ETFs ride the same wave of financial innovation, but they mainly compete for the attention of performance-chasing investors. Consequently, specialized ETFs, on average, have generated disappointing performance for their investors. 

Our work joins earlier literature that argues that issuers of securities and investment vehicles cater to investors’ sentiment. Lee et al. (1991) find that new closed-end funds are launched when investor sentiment for the respective asset class is high. Several studies found that structured products are issued in response to investor sentiment (C´el´erier and Vall´ee, 2017; Henderson et al., 2020; Vokata, 2021). 

> 4See models and studies of extrapolative beliefs in Barberis and Shleifer (2003), Greenwood and Shleifer (2014), Barberis, Greenwood, Jin, and Shleifer (2018), and Da, Huang, and Jin (2020). Davies (2022) and Egan, MacKay, and Yang (2022) recover expectations of leveraged ETF investors and show that these beliefs are consistent with extrapolative expectations. See models and studies of diagnostic expectations in Bordalo, Gennaioli, and Shleifer (2018) and Bordalo, Gennaioli, La Porta, and Shleifer (2019). 

> 5An important way in which broad-based ETFs reduce transaction costs is by being more tax-efficient than mutual funds (Moussawi, Shen, and Velthuis, 2020). 

7 

In the same spirit as our findings, prior literature shows that mutual funds cater to investor sentiment in order to attract flows by heavily weighting past winners (Chuprinin and Ruf, 2018) and changing their names to trendy ones (Cooper, Dimitrov, and Rau, 2001). Furthermore, new mutual funds tend to perform well right after their launch and underperform later, alluding to their focus on trendy themes (Karoui and Meier, 2009; Greene and Stark, 2016). Finally, mutual fund families engage in incubation of new funds (Evans, 2010). It appears, however, that ETFs are better situated to respond to investor sentiment than mutual funds for two main reasons. First, on the demand side, investors can trade ETFs more easily than mutual funds. Typically, investors access mutual funds through brokers, financial advisors, their retirement plans, or direct sales (e.g., by having an account at Vanguard). In contrast, ETFs can be traded continuously in the stock market leading to significantly higher liquidity. The ease of trading makes ETFs more suitable to chasing short term trends, while mutual funds tend to be used for longer-term investments, consistent with the evidence in Madhavan and Sobczyk (2019) and Vanguard (2020).<sup>6</sup> Second, from the point of view of the product providers, ETFs benefit from a shorter time-to-market. Specifically, in the last two decades, “White Label” platforms have allowed even small issuers to launch their ETFs and outsource some services to the platform, e.g., legal and registration processes. By doing that, the start-up costs and time to market of ETFs is markedly lower. In recent 

> 6The difference in investor attitude towards specialized ETFs (“short-term bets”) and mutual funds (“long-term investments”) might have a foundation in behavioral theories. Mutual funds have been traditionally distributed through channels associated with long-term wealth building (e.g., retirement plans), and therefore are likely to be associated with the “future income” account (Shefrin and Thaler, 1988). According to Shefrin and Thaler, individuals avoid tapping the “future income” account to finance current consumption, and this account is kept solely for future use. There are institutional reminders for investors about the intended use of mutual funds as long-term investment vehicles: they are relatively illiquid (traded once a day) and frequent trading is often penalized by front- and back-loads by distributors (or tax authorities, in the case of some retirement accounts). In contrast, the jazzy nature of ETFs—trendy themes and catchy tickers—makes them more associated with short-term trading, i.e., closer to the “current assets” account in Shefrin and Thaler (1988). This argument is consistent with the criticism by Jack Bogle, the founder of Vanguard, that ETFs are conducive to excessive trading. See Jack Bogle, “Jack Bogle: the lessons we must take from ETFs,” _Financial Times_ , December 12, 2016. 

8 

years, the time-to-market is as low as 75 days.<sup>7</sup> 

Our description of financial innovation via ETFs resonates with the model of Simsek (2013b) and Simsek (2013a), in which new financial products are used for both risk sharing and speculation. In the case of ETFs, it appears that broad-based products are primarily geared toward the risk-sharing goal, while specialized ETFs are catering to speculative behavior. 

Our work also relates to a few recent studies focusing on ETFs. Easley, Michayluk, O’Hara, and Putni¸nˇs (2021) propose that ETFs with a narrow focus are used as alphagenerating building blocks for active strategies. As such, they enhance price discovery and reduce mispricing. Our results, instead, suggest that specialized ETFs are not randomly launched, but rather respond to investor sentiment and to track segments of the market with overvalued securities. Therefore, going forward, they yield negative alphas. ETFs, therefore, can contribute in principle to overvaluation if they attract a new layer of investor demand to the underlying securities (see Ben-David, Franzoni, and Moussawi, 2018). In later work, Akey, Robertson, and Simutin (2021) confirm that less diversified ETFs underperform major benchmarks. 

Huang, Song, and Xiang (2020b) paper focuses on newly-launched smart-beta ETFs.<sup>8</sup> The authors argue that portfolios of smart-beta ETFs are designed by overfitting the data to generate indexes that outperform before launch (a similar argument is made in Harvey, 2021), but deliver zero alpha after launch.<sup>9</sup> We confirm these results (Figure 6). The mechanism behind the underperformance of specialized ETFs, which is the focus of our paper, is different from data mining. Our findings suggest that specialized ETFs are created 

> 7Additionally, in September 2019, towards the end of our sample period, the SEC adopted Rule 6c-11 to streamline the issuance of new ETFs. The goal is to “facilitate greater competition and innovation in the ETF marketplace,” by making it easier and faster for new ETFs “to come to market without the time or expense of applying for individual exemptive relief.” See `https://www.sec.gov/news/press-release/2019-190` . 

> 8Smart beta ETFs together with broad-index ETFs constitute the broad-based ETF category. As of the end of 2019, all broad-based ETFs manage about $2.14 trillion ($3.6 billion of revenues), and smart-beta ETFs constitute about 38% of these assets. The entire specialized category manages $0.46 trillion ($1.9 billion of revenues). 

> 9See also discussions in Harvey, Liu, and Zhu (2016) and Harvey (2017). 

9 

to cater to investors’ demand for popular themes and sectors. Because the securities in these segments are overvalued on average at the time of ETF creation, the portfolios of specialized ETFs underperform after launch. 

# **2 Testable Conjectures** 

The ETF market has grown substantially since the introduction of the first ETF in the early 1990s. In the United States alone, over 3,400 exchange-traded funds have been launched; of these, more than 1,000 invest in U.S. equities. Equity ETFs differ in the breadth of their holdings—ranging from a few stocks to over 3,000 stocks. And they differ also in the fees they charge—ranging from 4 basis points (bps) to over 150 bps per year. 

In the following section, we propose to use the model of Bordalo et al. (2016) as a framework to analyze the evolution and the current structure of the ETF industry.<sup>10</sup> 

## **2.1 Price Competition versus Quality Competition** 

The theory by Bordalo et al. (2016) describes a market in which producers face consumers with limited attention. Producers choose to compete on either of two dimensions, price or quality. For example, Walmart sells cheap commoditizied goods, while Starbucks emphasizes product quality and charges high prices. As a consequence, a market can gravitate around either ( _i_ ) a price-salient equilibrium in which products are commoditized and firms compete by offering low prices, or ( _ii_ ) a quality-salient equilibrium in which prices are high and firms differentiate themselves by offering distinct product features. While the theory predicts that one of these equilibria will emerge in a given market, we extend this interpretation by suggesting that the two equilibria can co-exist in different segments of the same industry. For example, the airline industry includes low-cost carriers who compete on price and carriers competing on first-class travel experience. 

> 10Bordalo et al. (2016) propose that their model can be applied to financial innovation, and C´el´erier and Vall´ee (2017) use this framework to describe competition in the market for structured products. 

10 

Figure 1 supports the view that the ETF market is characterized by the equilibria in Bordalo et al. (2016). Broad-based ETFs allow investors to achieve generic exposure to the market at a low cost and therefore can be mapped into the price-salient equilibrium. Specialized ETFs are differentiated products offered at a higher price point and reflect the quality-salient equilibrium. Investors who buy these ETFs are willing to overlook the high fees or loss of diversification as long as they can gain exposure to their desired investment themes. In this segment of the market, ETF issuers attract investor attention by designing products that lead investors to expect high utility and to neglect their expensive price tag. 

## **2.2 The Nature of Quality Competition** 

In mapping the Bordalo et al. (2016) model to the ETFs market, it is crucial to understand the nature of “quality competition.” Specifically, what is the value proposition that investors find attractive and that allows providers to charge high fees? After all, the specialized segment of the market accounts for 36% of the industry’s revenues at the end of our sample period, despite managing only 18% of the assets. 

We next formulate conjectures on the unique features that make specialized ETFs appealing to investors. In particular, we consider three potential explanations to describe the nature of quality competition. 

### **2.2.1 Delivering Alpha?** 

The first hypothesis is that specialized ETFs provide access to investment opportunities that would be otherwise unattainable to investors because of information or transaction costs. The resulting prediction is that specialized ETFs generate a positive alpha after fees. As such, ETFs benefit investors by delivering higher risk-adjusted returns. 

11 

### **2.2.2 Providing Hedging Services?** 

The second hypothesis is that investors use specialized ETFs for hedging some risks to which they are exposed. In this light, specialized ETFs are beneficial as they enable risk sharing among investors (Allen and Gale, 1994; Duffie and Rahi, 1995). Even though ETFs replicate cash flow profiles of securities that already exist in the market, they increase the accessibility of these portfolios to investors by reducing search and trading costs. Thus, the variety of products appearing on the market reflects the heterogeneity in investors’ endowments and in their need to insure against the risks associated with these endowments—i.e., their hedging demand. Viewed through this lens, the growth in the ETF market, including the specialized segment, responds to investors’ rational demand and is, therefore, welfare improving. 

According to this hypothesis, investors hold specialized ETFs even if their performance is negative because they provide insurance. Thus, we would expect investors _not to_ abandon specialized ETFs following poor performance. Moreover, if the risks for which specialized ETFs provide hedging are systematic, then we expect that the stocks that are exposed to these risks (i.e., they load positively on them) earn a risk premium. 

Similarly, if specialized ETFs provided non-pecuniary benefits in the form of access to themes complying with investors’ values (e.g., ESG ETFs, faith-compliant ETFs), we would expect investors to stay with them in spite of their negative performance. 

### **2.2.3 Catering to Investor Sentiment?** 

The third hypothesis that we entertain is that specialized ETFs cater to investor sentiment. A long literature cited in the introduction suggests that some financial innovators cater to investor sentiment (e.g., Lee et al., 1991), which is broadly defined as the component of expectations about future asset returns that are not warranted by fundamentals. Inspired by this literature, our third hypothesis is that specialized ETFs cater to investors’ optimistic expectations about future stock performance. 

12 

Thus, according to this hypothesis, new specialized ETFs are designed to appeal to investors’ irrational beliefs. For example, some investors may suffer from representativeness bias and they extrapolate past performance into the future (Greenwood and Shleifer, 2014; Barberis et al., 2018; Cosemans and Frehen, 2021). Or they might have diagnostic expectations (Bordalo et al., 2018, 2019), interpreting positive past performance as indicative of the best possible future scenario. These investor audiences would be drawn, for instance, to new ETFs that invest in past winners and stocks that delivered recent positive news. 

The catering hypothesis also implies that, if arbitrage is limited in the stock market, high-sentiment stocks are likely to be overvalued (e.g., Miller, 1977; Shleifer and Vishny, 1997). As a result, securities held by specialized ETFs are overvalued at the time of launch and their post-launch alpha would be negative.<sup>11</sup> 

# **3 Data** 

## **3.1 Data Sources** 

We use data on ETFs traded in the U.S. market from the Center for Research in Security Prices (CRSP) between 1993 and 2019. We restrict our sample to equity-focused ETFs that hold U.S. stocks in their portfolios. This choice allows us to more closely benchmark the ETF portfolios to broad-based U.S. stock indexes. Therefore, we exclude ETFs that are classified as non-equity, foreign equity, inverse and/or leveraged, and active. The final sample contains 1,080 U.S. equity ETFs. Appendix A introduces the mechanics of ETFs. We provide detailed data sources in Appendix B and variable descriptions in Appendix C. 

We compute ETFs’ portfolio holdings by combining the Thomson Reuters Global Mutual 

> 11Simsek’s (2013a) theory provides additional theoretical background for our third hypothesis. In his model, based on investor disagreement, financial products are used both by investors seeking risk sharing and by those with diverging beliefs interested in speculation. Financial innovators, to maximize their revenues, offer products for which the speculation motive is strongest. Therefore, this theory provides a rationalization for the two segments of the ETF market, where broad-based products are primarily geared toward the risksharing goal, while specialized ETFs are designed for speculators. 

13 

Fund Ownership and the CRSP Mutual Fund Holdings databases. We start with the data set that includes holdings information on the earliest date available (i.e., the closest to the launch date). We then use the other data set to complement missing data. We use Bloomberg and Morningstar Direct as guides for classifying ETFs, as described below. 

In addition, we use stock-level data from additional sources: market data from CRSP, short interest from Compustat, analyst expectations from I/B/E/S, firm-level news from RavenPack News Analytics, 13F institutional ownership data from Thomson Reuters, and Robinhood user data from Robintrack. 

## **3.2 Classification of ETFs** 

To analyze the evolution and motives behind the launch of new ETF products, we classify ETFs in two steps. First, we classify ETFs into four groups based on their investment objective (as was presented in Figure 1). The _thematic_ group comprises ETFs that, according to Bloomberg and CRSP, track multiple industries that are tied by a “theme” (e.g., clean energy). If ETFs track a single industry or sector, they belong to the _sector/industry_ category.<sup>12</sup> _Smart-beta_ ETFs are identified using the _Strategic Beta_ field in Morningstar. Finally, we identify as _broad-index_ those ETFs for which the Morningstar category _Index Selection_ variable has the value _Market Capitalization_ and that are not smart beta funds.<sup>13</sup> We do not create a separate category for ETF products specializing in environmental, social, and corporate governance topics (ESG) because they cut across multiple ETF classes with 

> 12Specifically, we reference the Bloomberg field _FUND_ _~~I~~ NDUSTRY_ _~~F~~ OCUS_ . Moreover, ETFs with a CRSP Objective Code ( _CRSP_ _~~O~~ BJ_ _~~C~~ D_ variable) starting with _EDS_ are classified as sector/industry ETFs. Also, those with Lipper Classification ( _LIPPER_ _~~C~~ LASS_ variable) with value _S_ are classified as thematic ETFs if they track religious, artificial intelligence, clean energy, or gender themes, and as sector/industry ETFs otherwise. 

> 13For the remaining equity ETFs, we rely on the variable _LIPPER_ _~~C~~ LASS_ in CRSP to classify funds as either broad-index or smart-beta. _LIPPER_ _~~C~~ LASS_ values of _LCV E_ , _MCV E_ , _MLV E_ , _SCV E_ , _LCGE_ , _MCGE_ , _MLGE_ , or _SCGE_ ; alternative funds; and funds that include factors in their names (e.g., value, growth, momentum, quality, sentiment, low volatility, dividends, earnings, profitability, alpha, multifactor, equal-weighted) are classified as smart-beta ETFs. We drop actively managed ETFs and ETFs with industry exclusions (e.g., S&P 500 ex-Technology ETF) from the list. The remaining funds are classified as broadindex ETFs. 

14 

different degrees of diversification.<sup>14</sup> 

In the second step, we consolidate ETFs into two broader groups to facilitate the analysis and presentation. We classify as _broad-based ETFs_ all ETFs that track broad market indexes, that is, the broad-index and smart-beta categories in Figure 1. The two types differ only in that smart-beta ETFs do not use capitalization-based weights. We classify as _specialized ETFs_ those that invest in a specific sector or in sectors that are tied by a theme, that is, sector/industry and thematic categories in the figure. 

Although all U.S. equity ETFs are included in our sample, some of the data items have limited availability in the pre-2000 period (e.g., holdings data). Given these data limitations, most of our empirical analysis begins in January 2000, including all ETFs launched earlier, and ends in December 2019.<sup>15</sup> The sample contains 554 broad-based ETFs (90 broad-index and 464 smart beta ETFs) and 526 specialized ETFs (411 sector/industry and 115 thematic ETFs). 

## **3.3 Descriptive Statistics** 

Since the late-1990s, the ETF industry experienced a great proliferation of new products. Figure 3 shows the time-series evolution of ETFs’ AUM and implied revenues (percentage fees times the average AUM in each year), as well as the time series of ETF launches and closures. 

Panel (a) of Figure 3 shows that the assets managed by broad-based ETFs have grown exponentially over the years, whereas the growth of the assets in specialized ETFs is less striking. By the end of 2019, broad-based ETFs accounted for about 82% of the assets invested in equity-based ETFs, and specialized ETFs accounted for the remaining 18%. Despite their relatively small market share, specialized ETFs at the end of the sample accounted for about 36% of the industry’s revenues, and broad-based ETFs generate 64% of it 

> 14In particular, ESG ETFs are classified as specialized if they are sector/industry or thematic ETFs (e.g., ALPS Clean Energy ETF). The remaining ESG ETFs, which are more diversified products (e.g., iShares ESG Screened S&P 500 ETF), are included in the broad-based category. 

> 15Exhibits’ captions include details about the exact sample periods. 

15 

### **Figure 3. Evolution of the ETF Industry** 

The figure presents the evolution of the stock-focused ETF industry, split by ETF category. The sample period is from 1993 to 2019. Panel (a) reports the aggregate assets under management (AUM), and Panel (b) shows implied revenues, computed as the sum across ETFs in the category of fee times the average AUM in each year. Panel (c) presents the number of ETF launches, and Panel (d) shows the number of ETF closures. 



<!-- Start of picture text -->
(a) Assets under management (b) Implied fee revenues<br>2 Broad-based ETFs Broad-based ETFs<br>Specialized ETFs 3 Specialized ETFs<br>2<br>1<br>1<br>0 0<br>1993 1998 2003 2008 2013 2018 1993 1998 2003 2008 2013 2018<br>(c) Number of ETF launches (d) Number of ETF closures<br>Broad-based ETFs Broad-based ETFs<br>100<br>Specialized ETFs 40 Specialized ETFs<br>50<br>20<br>0 0<br>1993 1998 2003 2008 2013 2018 1993 1998 2003 2008 2013 2018<br>($tn)AUM<br>($bn)Annualfeerevenues<br>ofNumberETFs ofNumberETFs<br><!-- End of picture text -->

(Panel (b)). The disproportionate share of revenues of specialized ETFs is due to the higher fees that they charge on average (Table 1). Over the entire sample period, broad-based ETFs and specialized ETFs generated cumulative revenues of $22.6bn and $14.6bn, respectively. Panels (c) and (d) of Figure 3 present the time series of ETF launches and closures. In the early years, most newly-launched ETFs were broad-based. A large batch of specialized ETFs was launched in 2006, and another in 2011. Interestingly, specialized ETFs experience higher closure rate throughout the sample period. 

In Table 1, we present summary statistics for our sample of ETFs. Specialized ETFs hold portfolios with fewer stocks than broad-based ETFs do: The median broad-based ETF holds 247 stocks, while the median specialized ETF holds 53 stocks. Broad-based ETFs charge 

16 

lower fees than specialized ETFs (medians of 35 versus 58 basis points, respectively).<sup>16</sup> 

### **Table 1. ETF Summary Statistics** 

The table shows summary statistics at the ETF level. The sample period is from 1993 to 2019. Panel A reports summary statistics for broad-based ETFs, and Panel B reports summary statistics for specialized ETFs. _Number of holdings_ represents the average number of stocks in the portfolios of ETFs. _Fee_ refers to the annualized expense ratio. _Share turnover_ is the average daily share turnover of the ETF over the six months after launch. _Market-adjusted return_ is the monthly ETF return in excess of the CRSP valueweighted return over the 60 months after launch. _Delisted_ is an indicator for whether the ETF was liquidated as of the end of 2019. _Assets under management_ (AUM) is the total market value of the investments as of the end of 2019. _Implied revenues_ are calculated by multiplying fees by the average AUM in 2019. 

|**Panel **|**A: Br**|**oad-Ba**|**sed ET**|**Fs**|||||
|---|---|---|---|---|---|---|---|---|
||N|Mean|SD|P5|P25|P50|P75|P95|
|Number of holdings|553|403|495|40|100|247|500|1,450|
|Fee (bps)|491|42|25|12|22|35|60|85|
|Share turnover (months 1–6; %)|543|2.83|3.25|0.19|0.93|2.01|3.48|7.95|
|Market-adjusted return (months 1–60; %)|551|_−_0.16|0.39|_−_0.88|_−_0.31|_−_0.11|0.04|0.33|
|Delisted|554|0.18|0.38|0|0|0|0|1|
|**2019 statistics**|||||||||
|Assets under management ($bn)|431|4.76|21.16|0.01|0.05|0.22|1.46|20.02|
|Implied revenues ($m)|389|8.94|31.36|0.03|0.22|0.97|5.12|45.36|
|**Panel**|**B: S**|**pecializ**|**ed ETF**|**s**|||||
||N|Mean|SD|P5|P25|P50|P75|P95|
|Number of holdings|515|87|87|21|34|53|100|272|
|Fee (bps)|455|55|21|18|39|58|70|86|
|Share turnover (months 1–6; %)|530|3.84|6.38|0.37|1.09|2.13|4.16|13.10|
|Market-adjusted return (months 1–60; %)|526|_−_0.44|1.42|_−_1.99|_−_0.73|_−_0.21|0.21|0.79|
|Delisted|526|0.30|0.46|0|0|0|1|1|
|**2019 statistics**|||||||||
|Assets under management ($bn)|354|1.30|3.72|0.01|0.04|0.18|0.82|6.09|
|Implied revenues ($m)|329|5.91|15.78|0.03|0.24|0.93|4.12|25.20|



There are other marked differences between the two groups of ETFs. Specialized ETFs generate more volatile returns than do broad-based ETFs. Furthermore, ETF share turnover is materially higher for specialized ETFs, reflecting a different use of these products by their investors relative to broad-based ETFs. Appendix Table D.1 breaks the two groups into the four categories of ETFs and provides summary statistics. 

> 16The apparent discrepancy between the means of fees reported in Table 1 and Figure 1 happens because the mean is equally weighted in Table 1 but AUM-weighted in Figure 1. 

17 

# **4 Empirical Analysis: Segmentation in the ETF Space** 

We begin our empirical examination by studying the joint distribution of fees and specialization. 

## **4.1 Segmentation Along the Fees and Diversification Dimensions** 

Several pieces of evidence support the view of a market segmented into price- and qualitysalient equilibria. First, in Figure 4, we plot ETF fees against product differentiation at two points in time: close to the birth of the industry (2002) and toward the end of our sample (2019).<sup>17</sup> The figure shows that two clusters of products have emerged over time. Broadbased ETFs, the early comers to the market, tend to charge lower fees and appear to be more similar to one another. Specialized products, which proliferate in the late sample, are more differentiated and expensive. 

In Appendix Table D.2, we show that the difference in fees between broad-based and specialized ETFs is statistically significant, even controlling for time and management company fixed effects. The latter set of controls allows us to rule out the possibility that the difference in fees results from different pricing power of different providers, for example, due to their brand recognition. Even within the same provider, specialized products are priced significantly higher. 

Based on the circles in Figure 4, whose size is proportional to the ETFs’ AUMs, we also conclude that the broad-based segment of the market is more concentrated. This is likely a consequence of the economies of scale in the price competition space, which lead to a winner-takes-all equilibrium. In the specialized segment, multiple differentiated products 

> 17Product differentiation is computed for each category as one minus the cosine similarity between the ETF portfolio weights and the weights of the aggregate portfolio of all ETFs in that category that exist in the market at that point in time. Kostovetsky and Warner (2020) develop an alternative measure of product differentiation for active mutual funds using textual analysis of the fund prospectus. They show that despite differentiation in strategy description, mutual fund holdings are similar. Likewise, we find that some portfolios that are marketed as differentiated products have almost identical holdings. A noticeable example are the ETFs offering investments based on religious or political values. Most of these ETFs hold portfolios that are very similar to broad-based indexes, but charge high fees. 

18 

### **Figure 4. Segmentation in the ETF Market** 

The figure presents the ETF market configuration at two points in time. Panel (a) shows a snapshot as of December 2002, and Panel (b) shows a snapshot as of December 2019. Product differentiation is computed for each category as one minus the cosine similarity between the ETF portfolio weights and the weights of the portfolio of all ETFs in that category that exist in the market at that point in time. The panels show the universe of ETFs at each date, on two dimensions: product differentiation and fees. Each circle represents one ETF, and the size of the circles represents relative share of assets under management across all ETFs. Blue circles represent broad-based ETFs, and red circles represent specialized ETFs. 



<!-- Start of picture text -->
(a) Differentiation, fees, and AUM: 2002 (b) Differentiation, fees, and AUM: 2019<br>100 100<br>Broad-based ETFs<br>80 Specialized ETFs 80<br>60 60<br>40 40<br>20 20<br>0 0<br>0 20 40 60 80 100 0 20 40 60 80 100<br>Product differentiation Product differentiation<br>(bps)Fee<br><!-- End of picture text -->

with smaller portfolio sizes can charge higher fees and survive, leading to lower concentration. Interestingly, the distribution of revenues generated by broad-based ETFs largely matches that of specialized ETFs, as can be seen in Table 1. For example, as of 2019, the median annual fee revenue was nearly $1m in each group and the revenues at the 75<sup>th</sup> percentile were above $5m and $4m for broad-based ETFs and specialized ETFs, respectively. The main difference between the groups is in the extreme right tail, where the large broad-based ETFs (like State Street’s SPDR tracking the S&P 500 index) generate higher revenues due to their sheer portfolio size. 

At the level of providers, the concentration also differs markedly between the two sets of products. Appendix Table D.3 reports that the concentration among providers declines uniformly moving to more specialized ETFs across the four categories depicted in Figure 1. Finally, the Venn diagram in Appendix Figure D.1 shows that while a significant fraction of providers (41%) operate in both segments of the market, non-negligible shares of asset managers offer only broad-based ETFs (37%) or specialized ETFs (23%). 

In sum, the dynamics of competition in the ETF market appear to differ markedly in 

19 

the broad-based and specialized segments. In the broad-based segment, a small number of issuers benefit from economies of scale, which allows them to spread the costs across a bigger customer base—e.g., the costs of data licensing. Thus, they can charge lower fees. At the same time, due to their large clientele, broad-based ETFs are a catalyst of significant trading volume, which constitutes a source of liquidity that investors value (Khomyn, Putni¸nˇs, and Zoican, 2020). Their economies of scale create barriers to entry for new contenders. On the other hand, for specialized ETFs, fees decline only slightly (see Figure 1), even though the supply of specialized products increases substantially over time. These products are very differentiated, so new entrants do not directly compete with the incumbents, who can preserve some of their monopolistic rents. 

## **4.2 Segmentation of Investor Demand** 

Next, we more directly investigate the conjecture that a price-salient and quality-salient equilibria characterize different segments of the ETF industry. To this purpose, Table 2 presents an analysis of the product features that attract investor demand. We report estimates from regressions of monthly capital flows into each ETF, a proxy for demand, on product characteristics. In particular, we focus on fees, as a measure of price, and on past returns, which approximate expected returns for investors with extrapolative beliefs and, in this sense, are a measure of quality. 

The results in Panel A suggest that investors pay more attention to price when trading broad-based ETFs than specialized products, as the sensitivity to fees is significantly more negative in the former products. In the late part of our sample period (2010–2019), when the bulk of specialized ETFs are present in the market, specialized ETFs’ sensitivity to fees is indistinguishable from zero providing clear evidence in support of a quality-salient equilibrium in which consumers disregard price.<sup>18</sup> To address the issue that fees are fairly 

> 18An additional reason for investors in specialized ETFs to overlook the high fees is their higher turnover in these products, i.e., shorter holding period, relative to broad-based ETFs (see Table 1). If investors expect a high return in the short run for specialized ETFs, then fees can be disregarded as they will only be born for a limited time. 

20 

### **Table 2. ETF Flow Sensitivity to Fees and Past Performance** 

The table presents the flow sensitivity of ETFs to their fees and past performance. Panel A compares flow sensitivity between broad-based and specialized ETFs. Panel B compares flow sensitivity between ETFs that recently received high media attention and those that recently received low media attention. The dependent variable is ETF flows in month _t_ + 1, computed as (AUM _t_ +1 _−_ AUM _t ×_ ETF return _t_ +1) _/_ AUM _t_ . In each month _t_ , we calculate the percentile rank of ETF returns. _Specialized_ is a dummy variable that equals 1 if an ETF is a specialized ETF. _High media_ is a dummy variable that equals 1 if the AUM-weighted media sentiment of an ETF’s underlying securities computed in month _t_ ranks in the top 20%. _AUM_ is an ETF’s assets under management ($ million) in month _t_ , and _Age_ is an ETF’s age in months. Standard errors are clustered at the ETF and the calendar-month levels. _t_ -statistics are reported in parentheses. *, **, and *** indicate significance at the 10%, 5%, and 1% levels, respectively. The overall adjusted R<sup>2</sup> is reported. 

|**Panel A: Flow**|**s and Sp**|**ecialized **|**ETFs**|**Panel B: Flows **|**and High **|**Media Se**|**ntiment**|
|---|---|---|---|---|---|---|---|
|Dependent variable:|F|lows_t_+1 (%|)|Dependent variable:|F|lows_t_+1 (%|)|
|Sample period:|2000–2019|2000–2009|2010–2019|Sample period:|2000–2019|2000–2009|2010–2019|
|Fee (bps)|_−_0.04***|_−_0.08***|_−_0.03***|Fee (bps)|_−_0.03***|_−_0.07***|_−_0.03***|
||(_−_6.97)|(_−_4.15)|(_−_5.91)||(_−_6.28)|(_−_3.9)|(_−_5.19)|
|Fee|0.01**|_−_0.00|0.02**|Fee|0.02**|0.01|0.02*|
|_×_ Specialized|(2.01)|(_−_0.14)|(2.60)|_×_ High media|(2.07)|(0.48)|(1.89)|
|Return rank_t_|0.04***|0.03***|0.04***|Return rank_t_|0.05***|0.04***|0.05***|
||(10.08)|(3.21)|(9.88)||(12.94)|(5.20)|(12.33)|
|Return rank_t_|0.01***|0.02*|0.01***|Return rank_t_|0.00|0.01|0.00|
|_×_ Specialized|(2.88)|(1.72)|(2.61)|_×_ High media|(0.59)|(0.82)|(0.22)|
|Specialized|_−_1.48***|_−_0.54|_−_1.73***|High media|_−_0.96*|_−_1.70|_−_0.62|
||(_−_3.15)|(_−_0.42)|(_−_3.73)||(_−_1.81)|(_−_1.24)|(_−_1.09)|
|log(AUM_t_)|_−_0.12**|_−_0.86***|0.01|log(AUM_t_)|_−_0.12*|_−_1.14***|0.03|
||(_−_1.98)|(_−_3.53)|(0.13)||(_−_1.72)|(_−_3.53)|(0.54)|
|log(Age_t_)|_−_1.84***|_−_1.42***|_−_1.93***|log(Age_t_)|_−_1.85***|_−_1.20**|_−_1.98***|
||(_−_12.37)|(_−_2.95)|(_−_12.28)||(_−_12.15)|(_−_2.10)|(_−_13.10)|
|Calendar month FE|Yes|Yes|Yes|Calendar month FE|Yes|Yes|Yes|
|Observations<br>|81,485|17,821|63,664|Observations<br>|64,425|12,282|52,143|
|Adj R<sup>2</sup>|0.063|0.067|0.059|Adj R<sup>2</sup>|0.069|0.080|0.060|



constant over the life of an ETF while flows vary considerably, Appendix Table D.4 reports estimates from a regression of cumulative flows over one- or two-year windows after the launch of the ETF onto average fees in the same window. The result that investors in specialized ETFs are significantly less sensitive to fees remains unchanged. 

In Panel B of Table 2, we study how the salience of ETFs’ portfolio composition modifies investors’ response to different product attributes. We measure the salience of ETFs’ portfolio assets as the average media sentiment score of the underlying stocks. Again, the 

21 

evidence suggests that two separate equilibria prevail in the industry.The investors in ETFs holding stocks that attract the most attention are almost insensitive to price and, instead, care mostly about past performance. As we show below, media attention is significantly higher for stocks in specialized ETFs’ portfolios relative to those in broad-based portfolios. 

Figure 5 provides a graphical representation of flow-performance sensitivity for broadbased and specialized ETFs. In each month _t_ , we compute next-period flows as (AUM _t_ +1 _−_ AUM _t ×_ ETF return _t_ +1) _/_ AUM _t_ . Then, we estimate a non-parametric relation between nextperiod flows and period- _t_ raw returns using local polynomials approximations. 

### **Figure 5. Flow-Performance Sensitivity** 

The figure presents the flow-performance sensitivity of ETFs per ETF category. The sample period is from 2000 to 2019. Flows are computed as (AUM _t_ +1 _−_ AUM _t ×_ ETF return _t_ +1) _/_ AUM _t_ . Returns are raw ETF returns. We estimate a non-parametric relation between flows and returns using local polynomials approximations obtained with Stata’s `-lpoly-` command with bandwidth of 0.04. The shaded areas represent 95% confidence intervals. 



<!-- Start of picture text -->
Broad-based ETFs<br>Specialized ETFs<br>2%<br>0%<br>− 2%<br>− 12% − 6% 0% 6% 12%<br>Return t (%)<br>(%)Flow+1 t<br><!-- End of picture text -->

Consistent with the results in Table 2, the figure shows that the return-chasing behavior of investors in broad-based ETF differs from that in specialized ETFs. The results are consistent with performance-chasing in the ETF market, as documented in Dannhauser and Pontiff (2019); however, here we find that the sensitivity of flows to past returns is significantly higher for specialized ETFs, consistent with investors paying more attention to 

22 

past performance in this segment of the market.<sup>19</sup> 

# **5 The “Quality” of Specialized ETFs** 

Having established that broad-based and specialized ETFs present different form of competition, we turn to exploring the value propositions in these two segments. While there is little doubt about the value created by broad-based ETFs in terms of facilitated market access and low-cost diversification, the case for value creation by specialized ETFs is less clear. 

Given investors’ revealed preferences of including specialized ETFs in their portfolios despite their higher fees, we investigate two conjectures that fall within the paradigm of rational investor behavior. 

The first possibility is that specialized ETFs deliver superior performance. Under this conjecture, the rationale for investing in high-fee ETFs is simply to achieve positive riskadjusted returns (alphas). Specialized ETFs, therefore, would provide a low-cost tool for accessing these investment ideas. 

The second possibility is that specialized ETFs create value by providing a hedging tool against some risks that investors care about. In other words, these products might operate like insurance policies. Hence, their risk-adjusted returns do not have to be positive, as long as their performance insulates against risks that investors care about. 

> 19In Appendix Figure E.1, we replicate the analysis in Figure 5 using market-adjusted returns and the percentile rank of returns within each month and find consistent results. Also, a legitimate concern is that the difference in flow-performance sensitivity between the two groups of ETFs results from a difference in the horizons at which the clienteles for the two types of products evaluate them. The monthly frequency in Figure 5 may be too restrictive, e.g., it may not capture the behavior of investors who rebalance their portfolios at lower frequencies. To address this concern, Appendix Figure E.2 shows that the same pattern is present when we measure performance at the quarterly (Panel (a)) and annual frequency (Panel (b)). 

23 

## **5.1 The Performance of Specialized ETFs** 

To measure the performance of specialized ETFs, we use a calendar-time portfolios approach, a standard approach in the asset pricing literature. We form portfolios that separately hold the universes of broad-based and specialized products. The portfolios are reformed each month and are weighted by firms’ market capitalization.<sup>20</sup> Then, we regress the net-of-fee returns of these portfolios in excess of the risk-free rate on commonly used risk factors, as is customary in asset pricing studies.<sup>21</sup> 

In Panel A of Table 3, we present excess returns as well as the alphas from these risk models. In general, specialized ETFs have negative performance across the different specifications. Focusing on the Fama-French-Carhart four-factor model (Fama and French, 1993; Carhart, 1997), specialized ETFs generate negative alphas of about _−_ 3 _._ 24% per year ( _−_ 0 _._ 27% _×_ 12). Underperformance is smaller (but still negative) when using richer factor models. In comparison, using the same risk model, broad-based ETFs generate negative alpha of about _−_ 0 _._ 24% a year ( _−_ 0 _._ 02% _×_ 12), which is closer to their average fees. 

We also note that the FF5 alphas are smaller in absolute value than the FFC4 alphas in Panel A of Table 3. This result follows from the fact that specialized ETFs have significant exposures to growing yet unprofitable firms—i.e., negative coefficients on the RMW and the CMA factors. This exposure leads them to generate lower returns. Adjusting for these factors absorbs part of their underperformance. 

Importantly, the relative underperformance of specialized ETFs cannot be accounted for by the higher fees that they charge. The difference in annual fees between specialized and broad-based ETFs is about 0.13% on average (see Table 1). Thus, the difference in alphas of specialized and broad-based ETFs (about _−_ 3% per year for the four-factor model) is an order of magnitude larger than the difference in fees between the two groups. Confirming 

> 20The results with equal-weighted portfolios are similar and are shown in Appendix Table F.1. 

> 21Risk factor returns are downloaded from Professor French’s website: `https://mba.tuck.dartmouth. edu/pages/faculty/ken.french/data_library.html` and Professors Hou, Xue, and Zhang’s website: `http://global-q.org/factors.html` . 

24 

### **Table 3. Calendar-Time Portfolios of ETFs** 

The table presents the risk-adjusted performance of ETFs from 2000 to 2019. In Panel A, we form portfolios consisting of all ETFs in the same category. In Panel B, we identify _new_ ETFs that were launched in the previous five years in each month. We then form portfolios consisting of all _new_ ETFs in the same category. In Panel C, we identify _seasoned_ ETFs that were launched more than five years prior in each month. We then form portfolios consisting of all _seasoned_ ETFs in the same category. The portfolio returns are valueweighted using one-month-lagged market capitalization. _Excess return_ refers to the average monthly return in excess of the risk-free rate. _CAPM_ , _FF3_ , _FFC4_ , _FF5_ , _FF6_ , and _Q_ alpha denote alphas with respect to the Capital Asset Pricing Model (Sharpe, 1964; Lintner, 1965; Mossin, 1966), the Fama-French three-factor model (Fama and French, 1993), the Fama-French-Carhart four-factor model (Carhart, 1997), the FamaFrench five-factor model (Fama and French, 2015), the Fama-French six-factor model (Fama and French, 2018), and the Q-factor model (Hou et al., 2015), respectively. The portfolios of all broad-based (specialized) ETFs comprise 171 (189) ETFs on average. _Sp minus BB_ denotes the specialized ETF portfolio minus the broad-based ETF portfolio. The excess return and alphas are in percentage points, and _t_ -statistics are reported in parentheses. *, **, and *** indicate significance at the 10%, 5%, and 1% levels, respectively. 

|||**Panel **|**A: All Mo**|**nths**||||
|---|---|---|---|---|---|---|---|
||Excess return|CAPM|FF3|FFC4|FF5|FF6|Q|
|Broad-based ETFs|0.46|_−_0.05|_−_0.03|_−_0.02|0.05|0.05|0.05|
||(1.50)|(_−_0.76)|(_−_0.65)|(_−_0.41)|(1.01)|(1.09)|(0.87)|
|Specialized ETFs|0.20|_−_0.32***|_−_0.28***|_−_0.27***|_−_0.13|_−_0.13|_−_0.13|
|Sp minus BB|(0.62)<br>_−_0.26***<br>(_−_3.22)|(_−_3.38)<br>_−_0.28***<br>(_−_3.47)|(_−_3.44)<br>_−_0.25***<br>(_−_3.22)|(_−_3.30)<br>_−_0.25***<br>(_−_3.22)|(_−_1.59)<br>_−_0.18**<br>(_−_2.22)|(_−_1.57)<br>_−_0.18**<br>(_−_2.24)|(_−_1.61)<br>_−_0.17**<br>(_−_2.22)|
|||**Panel B**|**: Months**|_≤_**60**||||
||Excess return|CAPM|FF3|FFC4|FF5|FF6|Q|
|Broad-based ETFs|0.31<br>(0.90)|_−_0.22*<br>(_−_1.68)|_−_0.17<br>(_−_1.51)|_−_0.13<br>(_−_1.18)|0.09<br>(0.86)|0.10<br>(1.00)|0.05<br>(0.50)|
|Specialized ETFs|_−_0.01<br>(_−_0.02)|_−_0.55***<br>(_−_4.10)|_−_0.53***<br>(_−_4.20)|_−_0.50***<br>(_−_4.02)|_−_0.35***<br>(_−_2.81)|_−_0.35***<br>(_−_2.76)|_−_0.34***<br>(_−_2.78)|
|Sp minus BB|_−_0.31**<br>(_−_2.20)|_−_0.32**<br>(_−_2.26)|_−_0.36**<br>(_−_2.49)|_−_0.37***<br>(_−_2.61)|_−_0.44***<br>(_−_3.00)|_−_0.45***<br>(_−_3.04)|_−_0.39***<br>(_−_2.62)|
|||**Panel C**|**: Months**|_>_ **60**||||
||Excess return|CAPM|FF3|FFC4|FF5|FF6|Q|
|Broad-based ETFs|0.70**|_−_0.03|_−_0.03|_−_0.03|_−_0.04*|_−_0.04*|_−_0.03|
||(2.38)|(_−_1.32)|(_−_1.28)|(_−_1.26)|(_−_1.91)|(_−_1.89)|(_−_1.13)|
|Specialized ETFs|0.60**|_−_0.11|_−_0.11|_−_0.12|_−_0.12|_−_0.12|_−_0.07|
||(2.04)|(_−_1.57)|(_−_1.56)|(_−_1.56)|(_−_1.54)|(_−_1.55)|(_−_1.00)|
|Sp minus BB|_−_0.10|_−_0.08|_−_0.08|_−_0.09|_−_0.07|_−_0.07|_−_0.05|
||(_−_1.49)|(_−_1.19)|(_−_1.25)|(_−_1.25)|(_−_1.02)|(_−_1.05)|(_−_0.67)|



this claim, Appendix Table F.2 reports the alphas for gross-of-fee returns.<sup>22</sup> 

To understand whether the observed underperformance of specialized ETFs crucially hinges on the valuation of their portfolios at the time of launch, we focus next on recently 

> 22Appendix Figure F.1 reproduces Figure 2 with gross-of-fee returns. 

25 

launched ETFs. In Panel B of Table 3, we form calendar-time portfolios that hold all the ETFs in each of the two categories that were launched in the prior five years. The results show that the underperformance of specialized ETFs is stronger in the years following their launch. For example, the four-factor alpha is _−_ 6% per year ( _−_ 0 _._ 50% _×_ 12).<sup>23</sup> The estimates show also a stark underperformance of recently launched specialized ETFs relative to the broad-based, ones with a four-factor alpha difference of _−_ 0 _._ 37% per month.<sup>24</sup> 

For completeness, Panel C of Table 3 shows that, after the first five years, the riskadjusted underperformance of specialized ETFs is substantially reduced and statistically indistinguishable from zero.<sup>25</sup> Nevertheless, the evidence about the underperformance in the early years of specialized ETFs raises questions about the timing of specialized ETF issuances. We address these questions in the next section. 

To further ensure that the underperformance of specialized ETFs is not driven by fees or the impact of trading costs, we repeat the analysis in Figure 2 using the indexes underlying the newly-launched ETFs, instead of the ETFs themselves.<sup>26</sup> We report the results in Figure 6. As evident from the figure, we obtain the same performance pattern for the 

two categories of ETFs that compose the specialized ETFs’ group—i.e., sector/industry and 

> 23Similar results are depicted in Figure 2 in the Introduction. Each point in the chart is produced by one regression based on the four-factor model (Fama and French, 1993; Carhart, 1997). The alpha associated with month one, for example, is produced from a regression on the performance of a portfolio that includes all the ETFs that are exactly one-month old; the alpha associated with month two is produced by a portfolio that comprises ETFs that are exactly two months old. We repeat the process up to the 60-month life span. The striking result is that, over the first five years of their life, specialized ETFs lose about 30% on average in terms of risk-adjusted returns. Appendix Figure F.1 finds the same result using gross-of-fee returns. 

> 24Our results imply that ETFs, on average, underperform post-launch. Brightman, Li, and Liu (2015) use a sample of all ETFs launched between 1993 and 2011, and find that post-launch returns were virtually flat (see also discussion in Harvey, 2021). We replicate and reconcile these results with our findings. There are two key factors driving the difference in the studies’ results. First, while Brightman et al. (2015) examine only ETFs that existed 36 months _after_ the launch date, we do not have such restriction. Second, our sample, being longer by nine years, covers a period with larger fraction of specialized ETFs (see Figure 3, Panel (c)). Third, Brightman et al. (2015) use traditional event study methodology (Ball and Brown, 1968), while we use calendar time methodology (Fama, 1998; Mitchell and Stafford, 2000). 

> 25We also verify that our results are not driven by ETFs that hold a majority of foreign stocks. In Appendix Table F.3, we restrict the sample to ETFs for which at least 80% of their market capitalization is invested in stocks traded in the United States. The results of the analysis are similar to those reported in Table 3. 

> 26We extract data from Bloomberg on the indexes that underlie the ETFs in our sample, using the Bloomberg variable: _ETF_ _~~U~~ NDL_ _~~I~~ NDEX_ _~~T~~ ICKER_ . We have been able to identify about 78.5% of the underlying indexes, for which we extract total return data. 

26 

### thematic ETFs.<sup>27</sup> 

### **Figure 6. Performance of the Indexes Underlying Newly-Launched ETFs** 

The figure shows the performance of the indexes underlying ETFs around launch per ETF category from 2000 to 2019. The index data are collected from Bloomberg. We were able to match 85.6% of the indexes for broad-index ETFs (Panel (a)), 81.6% of the indexes for smart-beta ETFs (Panel (b)), 78.8% of the indexes for sector/industry ETFs (Panel (c)), and 70.4% of the indexes for thematic ETFs (Panel (d)). For each ETF group, we form 97 calendar-time portfolios that include returns of ETFs in their month _−_ 36 _, −_ 35 _, . . . ,_ +59 _,_ +60 around the launch date (month 0). We have 97 time series of portfolio returns per ETF category. The portfolio returns are equal-weighted. To adjust returns for risk factors, we estimate the Fama-French-Carhart four-factor model (FFC-4) alphas of the portfolios (Fama and French, 1993; Carhart, 1997). We have 97 estimated FFC-4 alphas per ETF category. The lines represent cumulative FFC-4 alphas, and the shaded areas represent 95% confidence intervals. 



<!-- Start of picture text -->
(a) Broad-index ETFs (b) Smart-beta ETFs<br>10 10<br>0 0<br>− 10 − 10<br>− 36 − 24 − 12 0 12 24 36 48 60 − 36 − 24 − 12 0 12 24 36 48 60<br>(c) Sector/industry ETFs (d) Thematic ETFs<br>10 10<br>0 0<br>− 10 − 10<br>− 36 − 24 − 12 0 12 24 36 48 60 − 36 − 24 − 12 0 12 24 36 48 60<br>Months relative to ETF launch date Months relative to ETF launch date<br>(%)CumulativeFFC-4alphas<br>(%)CumulativeFFC-4alphas<br><!-- End of picture text -->

> 27 Bordalo et al. (2016) is a conceptual framework that derives two modes of competition and responses to demand. Naturally, reality is more complex and product offering in the ETF market is not necessarily binary. Because of this imperfect mapping from the theory to the data, the concern might arise that the results are sensitive to the classification method that we adopted. Therefore, we test whether the underperformance of specialized ETFs is robust to using other intuitive approaches to define this group. Appendix Table F.4 shows that the evidence in Table 3 is confirmed when we identify specialized products using heterogeneity along the investment strategy (i.e., active share), the portfolio size (i.e., number of holdings), and the cost dimensions. In particular, for this analysis, we define specialized ETFs as those with either a large active share, or a small number of portfolio holdings, or those charging high fees. Also, Appendix Table F.5 studies the four categories of ETFs separately and shows that both categories in the specialized segment, sector and thematic ETFs, display significant underperformance. Finally, in Appendix Table F.6, we propose a simple stock-level trading strategy based on holdings of new specialized ETFs instead of relying on ETF returns. In particular, the strategy is long in the top five holdings of ETFs that launched in the previous 12 months. We find a similar magnitude of underperformance. 

27 

Studying the performance of indexes instead of ETFs allows us also to extend the series to the period _preceding_ the launch, as many indexes were already in existence. We note that before ETFs inception, smart beta, sector/industry, and thematic ETFs, experience a price run-up. In the case of smart beta ETFs, the pre-launch run-up does not revert after the launch. This evidence is consistent with the claim of Brightman et al. (2015) and Huang et al. (2020b), that while these products are launch with the intent of capturing an alpha, their portfolio definitions are overfit based on past performance, and therefore deliver zero alpha going forward. In contrast, the post-launch performance of sector/industry and thematic ETFs reverses the pre-launch run-up. The reversal pattern is consistent with the overvaluation hypothesis, which is studied in Section 6. 

To summarize, this analysis suggests that specialized ETFs generate an economically and statistically significant negative alpha in the order of magnitude of _−_ 6% a year in the first five years of their existence. As such, they do not create value for their investors by providing outperforming investment strategies. Consequently, the combination of underperformance, high fees, and lack of diversification of these products remains a puzzle. For this reason, we entertain more closely the hypothesis that specialized ETFs provide insurance against some underlying risks that investors care about. 

## **5.2 Are Specialized ETFs Used for Hedging Purposes?** 

To explain investors’ demand for specialized ETFs in spite of their underperformance, we investigate whether these products deliver value as a form of insurance. Specialized ETFs might serve as a hedging tool for aggregate risks, in which case their underperformance could be construed as a negative risk premium, or for risks to which some subsets of investors are exposed, in which case we do not expect ETFs to command a negative risk premium. A related conjecture is that specialized ETFs generate non-pecuniary benefits by being compliant with investors’ values. 

28 

### **5.2.1 Is the Underperformance a Hedging Premium?** 

It is possible that our earlier tests fail to capture some unobserved risk factors that investors care about, and that specialized ETFs might be the right vehicle that allows investors to hedge against unobserved risk factors. For this reason, investors are willing to accept lower returns.<sup>28</sup> 

A testable implication of this conjecture is that the performance of specialized ETFs is negatively correlated with the performance of a portfolio of assets that investors dislike, i.e., a portfolio that earns a positive risk premium.<sup>29</sup> 

To test this prediction, we construct a portfolio of stocks that have negative correlation with the portfolio of all specialized ETFs. In particular, each month, we form five portfolios of stocks sorted on their betas on the specialized-ETF factor, constructed as the excess return of the market-capitalization-weighted portfolio of specialized ETFs.<sup>30</sup> Portfolio 1 has the stocks with the lowest correlation with the aggregate specialized ETF portfolio, and portfolio 5 has the highest correlation. 

The results, shown in Table 4, indicate no support for the conjecture that specialized ETFs provide hedging for an aggregate risk factor. The table reports the alphas from regressions of these portfolios’ returns on different factor models. In no specification, are the alphas of low-specialized-beta stocks consistent with a positive risk premium. 

Finally, a potential explanation for the underperformance of specialized ETFs could be inspired by the findings of Huang et al. (2020a), that sector/industry ETFs are short-sold by 

> 28The hedging motive we discuss here is different from the specific notion that arbitrageurs use industry ETFs as hedging tools within long-short strategies (Huang, O’Hara, and Zhong, 2020a). More broadly, our notion of hedging refers to the interpretation of financial innovation as a tool to improve risk sharing among investors (Allen and Gale, 1994). 

> 29We emphasize that in the current analysis we are looking for a risk factor that accounts for the evidence of negative average performance of the portfolio of _all_ specialized ETFs. It remains possible that different specialized ETFs serve as hedging tool for different groups of investors, a possibility that we entertain in Section 5.2.2. 

> 30The beta is estimated using 60-month rolling-window regressions, requiring each stock to have at least 36 months of available return observations. In these regressions, we control for the market factor. Then, we form five portfolios corresponding to the quintiles of the estimated betas on the specialized-ETF factor based on the breakpoints of the distribution of NYSE-listed stocks, to avoid giving disproportionate influence to smaller stocks listed on other exchanges (Fama and French, 1992). 

29 

### **Table 4. Hedging Motive?** 

The table presents the risk-adjusted monthly performance of stocks from 2000 to 2019 by quintiles of loadings on specialized ETFs. In each month, we sort stocks based on their beta on the excess return of the marketcapitalization-weighted portfolio of specialized ETFs, controlling for the market factor. The beta is estimated using 60-month rolling-window regressions, requiring each stock to have at least 36 months of observations with returns. We then form five portfolios corresponding to the quintiles of the estimated betas based on NYSE breakpoints. Portfolio Q1 (Q5) contains the stocks with the lowest (highest) correlation with the specialized portfolio. _CAPM_ , _FF3_ , _FFC4_ , _FF5_ , _FF6_ , and _Q_ alpha denote alphas with respect to the Capital Asset Pricing Model (Sharpe, 1964; Lintner, 1965; Mossin, 1966), the Fama-French three-factor model (Fama and French, 1993), the Fama-French-Carhart four-factor model (Carhart, 1997), the Fama-French five-factor model (Fama and French, 2015), the Fama-French six-factor model (Fama and French, 2018), and the Q- factor model (Hou et al., 2015), respectively. The alphas are in percentage points, and _t_ -statistics are reported in parentheses. *, **, and *** indicate significance at the 10%, 5%, and 1% levels, respectively. 

|Exposure to specialized ETFs:|Low|Q2|Q3|Q4|High|
|---|---|---|---|---|---|
|CAPM alpha|_−_0.03|0.04|0.07|0.04|_−_0.30|
||(_−_0.19)|(0.58)|(1.02)|(0.55)|(_−_1.64)|
|FF3 alpha|0.06|0.04|0.05|0.03|_−_0.32*|
||(0.55)|(0.58)|(0.77)|(0.44)|(_−_1.78)|
|FFC4 alpha|0.08|0.04|0.06|0.03|_−_0.31*|
||(0.65)|(0.62)|(0.80)|(0.44)|(_−_1.74)|
|FF5 alpha|0.13|0.02|0.00|0.04|_−_0.28|
||(1.16)|(0.21)|(0.03)|(0.52)|(_−_1.52)|
|FF6 alpha|0.14|0.02|0.01|0.04|_−_0.27|
||(1.24)|(0.25)|(0.07)|(0.53)|(_−_1.47)|
|Q alpha|0.02|0.04|0.04|0.02|_−_0.19|
||(0.18)|(0.50)|(0.54)|(0.30)|(_−_1.04)|



hedge funds to hedge industry risk. The results in Appendix Table F.7 appear to rule out this possibility as a main cause of the underperformance, as they show that the underperformance of specialized ETFs is present even for the subset of specialized ETFs that does not have shares available for borrowing in their first year of existence according to the Markit database. 

### **5.2.2 Capital Flows Over ETFs’ Life Cycle** 

Failing to find an aggregate risk factor of hedging concern points to the lack of a _systematic_ insurance motive behind the portfolio of _all_ specialized ETFs. Investors may still be willing to hold specialized ETFs in spite of their negative risk-adjusted returns for their idiosyncratic reasons. 

Directly testing for an investor-specific hedging motive would require observing investors’ endowments, which is not possible given the available data. Thus, we pursue a different strat- 

30 

egy. We study whether investors are ex-ante aware of the negative risk premium delivered by specialized ETFs and are willing to bear it as a form of insurance premium. In other words, we examine whether investors stick with these products _in spite_ of their negative performance. 

This empirical strategy also allows us to test the explanation that investors willingly sacrifice performance because specialized ETFs offer non-pecuniary benefits, e.g., in the form of compliance with investors’ ethical, political, or religious values. According to this explanation, investors should remain invested over time despite specialized ETFs’ underperformance. 

To implement this test, we analyze investors’ likelihood to allocate capital into specialized ETFs over the life of these products, and present the results in Table 5. Because there can be life-cycle patterns in ETF flows that are independent of performance, we benchmark specialized ETFs against broad-based ETFs. The sample consists of all ETF-months in our data. The dependent variable is an indicator for whether an ETF received positive flows in a particular month. The variable of interest is the interaction of the specialized ETF indicator and the logarithm of ETF age (in months). We include the main effects as well as calendar-month fixed effects. 

The estimates in Table 5 suggest that investors are very enthusiastic about specialized ETFs at their inception, but their enthusiasm fades over time. Naturally, ETFs tend to receive positive flows at the start of their life, arguably, because they are introduced in response to investors’ needs, whatever they are. Thus, at the beginning of the life of the ETF, the dependent variable is close to one. To illustrate, right after launch, 84% of broadbased ETFs have positive flows where the corresponding figure is 92% for specialized ETFs. As time passes, flows respond to performance. Thus, over time, the fraction of ETFs receiving positive flows decline below one, explaining the negative slope on the variable _Age_ . 

We are interested in the relative pace at which flows evolve over the life of the product. The negative interaction between age and the specialized dummy indicates that investors in specialized ETFs are more likely to be disappointed by performance than investors in 

31 

### **Table 5. Disappointment in Flows** 

The table studies the probability of positive flows into ETFs since launch. The sample period is from 2000 to 2019. The dependent variable is a dummy variable that equals 1 if ETF flows are positive, where ETF flows in month _t_ + 1 are defined as (AUM _t_ +1 _−_ AUM _t ×_ ETF return _t_ +1) _/_ AUM _t_ . _Specialized_ is a dummy variable that equals 1 if an ETF is a specialized ETF. _log(Age)_ is an ETF’s logged age, in months. The first two columns report results using the full sample from 2000 to 2019, and the last two columns report results for new ETFs launched in the previous five years. Standard errors are clustered at the ETF and the calendar-month levels, and _t_ -statistics are reported in parentheses. *, **, and *** indicate significance at the 10%, 5%, and 1% levels, respectively. 

|Dependent variable:||I(Positive l|flows_i,t_)||
|---|---|---|---|---|
|Sample:|Full sample|Full sample|Age _≤_60|Age _≤_60|
|Specialized|0.07***|0.07***|0.06**|0.06**|
||(3.01)|(3.32)|(2.18)|(2.53)|
|log(Age)|_−_0.05***|_−_0.05***|_−_0.03***|_−_0.03***|
||(_−_8.08)|(_−_8.25)|(_−_3.80)|(_−_4.66)|
|Specialized _×_ log(Age)|_−_0.03***<br>(_−_5.20)|_−_0.03***<br>(_−_5.48)|_−_0.03***<br>(_−_3.20)|_−_0.03***<br>(_−_3.81)|
|Constant|0.85***<br>(33.06)||0.80***<br>(29.70)||
|Calendar month FE|No|Yes|No|Yes|
|Observations|85,489|85,489|45,297|45,297|
|R<sup>2</sup>|0.027|0.104|0.009|0.132|



broad-based ETFs. This disenchantment manifests itself soon after the inception of the ETFs, as suggested by the estimates in Columns (3)–(4), where we restrict the sample to the first five years of ETFs’ lives. These findings are consistent with the positive slope of the flow-performance sensitivity for specialized ETFs shown in Figure 5. We interpret these results as suggestive of investor disappointment following the poor performance of specialized products. 

There is also a possibility that capital outflows create price pressure, which leads to the observed underperformance (`a la Gabaix and Koijen, 2021). We assess the viability of this possibility in Appendix F.7. Our analysis shows that the price impact of flows could be sizeable under certain assumptions, e.g., negative flows could amplify the underperformance of specialized ETFs by up to 2.7% over the five-year horizon since inception. However, the magnitude of the underperformance that we document is larger by an order of magnitude and exists independently of the magnifying effect of outflows. 

32 

ETF closures are another manifestation of disappointment. The termination of an ETF typically occurs when the fund does not have enough assets under management to justify its operating costs. Thus, the products that are more likely to be closed are those that investors did not find appealing, or stopped finding appealing. Therefore, studying the likelihood of ETF closures since launch and as a function of past performance allows us to study the evolution of investor interest in the products. 

We study in Appendix Figure F.3 both the likelihood of closure of ETFs as a function of time since launch as well as of their past performance. First, in Panel (a), we find that specialized ETFs are closed at a higher rate than broad-based ETFs at each point in time after their launch. One may argue that the higher rate of closure in the early life of specialized ETFs suggest that ETF providers test the waters with a large variety of products, some of which are soon terminated. However, higher closure rate that exists in the later stage of specialized ETFs’ lives indicates that investors are disappointed by their performance. Second, in Panel (b), we find that the closure rate is higher for specialized ETFs for the same level of underperformance. These results corroborate the earlier results that they are disappointed when specialized ETFs underperform, indicating that they were expecting positive alpha at the time of investment. 

Overall, the evidence in this subsection does not support the conjecture that investors invest in specialized ETFs for their hedging properties or that they willingly sacrifice performance because of non-pecuniary benefits. Therefore, in the next section, we turn to a different hypothesis to explain the demand for specialized products. 

# **6 Do Specialized ETFs Cater to Investor Sentiment?** 

Given that specialized ETFs deliver negative alpha and that there is no evidence that they serve as hedging tools, we turn to testing a third hypothesis, that specialized ETFs are launched in response to investors’ demand driven by performance chasing behavior. We 

33 

also provide evidence about the nature of these beliefs, i.e., whether they are consistent with rational expectations, or reflect irrational expectations such as extrapolative beliefs. 

We have already found some supporting evidence in Section 5.1 for the notion that securities in specialized ETFs are overvalued. Specifically, we found that the indexes underlying specialized ETFs exhibit a run-up in the period preceding the launch, and that specialized ETFs underperform after launch, potentially reversing the an earlier overvaluation. 

In this section, we conduct several tests studying whether the launch of specialized ETFs caters to investors’ irrational beliefs. First, if newly-launched specialized ETFs ride recent trends, then the securities included in their portfolios should ( _i_ ) have attracted investors’ attention, and ( _ii_ ) display traits of overvaluation. Second, the stocks in specialized portfolios should be attractive to investors who form expectations in an extrapolative way. Finally, specialized ETFs are likely to be especially attractive to investors who are, on average, less sophisticated, notably retail investors (Barber and Odean, 2013). 

## **6.1 Characteristics of the Underlying Portfolios** 

We begin by analyzing the characteristics of the stocks included in the portfolios of specialized and broad-based ETFs at the time of their launch. We focus on several characteristics that could indicate heightened investor attention and are likely associated with overvaluation. 

Table 6 compares the average ETF-level characteristic for specialized and broad-based portfolios. For each stock in an ETF portfolio, we measure different characteristics over the two-year period before the launch. Then, we compute the average of each characteristic at the ETF level (using the weights of each stock in the ETF) at the time of launch. 

The table shows that stocks in specialized ETFs have characteristics that could be appealing to investors with irrational beliefs and non-standard preferences. These stocks have significantly higher pre-launch market-adjusted returns, making them attractive to investors with extrapolative or diagnostic beliefs (e.g., Greenwood and Shleifer, 2014; Barberis et al., 

34 

### **Table 6. Portfolio Characteristics of ETFs Around Launch** 

The table reports the characteristics of stocks included in ETF portfolios over the two years before the launch. The sample period is from 2000 to 2019. We measure portfolio characteristics of ETFs from stockmonth level characteristics data. For each characteristic, we construct the time-series of the ETF-month level characteristic from month _−_ 24 to month _−_ 6 using the ETF’s portfolio weights in the launch month 0. We then compute the time-series average characteristic for each ETF. Finally, we calculate the average characteristic across all ETFs in the same category. We report the average characteristics and _t_ -test results. _Market-adjusted return_ represents returns in excess of CRSP value-weighted returns. _Return skewness_ is the skewness of returns following Ghysels et al. (2016). We use the 25<sup>th</sup> and 75<sup>th</sup> percentiles as cutoffs. _Size percentile rank_ is the percentile rank of market capitalization within each month using NYSE breakpoints. _Market-to-book_ is market equity divided by book equity. _Price-to-sales_ is price-to-sales ratio. _EV-to-EBITDA_ is enterprise value to earnings before interest, taxes, depreciation, and amortization. _Short interest_ is the monthly short interest ratio. _Media exposure_ is the number of monthly news articles scaled by market capitalization. _Media sentiment_ is the sum of each news article’s composite sentiment score from RavenPack scaled by market capitalization. For _Short interest_ , _Media exposure_ , and _Media sentiment_ , we subtract the median each month to filter out time trends, the mean being excessively impacted by outliers. _Earnings surprise_ denotes the average EPS surprise scaled by the one-quarter-lagged stock price. We standardize _Earnings surprise_ each year. _% Negative earnings_ is the percentage of firms with negative earnings. In the right-most column, we present the difference between the averages of specialized ETFs (Sp) and broad-based ETFs (BB). _t_ -statistics are reported in parentheses. *, **, and *** indicate significance at the 10%, 5%, and 1% levels, respectively. 

||Broad-based ETFs|Specialized ETFs|Sp minus BB|
|---|---|---|---|
|Market-adjusted return|0.66***|1.04***|0.38***|
||(11.51)|(9.23)|(4.15)|
|Return skewness|0.01|0.17***|0.15***|
||(0.40)|(4.80)|(4.12)|
|Size percentile rank|80.19***<br>|77.85***<br>|_−_2.35**<br>|
||(91.47)|(45.09)|(_−_1.98)|
|Market-to-book|2.98***|3.14***|0.15**|
||(44.51)|(32.10)|(2.07)|
|Price-to-sales|9.29***|28.83***|19.54***|
||(7.48)|(3.02)|(2.75)|
|EV-to-EBITDA|12.37***|14.69***|2.31***|
||(52.01)|(22.87)|(4.74)|
|Short interest|0.02***|0.03***|0.01***|
||(25.60)|(15.92)|(3.61)|
|Media exposure|_−_4.04|33.33***|37.37***|
||(_−_1.28)|(3.19)|(4.29)|
|Media sentiment|0.22***|0.64***|0.42***|
||(4.81)|(4.51)|(3.98)|
|Earnings surprise|0.02***|0.03***|0.01***|
||(9.00)|(10.78)|(2.50)|
|% Negative earnings|12.20***|20.10***|7.91***|
||(14.69)|(14.73)|(7.20)|



2018; Bordalo et al., 2018). Moreover, stocks held by specialized ETFs display more positive skewness, which would be appealing for investors who have a preference for lottery-like payoffs (Brunnermeier and Parker, 2005; Brunnermeier et al., 2007; Mitton and Vorkink, 2007; 

35 

Barberis and Huang, 2008; Kumar, 2009).<sup>31</sup> 

The table also suggests that specialized ETFs hold small growth stocks. They have high valuation multiples, notably the market-to-book, price-to-sales, and EV-to-EBITDA<sup>32</sup> ratios. Importantly, the stocks in the portfolios of specialized ETFs have higher short interest. All these characteristics are associated with lower future returns (Lakonishok, Shleifer, and Vishny, 1994; Daniel and Titman, 1997; Boehmer, Jones, and Zhang, 2008; Ben-David, Drake, and Roulstone, 2015). 

The characteristics of the securities included in the portfolios of specialized ETFs indicate that they are popular stocks, which attract investor attention. Relative to broad-based portfolios, stocks in specialized ETFs experienced greater media exposure with more positive sentiment, and greater earnings surprises. We also note that share turnover is materially larger for specialized products (see Table 1), which is consistent with the conjecture that these products are used for speculative purposes (e.g., Simsek, 2013b). 

The conjecture that specialized ETFs focus on sectors and themes that capture investor attention is consistent with anecdotal evidence on recent ETF launches. In 2019, for example, new ETFs included products focusing on cannabis, cybersecurity, and video games. In 2020, new specialized ETFs covered stocks related to the Black Lives Matter movement, COVID19 vaccines, and the work-from-home trend. In 2021, tracking the recovery after the COVID recession, new specialized ETFs covered the travel industry, and space travel as well as real estate and construction. 

To gain further intuition on the determinants of ETF inceptions, we analyze the behavior of a valuation ratio and media sentiment around launches. In Figure 7, we present the evolution of the market-to-book ratios (Panel (a)) and media sentiment scores (Panel (b)) of stocks included in broad-based and specialized ETFs. The figure shows that prior to launch, stocks included in specialized ETFs have a higher market-to-book ratio and a more positive media sentiment score, relative to those in broad-based ETFs. In the year after 

> 31In unreported analysis, we find that the difference in skewness persists after the ETF launch as well. 

> 32Enterprise value to earnings before interest taxes, depreciation, and amortization. 

36 

the launch, both market-to-book ratios and the media sentiment of the stocks in specialized ETFs quickly revert to lower levels.<sup>33</sup> 

### **Figure 7. Dynamics of ETF Portfolio Characteristics** 

The figure presents the evolution of ETF portfolio characteristics per ETF category. The sample period is from 2000 to 2019. Panel (a) shows the evolution of the market-to-book ratio, and Panel (b) shows the evolution of media sentiment. We measure portfolio characteristics of ETFs from stock-month level characteristics data. For each characteristic, we construct the time-series of the ETF-month level characteristic from month _−_ 24 to month +24 relative to the ETF launch month 0 using the ETF’s portfolio weights. In the pre-launch periods, we use the ETF’s initial portfolio weights in the launch month 0. In the post-launch periods, we use the actual portfolio weights. We then calculate the average characteristic across all ETFs in the same category each month. The shaded areas represent 95% confidence intervals. 



<!-- Start of picture text -->
(a) Market-to-book (b) Media sentiment<br>0 . 8<br>3 . 2<br>0 . 6<br>0 . 4<br>3<br>0 . 2<br>Broad-based ETFs<br>2 . 8<br>Specialized ETFs 0<br>− 20 − 10 0 10 20 − 20 − 10 0 10 20<br>Months relative to ETF launch date Months relative to ETF launch date<br>Market-to-book Mediasentiment<br><!-- End of picture text -->

This figure is consistent with the idea that the launches of specialized ETFs are timed to match investor excitement for the underlying themes. By the time an eligible sector or theme is identified by ETF issuers based on its popularity, the valuation cycle has already peaked. After launch, valuations start sliding downward. 

To provide further evidence on the overvaluation of specialized ETFs, we explore the relation between pre-launch characteristics denoting investor attention, i.e., returns and media sentiment, and subsequent performance _within_ each ETF category. The overvaluation conjecture suggests that greater pre-launch attention is likely to lead to overvaluation and is, therefore, correlated with subsequent underperformance. To construct Figure 8, we split the broad-based and specialized ETFs based on whether the pre-launch returns and me- 

> 33We note that, while we cannot infer that the two series in Panel (a) of Figure 7 differ at a given point in time for lack of power, the test in Table 6, using data over the entire 24-month period before launch, allows us to conclude that the market-to-book ratio of specialized ETFs is significantly higher than that of broad-based ETFs. 

37 

### **Figure 8. Performance of ETFs, Split by Pre-launch Stock Characteristics** 

The figure presents the Fama-French-Carhart four-factor model (Fama and French, 1993; Carhart, 1997) monthly alphas of the portfolios of ETFs from 2000 to 2019, split by ETF categories and stock characteristics groups. In Panel (a), we split each ETF category into two subgroups based on the past market-adjusted returns, computed as in Table 6. In Panel (b), we split each ETF category into two subgroups based on the past media sentiment, computed as in Table 6. In each month, we identify _new_ ETFs that were launched in the previous five years. We then form portfolios consisting of all _new_ ETFs in the same category and the same subgroup. The portfolio returns are value-weighted using one-month-lagged market capitalization. To adjust returns for risk factors, we estimate FFC-4 alphas of the portfolios. The alphas are in monthly percentage points. Error bars represent 95% confidence intervals. 



<!-- Start of picture text -->
(a) FFC-4 alphas, split by past returns (b) FFC-4 alphas, split by media sentiment<br>0 0<br>− 0 . 2 − 0 . 2<br>− 0 . 4 − 0 . 4<br>− 0 . 6 Low past returns − 0 . 6 Low media sentiment<br>High past returns High media sentiment<br>Broad-based ETFs Specialized ETFs Broad-based ETFs Specialized ETFs<br>(%)FFC-4factoralpha<br><!-- End of picture text -->

dia sentiment of the underlying portfolios are above or below the median. The figure plots the average post-launch Fama-French-Carhart four-factor alphas of the ETFs in the split groups. Within the specialized category, the ETFs that invest in stocks with the highest pre-launch returns and media sentiment, perform the worst, delivering a monthly FFC-4 alpha of _−_ 0 _._ 53% ( _−_ 0 _._ 58% in Panel (a) and _−_ 0 _._ 48% in Panel (b)).<sup>34</sup> In contrast, specialized ETFs that are launched following lower pre-launch returns and media sentiment underperform less—only _−_ 0 _._ 20% a month ( _−_ 0 _._ 01% in Panel (a) and _−_ 0 _._ 38% in Panel (b)). Given that these sorting characteristics are likely correlated with potential overvaluation, and they explain post-launch underperformance, the results corroborate our earlier evidence indicating that specialized ETFs tend to invest in overvalued assets. No significant separation along these dimensions is evident for broad-based ETFs, which suggests that overvaluation is likely to be an issue only within the specialized category. 

Overall, the evidence in this subsection suggests that the underperformance of specialized ETFs is likely related to the overvaluation of the securities in the underlying portfolios at the 

> 34Similar results are obtained with the other risk adjustments that we consider. 

38 

time of launch. Given that the pre-launch performance of the underlying portfolios of these ETFs, as well as the attention they attract, is high, the negative post-launch alpha suggests that the issuance of specialized ETFs occurs near the peak of valuation of the underlying securities. 

## **6.2 Evidence on the Nature of Investor Expectations** 

Given that specialized ETFs hold securities displaying high past returns, high media sentiment, and high valuations prior to launch, it is natural to ask whether the providers of specialized ETFs cater to investors’ extrapolative beliefs. Following Bordalo et al. (2019), we make the working assumption that analysts’ forecasts are reflective of investor beliefs and that they are informative about the expectations shaping market prices. 

In Figure 9, we study analysts’ forecasts for the stocks included in broad-based and specialized ETFs. We use data from I/B/E/S on analysts’ long-term earnings growth (LTG) forecasts and earnings-per-share (EPS) realizations. In Panel (a), we report the behavior of the average LTG forecasts for the stocks in the broad-based and specialized portfolios around the time of the ETF launch. Mirroring the pattern of the high-LTG portfolio in Bordalo et al. (2019), the portfolio of specialized stocks displays significantly higher forecasts on average. These forecasts become increasingly more positive in the period leading up to the launch. However, after the ETF launch, these stocks experience a marked downward revision in LTG expectations. No such pattern is found for the stocks in the broad-based portfolio. This finding cannot be attributed to attrition in the sample, as we keep only the stocks that have LTG forecasts for all the relevant periods. 

As argued by Bordalo et al. (2019), the mean-reversion in LTG forecasts could result from mean reversion in the underlying process, making Panel (a) compatible with rational expectations or excessively optimistic forecasts. To test the latter alternative, in Panel (b) of Figure 9, we report the average forecast errors for the stocks in the ETF portfolio in the eight quarters following the launch. Forecast errors are computed as the annual change in 

39 

realized EPS minus the LTG forecast at the time of launch. We find that forecast errors for specialized ETFs grow to be significantly negative and economically large, consistent with strong overoptimism in the expectations around the time of launch. We also find slightly negative forecast errors for broad-based ETFs, consistent with analysts’ incentives to inflate their forecasts (Easterwood and Nutt, 1999; Michaely and Womack, 1999; Dechow, Hutton, and Sloan, 2000). 

### **Figure 9. Dynamics of Earnings Forecasts Around Launch** 

The figure presents the evolution of earnings forecasts and forecast errors per ETF category. The sample period is from 2000 to 2019. Panel (a) shows the evolution of analysts’ expectations of long-term annual earnings growth (LTG). Panel (b) shows the evolution of forecast errors, defined as the difference between the realized annual earnings growth ([EPS _q_ /EPS _q−_ 4] _−_ 1) and LTG one quarter before launch (LTG _−_ 1). We measure portfolio-level earnings forecasts and forecast errors from stock-quarter level earnings data. For each variable, we construct the time-series of the ETF-quarter level variable from quarters _−_ 8 to +8 relative to the ETF launch quarter 0 using the ETF’s portfolio weights. In the pre-launch periods, we use the ETF’s portfolio weights in the launch quarter 0. In the post-launch periods, we use the actual portfolio weights. We then calculate the average across all ETFs in the same category each quarter. Shaded areas represent 95% confidence intervals. 



<!-- Start of picture text -->
(a) LTG (b) Forecast error<br>0<br>15<br>− 5<br>14<br>− 10<br>13<br>− 15<br>Broad-based ETFs<br>12<br>Specialized ETFs<br>− 20<br>− 8 − 6 − 4 − 2 0 2 4 6 8 0 2 4 6 8<br>Quarters relative to ETF launch date Quarters relative to ETF launch date<br>(%)LTG<br>(%)Forecasterror<br><!-- End of picture text -->

According to Bordalo et al. (2019), such patterns of expectations are inconsistent with a rational model of belief formation. Rather, these patterns can be generated in a model with diagnostic expectations, which represent a specific form of extrapolative beliefs. In particular, investors with diagnostic expectations would consider recent extreme realizations as representative of the prevailing distribution for a group of stocks—in our case the stocks that will be included in the specialized ETFs. Therefore, after positive surprises, expectations about future performance tend to be excessively optimistic. 

In sum, the evidence in this subsection supports the hypothesis that the providers of 

40 

specialized ETFs launch new products in segments of the stock market in which investors hold optimistic beliefs. These stocks likely experience greater investor demand, hence increasing the attractiveness of the new products. 

## **6.3 Who Is Attracted to Specialized ETFs?** 

As argued above, ETFs lower retail investors’ access costs to financial markets. Specialized ETFs, in particular, open up the opportunity to trading sectors and themes that would otherwise require significant search costs and, for this reason, would likely not be accessible to unsophisticated investors.<sup>35</sup> In this sense, ETFs are an important step towards realizing the vision of the former U.S. Securities and Exchange Commission (SEC) Chairman, Jay Clayton: “I believe it is important to focus on solutions that provide access [to Main Street investors] to investment opportunities on substantially the same terms as those that would be available to institutional investors.”<sup>36</sup> 

It is interesting, therefore, to understand whether specialized ETFs cater to a specific group of investors—unsophisticated investors. To answer this question, we examine the investor composition in the different ETF categories. In this analysis, we focus on the first year after launch to more closely identify the target clientele. 

We start by using regulatory filings by institutional investors. In particular, they report their ownership of ETFs on the mandatory quarterly SEC 13F forms.<sup>37</sup> Institutional investors include mutual funds, hedge funds, pension funds, banks, insurance companies, endowments, etc. Prior literature suggests that institutions are on average more sophisticated investors than individuals, i.e., their investment decisions are less prone to the systematic bi- 

> 35For example, an investor who is interested to invest in the restaurants sector does not need to conduct a thorough market research or security search; instead, the investor can conveniently buy the restaurant ETF, aptly called BITE. 

> 36Testimony before the U.S. Senate Committee on Banking, Housing, and Urban Affairs, Washington D.C., December 10, 2019. Available on `https://www.sec.gov/news/testimony/ testimony-clayton-2019-12-10` . 

> 37Only institutions that manage more than $100 million in U.S. equity and which are doing business with U.S. investors are required to file a 13F form. The filers need to report positions exceeding $200,000 or 10,000 shares. 

41 

ases (e.g., French, 2008; Stambaugh, 2014) that often impact the decisions of retail investors (Barber and Odean, 2013). 

Figure 10, Panel (a), reports the average fraction of shares owned by institutional investors in the first four quarters after launch. The panel shows that institutions own about 43% of the market capitalization of broad-based ETFs in their first year. In contrast, institutions own a significantly lower share of the market capitalization of specialized ETFs, about 39%. Because shares not owned by 13F-reporting institutions are either owned by smaller (non-reporting) institutions, managers, or retail investors, we deduce that retail investors are likely to own a greater share of the specialized ETFs universe than that of the broadbased ETF universe, supporting the view that unsophisticated investors are more likely to be attracted to specialized ETFs. 

### **Figure 10. ETF Ownership Soon After Launch** 

The figure presents the ownership structures of ETFs one year after launch per ETF category. Over the first 4 quarters after launch, we calculate the average ownership of 13F institutional investors and the number of Robinhood users scaled by AUM ($m). Panel (a) reports 13F ownership, and Panel (b) reports the number of Robinhood users per AUM. Bar charts represent the average ownership, and error bars represent 95% confidence intervals. 



<!-- Start of picture text -->
(a) Institutional ownership (b) Number of Robinhood users<br>20<br>0 . 44<br>0 . 42<br>10<br>0 . 4<br>0<br>Broad-based ETFs Specialized ETFs Broad-based ETFs Specialized ETFs<br>ownershipInstitutional<br>users/$mAUM#Robinhood<br><!-- End of picture text -->

We can also gain direct insights into ownership by sentiment-driven investors through user data from the discount brokerage Robinhood. These data are available starting in 2018 and include the number of Robinhood accounts holding each security at the daily frequency. The Robinhood platform has recently become known for investment frenzies, characterizing its users.<sup>38</sup> Panel (b) of Figure 10 shows that the number of Robinhood users scaled by ETF 38See `https://www.nytimes.com/2020/07/08/technology/robinhood-risky-trading.html` . 

42 

market capitalization is substantially higher for specialized ETFs than for the broad-based ETFs in their first year of existence. This result is consistent with the observations of Barber et al. (2022) and Welch (2020), that Robinhood investors hold attention-grabbing securities. The authors show that Robinhood traders experience negative returns shortly after they open their positions.<sup>39</sup> 

### **Figure 11. Robinhood Users’ Investments in the Underlying Stocks and ETFs** 

The figure presents the number of Robinhood users who hold ETFs or their underlying stocks per ETF category. We subtract the median of the Robinhood users each month to filter out time trends. In Panel (a), we construct the time series of the ETF-month level number of Robinhood users from month _−_ 18 to month +18 relative to the launch month 0 using the ETF’s portfolio weights. In the pre-launch periods, we use the ETF’s portfolio weights in the launch month 0. In the post-launch periods, we use the actual portfolio weights. We then calculate the average number of Robinhood users across all ETFs in the same category each month. Panel (b) reports the average number of Robinhood users who directly invest in ETFs. The shaded areas represent 95% confidence intervals. 



<!-- Start of picture text -->
(a) Robinhood users: Underlying stocks<br>30 , 000<br>20 , 000<br>10 , 000<br>− 10 − 5 0 5 10<br>Months relative to ETF launch date<br>(#)Robinhoodusers<br><!-- End of picture text -->

#### (b) Robinhood users: ETFs 



<!-- Start of picture text -->
Broad-based ETFs<br>Specialized ETFs<br>500<br>0<br>0 2 4 6 8 10 12<br>Months relative to ETF launch date<br><!-- End of picture text -->

Examining the portfolios of Robinhood users around the launch of ETFs provides further support for the hypothesis that specialized ETFs are launched in segments of the market that have attracted the attention of unsophisticated investors. In Figure 11, we use an event study around ETF launches to plot the holdings of stocks in ETF portfolios by Robinhood users. Specifically, we compute the number of users holding the stocks that will be included in the ETF (to be launched in month 0), weighted by their weight in the ETF. Because the Robinhood user base increased significantly over the sample period, we subtract the median 

> 39Welch (2020) also finds that Robinhood traders’ strategy, which is concentrated on high-volume and large stocks, delivers a positive alpha over the 1980–2020 period. This evidence, arising from trades in _stocks_ , does not necessarily contradict our results showing that _specialized ETFs_ , which are favored by Robinhood traders, deliver a negative alpha. 

43 

stock holding in the relevant calendar month.<sup>40</sup> We also report the number of users holding the ETFs directly. 

The results in Panel (a) of Figure 11 show that the number of users holding the stocks that will be included in specialized ETFs increases and peaks right before the launch. Around the launch time, the number of users starts declining. We observe no similar pattern for broad-based ETFs. These results reiterate the point made in Section 6.1 that specialized ETFs are launched in segments of the market about which investors hold positive views; further, these products arrive to the market after the excitement has peaked. 

Once new specialized ETFs are launched, they attract some of the Robinhood traders (Figure 11, Panel (b)), though not at the same rate as the underlying stocks do. Investors who are drawn to new specialized ETFs lose their interest after a few months. Broad-based ETFs do not exhibit these patterns. 

The picture that emerges from these results is that specialized ETFs cater to investors’ expectations formed by extrapolating positive past performance of popular investment themes into the future. These portfolios include attention-grabbing stocks that are overvalued at the time of launch. In the years following the launch, the value of the underlying assets decline, together with the value of the specialized ETFs holding them. 

# **7 Conclusion** 

This paper studies the most prominent financial innovation in the last 30 years: exchangetraded funds (ETFs). Many observers view the growth of ETFs as a positive development that allows ordinary investors to achieve diversification at low cost and to construct payoff profiles that would otherwise be unattainable. 

Our evidence shows a more nuanced reality. We identify two segments in the ETF market. Broad-based ETFs hold diversified portfolios and charge low fees. These products respond 

> 40Due to the skewness of the holdings data, adjusting user holdings by the median gives more meaningful and stable results than adjusting by the mean. 

44 

to investors’ motive to achieve diversification and market access at a low cost. Specialized ETFs, in contrast, offer investors exposure to trendy themes at a high cost and low level of diversification. Although the average AUM of these funds is smaller, in the aggregate, they drive over one-third of the revenues of the equity-based ETF industry in the U.S. 

While broad-based ETFs clearly achieve their goal of providing diversification at low cost, we examine whether specialized ETFs provide value in terms of exposure to successful investment ideas or, if that is not the case, in the form of insurance. Our results suggest that specialized ETFs, on average, do not create value for investors. These ETFs tend to hold attention-grabbing and overvalued stocks and therefore underperform significantly: They deliver a negative annual alpha of about _−_ 6% in the five years after their inception, on average. We find no evidence that the negative performance corresponds to the price that investors are willing pay to insure against relevant risk factors, or that they are willing to pay a premium for some non-pecuniary benefits. 

Instead, our evidence suggests that specialized ETFs appear to cater to overoptimistic investors. Specialized ETFs are launched just after the very peak of excitement around popular investment themes. Over the years following the launch, the underlying assets shed some of their initial overvaluation, and so do the prices of specialized ETFs. 

We conclude that the implications of the “democratization of investment” that ETFs bring about are mixed. On the one hand, investors can now access financial markets at low cost, which can be welfare-improving because it allows broader risk sharing. On the other hand, the marketing strategies of specialized ETFs facilitate speculation in overvalued securities, which subsequently underperform. It is possible that, absent specialized ETFs, these investors would still invest their money inefficiently. However, specialized ETFs likely encourage greater investor participation due to their marketing efforts and competitive strategies. Investors on the extensive margin may be worse off as a result of holding specialized ETFs. 

45 

# **References** 

- Akey, Pat, Adriana Robertson, and Mikhail Simutin, 2021, Closet active management of passive funds, Working paper, University of Toronto. 

- Allen, Franklin, and Douglas Gale, 1994, _Financial innovation and risk sharing_ (MIT press). 

- Arteaga, Kenneth R, Conrad S Ciccotello, and C Terry Grant, 1998, New equity funds: Marketing and performance, _Financial Analysts Journal_ 54, 43–49. 

- Baker, Malcolm, and Jeffrey Wurgler, 2007, Investor sentiment in the stock market, _Journal of Economic Perspectives_ 21, 129–152. 

- Ball, Ray, and Philip Brown, 1968, An empirical evaluation of accounting income numbers, _Journal of Accounting Research_ 159–178. 

- Barber, Brad M, Xing Huang, Terrance Odean, and Christopher Schwarz, 2022, Attentioninduced trading and returns: Evidence from Robinhood, _Journal of Finance_ forthcoming. 

- Barber, Brad M, and Terrance Odean, 2013, The behavior of individual investors, in _Handbook of the Economics of Finance_ , volume 2, 1533–1570 (Elsevier). 

- Barberis, Nicholas, Robin Greenwood, Lawrence Jin, and Andrei Shleifer, 2018, Extrapolation and bubbles, _Journal of Financial Economics_ 129, 203–227. 

- Barberis, Nicholas, and Ming Huang, 2008, Stocks as lotteries: The implications of probability weighting for security prices, _American Economic Review_ 98, 2066–2100. 

- Barberis, Nicholas, and Andrei Shleifer, 2003, Style investing, _Journal of Financial Economics_ 68, 161–199. 

- Ben-David, Itzhak, Michael S Drake, and Darren T Roulstone, 2015, Acquirer valuation and acquisition decisions: Identifying mispricing using short interest, _Journal of Financial and Quantitative Analysis_ 50, 1–32. 

- Ben-David, Itzhak, Francesco Franzoni, and Rabih Moussawi, 2017, Exchange-traded funds, _Annual Review of Financial Economics_ 9, 169–189. 

- Ben-David, Itzhak, Francesco Franzoni, and Rabih Moussawi, 2018, Do ETFs increase volatility?, _Journal of Finance_ 73, 2471–2535. 

- Ben-David, Itzhak, Francesco Franzoni, and Rabih Moussawi, 2019, An improved method to predict assignment of stocks into Russell indexes, _Journal of Finance: Replications and Corrigenda (web-only:_ _`https: // doi. org/ 10. 37214/ jofweb. 1` )_ . 

- Boehmer, Ekkehart, Charles M Jones, and Xiaoyan Zhang, 2008, Which shorts are informed?, _Journal of Finance_ 63, 491–527. 

- Bordalo, Pedro, Nicola Gennaioli, Rafael La Porta, and Andrei Shleifer, 2019, Diagnostic expectations and stock returns, _Journal of Finance_ 74, 2839–2874. 

46 

- Bordalo, Pedro, Nicola Gennaioli, and Andrei Shleifer, 2016, Competition for attention, _Review of Economic Studies_ 83, 481–513. 

- Bordalo, Pedro, Nicola Gennaioli, and Andrei Shleifer, 2018, Diagnostic expectations and credit cycles, _Journal of Finance_ 73, 199–227. 

- Brightman, Chris, Feifei Li, and Xi Liu, 2015, Chasing performance with ETFs, White paper, Research Affiliates. 

- Brunnermeier, Markus K, Christian Gollier, and Jonathan A Parker, 2007, Optimal beliefs, asset prices, and the preference for skewed returns, _American Economic Review_ 97, 159– 165. 

- Brunnermeier, Markus K, and Jonathan A Parker, 2005, Optimal expectations, _American Economic Review_ 95, 1092–1118. 

- Carhart, Mark M, 1997, On persistence in mutual fund performance, _Journal of Finance_ 52, 57–82. 

- C´el´erier, Claire, and Boris Vall´ee, 2017, Catering to investors through security design: Headline rate and complexity, _Quarterly Journal of Economics_ 132, 1469–1508. 

- Chuprinin, Oleg, and Thomas Ruf, 2018, Rent seeking and mutual fund inceptions, Working paper, University of New South Wales. 

- Cooper, Michael J, Orlin Dimitrov, and P Raghavendra Rau, 2001, A Rose.com by any other name, _Journal of Finance_ 56, 2371–2388. 

- Cooper, Michael J, Huseyin Gulen, and P Raghavendra Rau, 2005, Changing names with style: Mutual fund name changes and their effects on fund flows, _Journal of Finance_ 60, 2825–2858. 

- Cosemans, Mathijs, and Rik Frehen, 2021, Salience theory and stock prices: Empirical evidence, _Journal of Financial Economics_ 140, 460–483. 

- Da, Zhi, Xing Huang, and Lawrence J Jin, 2020, Extrapolative beliefs in the cross-section: What can we learn from the crowds?, _Journal of Financial Economics_ 140, 175–196. 

- Daniel, Kent, and Sheridan Titman, 1997, Evidence on the characteristics of cross sectional variation in stock returns, _Journal of Finance_ 52, 1–33. 

- Dannhauser, Caitlin D, and Jeffrey Pontiff, 2019, Flow, Working paper, Boston College. 

- Davies, Shaun, 2022, Speculation sentiment, _Journal of Financial and Quantitative Analysis_ forthcoming. 

- De Long, J Bradford, Andrei Shleifer, Lawrence H Summers, and Robert J Waldmann, 1990a, Noise trader risk in financial markets, _Journal of Political Economy_ 98, 703–738. 

47 

- De Long, J Bradford, Andrei Shleifer, Lawrence H Summers, and Robert J Waldmann, 1990b, Positive feedback investment strategies and destabilizing rational speculation, _Journal of Finance_ 45, 379–395. 

- Dechow, Patricia M, Amy P Hutton, and Richard G Sloan, 2000, The relation between analysts’ forecasts of long-term earnings growth and stock price performance following equity offerings, _Contemporary Accounting Research_ 17, 1–32. 

- Duffie, Darrell, and Rohit Rahi, 1995, Financial market innovation and security design: An introduction, _Journal of Economic Theory_ 65, 1–42. 

- Easley, David, David Michayluk, Maureen O’Hara, and T¯alis J Putni¸nˇs, 2021, The active world of passive investing, _Review of Finance_ 25, 1433–1471. 

- Easterwood, John C, and Stacey R Nutt, 1999, Inefficiency in analysts’ earnings forecasts: Systematic misreaction or systematic optimism?, _Journal of Finance_ 54, 1777–1797. 

- Egan, Mark, Alexander MacKay, and Hanbin Yang, 2022, Recovering investor expectations from demand for index funds, _Review of Economic Studies_ forthcoming. 

- Elton, Edwin J, Martin J Gruber, and Joel Rentzler, 1989, New public offerings, information, and investor rationality: The case of publicly offered commodity funds, _Journal of Business_ 62, 1–15. 

- Evans, Richard B, 2010, Mutual fund incubation, _Journal of Finance_ 65, 1581–1611. 

- Fama, Eugene F, 1998, Market efficiency, long-term returns, and behavioral finance, _Journal of Financial Economics_ 49, 283–306. 

- Fama, Eugene F, and Kenneth R French, 1992, The cross-section of expected stock returns, _Journal of Finance_ 47, 427–465. 

- Fama, Eugene F, and Kenneth R French, 1993, Common risk factors in the returns on stocks and bonds, _Journal of Financial Economics_ 33, 3–56. 

- Fama, Eugene F, and Kenneth R French, 2015, A five-factor asset pricing model, _Journal of Financial Economics_ 116, 1–22. 

- Fama, Eugene F, and Kenneth R French, 2018, Choosing factors, _Journal of Financial Economics_ 128, 234–252. 

- French, Kenneth R, 2008, Presidential address: The cost of active investing, _Journal of Finance_ 63, 1537–1573. 

- Gabaix, Xavier, and Ralph SJ Koijen, 2021, In search of the origins of financial fluctuations: The inelastic markets hypothesis, Technical report, National Bureau of Economic Research. 

- Gao, Pengjie, Allen Hu, Peter Kelly, Cameron Peng, and Ning Zhu, 2020, Exploited by complexity, Working paper, University of Notre Dame. 

48 

- Gennaioli, Nicola, Andrei Shleifer, and Robert Vishny, 2012, Neglected risks, financial innovation, and financial fragility, _Journal of Financial Economics_ 104, 452–468. 

- Ghysels, Eric, Alberto Plazzi, and Rossen Valkanov, 2016, Why invest in emerging markets? The role of conditional return asymmetry, _Journal of Finance_ 71, 2145–2192. 

- Greene, Jason T, and Jeffrey Stark, 2016, What’s trending? The performance and motivations for mutual fund startups, Working paper, Bridgewater State University. 

- Greenwood, Robin, and Samuel G Hanson, 2013, Issuer quality and corporate bond returns, _Review of Financial Studies_ 26, 1483–1525. 

- Greenwood, Robin, and Andrei Shleifer, 2014, Expectations of returns and expected returns, _Review of Financial Studies_ 27, 714–746. 

- Harvey, Campbell R, 2017, Presidential address: The scientific outlook in financial economics, _Journal of Finance_ 72, 1399–1440. 

- Harvey, Campbell R, 2021, Be skeptical of asset management research, Working paper, Duke University. 

- Harvey, Campbell R, Yan Liu, and Heqing Zhu, 2016, . . . and the cross-section of expected returns, _Review of Financial Studies_ 29, 5–68. 

- Henderson, Brian J, and Neil D Pearson, 2011, The dark side of financial innovation: A case study of the pricing of a retail financial product, _Journal of Financial Economics_ 100, 227–247. 

- Henderson, Brian J, Neil D Pearson, and Li Wang, 2020, Retail derivatives and sentiment: A sentiment measure constructed from issuances of retail structured equity products, Working paper, University of Illinois at Urbana-Champagne. 

- Hou, Kewei, Chen Xue, and Lu Zhang, 2015, Digesting anomalies: An investment approach, _Review of Financial Studies_ 28, 650–705. 

- Huang, Shiyang, Maureen O’Hara, and Zhuo Zhong, 2020a, Innovation and informed trading: Evidence from industry ETFs, _Review of Financial Studies_ 34, 1280–1316. 

- Huang, Shiyang, Yang Song, and Hong Xiang, 2020b, The Smart Beta mirage, Working paper, University of Washington. 

- Jain, Prem C, and Joanna Shuang Wu, 2000, Truth in mutual fund advertising: Evidence on future performance and fund flows, _Journal of Finance_ 55, 937–958. 

- Karoui, Aymen, and Iwan Meier, 2009, Performance and characteristics of mutual fund starts, _European Journal of Finance_ 15, 487–509. 

- Khomyn, Marta, T¯alis J Putni¸nˇs, and Marius Zoican, 2020, The value of ETF liquidity, Working paper, University of Technology Sydney. 

49 

- Khorana, Ajay, and Henri Servaes, 1999, The determinants of mutual fund starts, _Review of Financial Studies_ 12, 1043–1074. 

- Kostovetsky, Leonard, and Jerold B Warner, 2020, Measuring innovation and product differentiation: Evidence from mutual funds, _Journal of Finance_ 75, 779–823. 

- Kumar, Alok, 2009, Who gambles in the stock market?, _Journal of Finance_ 64, 1889–1933. 

- Lakonishok, Josef, Andrei Shleifer, and Robert W Vishny, 1994, Contrarian investment, extrapolation, and risk, _Journal of Finance_ 49, 1541–1578. 

- Lee, Charles MC, Andrei Shleifer, and Richard H Thaler, 1991, Investor sentiment and the closed-end fund puzzle, _Journal of Finance_ 46, 75–109. 

- Lintner, John, 1965, The valuation of risk assets and the selection of risky investments in stock portfolios and capital budgets, _Review of Economics and Statistics_ 47, 13–37. 

- Madhavan, Ananth, and Aleksander Sobczyk, 2019, Does trading by ETF and mutual fund investors hurt performance? Evidence from time-and dollar-weighted returns, _Journal of Investment Management_ 17, 1–17. 

- Massa, Massimo, 1998, Why so many mutual funds? Mutual fund families, market segmentation and financial performance, Working paper, Insead. 

- Michaely, Roni, and Kent L Womack, 1999, Conflict of interest and the credibility of underwriter analyst recommendations, _Review of Financial Studies_ 12, 653–686. 

- Miller, Edward M, 1977, Risk, uncertainty, and divergence of opinion, _Journal of Finance_ 32, 1151–1168. 

- Mitchell, Mark L, and Erik Stafford, 2000, Managerial decisions and long-term stock price performance, _Journal of Business_ 73, 287–329. 

- Mitton, Todd, and Keith Vorkink, 2007, Equilibrium underdiversification and the preference for skewness, _Review of Financial Studies_ 20, 1255–1288. 

- Mossin, Jan, 1966, Equilibrium in a capital asset market, _Econometrica_ 34, 768–783. 

- Moussawi, Rabih, Ke Shen, and Raisa Velthuis, 2020, ETF heartbeat trades, tax efficiencies, and clienteles: The role of taxes in the flow migration from active mutual funds to ETFs, Working paper, Villanova University. 

- Novick, Barbara, 2017, How index funds democratize investing, _Wall Street Journal_ (January, 8). 

- Sharpe, William F, 1964, Capital asset prices: A theory of market equilibrium under conditions of risk, _Journal of Finance_ 19, 425–442. 

- Shefrin, Hersh M, and Richard H Thaler, 1988, The behavioral life-cycle hypothesis, _Economic Inquiry_ 26, 609–643. 

50 

- Shleifer, Andrei, and Robert W Vishny, 1997, The limits of arbitrage, _Journal of Finance_ 52, 35–55. 

- Simsek, Alp, 2013a, Financial innovation and portfolio risks, _American Economic Review: Papers & Proceedings_ 103, 398–401. 

- Simsek, Alp, 2013b, Speculation and risk sharing with new financial assets, _Quarterly Journal of Economics_ 128, 1365–1396. 

- Stambaugh, Robert F, 2014, Presidential address: Investment noise and trends, _Journal of Finance_ 69, 1415–1453. 

- Vanguard, 2020, How America invests, White paper, The Vanguard Group. 

- Vokata, Petra, 2021, Engineering lemons, _Journal of Financial Economics_ 142, 737–755. 

- Welch, Ivo, 2020, Retail raw: Wisdom of the Robinhood crowd and the Covid crisis, Working paper, National Bureau of Economic Research. 

51 

# **Appendix A A Primer on ETFs** 

Exchange-traded products (ETPs) are investment companies whose objective is to replicate the performance of an index, in a similar manner to index mutual funds. Unlike index funds, however, ETPs are listed on an exchange and are traded throughout the day. These funds are organized in several legal structures, such as exchange-traded funds (ETFs), exchange-traded notes (ETNs), exchange-traded commodities, and index participation units (IPU). In this article, we focus exclusively on ETFs. 

The first U.S. ETF was launched in January 1993. It tracked the S&P 500 (ticker: SPY). SPY is currently the largest ETF in the world, with nearly $300 billion in assets. As of the end of 2019, the number of ETFs has grown to over 3,000 in the United States and nearly 7,000 globally, with these products spanning various asset classes. 

ETFs can reproduce the performance of the relevant index in two distinct ways. First, they can hold a basket of securities that, more or less, replicates the index (“physical replication”). Second, they can enter into swap agreements with financial institutions to have the performance of the index delivered by these counterparties in exchange for a fee (“synthetic replication”). The physical structure is prevalent in the United States, and it characterizes all the ETFs in our sample. 

The focus in this article is on “plain vanilla” equity ETFs that hold portfolios of stocks that track an index. The index can be an existing index, such as the S&P 500 or Russell 2000, or an index that is designed by the issuers expressly for the ETF, e.g., the index tracked by the work-from-home ETF, launched in June 2020. 

The innovation in the ETF structure revolves around the creation and redemption mechanism that takes place on a daily basis and keeps the market price of the ETF in close proximity to the value of the basket of securities in the index it tracks. Because ETFs hold securities that are, themselves, traded on the market, there is a possibility of temporary misalignment between the price of ETF shares and the value of the basket of securities. For example, when there is high demand for the ETF, but not yet for the underlying securities, 

52 

the ETF will trade at a premium relative to the underlying index. To ensure that significant deviations are not created between the ETF and the underlying securities portfolio, ETFs continuously issue new shares when investor demand is high or redeem shares when investor demand is low. The creation or redemption of ETF shares is called _flows_ , which can be positive or negative, and can indicate the demand for the ETF in excess of the demand for the underlying securities. 

For further reading about ETFs, please see Ben-David, Franzoni, and Moussawi (2017), Ben-David, Franzoni, and Moussawi (2018), and Ben-David, Franzoni, and Moussawi (2019). 

53 

# **Appendix B Data Sources** 

## **B.1 ETF Data** 

We use information from the Center for Research in Security Prices (CRSP) to identify a comprehensive and survivorship-bias-free list of all U.S. equity ETFs. We first select securities with share code of 73 from CRSP, or a non-missing ETF flag in the CRSP Mutual Fund Database. Because we are interested in ETFs that hold U.S. equities, we drop ETFs focusing on the bond market (that have a CRSP style of fixed income, mixed holdings, or other—style codes: _I_ , _M_ , _O_ , or names that contain the word “bond”). We also drop inverse and leveraged ETFs (that have a Lipper classification code of _DSB_ ,<sup>41</sup> or CRSP style code _EDY S_ or _EDY H_ ,<sup>42</sup> or the name contains any of the following: 2 _×_ , 3 _×_ , bear, or bull). We exclude ETFs that are classified as foreign equity ETFs (CRSP style code _F_ ). The final sample contains 1,080 distinct U.S. equity ETFs that satisfy all requirements. 

CRSP is our primary source for daily trading data. We rely on Bloomberg for ETF shares outstanding information, and supplement it with Compustat when the Bloomberg data are not available. Furthermore, we use CRSP’s end-of-month information about returns and prices, and supplement it with Bloomberg’s and Compustat’s total shares outstanding to calculate month-end assets under management (AUM). Compustat is our primary source for monthly short interest data. 

## **B.2 ETF Holdings Data** 

We obtain ETF holdings information from two sources: the Thomson Reuters Global Mutual Fund Ownership and CRSP Mutual Fund Holdings databases. For many ETFs, both sources contain holdings information; for others, holdings information is only available 

> 41 _DSB_ : dedicated short bias funds. More information about Lipper classification codes is provided in: `http://www.crsp.org/products/documentation/lipper-objective-and-classification-codes` . 

> 42 _EDY S_ : Dedicated Short Bias Funds. _EDY N_ : long/short equity funds, equity market neutral funds, absolute return funds, and equity leverage funds. More information about CRSP style codes is provided in: `http://www.crsp.org/products/documentation/crsp-style-code` . 

54 

in one of the sources. In many cases, first report dates of portfolio holdings differ between the two. Our approach is to take one source per ETF as the reference for its holdings. If an ETF has holdings information in both sources, we use the one with the start date that is closer to the launch date in CRSP. We notice that CRSP holdings data are relatively more reliable and timely after June 2010 and those in the earlier period of the sample, the Thomson Reuters Global Ownership data are more reliable to track ETF ownership soon after launch dates. 

## **B.3 Firm-Level Data** 

We use Compustat for firm-level accounting information and obtain the analysts-forecastbased measure of earnings surprises from I/B/E/S. Firm-level news data are from RavenPack News Analytics. We aggregate daily-level news items into monthly-level news counts. 13F institutional ownership data are from Thomson Reuters, and Robinhood users data are from Robintrack. 

## **B.4 Financial Markets Data** 

We calculate risk-adjusted returns using six different risk models: the CAPM (Sharpe, 1964; Lintner, 1965; Mossin, 1966), the Fama-French three-factor (Fama and French, 1993), the Fama-French-Carhart four-factor (Carhart, 1997), the Fama-French five-factor (Fama and French, 2015), the Fama-French six-factor (Fama and French, 2018), and the Q-factor (Hou et al., 2015) models.<sup>43</sup> 

> 43Risk factor returns are downloaded from Professor French’s website: `https://mba.tuck.dartmouth. edu/pages/faculty/ken.french/data_library.html` and Professors Hou, Xue, and Zhang’s website: `http://global-q.org/factors.html` . 

55 

# **Appendix C Variable Definitions** 

|**Variable**|**Definition**|**Source**|
|---|---|---|
|**ETF-level variables**|||
|Active share|The sum of the absolute value of the difference between<br>the fund portfolio weight and the weight in the market<br>portfolio.|Thomson Reuters Global,<br>CRSP Mutual Fund|
|Fee|Fiscal year-end expense ratio.|Bloomberg|
|Turnover|The average daily trading volume scaled by the total<br>shares outstanding.|CRSP|
|Market-adjusted|ETF monthly returns in excess of CRSP value-|CRSP|
|return|weighted returns.||
|Delisted|An indicator for whether an ETF is liquidated as of<br>the end of the sample.|CRSP|
|AUM|The total market value of the investments ($bn).|CRSP|
|Implied revenues|Fees multiplied by the average AUM ($m) in each year.|Bloomberg, CRSP|
|Differentiation|One minus the cosine similarity between the ETF port-<br>folio weights and the weights of the aggregate portfolio<br>of all ETFs in the same category that exist in the mar-<br>ket at that point in time.|Thomson Reuters Global,<br>CRSP Mutual Fund|
|Flows|Flows in month _t_ + 1 are computed as (AUM_t_+1 _−_<br>AUM_t ×_ETF return_t_+1)_/_AUM_t_.|CRSP|
|Age|Age in each month _t_ is an ETF’s age in months since<br>the launch month 0.|CRSP|
|13F ownership<br># of Robinhood users|The total ownership of 13F institutional investors.<br>The number of Robinhood users holding an ETF.|Thomson Reuters<br>Robintrack|
|**Firm-level variables**|||
|Market-adjusted|Monthly returns in excess of CRSP value-weighted re-|CRSP|
|return|turns.||
|Return skewness|The skewness of returns following Ghysels et al. (2016).<br>We use the 25<sup>th </sup>and 75<sup>th </sup>percentiles as cutoffs.|CRSP|
|Media exposure|The number of monthly news articles scaled by market<br>capitalization.|RavenPack|
|Media sentiment|Sum of each news article’s composite sentiment score<br>scaled by market capitalization.|RavenPack|
|Earnings surprise|The average earnings-per-share (EPS) surprises scaled<br>by the one-quarter-lagged stock price.|I/B/E/S, CRSP|
|Market-to-book|Market equity divided by book equity.|Compustat, CRSP|
|Price-to-sale|Market equity divided by sales.|Compustat, CRSP|
|EV-to-EBITDA|Enterprise<br>value<br>(market<br>equity+book<br>value<br>of<br>debt_−_cash) divided by earnings before interest, taxes,<br>depreciation, and amortization.|Compustat, CRSP|
|Short interest|The ratio of the number of shares shorted to the total<br>shares outstanding.|Compustat|
|LTG|Analysts’ expectation of long-term annual earnings<br>growth.|I/B/E/S|
|Forecast error|The difference between the realized annual earnings<br>|I/B/E/S|
||growth and LTG.||
|# of Robinhood users|The number of Robinhood users holding a stock.|Robintrack|



56 

# **Appendix D Additional Empirical Results** 

### **Table D.1. ETF Summary Statistics** 

The table shows summary statistics at the ETF level. The sample period is from 1993 to 2019. Panels A, B, C, and D report summary statistics for broad-index ETFs, smart-beta ETFs, sector/industry ETFs, and thematic ETFs, respectively. _Number of holdings_ represents the average number of stocks in the portfolios of ETFs. _Fee_ refers to annualized expense ratio. _Share turnover_ is the average daily share turnover of the ETF over the six months after launch. _Market-adjusted return_ is monthly ETF return in excess of CRSP value-weighted return over the 60 months after launch. _Delisted_ is an indicator for whether the ETF was liquidated as of the end of 2019. _Assets under management_ (AUM) is the total market value of the investments as of the end of 2019. _Implied revenues_ are calculated by multiplying fee by the average AUM in 2019. 

||**Panel A: B**|**road-In**|**dex ET**|**Fs**|||||
|---|---|---|---|---|---|---|---|---|
||N|Mean|SD|P5|P25|P50|P75|P95|
|Number of holdings|90|865|823|50|266|538|1262|2938|
|Fee (bps)|77|28|23|5|15|20|28|75|
|Share turnover (months 1–6; %)|87|3.64|3.99|0.33|0.94|1.88|5.84|9.82|
|Market-adjusted return (months 1|–60, %)<br>88|_−_0.01|0.30|_−_0.37|_−_0.17|_−_0.02|0.15|0.42|
|Delisted|90|0.17|0.37|0|0|0|0|1|
|**2019 statistics**|||||||||
|Assets under management ($bn)|75|17.49|47.70|0.00|0.11|1.00|10.17|130.54|
|Implied revenues ($m)|63|27.82|70.50|0.02|0.55|2.31|19.27|134.15|
||**Panel B: **|**Smart-B**|**eta ET**|**Fs**|||||
||N|Mean|SD|P5|P25|P50|P75|P95|
|Number of holdings|463|313|336|36|99|199|437|954|
|Fee (bps)|418|44|24|13|26|38|60|85|
|Share turnover (months 1–6; %)|460|2.73|3.11|0.19|0.90|2.06|3.42|7.77|
|Market-adjusted return (months 1|–60, %)<br>463|_−_0.18|0.40|_−_0.90|_−_0.35|_−_0.12|0.03|0.30|
|Delisted|464|0.18|0.39|0|0|0|0|1|
|**2019 statistics**|||||||||
|Assets under management ($bn)|357|2.31|6.83|0.01|0.05|0.18|0.96|11.62|
|Implied revenues ($m)|327|5.68|13.92|0.03|0.20|0.79|4.06|28.37|
||**Panel C: Se**|**ctor/Ind**|**ustry **|**ETFs**|||||
||N|Mean|SD|P5|P25|P50|P75|P95|
|Number of holdings|401|80|80|20|32|50|93|238|
|Fee (bps)|366|52|20|17|35|55|68|82|
|Share turnover (months 1–6; %)|411|4.04|7.04|0.37|1.09|2.14|4.22|13.63|
|Market-adjusted return (months 1|–60, %)<br>411|_−_0.32|0.94|_−_1.98|_−_0.68|_−_0.18|0.27|0.80|
|Delisted|411|0.28|0.45|0|0|0|1|1|
|**2019 statistics**|||||||||
|Assets under management ($bn)|281|1.55|4.13|0.01|0.05|0.23|1.02|7.87|
|Implied revenues ($m)|272|6.68|17.17|0.05|0.29|1.02|4.37|37.30|



(continued below) 

57 

### **Table D.1. ETF Summary Statistics (Continued)** 

(continued from the previous page) 

|**Pane**|**l D: T**|**hemati**|**c ETF**|**s**|||||
|---|---|---|---|---|---|---|---|---|
||N|Mean|SD|P5|P25|P50|P75|P95|
|Number of holdings|114|108|106|27|39|75|106|350|
|Fee (bps)|85|67|20|35|50|65|75|95|
|Share turnover (months 1–6; %)|115|2.93|2.87|0.37|1.05|2.04|3.69|9.08|
|Market-adjusted return (months 1–60, %)|115|_−_0.87|2.43|_−_5.04|_−_0.83|_−_0.30|0.02|0.50|
|Delisted|115|0.37|0.48|0|0|0|1|1|
|**2019 statistics**|||||||||
|Assets under management ($bn)|73|0.33|0.66|0.00|0.01|0.06|0.20|1.84|
|Implied revenues ($m)|57|2.22|3.77|0.02|0.14|0.43|2.10|12.35|



### **Table D.2. Difference in Fees Across ETF Categories** 

The table reports the difference in fees across ETF categories from 2000 to 2019. The dependent variable _Fee_ is the annualized expense ratio of an ETF in each month. _Specialized_ is a dummy variable that equals 1 if an ETF is a specialized ETF. _Thematic_ is a dummy variable that equals 1 if an ETF is a thematic ETF. _Sector/industry_ is a dummy variable that equals 1 if an ETF is a sector/industry ETF. _Smart-beta_ is a dummy variable that equals 1 if an ETF is a smart-beta ETF. Standard errors are clustered at the ETF, the management company, and the calendar-month levels. _t_ -statistics are reported in parentheses. *, **, and *** indicate significance at the 10%, 5%, and 1% levels, respectively. 

|Dependent variable:||||Fee_t_|(bps)||||
|---|---|---|---|---|---|---|---|---|
||(1)|(2)|(3)|(4)|(5)|(6)|(7)|(8)|
|Specialized|14.17***|12.52***|13.72***|11.82***|||||
||(3.98)|(3.20)|(4.87)|(3.61)|||||
|Thematic|||||41.77***|19.96***|29.77***|18.45***|
||||||(10.50)|(6.01)|(7.56)|(9.16)|
|Sector/industry|||||26.98***|16.65***|22.03***|15.94***|
||||||(9.94)|(4.26)|(10.51)|(4.58)|
|Smart-beta|||||18.71***|5.79***|11.81***|5.62***|
||||||(4.82)|(4.35)|(4.25)|(4.10)|
|Constant|35.50***|36.35***|35.73***|36.71***|20.97***|31.84***|26.54***|32.33***|
||(6.53)|(18.01)|(10.12)|(21.79)|(7.14)|(15.59)|(9.52)|(17.09)|
|Mgmt company FE|No|Yes|No|Yes|No|Yes|No|Yes|
|Launch year FE|No|No|Yes|Yes|No|No|Yes|Yes|
|Observations|81,594|81,594|81,594|81,594|81,594|81,594|81,594|81,594|
|R-squared|0.100|0.710|0.353|0.757|0.182|0.715|0.378|0.762|



58 

### **Table D.3. Concentration Among Issuers** 

The table presents the number of ETFs and issuers across ETF categories from 1993 to 2019. We also report the concentration among issuers within each ETF category in 2019. We proxy the concentration level by computing the Herfindahl-Hirschman Index (HHI) of issuers’ market shares in 2019. 

||# ETFs|# Issuers|# Issuers/# ETFs|HHI (2019)|
|---|---|---|---|---|
|Broad-index|90|26|0.289|0.31|
|Smart-beta|464|86|0.185|0.28|
|Sector/industry|411|50|0.122|0.24|
|Thematic|115|44|0.383|0.20|



### **Table D.4. Sensitivity of ETF Flows to Fees (Robustness)** 

The table reports the flow sensitivity of ETFs to their fees. The sample period is from 2000 to 2019. The observations are at the ETF level. The dependent variable is cumulative flows over a 12-month or 24-month window after the launch of each ETF. _Fee_ is the average annualized expense ratio of an ETF over the 12month or 24-month time window. _Return rank_ is the average percentile rank of returns within each month over the 12-month or 24-month time window. _Specialized_ is a dummy variable that equals 1 if an ETF is a specialized ETF. _t_ -statistics are reported in parentheses. *, **, and *** indicate significance at the 10%, 5%, and 1% levels, respectively. 

|Dependent variable:|Cumulative flo|lws (%) over. . .|
|---|---|---|
||12 months since launch|24 months since launch|
|Fee (bps)|_−_0.58***<br>(_−_2.67)|_−_0.92***<br>(_−_3.63)|
|Fee _×_ Specialized|0.70**|0.76*|
||(2.08)|(1.92)|
|Return rank|1.10<br>(1.55)|2.57**<br>(2.34)|
|Return rank _×_ Specialized|0.60<br>(0.69)|_−_1.34<br>(_−_1.00)|
|Specialized|_−_82.03*<br>(_−_1.65)|17.32<br>(0.23)|
|Launch year FE|Yes|Yes|
|Observations|931|931|
|R<sup>2</sup>|0.084|0.100|



59 

### **Figure D.1. Number of ETF Issuers** 

The Venn diagram presents the number of issuers per ETF category from 1993 to 2019. 



<!-- Start of picture text -->
44 49 27<br>(37%) (41%) (23%)<br>Broad-based ETFs<br>Specialized ETFs<br><!-- End of picture text -->

60 

# **Appendix E** 

# **Flow-Performance Sensitivity (Robustness)** 

In Appendix Figure E.1, we replicate the analysis in Figure 5 using market-adjusted returns and the percentile rank of returns within each month. We confirm that the inferences remain unchanged. In Appendix Figure E.2, we show that the same flow-performance sensitivity pattern is present when we measure the performance at the quarterly and annual frequencies. 

### **Figure E.1. Flow-Performance Sensitivity with Alternative Performance Measure** 

The figure presents the flow-performance sensitivity of ETFs per ETF category. The sample period is from 2000 to 2019. Flows are computed as (AUM _t_ +1 _−_ AUM _t ×_ ETF return _t_ +1) _/_ AUM _t_ . Market-adjusted returns are raw ETF returns in excess of CRSP value-weighted returns. Return percentile rank is the percentile rank of returns within each month. We estimate a non-parametric relation between flows and returns using local polynomial approximations obtained with Stata’s `-lpoly-` command with bandwidth of 0.04. The shaded areas represent 95% confidence intervals. 

#### (a) Market-adjusted returns 



<!-- Start of picture text -->
4%<br>Broad-based ETFs<br>Specialized ETFs<br>2%<br>0%<br>− 2%<br>− 4%<br>− 12% − 6% 0% 6% 12%<br>Market-adjusted return t (%)<br>(%)Flow+1 t<br><!-- End of picture text -->



<!-- Start of picture text -->
(b) Percentile rank of returns<br>4%<br>2%<br>0%<br>− 2%<br>− 4%<br>0 20 40 60 80 100<br>Return percentile rank t<br><!-- End of picture text -->

61 

### **Figure E.2. Flow-Performance Sensitivity with Low Frequency Data** 

The figure presents the flow-performance sensitivity of ETFs per ETF category. The sample period is from 2000 to 2019. Flows are computed as (AUM _t_ +1 _−_ AUM _t ×_ ETF return _t_ +1) _/_ AUM _t_ . Returns are raw ETF returns. In Panel (a) (Panel (b)), we measure performance and flow at the quarterly (annual) frequency. We estimate a non-parametric relation between flows and returns using local polynomial approximations obtained with Stata’s `-lpoly-` command with bandwidth of 0.04. The shaded areas represent 95% confidence intervals. 



<!-- Start of picture text -->
(a) Quarterly frequency (b) Annual frequency<br>10% 30%<br>Broad-based ETFs<br>Specialized ETFs<br>15%<br>0% 0%<br>− 15%<br>− 10% − 30%<br>− 20% − 10% 0% 10% 20% − 40% − 20% 0% 20% 40%<br>Return q (%) Return y (%)<br>(%)Flow+1 q (%)Flow+1 y<br><!-- End of picture text -->

62 

# **Appendix F ETF Performance (Robustness)** 

## **F.1 ETF Performance with Equally Weighted Returns** 

Appendix Table F.1 reports the performance of ETFs with equal-weighted returns. 

### **Table F.1. Calendar-Time Portfolios of ETFs (Equally-Weighted)** 

The table presents the risk-adjusted performance of ETFs from 2000 to 2019. In Panel A, we form portfolios consisting of all ETFs in the same category. In Panel B, we identify _new_ ETFs that were launched in the previous five years in each month. We then form portfolios consisting of all _new_ ETFs in the same category. In Panel C, we identify _seasoned_ ETFs that were launched more than five years prior in each month. The portfolio returns are equal-weighted. _Excess return_ refers to the average monthly return in excess of the risk-free rate. _CAPM_ , _FF3_ , _FFC4_ , _FF5_ , _FF6_ , and _Q_ denote alphas with respect to the Capital Asset Pricing Model (Sharpe, 1964; Lintner, 1965; Mossin, 1966), the Fama-French three-factor model (Fama and French, 1993), the Fama-French-Carhart four-factor model (Carhart, 1997), the Fama-French five-factor model (Fama and French, 2015), the Fama-French six-factor model (Fama and French, 2018), and the Q- factor model (Hou et al., 2015), respectively. The portfolios of all broad-based (specialized) ETFs comprise 171 (189) ETFs on average. _Sp minus BB_ denotes the specialized ETF portfolio minus the broad-based ETF portfolio. The excess return and alphas are in percentage points, and _t_ -statistics are reported in parentheses. *, **, and *** indicate significance at the 10%, 5%, and 1% levels, respectively. 

|||**Panel A**|**: All Mo**|**nths**||||
|---|---|---|---|---|---|---|---|
||Excess return|CAPM|FF3|FFC4|FF5|FF6|Q|
|Broad-based ETFs|0.50*|0.02|_−_0.03|_−_0.02|_−_0.05|_−_0.05|_−_0.03|
|Specialized ETFs|(1.73)<br>0.29|(0.41)<br>_−_0.25***|(_−_0.77)<br>_−_0.25***|(_−_0.48)<br>_−_0.20***|(_−_1.47)<br>_−_0.19**|(_−_1.38)<br>_−_0.17**|(_−_0.90)<br>_−_0.11|
|Sp minus BB|(0.89)<br>_−_0.20**<br>(_−_2.37)|(_−_3.02)<br>_−_0.26***<br>(_−_3.31)|(_−_3.06)<br>_−_0.22***<br>(_−_2.92)|(_−_2.72)<br>_−_0.18**<br>(_−_2.58)|(_−_2.27)<br>_−_0.14*<br>(_−_1.79)|(_−_2.25)<br>_−_0.12*<br>(_−_1.71)|(_−_1.50)<br>_−_0.08<br>(_−_1.15)|
|||**Panel B**|**: Months**|_≤_**60**||||
||Excess return|CAPM|FF3|FFC4|FF5|FF6|Q|
|Broad-based ETFs|0.47<br>(1.65)|_−_0.00<br>(_−_0.07)|_−_0.05<br>(_−_1.27)|_−_0.04<br>(_−_1.03)|_−_0.05<br>(_−_1.38)|_−_0.05<br>(_−_1.29)|_−_0.05<br>(_−_1.20)|
|Specialized ETFs|0.21<br>(0.62)|_−_0.34***<br>(_−_3.49)|_−_0.34***<br>(_−_3.58)|_−_0.29***<br>(_−_3.29)|_−_0.28***<br>(_−_2.85)|_−_0.26***<br>(_−_2.85)|_−_0.19**<br>(_−_2.13)|
|Sp minus BB|_−_0.26**<br>(_−_2.53)|_−_0.33***<br>(_−_3.53)|_−_0.29***<br>(_−_3.20)|_−_0.25***<br>(_−_2.89)|_−_0.23**<br>(_−_2.39)|_−_0.21**<br>(_−_2.34)|_−_0.15*<br>(_−_1.70)|
|||**Panel C**|**: Months**|_>_ **60**||||
||Excess return|CAPM|FF3|FFC4|FF5|FF6|Q|
|Broad-based ETFs|0.69**|_−_0.06|_−_0.03|_−_0.03|_−_0.06**|_−_0.06**|_−_0.03|
||(2.27)|(_−_1.41)|(_−_1.25)|(_−_1.13)|(_−_2.13)|(_−_2.00)|(_−_0.87)|
|Specialized ETFs|0.65**<br>(2.12)|_−_0.10<br>(_−_1.55)|_−_0.09<br>(_−_1.46)|_−_0.07<br>(_−_1.24)|_−_0.08<br>(_−_1.20)|_−_0.06<br>(_−_0.95)|_−_0.02<br>(_−_0.38)|
|Sp minus BB|_−_0.05<br>(_−_0.86)|_−_0.04<br>(_−_0.67)|_−_0.06<br>(_−_1.00)|_−_0.04<br>(_−_0.79)|_−_0.02<br>(_−_0.31)|_−_0.00<br>(_−_0.05)|0.00<br>(0.07)|



63 

## **F.2 ETF Performance with Gross Returns** 

We replicate the results on ETF performance with gross-of-fee returns. Appendix Figure F.1 reproduces Figure 2, and Appendix Table F.2 reproduces Table 3. 

### **Figure F.1. Performance of ETFs Around Launch with Gross Returns** 

The figure reproduces Figure 2 with gross-of-fee returns. For each ETF group, we form 60 calendar-time portfolios that include returns of ETFs in their month +1 _,_ +2 _, . . . ,_ +60 since the launch date (month 0). The portfolio returns are value-weighted using one-month-lagged market capitalization. We have 60 time series of portfolio returns per ETF category. To adjust returns for risk factors, we estimate the Fama-FrenchCarhart four-factor model (FFC-4) alphas of the portfolios (Fama and French, 1993; Carhart, 1997). We have 60 estimated FFC-4 alphas per ETF category. The lines represent cumulative FFC-4 alphas, and the shaded areas represent 95% confidence intervals. 



<!-- Start of picture text -->
0<br>− 5<br>− 10<br>− 15<br>− 20<br>− 25<br>− 30<br>Broad-based ETFs<br>Specialized ETFs<br>− 35<br>0 10 20 30 40 50 60<br>Months relative to ETF launch date<br>(%)FFC-4Cumulativealphas<br><!-- End of picture text -->

64 

### **Table F.2. Calendar-Time Portfolios of ETFs with Gross Returns** 

The table presents reproduces Table 3 with gross-of-fee returns. In Panel A, we form portfolios consisting of all ETFs in the same category. In Panel B, we identify _new_ ETFs that were launched in the previous five years in each month. We then form portfolios consisting of all _new_ ETFs in the same category. In Panel C, we identify _seasoned_ ETFs that were launched more than five years prior in each month. We then form portfolios consisting of all _seasoned_ ETFs in the same category. The portfolio returns are value-weighted using one-month-lagged market capitalization. _Excess return_ refers to the average monthly return in excess of the risk-free rate. _CAPM_ , _FF3_ , _FFC4_ , _FF5_ , _FF6_ , and _Q_ alpha denote alphas with respect to the Capital Asset Pricing Model (Sharpe, 1964; Lintner, 1965; Mossin, 1966), the Fama-French three-factor model (Fama and French, 1993), the Fama-French-Carhart four-factor model (Carhart, 1997), the Fama-French five-factor model (Fama and French, 2015), the Fama-French six-factor model (Fama and French, 2018), and the Q- factor model (Hou et al., 2015), respectively. The portfolios of all broad-based (specialized) ETFs comprise 171 (189) ETFs on average. _Sp minus BB_ denotes the specialized ETF portfolio minus the broad-based ETF portfolio. The excess return and alphas are in percentage points, and _t_ -statistics are reported in parentheses. *, **, and *** indicate significance at the 10%, 5%, and 1% levels, respectively. 

|||**Panel A**|**: All Mo**|**nths**||||
|---|---|---|---|---|---|---|---|
||Excess return|CAPM|FF3|FFC4|FF5|FF6|Q|
|Broad-based ETFs<br>Specialized ETFs<br>Sp minus BB|0.47<br>(1.55)<br>0.23<br>(0.71)<br>_−_0.24***<br>(_−_3.02)|_−_0.03<br>(_−_0.52)<br>_−_0.29***<br>(_−_3.06)<br>_−_0.26***<br>(_−_3.27)|_−_0.02<br>(_−_0.38)<br>_−_0.25***<br>(_−_3.07)<br>_−_0.23***<br>(_−_3.02)|_−_0.01<br>(_−_0.14)<br>_−_0.24***<br>(_−_2.93)<br>_−_0.24***<br>(_−_3.01)|0.07<br>(1.29)<br>_−_0.10<br>(_−_1.21)<br>_−_0.16**<br>(_−_2.02)|0.07<br>(1.36)<br>_−_0.10<br>(_−_1.19)<br>_−_0.16**<br>(_−_2.04)|0.06<br>(1.15)<br>_−_0.10<br>(_−_1.24)<br>_−_0.16**<br>(_−_2.02)|
|||**Panel B**|**: Months**|_≤_**60**||||
||Excess return|CAPM|FF3|FFC4|FF5|FF6|Q|
|Broad-based ETFs<br>Specialized ETFs|0.33<br>(0.96)<br>0.03|_−_0.20<br>(_−_1.53)<br>_−_0.51***|_−_0.15<br>(_−_1.33)<br>_−_0.49***|_−_0.11<br>(_−_0.99)<br>_−_0.46***|0.11<br>(1.06)<br>_−_0.31**|0.12<br>(1.20)<br>_−_0.31**|0.07<br>(0.69)<br>_−_0.30**|
||(0.10)|(_−_3.80)|(_−_3.88)|(_−_3.70)|(_−_2.49)|(_−_2.45)|(_−_2.45)|
|Sp minus BB|_−_0.29**<br>(_−_2.06)|_−_0.30**<br>(_−_2.12)|_−_0.34**<br>(_−_2.36)|_−_0.35**<br>(_−_2.48)|_−_0.42***<br>(_−_2.87)|_−_0.43***<br>(_−_2.91)|_−_0.37**<br>(_−_2.50)|
|||**Panel C**|**: Months**|_>_ **60**||||
||Excess return|CAPM|FF3|FFC4|FF5|FF6|Q|
|Broad-based ETFs|0.71**|_−_0.02|_−_0.02|_−_0.02|_−_0.03|_−_0.03|_−_0.01|
||(2.42)|(_−_0.79)|(_−_0.71)|(_−_0.69)|(_−_1.35)|(_−_1.32)|(_−_0.59)|
|Specialized ETFs|0.63**<br>(2.12)|_−_0.09<br>(_−_1.22)|_−_0.09<br>(_−_1.21)|_−_0.09<br>(_−_1.21)|_−_0.09<br>(_−_1.20)|_−_0.09<br>(_−_1.21)|_−_0.05<br>(_−_0.64)|
|Sp minus BB|_−_0.09|_−_0.07|_−_0.07|_−_0.07|_−_0.06|_−_0.06|_−_0.03|
||(_−_1.30)|(_−_1.01)|(_−_1.06)|(_−_1.07)|(_−_0.84)|(_−_0.87)|(_−_0.48)|



65 

## **F.3 ETF Performance: U.S. Equity ETFs** 

In Appendix Table F.3, we restrict the sample of broad-based and specialized ETFs to those that include at least 80% of their market capitalization invested in stocks traded in the United States, and estimate risk-adjusted returns using the calendar-time portfolio approach as in Table 3. The results of the analysis are similar to those reported in Table 3. 

### **Table F.3. Calendar-Time Portfolios Around ETF Launches (U.S. Equity ETFs)** 

The table presents risk-adjusted performance of ETFs from 2000 to 2019. We require ETFs to hold at least 80% of their AUM in U.S. stocks. In each month, we identify _new_ ETFs that were launched within the previous five years. We then form a portfolio consisting of all _new_ ETFs in the same category. The portfolio returns are value-weighted using one-month-lagged market capitalization. _Excess return_ refers to the average monthly return in excess of the risk-free rate. _CAPM_ , _FF3_ , _FFC4_ , _FF5_ , _FF6_ , and _Q_ alpha denote alphas with respect to the Capital Asset Pricing Model (Sharpe, 1964; Lintner, 1965; Mossin, 1966), the Fama-French three-factor model (Fama and French, 1993), the Fama-French-Carhart four-factor model (Carhart, 1997), the Fama-French five-factor model (Fama and French, 2015), the Fama-French six-factor model (Fama and French, 2018), and the Q-factor model (Hou et al., 2015), respectively. The portfolios of broad-based (specialized) ETFs include 89 (79) ETFs on average. _Sp minus BB_ denotes the specialized ETF portfolio minus the broad-based ETFs portfolio. The excess return and alphas are in percentage points, and _t_ -statistics are reported in parentheses. *, **, and *** indicate significance at the 10%, 5%, and 1% levels, respectively. 

||Excess return|CAPM|FF3|FFC4|FF5|FF6|Q|
|---|---|---|---|---|---|---|---|
|Broad-based ETFs|0.31|_−_0.22*|_−_0.18|_−_0.13|0.10|0.11|0.06|
||(0.90)|(_−_1.67)|(_−_1.55)|(_−_1.20)|(1.00)|(1.10)|(0.53)|
|Specialized ETFs|_−_0.07|_−_0.62***|_−_0.60***|_−_0.58***|_−_0.42***|_−_0.42***|_−_0.42***|
||(_−_0.07)|(_−_3.78)|(_−_3.85)|(_−_3.72)|(_−_2.65)|(_−_2.63)|(_−_2.72)|
|Sp minus BB|_−_0.38**|_−_0.40**|_−_0.42**|_−_0.45**|_−_0.53***|_−_0.54***|_−_0.48**|
||(_−_2.11)|(_−_2.19)|(_−_2.32)|(_−_2.47)|(_−_2.78)|(_−_2.81)|(_−_2.54)|



66 

## **F.4 ETF Performance: Alternative Classification** 

In Appendix Table F.4, we confirm the underperformance of specialized ETFs when we identify them as those with either a large active share, a small number of portfolio holdings, or those charging high fees. 

In Appendix Table F.5, we show that both sector/industry and thematic ETFs exhibit significant underperformance. The sample period starts in 2010 since few new thematic ETFs are available to form portfolios before 2010. 

### **Table F.4. New ETFs’ Performance (Alternative Classification)** 

The table presents risk-adjusted performance of ETFs from 2000 to 2019. We identify _new_ ETFs that were launched within the previous five years. In each month, we form 5 portfolios by sorting _new_ ETFs on an active share (Panel A), the number of holdings (Panel B), or fee (Panel C). The three variables are measured within the first six months after the launch of ETFs. The portfolio returns are value-weighted using onemonth-lagged market capitalization. We exclude ETFs’ first six months of returns to avoid a look-ahead bias. _Excess return_ refers to the average monthly return in excess of the risk-free rate. _CAPM_ , _FF3_ , _FFC4_ , _FF5_ , _FF6_ , and _Q_ denote alphas with respect to the Capital Asset Pricing Model (Sharpe, 1964; Lintner, 1965; Mossin, 1966), the Fama-French three-factor model (Fama and French, 1993), the Fama-French-Carhart four-factor model (Carhart, 1997), the Fama-French five-factor model (Fama and French, 2015), the FamaFrench six-factor model (Fama and French, 2018), and the Q-factor model (Hou et al., 2015), respectively. The excess return and alphas are in percentage points, and _t_ -statistics are reported in parentheses. *, **, and *** indicate significance at the 10%, 5%, and 1% levels, respectively. 

||**Panel A: **|**Portfolios**|**Sorted b**|**y Active **|**Share**|||
|---|---|---|---|---|---|---|---|
||Excess return|CAPM|FF3|FFC4|FF5|FF6|Q|
|Low active share|0.52*|_−_0.02|_−_0.01|_−_0.00|_−_0.03|_−_0.03|_−_0.02|
||(1.94)|(_−_0.57)|(_−_0.22)|(_−_0.11)|(_−_0.73)|(_−_0.74)|(_−_0.64)|
|Q2|0.45|_−_0.14*|_−_0.14*|_−_0.12|_−_0.08|_−_0.09|_−_0.09|
||(1.49)|(_−_1.92)|(_−_1.92)|(_−_1.63)|(_−_1.08)|(_−_1.10)|(_−_1.17)|
|Q3|0.56*|_−_0.02|_−_0.08|_−_0.07|_−_0.07|_−_0.07|_−_0.04|
||(1.86)|(_−_0.18)|(_−_1.00)|(_−_0.87)|(_−_0.83)|(_−_0.84)|(_−_0.51)|
|Q4|0.46|_−_0.14|_−_0.20|_−_0.20|_−_0.23*|_−_0.23*|_−_0.13|
||(1.42)|(_−_0.99)|(_−_1.61)|(_−_1.55)|(_−_1.76)|(_−_1.76)|(_−_1.00)|
|High active share|_−_0.05|_−_0.62**|_−_0.67***|_−_0.66***|_−_0.63**|_−_0.63**|_−_0.55**|
||(_−_0.14)|(_−_2.43)|(_−_2.69)|(_−_2.61)|(_−_2.38)|(_−_2.38)|(_−_2.15)|
|High minus low|_−_0.57**|_−_0.60**|_−_0.67***|_−_0.66**|_−_0.60**|_−_0.60**|_−_0.52**|
||(_−_2.23)|(_−_2.31)|(_−_2.64)|(_−_2.58)|(_−_2.27)|(_−_2.27)|(_−_2.05)|



(continued below) 

67 

**Table F.4. New ETFs’ performance (Alternative Classification)** 

(continued from the previous page) 

||**Panel **|**B: Portfol**|**ios Sorted**|**by # Ho**|**ldings**|||
|---|---|---|---|---|---|---|---|
||Excess return|CAPM|FF3|FFC4|FF5|FF6|Q|
|Low # holdings|0.17|_−_0.44***|_−_0.47***|_−_0.42***|_−_0.35**|_−_0.35**|_−_0.32**|
||(0.52)|(_−_3.22)|(_−_3.52)|(_−_3.21)|(_−_2.51)|(_−_2.57)|(_−_2.46)|
|Q2|0.05|_−_0.49**|_−_0.51**|_−_0.50**|_−_0.53**|_−_0.53**|_−_0.45**|
||(0.14)|(_−_2.36)|(_−_2.43)|(_−_2.37)|(_−_2.44)|(_−_2.44)|(_−_2.13)|
|Q3|0.48*|_−_0.07|_−_0.08|_−_0.09|_−_0.09|_−_0.09|_−_0.08|
||(1.69)|(_−_0.83)|(_−_0.97)|(_−_1.05)|(_−_0.97)|(_−_0.97)|(_−_0.95)|
|Q4|0.54*|_−_0.05|_−_0.06|_−_0.04|_−_0.10|_−_0.10|_−_0.04|
||(1.82)|(_−_0.62)|(_−_0.91)|(_−_0.63)|(_−_1.41)|(_−_1.46)|(_−_0.49)|
|High # holdings|0.65**|0.05|_−_0.00|0.01|0.01|0.00|0.02|
||(2.13)|(0.67)|(_−_0.03)|(0.18)|(0.10)|(0.09)|(0.36)|
|Low minus high|_−_0.47***|_−_0.49***|_−_0.47***|_−_0.43***|_−_0.35**|_−_0.35**|_−_0.34**|
||(_−_3.51)|(_−_3.60)|(_−_3.49)|(_−_3.22)|(_−_2.52)|(_−_2.56)|(_−_2.58)|
||**Pa**|**nel C: Po**|**rtfolios So**|**rted by Fe**|**e**|||
||Excess return|CAPM|FF3|FFC4|FF5|FF6|Q|
|Low fee|0.36|_−_0.20|_−_0.14|_−_0.11|0.12|0.13|0.08|
||(0.99)|(_−_1.48)|(_−_1.24)|(_−_0.94)|(1.11)|(1.22)|(0.74)|
|Q2|0.61*|0.06|0.01|0.06|0.08|0.09|0.11|
||(1.89)|(0.45)|(0.11)|(0.48)|(0.58)|(0.66)|(0.81)|
|Q3|0.34|_−_0.13|_−_0.08|_−_0.01|_−_0.08|_−_0.05|0.00|
||(0.98)|(_−_0.62)|(_−_0.41)|(_−_0.05)|(_−_0.37)|(_−_0.24)|(0.02)|
|Q4|0.16|_−_0.44***|_−_0.47***|_−_0.45***|_−_0.47***|_−_0.47***|_−_0.40***|
||(0.49)|(_−_3.42)|(_−_3.68)|(_−_3.54)|(_−_3.51)|(_−_3.52)|(_−_3.08)|
|High fee|0.03|_−_0.58***|_−_0.60***|_−_0.57***|_−_0.76***|_−_0.73***|_−_0.68***|
||(0.09)|(_−_3.10)|(_−_3.32)|(_−_3.14)|(_−_4.30)|(_−_4.13)|(_−_3.56)|
|High minus low|_−_0.43*|_−_0.40|_−_0.46*|_−_0.44*|_−_0.83***|_−_0.80***|_−_0.75***|
||(_−_1.69)|(_−_1.57)|(_−_1.94)|(_−_1.85)|(_−_3.84)|(_−_3.70)|(_−_3.04)|



68 

### **Table F.5. New ETFs’ Performance by Categories** 

The table presents risk-adjusted performance of ETFs from 2010 to 2019. In each month, we identify _new_ ETFs that were launched within the previous five years. We then form a portfolio consisting of all _new_ ETFs in the same category. The portfolio returns are value-weighted using one-month-lagged market capitalization. _Excess return_ refers to the average monthly return in excess of the risk-free rate. _CAPM_ , _FF3_ , _FFC4_ , _FF5_ , _FF6_ , and _Q_ denote alphas with respect to the Capital Asset Pricing Model (Sharpe, 1964; Lintner, 1965; Mossin, 1966), the Fama-French three-factor model (Fama and French, 1993), the Fama-French-Carhart four-factor model (Carhart, 1997), the Fama-French five-factor model (Fama and French, 2015), the FamaFrench six-factor model (Fama and French, 2018), and the Q-factor model (Hou et al., 2015), respectively. The excess return and alphas are in percentage points, and _t_ -statistics are reported in parentheses. *, **, and *** indicate significance at the 10%, 5%, and 1% levels, respectively. 

||Excess return|CAPM|FF3|FFC4|FF5|FF6|Q|
|---|---|---|---|---|---|---|---|
|Broad-index|1.01***|_−_0.04|_−_0.03|_−_0.03|_−_0.03|_−_0.03|_−_0.03|
||(3.04)|(_−_1.07)|(_−_0.72)|(_−_0.69)|(_−_0.79)|(_−_0.77)|(_−_0.64)|
|Smart-beta|0.92***|0.04|0.03|0.04|_−_0.03|_−_0.01|_−_0.01|
||(3.21)|(0.47)|(0.34)|(0.51)|(_−_0.34)|(_−_0.16)|(_−_0.09)|
|Sector/industry|0.36|_−_0.69***|_−_0.65***|_−_0.60***|_−_0.60***|_−_0.55***|_−_0.46**|
||(0.95)|(_−_3.39)|(_−_3.21)|(_−_2.99)|(_−_2.93)|(_−_2.73)|(_−_2.38)|
|Thematic|0.55|_−_0.71***|_−_0.79***|_−_0.75***|_−_0.73***|_−_0.70***|_−_0.71***|
||(1.26)|(_−_3.77)|(_−_4.18)|(_−_3.99)|(_−_3.88)|(_−_3.72)|(_−_3.79)|



69 

## **F.5 A Stock-Level Trading Strategy** 

In Appendix Table F.6, we propose a simple stock-level trading strategy instead of relying on ETF returns. In each month, we identify the top-five holdings of specialized ETFs at the time of launch. Then, we use a moving window and collect the top holdings from all specialized ETFs launched in the previous 12 months. Finally, we use this stock list to construct a portfolio with monthly rebalancing. We present results with equal- and valueweighted returns with one-month-lagged market capitalization. 

### **Table F.6. Stock-Level Trading Strategy** 

The table presents the performance of the stock-level trading strategy from 2000 to 2019. In each month, we identify the top-five holdings of specialized ETFs launched within the previous 12 months. We then form a portfolio consisting of all distinct stocks in the recently launched specialized ETFs. The portfolio returns are equal- or value-weighted using one-month-lagged market capitalization with monthly rebalancing. _Excess return_ refers to the average monthly return in excess of the risk-free rate. _CAPM_ , _FF3_ , _FFC4_ , _FF5_ , _FF6_ , and _Q_ denote alphas with respect to the Capital Asset Pricing Model (Sharpe, 1964; Lintner, 1965; Mossin, 1966), the Fama-French three-factor model (Fama and French, 1993), the Fama-French-Carhart four-factor model (Carhart, 1997), the Fama-French five-factor model (Fama and French, 2015), the Fama-French sixfactor model (Fama and French, 2018), and the Q-factor model (Hou et al., 2015), respectively. The excess return and alphas are in percentage points, and _t_ -statistics are reported in parentheses. *, **, and *** indicate significance at the 10%, 5%, and 1% levels, respectively. 

||Excess return|CAPM|FF3|FFC4|FF5|FF6|Q|
|---|---|---|---|---|---|---|---|
|Equal-weighted|_−_0.01|_−_0.53***|_−_0.51***|_−_0.50***|_−_0.57***|_−_0.56***|_−_0.45**|
||(_−_0.02)|(_−_3.08)|(_−_2.98)|(_−_2.87)|(_−_3.17)|(_−_3.14)|(_−_2.54)|
|Value-weighted|_−_0.00|_−_0.43**|_−_0.33**|_−_0.32**|_−_0.40**|_−_0.40**|_−_0.30*|
||(_−_0.00)|(_−_2.52)|(_−_2.20)|(_−_2.08)|(_−_2.52)|(_−_2.48)|(_−_1.84)|



70 

## **F.6 ETF Performance: Potential Price Impact of Short Sales** 

In Appendix Table F.7, we study the performance of ETFs in the first year since launch conditioning on ETFs that do not have lendable shares in their first year. 

### **Table F.7. First-Year ETF Performance for ETFs with Zero Lendable Shares** 

The table presents the first-year-after-launch alphas computed based on different asset pricing models. The sample period is from 2000 to 2019. ETFs are split according to two criteria: _i_ ) whether there were lendable shares available on Markit in the first year since launch, and _ii_ ) ETF classification as broad-based or specialized. The Markit variable that we use to measure the availability of lendable shares for market participants is Total Demand Quantity (TDQ). There were 412 (366) broad-based (specialized) ETFs that did not have lendable shares in the first year. _Excess return_ refers to the average monthly return in excess of the risk-free rate. _CAPM_ , _FF3_ , _FFC4_ , _FF5_ , _FF6_ , and _Q_ denote monthly alphas with respect to the Capital Asset Pricing Model (Sharpe, 1964; Lintner, 1965; Mossin, 1966), the Fama-French three-factor model (Fama and French, 1993), the Fama-French-Carhart four-factor model (Carhart, 1997), the Fama-French five-factor model (Fama and French, 2015), the Fama-French six-factor model (Fama and French, 2018), and the Q- factor model (Hou et al., 2015), respectively. The excess return and alphas are in percentage points, and _t_ -statistics are reported in parentheses. *, **, and *** indicate significance at the 10%, 5%, and 1% levels, respectively. 

|First|year performance|of ETFs wi|thout lenda|ble shares wi|thin the fir|ist year||
|---|---|---|---|---|---|---|---|
||Excess Return|CAPM|FF3|FFC4|FF5|FF6|Q|
|Broad-based ETFs|0.46|0.02|_−_0.03|_−_0.05|0.05|0.04|_−_0.04|
||(1.64)|(0.19)|(_−_0.36)|(_−_0.57)|(0.56)|(0.43)|(_−_0.47)|
|Specialized ETFs|_−_0.09|_−_0.63***|_−_0.61***|_−_0.59***|_−_0.37**|_−_0.36**|_−_0.43***|
||(_−_0.21)|(_−_3.20)|(_−_3.60)|(_−_3.48)|(_−_2.17)|(_−_2.15)|(_−_2.63)|



71 

## **F.7 ETF Performance: Potential Price Impact of ETF Flows** 

There are three distinct time periods around the launch of an ETF in which investors’ flows can create price impact in the underlying portfolio. 

### **F.7.1 Front-Running a Future ETF** 

Investors could front-run an ETF prior to its launch by buying the underlying portfolio. While this possibility is technically possible, it is not likely to generate the run up in prices of the underlying portfolio, which is observed in the three years prior to launch (Figure 6). The reason is the time scale: while the run up window is about three years, it takes three to five months to launch an ETF. 

Furthermore, for specialized ETFs, the price of the underlying indexes seems to stabilize in the few months just before the launch. Thus, front-running an ETF prior to its launch date is not likely to drive the price run-up of the underlying securities. Nevertheless, it is possible that the observed plateau/minor decline of the underlying indexes prior to ETF launches (Figure 6) reflects the _net_ performance, combining the price pressure of market participants front-running the ETF and the start of the decline of the overvaluation. 

### **F.7.2 Initial Construction of an ETF Portfolio** 

The initial construction of an ETF portfolio requires the ETF issuer to purchase the securities of the underlying index. These purchases can create upwards price pressure on the stocks. We estimate the price pressure to be in the order of 0 _._ 3%. In the next paragraphs, we describe how we reached this conclusion. 

### **F.7.3 ETF Flows Over the ETF’s Life** 

Flows over the life of the ETF can create price impact on the underlying assets, consistent with Ben-David et al. (2018). The magnitude of this price impact will depend on the extent to which the money that goes into/out of the ETFs is not channeled from/to the underlying 

72 

securities. To illustrate, if the flows to an ETF that invests in high-tech firms are replacing current investments in the same firms, the price impact will be minimal. 

To estimate the potential price impact of ETF flows, including the price impact due to the initial portfolio construction (as discussed above), we draw inspiration from the work of Gabaix and Koijen (2021). More precisely, we estimate the upper bound of price impact of ETF flows assuming that the flows originate from outside the equity market (e.g., from scaling down a bond portfolio) and that the multiplier for $1 of flows is 5.<sup>44</sup> 

Moreover, we need to make assumptions about the horizon over which the price impact dissipates. At one extreme, we assume that its half life is one month. At the other extreme, we assume that the price impact is permanent. We also have two intermediate cases with half lives of about two months and six months. In other words, we assume that the price impact at the monthly frequency has a rate of exponential persistence taking values in _{_ 0.5, 0.7, 0.9, and 1 _}_ . 

In greater detail, using all the ETFs in a specific category, we compute the price impact of their flows in a given month on all the stocks in their portfolios apportioning the flows according to the ETF weights. We can then obtain a _counterfactual_ price level that we would have observed _in the absence of flows_ by subtracting the price impact from the observed market prices of the underlying stocks. We note that the price impact could be negative, in principle, if the flows in a given month are negative. Then, using the counterfactual price level, we can construct the event-time evolution of the value of the ETF basket after launch and compare it to the series in the original Figure 2. 

We report these results in Appendix Figure F.2. In the figure, the _observed_ series are constructed using the actual market prices (solid lines), and the _counterfactual_ series (dotted lines) are constructed netting out the price impact, as described above. We note that because we conduct this analysis using the prices of the stocks underlying the ETF baskets, as opposed to the ETFs’ prices, the magnitudes of the next results are not directly compareble to those 

> 44From our data, there is no way to know where the demand comes from. Therefore, we estimate the upper bound of the effect, assuming that all flows reflect external capital flows. 

73 

in Figure 2. 

### **Figure F.2. Performance of the ETFs’ Underlying Portfolios: Potential Price Impact of ETF Flows** 

The figure shows the performance of ETFs around launch, split by groups of broad-based (BB) and specialized (Sp) ETFs. The sample period is from 2000 to 2019. We estimate monthly ETF returns using the ETF portfolio weights and stock returns. We then obtain the counterfactual returns of broad-based (specialized) ETFs by subtracting the estimated price impact arising from flows of broad-based (specialized) ETFs from observed market prices according to the ETF weights. We assume that flows originate from outside the equity market and that the multiplier for $1 of flows is 5. For each ETF group, we form 60 calendar-time portfolios that include returns of ETFs in their month +1 _,_ +2 _, . . . ,_ +60 since the launch date (month 0). The portfolio returns are value-weighted using one-month-lagged market capitalization. We have 60 time series of portfolio returns per ETF category. We repeat this process with the counterfactual ETF returns. To adjust returns for risk factors, we estimate the Fama-French-Carhart four-factor model (FFC-4) alphas of the portfolios (Fama and French, 1993; Carhart, 1997). We have 60 estimated FFC-4 alphas per ETF category with observed ETF returns and additional 60 estimated FFC-4 alphas per ETF category with the counterfactual ETF returns. The solid lines represent the estimated performance of ETFs with observed stock returns, and the dotted lines represent that with counterfactual stock returns. 

#### (a) Smoothing factor: 0.5 



<!-- Start of picture text -->
0<br>− 10<br>BB (observed)<br>− 20 BB (counterfactual)<br>Sp (observed)<br>− 30 Sp (counterfactual)<br>0 10 20 30 40 50 60<br>(c) Smoothing factor: 0.9<br>0<br>− 10<br>− 20<br>− 30<br>0 10 20 30 40 50 60<br>Months relative to ETF launch date<br>(%)CumulativeFFC-4alphas<br>(%)CumulativeFFC-4alphas<br><!-- End of picture text -->



<!-- Start of picture text -->
(b) Smoothing factor: 0.7<br><!-- End of picture text -->



<!-- Start of picture text -->
0<br>− 10<br>− 20<br>− 30<br>0 10 20 30 40 50 60<br>(d) Smoothing factor: 1.0<br>0<br>− 10<br>− 20<br>− 30<br>0 10 20 30 40 50 60<br>Months relative to ETF launch date<br><!-- End of picture text -->

Our evidence suggests the following. First, the price impact of the initial construction of the portfolio is relatively small, with a magnitude of 0.3%. Second, in the case of permanent price impact, because the average flows are positive and the price impact never reverts, the cumulative price impact of flows raises the prices of the underlying securities above the counterfactual prices, which are net of price pressure. Third, in all other cases (smoothing 

74 

factors equal to 0.5, 0.7, and 0.9), we observe the negative price impact of disappointed flows. In these cases, when flows turn negative, the early positive price impact has already dissipated and, eventually, it leaves the way to the negative impact of the disappointed flows. At the end of our window, the prices of the stocks in the specialized basket are below the level they would have in the counterfactual case of no price pressure from ETF flows. 

Again, these results represent a limit case. However, their magnitude is potentially economically significant. The maximum price impact that we observe is a positive 7.7% in the case of broad-based ETFs and a positive 8.9% in the case of specialized ETFs with a smoothing factor equal to 1 (Panel (d)). 

With a more realistic smoothing factor of 0.9 (Panel (c)), the cumulative price impact is negligible for broad-based ETFs; instead, for specialized ETFs, the negative cumulative price impact of flows at the end of the 60-month horizon is _−_ 2.7%. 

Importantly, the main evidence of a decline in the specialized ETF prices exists irrespective of the amplifying effect of negative flows. 

75 

## **F.8 ETF Performance and Closures** 

Appendix Figure F.3 reports the likelihood of closure of ETFs as a function of time since launch as well as of their past performance. 

### **Figure F.3. Likelihood of ETF Closures** 

The figure shows the cumulative likelihood of ETF closures since launch (Panel (a)) and the sensitivity of ETF closures to past performance (Panel (b)). The sample period is from 2000 to 2019. 



<!-- Start of picture text -->
(a) Cumulative likelihood of closure<br>0 . 2<br>0 . 1<br>0<br>0 10 20 30 40 50 60<br>Months relative to ETF launch date<br>ofclosures<br>Cumulativefraction<br><!-- End of picture text -->

- (b) Performance and likelihood of closure 



<!-- Start of picture text -->
0 . 8 Broad-based ETFs<br>Specialized ETFs<br>0 . 6<br>0 . 4<br>0 . 2<br>− 10% − 5% 0% 5%<br>Average quarterly return<br>ofLikelihoodclosure<br><!-- End of picture text -->

76 

