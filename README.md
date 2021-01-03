# GUI
设计一个监控程序，在某只股票放量跳空或异常放量时提醒
斯劳森和其他一些人注意到，期权标的股的重要交易和支撑与阻力往往集中在期权的行权价附近。实际上，期权的行权价对股票的价格有一定的影响，因此往往成为“重要”的买入和卖出区域。
显然，支撑位和阻力位是多空双方集中交战的产物，这可以用战场来比喻：自古希腊时代以来，同样的那些地点发生过一次又一次的战役。期权的行权价吸引交易者集中交
易，这恰如理想的战场吸引军队统帅前来交战，它们都是检验对手实力的好地方。
PowerStrikeTM能分析交易品种在期权行权价附近的成交价与成交量，以此来判断支撑或阻力的强弱程度。该软件巧妙地将量化技术应用于支撑和阻力的分析，可为图表分析提供补充参考
本书编辑在“自然对冲”理论中领悟到的道理，非常有价值。考虑到现代市场的复杂性，对冲的双边都有获利机会。投资者应该将双边获利作为交易目标。
让我们总结一下道氏理论带来的几条重要经验：勿将资金大头用于和长线趋势相反的交易中；在趋势有可能反转时，逐步调低多头仓位，且仅做空少数弱势股票；勿将全部资金用于反向交易，以期抓住平均指数的长线顶部或长线底部。

形态、趋势、支撑位和阻力位都会重复出现

在多头仓位和空头仓位之间，分配全部或部分资金。假设你对自己图表的解释在大部分情况下都是合理正确的，那么你可在任何特定的时候，选择若干强于平均水平的股票，同时也选择若干弱于平均水平的股票。

而在一个正常的市场里，多头仓位和空头仓位很可能同时获利。

查看迈吉评价指数？跟反转信号很像。

我们建议采用系统化、持续性的套利或对冲。随着迈吉评价指数的上涨，空头仓位的比重逐渐下降，多头仓位的比重逐渐上升。而随着迈吉评价指数的下跌，会出现相反的情况。（第9版编者按：我曾建议将此处介绍的方法称为“自然对冲”，并将这种方法的实施过程称为“节奏化交易”。）针对道指的自然对冲可以包括一个多头仓位（例如牛市中
的道琼斯工业平均指数）和若干空头仓位（在看跌的道指成分股中），或者（更好的选择是）与弱势道指成分股正相关的空头仓位。这是因为，弱势道指成分股的风险往往可通过大量持有被动型指数基金来缓冲。

你不能从一开始就依赖从交易中赚取的回报过活。你得在交易资金之外规划好自己的预算，即使这意味着你要节衣缩食。然后你就能自由地运用自己的交易方法，无须在压力之下冒不必要的风险，无须过早地出售股票以偿还债务，也不会受到各种恐惧和担忧的影响。

我们可将股票的长线走势大致地记为如下形状。牛市通常脱胎于一系列不规则的涨跌，起步于一波温和的上攻，然后逐渐加速上涨，最后到达终极顶点。熊市则往往在开始时跌势最猛，然后逐渐减缓，最终止步见底。因此，熊市的走势一般比牛市陡峭。根据这些规律，我们可大致判断何时将出现最好的机会，何时应该加大综合杠杆。

我们知道，在一轮大牛市里，高等级（且往往是保守型）的股票作为活跃的市场领导者，通常率先启动，持续稳步上攻，最终到达顶点，然后构筑反转形态。从这个顶点开始，它们将以比上涨时更为陡峭的角度下挫。相比之下，低等级的低价股往往启动较慢，在牛市早期保持休眠状态，然后突然大幅飙升，连续上攻，直到见顶。但是，这个顶点往往出现在许多保守型股票见顶回落以后（可能晚几个月）。投机型股票见顶后，将快速回落到原先成交清淡时的价位水平，而保守型股票的长线跌势要晚一些才能终结。这意味着，在牛市早期，最好专注于高等级股票的交易；在牛市晚期，最好专注于低等级股票的交易。而在熊市中，即使是当有些绩差股尚处在最后一波上涨中时，你如果卖空高等级股票也可能失手；不过，你可以伺机回补这些空头仓位，并且在低等级股票发出反转信号时卖空它们。

Quantitative Trading:
When it comes to judging the current financial performanceof a company compared to its peers or compared to its
historical performance, the computer is often just as good as human financial analysts—and the computer can watch thousands of
such companies all at once. Some advanced quantitative systems can even incorporate news events as inputs: Nowadays, it is possible to use a computer to parse and understand the news report.

What does Ernest Chan do as a quantitative trader?
I consider myself to be in the middle of the pack in terms of automation. The largest block of time I need to spend is in the morning before the market opens: I typically need to run various programs to download and process the latest historical data, read company news that comes up on my alert screen, run programs to generate the orders for the day, and then launch a few baskets of orders before the market opens and start a program that will launch orders automatically throughout the day. I would also update my spreadsheet to record the previous day’s profit and loss (P&L) of the different strategies I run based on the brokerages’ statements. All of this takes about two hours.

After that, I spend another half hour near the market close to direct the programs to exit various positions, manually checking that those exit orders are correctly transmitted, and closing down various automated programs properly.

In between market open and close, everything is supposed to be on autopilot. Alas, the spirit is willing but the flesh is weak: I often cannot resist the urge to take a look (sometimes many looks) at the intraday P&L of the various strategies on my trading screens. In extreme situations, I might even be transfixed by the huge swings in P&L and be tempted to intervene by manually exiting positions. Fortunately, I have learned to better resist the temptation as time goes on.

Ernest Chan on AI:
Every time a carefully constructed model that seems to work marvels in backtest came up, they inevitably performed miserably going forward. The main reason for this seems to be that the amount of statistically independent financial data is far more limited compared to the billions of independent consumer and credit transactions available.
This is not to say that no methods based on AI will work in prediction. The ones that work for me are usually characterized by these properties:
 They are based on a sound econometric or rational basis, and not on random discovery of patterns.
 They have few parameters that need to be fitted to past data.
 They involve linear regression only, and not fitting to some esoteric nonlinear functions.
 They are conceptually simple.
 All optimizations must occur in a lookback moving window, involving no future unseen data. And the effect of this optimization must be continuously demonstrated using this future, unseen data.

How to quickly filter out some unsuitable strategies:
 Does it outperform a benchmark?
 Does it have a high enough Sharpe ratio?
 Does it have a small enough drawdown and short enough drawdown duration?
 Does the backtest suffer from survivorship bias?
 Does the strategy lose steam in recent years compared to its earlier years?
 Does the strategy have its own “niche” that protects it from intense competition from large institutional money managers?

common pitfalls related to how the backtest program:
1. looking ahead bias:
2. Data-Snooping Bias
    sample size = number of parameters X 252
    parameterless trading model
    paper trading (out of sample)
    sensitivity analysis

Strategy refinement:
1. Whatever changes you make to the strategy to improve its performance on the training set, it must also improve the performance on the test set.
2. When introducing these refinements to your strategy, it is preferable that the refinement has some basis in fundamental economics or a well-studied market phenomenon, rather than some arbitrary rule based on trial and error. Otherwise, data-snooping bias looms.

Kelly formula

Trending regimes are usually triggered by the diffusion of new information, the execution of a large institutional order, or
“herding” behavior. We need to find a way to find the leading sheep.

 Competition between traders tends to reduce the number of mean-reverting trading opportunities.
 Competition between traders tends to reduce the optimal holding period of a momentum trade.

The opening gap strategy is a breakout strategy that works for some futures and currencies.
