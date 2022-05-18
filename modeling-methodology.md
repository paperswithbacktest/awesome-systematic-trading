<div align="center">
    <h1>Modeling Methodology</h1>
</div>

<!-- omit in toc -->
# Table of Content

- [The variables](#the-variables)
  - [Variables to be explained](#variables-to-be-explained)
  - [Potential explanatory variables](#potential-explanatory-variables)
- [Modeling](#modeling)
  - [Explorations](#explorations)
  - [Overfitting measurement](#overfitting-measurement)
  - [Eigendimension estimation](#eigendimension-estimation)



To start, you need to make a distinction between two main types of variables in your dataset:

- **the variables to be explained** (which correspond to market characteristics that can be exploited in terms of trading)
- and **the potentially explanatory variables**.

> A multi-scale view of the variables must always be maintained. The more independent scales the multiscale analysis will reveal, the more easily they will be recombined.

A first step is to label the data. You need to pre-compute a multi-scale target signal, which is the one you will then try to predict. A very important point is that you are allowed to use future information for this.

Then you need to decompose the explanatory variables on multiple scales and make them independent.
In this step, you will have to see the results of the pre-treatments as estimators, and retain the uncertainty that they owe to the estimation processes that allowed them to be estimated.

You will systematically use descriptive statistics to qualify a variable before including it in any further analysis.

# The variables

## Variables to be explained

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

The first variables you will look at are:

- the trend
- the reversals
- the range
- the volatility
- oscillations
- imbalance
- range movements

> Contrary to the treatments of the variables to be explained, all the treatments of the explanatory variables must be causal: they must be able to be reproduced in real time on the market data (thus out of the question to use the future).

It is not at all problematic to use the trend and the reversals (which are also variables to be explained, it simply means that we are not forbidden to predict a future trend from a conjunction of reversals and past trends.

<!-- omit in toc -->
### Monovariate pre-processing

These variables must also undergo a multi-scale decomposition, according to three types of scales (calendar / trade / volumes).

For example, a 60-trade causal trend (at times, prices and quantities *(t(n),S(n),Q(n)))* can be estimated:
- by the Bayesian slope: *(S(60)-S(1))/60*
- by the slope of the linear regression of *S(n)* on *t(n)*
- by the median of the progressive slopes *(S(n)-S(1))/n*
- by the median of the local slopes *S(n)-S(n+1)*
- by the barycenter of the progressive slopes: *sum( Q(n) * (S(n)-S(1))/n ) / sum(Q(n))*
- etc

For a single "concept", we will have to choose one or more estimators and not deviate from them before having totally invalidated or validated it.

The results of these calculations being only estimators of an underlying value, it will be necessary to keep a quantification of the variability of their values. For each of these estimators we can calculate a "variability". This can be the variance of the estimator under distribution assumptions, or simply a bootstrap scoring.

<!-- omit in toc -->
### Multivariate pretreatments

As the characteristics of the potentially explanatory variables will be recombined in order to best explain those of the variables to be explained, the more independent they are, the better things will go.

We will use a conditional information measure in a systematic way to quantify the dependencies between variables.

This phase of the analysis will be increasingly costly, since when we add an Nth potentially explanatory variable, we will have to phase it with the previous N-1. It will therefore be necessary to systematize / automate this phase.

<!-- omit in toc -->
### Output

At the end of the study phase of the potentially explanatory variables, we will have for each type of scale (calendar / trade / volume) a characterization of these variables (value, variability), as well as an analysis of their intra (i.e. between the different scales and types of scale) and inter (i.e. cross indicators) dependencies.

# Modeling

The objective of modeling is to capture common joint phenomena.

## Explorations

Any parametric modeling will be preceded by a non-parametric analysis to guide the choice of models.

- **Non-parametric explorations** Non-parametric methods are useful for exploration purposes, but are generally less effective for prediction or anticipation, as they have a strong tendency to over-learn. Before choosing a model, these methods allow us to have an idea of the relationships between the variables. We will typically use informational methods (conditional entropy), which will tell us if a characteristic CX contains information about a characteristic CY to be predicted, but it is possible that the type of relationship is not capturable by any model. We will just know that "there is a link" between the two features without being able to exploit it. These analyses will nevertheless allow us to discard some features since we will have results like "CX contains no information about CY". This is a dimension reduction technique.

- **Rare event conjunctions** In a second step (and therefore once the number of potentially explanatory features has been reduced) we will try to measure if there are rare event conjunctions for CY and for CX. To do so, we will score CX and CY with respect to their empirical distributions and thus obtain SX and SY scores that marginally follow a uniform distribution (Poisson lemma). We will then simply look for Baysian thresholds that maximize the probability of rare events between CX and CY.

## Overfitting measurement

We will use systematic methods to measure the over-fitting of the estimated parameters.

- **Cross validation** The most generic way to validate the complexity of a model is cross-validation. It consists in keeping a part (randomly chosen) of the database (about 20%) and calculating the residuals of the model on this validation base.

- **Bootstrap and variability of model parameters** The bootstrap is a method similar to cross validation. It focuses on the variability of the model's parameter values. It consists in calculating the parameters of the model (the coefficients of a linear regression, for example) on a random draw of 80% of the database, several times in a row (a good 100 times). We will then obtain a probable distribution of the model parameters. If the model indeed captures a relationship between X and Y, then its parameters should not be too variable. If they are, we will ask ourselves about the temporal variations of their values. Indeed, if the model is structurally sound (i.e. the nature of the relationship between X and Y is linear), but its parameters evolve over time (following "market phases"), we need to be able to see this.

## Eigendimension estimation

Eigendimension estimates will also be discussed in a systematic framework.

In order to model the relationship between *Y(t)* (to be explained) and *X(t)* (potentially explanatory), we can exploit values of X in the past. For example, instead of using a formal model like :

*Y(t) = F( X(t-1) ) + noise*

It is often better to use a model like:

*Y(t) = F( X(t-1), X(t-2), …, X(t-K) ) + bruit*

The choice of K is an integral part of the choice of the model.
The real danger is that the dimension (i.e. the number of variables) of this kind of model is quickly very high (if X is of dimension 4 and K is 5, this amounts to a model of dimension 20).



In general, in modeling, we can "exchange data for knowledge". The more explicit behavior we have identified (from blind modeling) that we can incorporate into the models, the less we need long histories (and the less we are exposed to the risk of overlearning).


