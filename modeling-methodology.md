<div align="center">
    <h1>Modeling Methodology</h1>
</div>

<!-- omit in toc -->
# Table of Content

- [The variables](#the-variables)
  - [The variables to be explained](#the-variables-to-be-explained)
  - [Potential explanatory variables](#potential-explanatory-variables)



To start, you need to make a distinction between two main types of variables in your dataset:

- **the variables to be explained** (which correspond to market characteristics that can be exploited in terms of trading)
- and **the potentially explanatory variables**.

> A multi-scale view of the variables must always be maintained. The more independent scales the multiscale analysis will reveal, the more easily they will be recombined.

A first step is to label the data. You need to pre-compute a multi-scale target signal, which is the one you will then try to predict. A very important point is that you are allowed to use future information for this.

Then you need to decompose the explanatory variables on multiple scales and make them independent.
In this step, you will have to see the results of the pre-treatments as estimators, and retain the uncertainty that they owe to the estimation processes that allowed them to be estimated.

You will systematically use descriptive statistics to qualify a variable before including it in any further analysis.

# The variables

## The variables to be explained

The two variables that you will look at first are
- the price reversal (i.e. the alternation)
- the trend (i.e. the continuation)

They are only defined in terms of a time horizon. You will therefore not define "THE" price reversal, but reversals at 5 seconds, 10 seconds, 1 minute, 10 minutes, etc. as different variables (each associated with a scale).

You will have to take care of the sensitivity to the initial conditions. You will thus obtain for each scale an "intensity" of the variable over time. As you are interested in high frequencies, the "market realizability" of a trend or a reversal is crucial; it will therefore also be necessary to quantify its liquidity over time: a trend with zero market volume does not have the same liquidity as a trend of the same intensity (i.e. slope) accompanied by a high volume.

Three types of scale will be considered:

- in **calendar time** (second),
- in **trade time** (number of trades),
- and **volume time** (quantity traded).

You will thus have for each Y(scale), and at each moment:
- **an intensity value**,
- and **a liquidity value**.

To calculate the value of these characteristics of the variables to be explained, you have the right to the future. For example, to calculate a local maximum at the 10-trade scale, you can look at the trades before and the trades after.

The characteristics of a variable to be explained must be computed on the whole perimeter in a systematic way.

It is out of the question to find oneself in a situation where one has gone far enough on the analysis of a future over 3 weeks before realizing that what one has been able to capture does not generalize to any other period of time and on any other future.

## Potential explanatory variables

The first variables you will look at are :

- the trend
- the reversals
- the range
- the volatility
- oscillations
- imbalance
- range movements

> Contrary to the treatments of the variables to be explained, all the treatments of the explanatory variables must be causal: they must be able to be reproduced in real time on the market data (thus out of the question to use the future).

It is not at all problematic to use the trend and the reversals (which are also variables to be explained), it simply means that we are not forbidden to predict a future trend from a conjunction of reversals and past trends.



